# NotiCon

This software is designed to create a file named `hotel_prices.json`. This file acts as a reference for hotel prices. The software is able to compare and notify you if a hotel is no longer sold out or if the price gets cheaper. This way, we have our own little notification system. This uses Selenium to load the window and render the divs that we pull information from, if theres an issue, try running it not headless, or do, it doesn't matter to me.

## Requirements

- Python 3.12
- Copy `.env.example` to `.env` and fill in the required attributes

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the software, use the following command:

```bash
python main.py
```
