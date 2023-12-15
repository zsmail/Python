from bs4 import BeautifulSoup
import requests

# Function to read already posted links (to make sure we don't get pull the same information)
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

# URL of the RSS feed
rss_url = 'url'

# Make a GET request to the RSS feed URL
headers = {'User-Agent': 'Mozilla/5.0 (compatible; RSS Feed Reader)'}
response = requests.get(rss_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML content of the response
    soup = BeautifulSoup(response.content, 'xml') 
    
    # Read already posted links
    posted_links = read_posted_links(posted_links_file)

    # Find all items in the RSS feed
    items = soup.find_all('item')

    # Iterate over each item
    new_articles_count = 0  # Counter for new articles
    for item in items:
        title = item.title.text if item.title else 'No Title'
        article_link = item.link.text if item.link else 'No Link'

        # Check if the article has already been posted
        if article_link not in posted_links:
            # Print the article title and link
            print(f"Article: {title}")
            print(f"Link: {article_link}")

            # Add the link to the posted links file
            add_posted_link(posted_links_file, article_link)
            new_articles_count += 1
            
            # Stop after processing 3 new articles (adjust how you want it)
            if new_articles_count >= 3:
                break
else:
    print(f"Failed to fetch RSS feed: HTTP Status Code {response.status_code}")
