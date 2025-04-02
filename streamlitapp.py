import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import base64
import streamlit as st
from PIL import Image
from PIL import Image
import streamlit as st
import snscrape
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter

base="dark"
primaryColor="purple"

import streamlit as st
st.markdown("---")
st.title("SCRAPING TWITTER")
st.markdown("---")

def get(path:str):
    with open(path, "r") as p:
        return json.load(p)
    
path = get("./com.json.json")
st_lottie(path)
st.markdown("Hi am Rabin currently doing IIT MADRAS ADVANCED DATA SCIECNE PROGRAM IN GUVI GEEK NETWORK here We used Python to scrape data from Twitter, using the Tweepy library to interact with the Twitter API. We searched for tweets using relevant keywords and hashtags, and collected data such as the text of the tweet, the user who posted it, the date and time, and the number of likes and retweets. We then used sentiment analysis tools to classify each tweet as positive, negative, or neutral.")
st.header("About")

st.markdown("Twitter is a social media platform where users can post short messages, called tweets, with a limit of 280 characters. Users can also follow other users and view their tweets in a timeline. Twitter is often used for news, real-time events, and social interaction.")
st.markdown("Twitter also provides an API (Application Programming Interface) that developers can use to programmatically access Twitter data, such as tweets, user profiles, and trends. The Twitter API is commonly used for sentiment analysis, social media monitoring, and other data analysis task")
st.markdown("The co-founders of Twitter are Jack Dorsey, Biz Stone, and Evan Williams. Jack Dorsey served as the CEO of Twitter from 2007 to 2008 and again from 2015 to 2021. In November 2021, it was announced that Jack Dorsey would be stepping down as CEO of Twitter and would be replaced by Parag Agrawal, who had been serving as Twitter's Chief Technology Officer.")

st.markdown("As of 2023, Twitter is a publicly traded company and has many shareholders, so it does not have a single owner in the traditional sense. However, the largest shareholder of Twitter is currently investment firm Vanguard Group, Inc.")

st.markdown("---")
st.title("TWITTER SCRAPING")
st.markdown("---")

st.markdown("Snscrape is a Python package that can be used to scrape data from various social media platforms, including Twitter. Snscrape allows you to scrape tweets and other Twitter data without using the Twitter API. Here's an example of how to use snscrape to scrape tweets:")
st.markdown("Twitter's API: Twitter provides an API (Application Programming Interface) that developers can use to programmatically access data from Twitter. This is the recommended way to access Twitter data, as it is more reliable and less likely to be blocked by Twitter.")
st.markdown("Third-party libraries: There are several third-party libraries available that make it easier to access Twitter data, such as tweepy, snscrape, and twint. These libraries handle the API authentication and provide functions for accessing Twitter data.")
st.markdown("Data cleaning: The data you scrape from Twitter may contain irrelevant or inaccurate information, such as retweets or spam. You will need to clean and filter the data to ensure it is usable for your project.")


def get(path:str):
    with open(path, "r") as p:
        return json.load(p)
    
path = get("./twit.json.json")
st_lottie(path)

image_path = "D:\streamlit\May!.png"
t_image = Image.open(image_path)

# Display the image in Streamlit
st.image(t_image)

import streamlit as st

import streamlit as st

# Create a sidebar with a title
st.sidebar.title("SCRAPING DATA")

# Add some text to the sidebar
st.sidebar.write("WELCOME TO MY PROJECT !")

# Add a separator to the sidebar
st.sidebar.write("---")

# Add more text to the sidebar
st.sidebar.write("Web scraping Twitter refers to the process of extracting data from Twitter's website using an automated program or script. The data that can be scraped from Twitter includes tweets, user profiles, followers, and other information that is publicly available on the sit")

# Add a separator to the sidebar
st.sidebar.write("---")

# Add some final text to the sidebar
st.sidebar.write("Thank you for using ! ")
st.sidebar.write("Project given by GUVI GEEK NETWORK IITM RESEARCH PARK ")



import pandas as pd
import snscrape.modules.twitter as sntwitter
from pymongo import MongoClient
import json
import base64
import streamlit as st


# Function to scrape Twitter data and return a list of dictionaries
def scrape_twitter_data(keyword, start_date, end_date, tweet_count):
    # Create a list to store the scraped data
    scraped_data = []
    
    # Define the search query
    search_query = f"{keyword} since:{start_date} until:{end_date}"
    
    # Loop through the Twitter search results and extract the data
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_query).get_items()):
        if i >= tweet_count:
            break
        
        # Extract the tweet data
        tweet_data = {
            "date": tweet.date,
            "id": tweet.id,
            "url": tweet.url,
            "content": tweet.content,
            "user": tweet.user.username,
            "reply_count": tweet.replyCount,
            "retweet_count": tweet.retweetCount,
            "language": tweet.lang,
            "source": tweet.sourceLabel,
            "like_count": tweet.likeCount
        }
        
        # Append the tweet data to the scraped_data list
        scraped_data.append(tweet_data)
        
    return scraped_data

def create_df(scraped_data):
    tweet_data=pd.DataFrame(scraped_data,columns=["date","id","url","content","user","reply_count","retweet_count","Language","source","like_count"])        
    return tweet_data

# GUI.py
st.title("Scrape the Tweets")

# Get input from user for hashtag
keyword = st.text_input("Enter the hashtag:")

# Get starting date from user
start_date = st.date_input("Select start date:", key="start_date")

# Get end date from user
end_date = st.date_input("Select end date:", key="end_date")

# Get tweet limit from user
tweet_count = st.number_input("Enter the number of tweet you need:", key="limit")

# Scrape tweets
if st.button("Scrape Tweets"):
    scraped_data = scrape_twitter_data(keyword, start_date, end_date, tweet_count)
    tweet_data = create_df(scraped_data)
    st.dataframe(tweet_data)
    
    # Download as csv
    st.write("Saving dataframe as csv")
    csv = tweet_data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="tweet_data.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
    
    # Download as JSON
    st.write("Saving dataframe as json")
    json_string = tweet_data.to_json(indent=2)
    b64 = base64.b64encode(json_string.encode()).decode()
    href = f'<a href="data:file/json;base64,{b64}" download="tweet_data.json">Download JSON File</a>'
    st.markdown(href, unsafe_allow_html=True)

    # Upload to MongoDB
if st.button("Upload to MongoDB"):
    tweet = scrape_twitter_data(keyword, start_date, end_date, tweet_count)
    tweet_data = create_df(tweet)

    client = MongoClient('mongodb://santhiya1204:santhiya1204@ac-dqtoutk-shard-00-00.oeojj5f.mongodb.net:27017,ac-dqtoutk-shard-00-01.oeojj5f.mongodb.net:27017,ac-dqtoutk-shard-00-02.oeojj5f.mongodb.net:27017/?ssl=true&replicaSet=atlas-6lfbkt-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = client["twitter_db_streamlit"]
    collection = db['tweet']
    tweet_data_json = json.loads(tweet_data.to_json(orient='records'))
    collection.insert_many(tweet_data_json)
    st.success('Uploaded to MongoDB')

# Download as csv
if st.button("Download as CSV"):
    tweet = scrape_twitter_data(keyword, start_date, end_date, tweet_count)
    tweet_data = create_df(tweet)
    st.write("Saving dataframe as csv")
    csv = tweet_data.to_csv(index=False)
    print(csv) # print the content of the CSV data
    b64 = base64.b64encode(csv.encode()).decode()
    print(b64) # print the encoded data
    href = f'<a href="data:file/csv;base64,{b64}"download="tweet_data.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)

# Download as JSON
if st.button("Download as Json"):
    tweet = scrape_twitter_data(keyword, start_date, end_date, tweet_count)
    tweet_data = create_df(tweet)
    st.write("Saving dataframe as json")
    json_string = tweet_data.to_json(indent=2)
    print(json_string) # print the content of the JSON data
    b64 = base64.b64encode(json_string.encode()).decode()
    print(b64) # print the encoded data
    href = f'<a href="data:file/json;base64,{b64}"download="tweet_data.json">Download json File</a>'
    st.markdown(href, unsafe_allow_html=True)
