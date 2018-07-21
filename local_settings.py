'''
Local Settings for a heroku_ebooks account. 
'''
import os
from dotenv import load_dotenv, find_dotenv
# Configuration for Twitter API
is_production = os.environ.get('IS_HEROKU', None)
ENABLE_TWITTER_SOURCES = False # Fetch twitter statuses as source
ENABLE_TWITTER_POSTING = False # Tweet resulting status?
if is_production:
    MY_CONSUMER_KEY = os.environ['MY_CONSUMER_KEY']
    MY_CONSUMER_SECRET = os.environ['MY_CONSUMER_SECRET']
    MY_ACCESS_TOKEN_KEY = os.environ['MY_ACCESS_TOKEN_KEY']
    MY_ACCESS_TOKEN_SECRET = os.environ['MY_ACCESS_TOKEN_SECRET']
    TWEET_ACCOUNT = os.environ['HANDLE']
else:
    load_dotenv(find_dotenv())
    MY_CONSUMER_KEY = os.getenv('MY_CONSUMER_KEY')
    MY_CONSUMER_SECRET = os.getenv('MY_CONSUMER_SECRET')
    MY_ACCESS_TOKEN_KEY = os.getenv('MY_ACCESS_TOKEN_KEY')
    MY_ACCESS_TOKEN_SECRET = os.getenv('MY_ACCESS_TOKEN_SECRET')
    TWEET_ACCOUNT = os.getenv('HANDLE')

# Configuration for Mastodon API
ENABLE_MASTODON_SOURCES = False # Fetch mastodon statuses as a source?
ENABLE_MASTODON_POSTING = False # Toot resulting status?
MASTODON_API_BASE_URL = "" # an instance url like https://botsin.space
CLIENT_CRED_FILENAME = '' # the MASTODON client secret file you created for this project
USER_ACCESS_FILENAME = '' # The MASTODON user credential file you created at installation.

# Sources (Twitter, Mastodon, local text file or a web page)
SOURCE_ACCOUNTS = ["boredelonmusk", "tesla", "spacex", "elonmusk", "dogecoin", "dog_feelings", "SICKOFWOLVES", "cleantechnica"]  # A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
TWITTER_SOURCE_ACCOUNTS = ["boredelonmusk", "tesla", "spacex", "elonmusk", "dogecoin", "dog_feelings", "SICKOFWOLVES", "cleantechnica"]  # A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
MASTODON_SOURCE_ACCOUNTS = [""] # A list, e.g. ["@user@instance.tld"]
SOURCE_EXCLUDE = r'^$'  # Source tweets that match this regexp will not be added to the Markov chain. You might want to filter out inappropriate words for example.
STATIC_TEST = True  # Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = "training.txt"  # The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
SCRAPE_URL = False  # Set this to true to scrape a webpage.
SRC_URL = ['http://www.example.com/one', 'https://www.example.com/two']  # A comma-separated list of URLs to scrape
WEB_CONTEXT = ['span', 'h2']  # A comma-separated list of the tag or object to search for in each page above.
WEB_ATTRIBUTES = [{'class': 'example-text'}, {}] # A list of dictionaries containing the attributes for each page.

ODDS = 1  # How often do you want this to run? 1/8 times?
ORDER = 3  # How closely do you want this to hew to sensical? 2 is low and 4 is high.

DEBUG = True  # Set this to False to start Tweeting live
  # The name of the account you're tweeting to.
