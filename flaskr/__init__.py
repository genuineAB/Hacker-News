# from crypt import methods
import json
import os
from flask import Flask
from flask_restful import abort
from flask_cors import CORS
import requests
from models import News
from apscheduler.schedulers.background import BackgroundScheduler

from models import setup_db, News



 ## Job Scheduling
### Adding News to db
# @app.route('/news', methods=['POST'])
def sync_news():
    newsId = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()

    try:
        id = 0
        while id < 10:
            body = requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(newsId[id])+'.json?print=pretty').json()
            
            new_id = body["id"]
            new_time = body["time"]
            if "deleted" in body:
                new_deleted = body["deleted"]
            else:
                new_deleted = None
            new_type = body["type"]
            new_by = body["by"]
            if "dead" in body:
                new_dead = body["dead"]
            else:
                new_dead = None
            if "kids" in body:
                new_kids = body["kids"]
            else:
                new_kids = None
            if "parent" in body:
                new_parent = body["parent"]
            else:
                new_parent = None
            if "text" in body:
                new_text = body["text"]
            else: 
                new_text = None
            if "url" in body:
                new_url = body["url"]
            else:
                new_url = None
            new_title = body["title"]
            if "parts" in body:
                new_parts = body["parts"]
            else: 
                new_parts = None
            if "descedants" in body:
                new_descendants =body["descendants"]
            else:
                new_descendants = None
            if "score" in body:
                new_score = body["score"]
            else: 
                new_descendants = None
            
            new = News.query.filter_by(id=new_id).first()
            if new is None:
                print("Got Here")
                news = News(id=new_id, time=new_time, by=new_by, deleted=new_deleted, type=new_type, dead=new_dead, kids=new_kids, parent=new_parent, text=new_text, url=new_url, title=new_title, parts=new_parts, descendants=new_descendants, score=new_score)
                news.insert() 
            else:
                print("Viola")   
            
            id += 1
        return {
            "success": True
        }
    except:
        abort(404, "Not Found")

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(sync_news,'interval',minutes=5)
scheduler.start()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    
    ## Implementing controlled Access
    CORS(app, resources={r"*": {"origins": ['http://localhost:5000', 'http://localhost:3000']}})
    
    
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        response.headers.add("Access-Control-Allow-Credentials", "true")
        return response
    
    ## Get News Endpoint
    @app.route('/news', methods=['GET'])
    def get_news():
        newsId = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()
        
        print(newsId[499])
        print((len(newsId)-1))
        
        
        
        if not newsId :
            return(404, 'News not found')
        
        for id in newsId:
            print(requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(id)+'.json?print=pretty').json())
        # print(requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(32741800)+'.json?print=pretty').json())
            
        return "Got Here"
    
   
            
        
        
        
        
        
    
    return app