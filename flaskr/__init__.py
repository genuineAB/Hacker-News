# from crypt import methods
import json
import os
from flask import Flask, request
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
            new_created = False
            new = News.query.filter_by(id=new_id).first()
            if new is None:
                print("Got Here")
                news = News(id=new_id, time=new_time, by=new_by, deleted=new_deleted, type=new_type, dead=new_dead, kids=new_kids, parent=new_parent, text=new_text, url=new_url, title=new_title, parts=new_parts, descendants=new_descendants, score=new_score, created=new_created)
                news.insert() 
            else:
                print("Viola")   
            
            id += 1
        return {
            "success": True
        }
    except:
        abort(404)

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(sync_news,'interval',minutes=5)
scheduler.start()


NEWS_PER_PAGE = 50

def paginate_news(selection):
    page = request.args.get('page', 1, type=int)
    start = (page  - 1) * NEWS_PER_PAGE
    end = start + NEWS_PER_PAGE

    news = [new_news.serialize() for new_news in selection]
    current_news = news[start:end]

    return current_news


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
        try:
            
            get_news = News.query.order_by(News.id).all()
            # print(get_news)
            
            if len(get_news) == 0 :
                abort(404)

            news = paginate_news(get_news)
            print(news)
            
            return {
                "News": news
            }

        except:
            abort(422)
   
            
        
        ## POST and SEARCH METHOD
        
    @app.route('/news', methods=['POST'])
    def post_news():
        body = request.get_json()

        new_id = body.get("id")
        new_time = body.get("time", None)
        new_deleted = body.get("deleted", None)
        new_type = body.get("type", None)
        new_by = body.get("by", None)
        new_dead = body.get("dead", None)
        new_kids = body.get("kids", None)
        new_parent = body.get("parent", None)
        new_text = body.get("text", None) 
        new_url = body.get("url", None)
        new_title = body.get("title", None)
        new_parts = body.get("parts", None)
        new_descendants =body.get("descendants", None)
        new_score = body.get("score", None)
        new_created = body.get("created")
        search = body.get("search_term", None)
        
        try:
            if search:
                
                news = News.query.order_by(News.id).filter(News.text.ilike("%{}%".format(search))).all()
                search_result = [new_news.serialize() for new_news in news]

                return ({
                    "News": search_result
                })
                
            else:
                news = News(id=new_id, time=new_time, by=new_by, deleted=new_deleted, type=new_type, dead=new_dead, kids=new_kids, parent=new_parent, text=new_text, url=new_url, title=new_title, parts=new_parts, descendants=new_descendants, score=new_score, created=new_created)
                news.insert() 
                
                return {
                    'success': True
                }
            
        except:
            abort(422, 'Got Here')
        
    ###
    @app.route('/news/<int:news_id>', methods=['DELETE'])
    def delete_news(news_id):
        try:
            news = News.query.filter(News.id==news_id).one_or_none() 
            print(news.created)
            
            if news is None:
                abort(404)
            
            if news.created != True:
                abort(405)
                
            news.delete()
            return {
                'success': True
            }
        except:
            return{
                abort(422)
            }
    
    
    ### Handling Errors
    @app.errorhandler(404)
    def not_found(error):
        return({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404
        
    @app.errorhandler(422)
    def unprocessable(error):
        return{
            'success': False,
            'error': 422,
            'message': 'Could not process request'
        },422

    @app.errorhandler(400)
    def bad_request(error):
        return{
            'success': False,
            'error': 400,
            'message': 'Bad Request, Make adjustment'
        },400
     
    @app.errorhandler(405)
    def not_allowed(error):
        return{
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed'
        }, 405
           
    @app.errorhandler(500)
    def internal_server_error(error):
        return{
            'success': False,
            'error': 500,
            'message': 'Server Currently Down'
        }, 500
        
    
    return app