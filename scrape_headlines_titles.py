from bs4 import BeautifulSoup
import requests

# Function to read already posted links
def read_posted_links(filename):
    try:
        with open(filename, 'r') as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()

# Function to add a new link to the file
def add_posted_link(filename, link):
    with open(filename, 'a') as file:
        file.write(link + '\n')

# File to store posted links (choose a path)
posted_links_file = 'file.txt'

# This section of code is designed to scrape headlines and links from a website's HTML page.
# You should modify the class names and structure according to the specific website you are targeting.

def scrape_headlines(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    headlines_with_links = []

    # Find the list container. Replace 'list-container-class' with the actual class name of the container.
    list_container = soup.find('ul', class_='list-container-class')
    
    # Find the list items within the container. Replace 'list-item-class' with the actual class name of the list items.
    # Adjust the 'limit' value as needed to control the number of items you want to scrape.
    list_items = list_container.find_all('li', class_='list-item-class', limit=3) if list_container else []

    for item in list_items:
        a_tag = item.find('a')  # Find the <a> tag within the list item.
        if a_tag:
            article_link = a_tag['href']
            headline_text = a_tag.get_text().strip()
            headlines_with_links.append((headline_text, article_link))

    return headlines_with_links

if __name__ == "__main__":
    news_url = 'url'
    headlines_with_links = scrape_headlines(news_url)
    
    # Read already posted links
    posted_links = read_posted_links(posted_links_file)

    # Counter for new articles
    new_articles_count = 0
    
    for headline, link in headlines_with_links:
        full_link = requests.compat.urljoin(news_url, link)
        
        # Check if the article has already been posted
        if full_link not in posted_links:
            # Print the article title and link
            print(f"Article: {headline}")
            print(f"Link: {full_link}")

            # Add the link to the posted links file
            add_posted_link(posted_links_file, full_link)
            new_articles_count += 1

            # Stop after printing 3 new articles
            if new_articles_count >= 3:
                break
