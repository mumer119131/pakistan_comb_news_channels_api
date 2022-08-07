import requests
from bs4 import BeautifulSoup
baseUrls = {
    "samma" : {
        "url" : "https://www.samaa.tv/",
        "class" : "story__title"
    } ,
    "jang" : {
        "url" : "https://jang.com.pk/",
        "class" : "main-heading"
    } ,
    "ary" :{
        "url" : "https://arynews.tv/",
        "class" : "entry-title"
    } ,
    "92-News" :{
        "url" : "https://92newshd.tv/latest-news",
        "class" : "title"
    } , 
    "sports" :{
        "url" : "https://www.bolnews.com/sports/",
        "class" : "title"
    } 
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

def scrape_news():
    all_news = dict()
    for web_name in baseUrls:
        response = requests.get(baseUrls[web_name]["url"], headers= headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_list = []
        
        news_ele_list =  soup.find_all(class_=baseUrls[web_name]["class"])
            
        for news in news_ele_list:
            news_list.append(news.text.strip())

        all_news[web_name] = news_list
    
    return all_news


scrape_news()