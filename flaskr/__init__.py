from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    
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