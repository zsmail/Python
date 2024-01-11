from selenium import webdriver
import platform
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Chrome options
chrome_options = Options()

# Set up the Selenium WebDriver
service = Service(executable_path="C:\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe",
                log_path='NUL' if platform.system() == 'Windows' else '/dev/null')  # Redirect logs to NUL (Windows) or /dev/null (Unix-based)
driver = webdriver.Chrome(service=service)

# URL of the page to scrape
url = 'https://www.balticexchange.com/en/index.html'

# Go to the webpage
driver.get(url)

# List of indices you are interested in
interested_indices = ["BCI", "BPI", "BDI", "FBX", "BLPG", "BOPEX"]

# Wait for the content to load
try:
    # Wait until the ticker items are present
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ticket")))

    # Now that the page is fully loaded, access the ticker container
    ticker_container = driver.find_element(By.ID, 'ticker')
    
    # Get the HTML content of the ticker container
    html_content = ticker_container.get_attribute('innerHTML')

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    tickets = soup.find_all('div', class_='ticket')

    # Scrape the ticker data
    for ticket in tickets:
        index_name = ticket.find('span', class_='index').get_text().strip() if ticket.find('span', class_='index') else 'N/A'

        # Check if the index is one of the interested indices
        if index_name in interested_indices:
            value = ticket.find('span', class_='value').get_text().strip() if ticket.find('span', class_='value') else 'N/A'
            change_class = ticket.find('span', class_='change')
            change = '🟢' if 'up' in change_class['class'] else '🔴' if 'down' in change_class['class'] else 'no change'
            
            # Print each ticker item as it's read
            print(f"{index_name}: {value} , Change: {change}")

    # Print the source
    print("@BalticExchange - https://www.balticexchange.com/en/index.html -")

finally:
    # Close the browser
    driver.quit()
