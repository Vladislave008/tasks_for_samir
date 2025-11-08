from selenium import webdriver as wd
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from lxml import html
from selenium.webdriver.chrome.options import Options


def find_voyager_date():
    try:
        response = requests.get('https://science.nasa.gov/mission/voyager/voyager-1/') # Voyager 1 page on the NASA official website
        soup = BeautifulSoup(response.text, 'html.parser')
        launch_element = soup.find(string="launch")
        launch_container = launch_element.n
        next_sibling = launch_container.find_next_sibling()
        date = next_sibling.string
        month_dict = {
            'jan': 1, 'jan.': 1, 'january': 1,
            'feb': 2, 'feb.': 2, 'february': 2,
            'mar': 3, 'mar.': 3, 'march': 3,
            'apr': 4, 'apr.': 4, 'april': 4,
            'may': 5, 'may.': 5, 
            'jun': 6, 'jun.': 6, 'june': 6,
            'jul': 7, 'jul.': 7, 'july': 7,
            'aug': 8, 'aug.': 8, 'august': 8,
            'sep': 9, 'sep.': 9, 'sept': 9, 'sept.': 9, 'september': 9,
            'oct': 10, 'oct.': 10, 'october': 10,
            'nov': 11, 'nov.': 11, 'november': 11,
            'dec': 12, 'dec.': 12, 'december': 12
        }
        date_split = date.replace(',', '').split()
        if len(date_split) != 3:
            raise ValueError(f"Bad date: {date}")
        month_str, day_str, year_str = date_split
        month = month_dict.get(month_str.strip().lower())
        if month is None:
            raise ValueError(f"Bad month: {month_str}")
        day = int(day_str.strip())
        if day < 1 or day > 31:
            raise ValueError(f"Bad day: {day}")
        year = int(year_str.strip())
        return f"{year:04d}{month:02d}{day:02d}"
    except Exception as e:
        print(f"Error in find_voyager_date: {e}")
    
def find_rfc1149_date():
    try:
        response = requests.get('https://datatracker.ietf.org/doc/rfc1149/history/') # rfc1149 history page on datatracker website
        soup = BeautifulSoup(response.text, 'html.parser')
        publish_element = soup.find(string="RFC published")
        row = publish_element.find_parent('tr')
        date_cell = row.find('td')
        if date_cell.string is None:
            date_div = date_cell.find('div')
            date = date_div.text.strip()
        else:
            date = date_cell.string
        date= date.replace('-','')
        return date
    except Exception as e:
        print(f"Error in find_rfc1149_date: {e}")

def find_brain_codepoint():
    try:
        response = requests.get(
            'https://unicode.org/Public/emoji/latest/emoji-test.txt',  # unicode official emoji list
        )
        for line in response.text.split('\n'):
            if 'brain' in line.lower():
                parts = line.split('#')
                if len(parts) >= 2:
                    code_info = parts[0].strip()
                    res = code_info.split(';')[0].strip()
                    break
    except Exception as e:
        print(f"Error in find_rfc1149_date: {e}")
    return res

def find_isbn():
    try:
        #response = requests.get('https://search.catalog.loc.gov/instances/9acb1e70-9ea7-5ec1-9e9e-4d1e8b6d865e?option=lccn&query=88005934') # The C programming language page on library of congress website
        #soup = BeautifulSoup(response.text, 'html.parser')
        options = Options()
        options.add_argument("--headless")
        driver = wd.Chrome(options=options)
        driver.get("https://search.catalog.loc.gov/instances/9acb1e70-9ea7-5ec1-9e9e-4d1e8b6d865e?option=lccn&query=88005934")
        wait = WebDriverWait(driver, 10)
        isbn_title_div = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'ISBN')]"))
    )
        page_source = driver.page_source
        isbn_title = driver.find_element(By.XPATH, "//h3[contains(text(), 'ISBN')]")
        # Переходим к следующему элементу (предполагая ту же структуру)
        isbn_value = isbn_title.find_element(By.XPATH, "./../following-sibling::div")
        print(isbn_value.text)
    except Exception as e:
        print(f"Error in find_isbn: {e}")


def find_bitcoin_date():
    try:
        response = requests.get('https://www.blockchain.com/ru/explorer/blocks/btc/0') # bitcoin history page on blockchain.com
        soup = BeautifulSoup(response.text, 'html.parser')
        
        publish_element = soup.find(string="Добыто")
        parent = publish_element.parent.parent.parent
        next_sibling = parent.find_next_sibling()
        
        date_element = next_sibling.find('div', string=lambda text: text and any(x in text for x in ['янв', 'фев', 'мар']))
        if date_element:
            return date_element.get_text(strip=True)
    except Exception as e:
        print(f"Error in find_bitcoin_date: {e}")

#print(find_voyager_date())
#print(find_rfc1149_date())
#print(find_brain_codepoint())
#print(find_isbn())
print(find_bitcoin_date())