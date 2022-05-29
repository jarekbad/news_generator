import requests
from bs4 import BeautifulSoup

# Showing the 20 best stories from hacker_news
def hacker_news():
    response_beststories = requests.get("https://hacker-news.firebaseio.com//v0/beststories.json?print=pretty")
    data_beststories = response_beststories.json()
    beststories = []
    for i in range(20):
        response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{data_beststories[i]}.json?print=pretty")
        data_beststory = response.json()
        story = {}
        story["title"] = data_beststory["title"]
        try:
            story["url"] = data_beststory["url"]
        except:
            story["url"] = "no url"
        finally:
            beststories.append(story)
    return beststories


def find_article_from_Hacker_News(num_of_pages, limit_score):
    """
    The function scrap data from Hacker News (the specified number of pages - num_of_pages):
    - the title of the article,
    - the link to the article,
    - and the number of votes of the article.
    Then it selects those articles that have the appropriate number of votes (limit_score)
    and returns the sorted result (from the most popular).
    """
    num_of_pages_to_scrap = num_of_pages + 1
    sum_title_link_from_page = []
    sum_score_from_page = []
    for i in range(1, num_of_pages_to_scrap):
        response = requests.get(f"https://news.ycombinator.com/news?p={i}")
        soup = BeautifulSoup(response.text, "html.parser")
        title_link_from_page = soup.select(".titlelink")
        score_from_page = soup.select(".subtext")
        sum_title_link_from_page += title_link_from_page
        sum_score_from_page += score_from_page
    articles = []
    for i, article in enumerate(sum_title_link_from_page):
        article_title = article.getText()
        article_link = article.get("href", None)
        article_score_check = sum_score_from_page[i].select(".score")
        if len(article_score_check):
            article_score = int(article_score_check[0].getText().split()[0])
            if article_score > limit_score:
                articles.append({"title": article_title, "link": article_link, "score": article_score})
    return sorted(articles, key= lambda k:k["score"], reverse=True)


def polish_news():
    response = requests.get("https://newsapi.org/v2/top-headlines?country=pl&apiKey=4e94fc1519d44c308dbd5e1a648e6fd4")
    data = response.json()
    article_titles = []
    article_descriptions = []
    article_urls = []
    article_urls_to_images = []
    article_dates = []

    for element in data["articles"]:
        article_title = element["title"]
        article_titles.append(article_title)
        article_description = element["description"]
        article_descriptions.append(article_description)
        article_url = element["url"]
        article_urls.append(article_url)
        article_urls_to_image = element["urlToImage"]
        article_urls_to_images.append(article_urls_to_image)
        article_date = element["publishedAt"].replace("Z","")
        article_date_change = article_date.replace("T", " ")
        article_dates.append(article_date_change)

    results = []
    for i in range(len(article_titles)):
        result = {}
        result["title"] = article_titles[i]
        result["description"] = article_descriptions[i]
        result["url"] = article_urls[i]
        result["urlimage"] = article_urls_to_images[i]
        result["date"] = article_dates[i]
        results.append(result)

    return  results


def world_news(key_word):
    url = ('https://newsapi.org/v2/everything?'
           f'q={key_word}&'
           'from=2022-01-26&'
           'sortBy=popularity&'
           'apiKey=4e94fc1519d44c308dbd5e1a648e6fd4')
    response = requests.get(url)
    data = response.json()
    article_titles = []
    article_descriptions = []
    article_urls = []
    article_urls_to_images = []
    article_dates = []

    for element in data["articles"]:
        article_title = element["title"]
        article_titles.append(article_title)
        article_description = element["description"]
        article_descriptions.append(article_description)
        article_url = element["url"]
        article_urls.append(article_url)
        article_urls_to_image = element["urlToImage"]
        article_urls_to_images.append(article_urls_to_image)
        article_date = element["publishedAt"].replace("Z", "")
        article_date_change = article_date.replace("T", " ")
        article_dates.append(article_date_change)

    results = []
    for i in range(len(article_titles)):
        result = {}
        result["title"] = article_titles[i]
        result["description"] = article_descriptions[i]
        result["url"] = article_urls[i]
        result["urlimage"] = article_urls_to_images[i]
        result["date"] = article_dates[i]
        results.append(result)

    return results
