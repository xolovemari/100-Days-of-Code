import requests
from twilio.rest import Client
from config import *

# API error handling
def fetch_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return {}
    except ValueError as e:
        print(f"JSON error: {e}")
        return {}


# send a sms with infos
def send_sms(news_info, percentual):
    if percentual > 0:
        symbol = "🔺"
    else:
        symbol = "🔻"

    client = Client(ACC_SID, AUTH_TOKEN)
    for headline, brief in news_info:
        try:
            message = client.messages.create(
                body=f"{STOCK}: {symbol}{percentual}\nHeadline: {headline}\nBrief: {brief}",
                from_="example",
                to="example"
            )
        except Exception as e:
            print(f"Error sending SMS: {e}")


# check the news from the company
news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&sortBy=publishedAt&apiKey={NEWS_KEY}&language=en&pageSize=3"
news_data = fetch_api_data(news_url)
if "articles" not in news_data:
    print(f"Error: data not found. API response: {news_data}")
else:
    news_info = [(article["title"], article["description"]) for article in news_data["articles"]]


# check the stock vartiation
alpha_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_KEY}"
alpha_data = fetch_api_data(alpha_url)

if "Time Series (Daily)" not in alpha_data:
    print(f"Error: data not found. API response: {alpha_data}")
else:
    daily_data = alpha_data["Time Series (Daily)"]

    dates = list(daily_data.keys())[:2]

    if len(dates) < 2:
        print("Error: there is not enough data to compare.")
    else:
        yesterday = float(daily_data[dates[0]]["4. close"])
        before_yesterday = float(daily_data[dates[1]]["4. close"])

        percentual = round((yesterday - before_yesterday)/before_yesterday * 100)

        if abs(percentual) >= 5:
            send_sms(news_info, percentual)
        else:
            print("Variation less than 5%")