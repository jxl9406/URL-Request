import requests
from send_email import send_email

topic = "Tesla"

api_key = "830bc471befb4d6e9ca35c306b2119fd"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2024-05-07&sortBy=publishedAt&" \
       "apiKey=830bc471befb4d6e9ca35c306b2119fd&" \
       "language=en"

#Make request
request = requests.get(url)

#Get a dictionary
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article['title'] is not None:
        body = "subject: Today's news " \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
