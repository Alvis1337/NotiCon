import time
import json
import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class PriceCalculator:
    @staticmethod
    def check_prices(search_url, price_file):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            driver.get(search_url)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            wait = WebDriverWait(driver, 60)  # Increase the wait time to 20 seconds
            elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.property-card')))
            hotels = []

            for element in elements:
                try:
                    price_element = element.find_element(By.CSS_SELECTOR, 'span.price-value.currency-value')
                    hotel_name_element = element.find_element(By.CSS_SELECTOR, 'div.title-primary')
                    hotel_name = hotel_name_element.text.strip()
                    price_text = price_element.text.strip()
                    match = re.search(r'(\d+,\d+|\d+)', price_text)

                    if match:
                        price = int(match.group(1).replace(',', ''))
                        print('')
                        hotels.append((price, hotel_name))
                except NoSuchElementException:
                    if element.find_element(By.CSS_SELECTOR, 'div.title-primary'):
                        hotel_name_element = element.find_element(By.CSS_SELECTOR, 'div.title-primary')
                        hotel_name = hotel_name_element.text.strip()
                        price_text = 0
                        hotels.append((price_text, hotel_name))
                        print(hotel_name + ' is sold out')
                    else:
                        print('No hotel found')

            return hotels

        finally:
            driver.quit()
            print('Selenium driver has been closed')

    @staticmethod
    def get_previous_price(hotel_name, price_file):
        if os.path.exists(price_file):
            with open(price_file, 'r') as f:
                prices = json.load(f)
                return prices.get(hotel_name, float('inf'))
        return float('inf')

    @staticmethod
    def update_price_storage(hotel_name, price, price_file):
        if os.path.exists(price_file):
            with open(price_file, 'r') as f:
                prices = json.load(f)
        else:
            prices = {}
        prices[hotel_name] = price
        with open(price_file, 'w') as f:
            json.dump(prices, f)

    @staticmethod
    def check_if_sold_out(hotel_price, previous_hotel_price):
        if previous_hotel_price:
            if hotel_price != previous_hotel_price:
                return "This retard is no longer sold out"
