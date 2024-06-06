import time

from selenium.common import NoSuchElementException

from query_builder import QueryBuilder
from price_calculator import PriceCalculator
from telegram_message import TelegramMessage

query_builder = QueryBuilder()

PRICE_FILE = "hotel_prices.json"
CHECK_INTERVAL = 600

# mutable variables
records_per_page_value = '20'
destination_address_latitude_value = '40.44062479999999'
destination_address_longitude_value = '-79.9958864'
destination_address_value = 'PA'
search_radius_value = '50'
destination_address_place_id_value = 'ChIJA4UGSG_xNIgRNBuiWqEV-Y0'
destination_address_address_value = 'Pittsburgh,+PA,+USA'
destination_address_secondary_text_value = 'PA,+USA'
destination_address_city_value = 'Pittsburgh'
destination_address_main_text_value = 'Pittsburgh'
destination_address_website_value = 'https://maps.google.com/?q=Pittsburgh,+PA,+USA&ftid=0x8834f16f48068503:0x8df915a15aa21b34'
destination_address_destination_value = 'Pittsburgh,+PA,+USA'
from_to_date_submit_value = '07/08/2024'
from_date_value = '07/04/2024'
to_date_value = '07/08/2024'
to_date_default_format_value = '07/08/2024'
from_date_default_format_value = '07/04/2024'
flexible_date_search_value = 'false'
is_hide_flexible_date_calendar_value = 'false'
t_start_value = '2024-07-04'
t_end_value = '2024-07-08'
length_of_stay_value = '1'
room_count_box_value = '1+Room'
guest_count_box_value = '3+Adults+Per+Room'
num_adults_per_room_value = '3'
children_count_box_value = '0+Children+Per+Room'
children_count_value = '0'
SEARCH_URL = query_builder.build_query(records_per_page_value, destination_address_latitude_value,
                                       destination_address_longitude_value, destination_address_value,
                                       search_radius_value, destination_address_place_id_value,
                                       destination_address_address_value, destination_address_secondary_text_value,
                                       destination_address_city_value, destination_address_main_text_value,
                                       destination_address_website_value, destination_address_destination_value,
                                       from_to_date_submit_value, from_date_value, to_date_value,
                                       to_date_default_format_value, from_date_default_format_value,
                                       flexible_date_search_value, is_hide_flexible_date_calendar_value, t_start_value,
                                       t_end_value, length_of_stay_value, room_count_box_value, guest_count_box_value,
                                       num_adults_per_room_value, children_count_box_value, children_count_value)


def main():
    while True:
        try:
            hotels = PriceCalculator.check_prices(SEARCH_URL, PRICE_FILE)

            for price, hotel in hotels:
                previous_price = PriceCalculator.get_previous_price(hotel, PRICE_FILE)
                if price != previous_price:
                    message = f"The price for {hotel} has changed!\nPrevious Price: {PriceCalculator.check_if_sold_out(price, previous_price)}\nCurrent Price: ${price}"
                    TelegramMessage.send_telegram_message(message)
                    PriceCalculator.update_price_storage(hotel, price, PRICE_FILE)
                else:
                    print(f"No price change for {hotel}")
            time.sleep(CHECK_INTERVAL)
        except NoSuchElementException:
            print("Element not found. Skipping this iteration.")
            continue


if __name__ == "__main__":
    main()
