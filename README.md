# HACKER NEWS

Have you ever heard of Hacker News? It's a great source of tech-related news. They provide a public API at https://hackernews.api-docs.io.

This project's goal is to make a web app to make it easier to navigate the news.

## Installing Dependences

    1. Python 3.7 - Follow instructions to install the latest version of python for your platform in the python docs

   2. Virtual Environment - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the python docs

    3. PIP Dependencies - Once your virtual environment is setup and running, install the required dependencies:

    ```
    pip install -r requirements.txt
    
    ```

## SETUP DATABASE
    The database used for this application is postgresql. With Postgres running, create a hacker_news database:

    ```
    CREATE DATABASE hacker_news

    ```

## RUN THE SERVER
    From within the ./src directory first ensure you are working using your created virtual environment.

To run the server, execute:
```
export FLASK_APP=flaskr
export FLASK_DEBUG=1
flask run

```


## API REFERENCE

### GETTING STARTED
    Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/.

    Authentication: This version of the application does not require authentication or API keys



### ENDPOINTS

#### GET /news
    General:
        Returns a list of questions in the database.
        For documentation purpose, results are paginated in groups of 5. This can be adjsted to suit your use
        Sample: GET http://127.0.0.1:5000/news {
            {
                "News": [
                    {
                        "by": "Chinedu Oguejiofor",
                        "created": true,
                        "dead": false,
                        "deleted": false,
                        "descendants": null,
                        "id": 1,
                        "kids": 123113,
                        "parent": 134645737,
                        "parts": 2,
                        "score": 25462,
                        "text": "This is the story of how I transitioned from an instructor to a software engineer",
                        "time": 142546232,
                        "title": "Stories that touch",
                        "type": "Story",
                        "url": "https://google.com"
                    },
                    {
                        "by": "Chinedu Oguejiofor",
                        "created": true,
                        "dead": false,
                        "deleted": false,
                        "descendants": null,
                        "id": 12345,
                        "kids": 123113,
                        "parent": 134645737,
                        "parts": 2,
                        "score": 25462,
                        "text": "This is the story of how I transitioned from an instructor to a software engineer",
                        "time": null,
                        "title": "Stories that touch",
                        "type": "Story",
                        "url": "https://google.com"
                    },
                    {
                        "by": "gmays",
                        "created": false,
                        "dead": null,
                        "deleted": null,
                        "descendants": null,
                        "id": 32791978,
                        "kids": [
                            32810356,
                            32806992,
                            32809265,
                            32806608,
                            32809927,
                            32809821,
                            32806338,
                            32806365,
                            32807242,
                            32807414,
                            32806834
                        ],
                        "parent": null,
                        "parts": null,
                        "score": 169,
                        "text": null,
                        "time": 1662826799,
                        "title": "A look inside Feynman’s calculus notebook",
                        "type": "story",
                        "url": "https://physicstoday.scitation.org/do/10.1063/PT.5.9099/full/"
                    },
                    {
                        "by": "0x54MUR41",
                        "created": false,
                        "dead": null,
                        "deleted": null,
                        "descendants": null,
                        "id": 32800027,
                        "kids": [
                            32810500,
                            32809908,
                            32810391,
                            32810444,
                            32810054,
                            32805944,
                            32810405,
                            32810320,
                            32803229
                        ],
                        "parent": null,
                        "parts": null,
                        "score": 19,
                        "text": null,
                        "time": 1662907596,
                        "title": "Can the American mall survive?",
                        "type": "story",
                        "url": "https://newrepublic.com/article/167260/can-american-mall-survive"
                    },
                    {
                        "by": "rtpg",
                        "created": false,
                        "dead": null,
                        "deleted": null,
                        "descendants": null,
                        "id": 32807903,
                        "kids": [
                            32809107,
                            32808184,
                            32808326,
                            32808511,
                            32808688
                        ],
                        "parent": null,
                        "parts": null,
                        "score": 98,
                        "text": null,
                        "time": 1662976556,
                        "title": "Exploring FPGA Graphics",
                        "type": "story",
                        "url": "https://projectf.io/posts/fpga-graphics/"
                    }
                ]
            }
        }


#### POST /news
    General:
        This endpoint creates a new news using the provided information from the request's json body. 
        It returns true when successful
        Sample: POST http://127.0.0.1:5000/news {
            {
                "id": 123457,
                "deleted": false,
                "dead": false,
                "kids": 123113,
                "parent": 134645737,
                "url": "https://google.com",
                "title": "Story of my life",
                "parts": 2,
                "descendant": 1323542,
                "score": 25462,
                "type": "Story",
                "by": "Olumide Bakare",
                "text": "This is the story of how I transitioned from an instructor to a software engineer"
            } {
            "success": true }
        }

#### POST /news
    General:
        Returns a list of question that has the search substring, and a success value.
        Sample: POST http://127.0.0.1:5000/news {
            {
                "search_term": "story"
            } {
            {
                "News": [
                    {
                        "by": "Chinedu Oguejiofor",
                        "created": true,
                        "dead": false,
                        "deleted": false,
                        "descendants": null,
                        "id": 1,
                        "kids": 123113,
                        "parent": 134645737,
                        "parts": 2,
                        "score": 25462,
                        "text": "This is the story of how I transitioned from an instructor to a software engineer",
                        "time": 142546232,
                        "title": "Stories that touch",
                        "type": "Story",
                        "url": "https://google.com"
                    },
                    {
                        "by": "Chinedu Oguejiofor",
                        "created": true,
                        "dead": false,
                        "deleted": false,
                        "descendants": null,
                        "id": 12345,
                        "kids": 123113,
                        "parent": 134645737,
                        "parts": 2,
                        "score": 25462,
                        "text": "This is the story of how I transitioned from an instructor to a software engineer",
                        "time": null,
                        "title": "Stories that touch",
                        "type": "Story",
                        "url": "https://google.com"
                    },
                    {
                        "by": "Olumide Bakare",
                        "created": true,
                        "dead": false,
                        "deleted": false,
                        "descendants": null,
                        "id": 123457,
                        "kids": 123113,
                        "parent": 134645737,
                        "parts": 2,
                        "score": 25462,
                        "text": "This is the story of how I transitioned from an instructor to a software engineer",
                        "time": null,
                        "title": "Story of my life",
                        "type": "Story",
                        "url": "https://google.com"
                    }
                ]
            }
        }


#### PUT /api/contacts/<int:news_id>
    General:
        This endpoint makes it possible to update the details of a news, it takes the id of the contact to be updated, check to see if it is was created locally or retrieved from hacker news API.
        News will only be updated if it is not retrieved from hacker news API
        It returns a success value. The header key we use is Content-Type with a value of application/json. This is best done with a postman app. 
        Sample: PATCH http://127.0.0.1:5000/news/12345 {{
                "text": "This is is my story"
            }} {
                "msg": "News Updated",
                "success": true
            }
        }

        Sample: PATCH http://127.0.0.1:5000/news/12345 {{
                "text": "This is is my story"
            }} {
                "error": 405,
                "message": "Method Not Allowed",
                "success": false
            }
        }

#### DELETE /api/contacts/<int:news_id>
    General:
        This endpoint makes it possible to delete a news, it requires the id of the news to be deletedd, a check is performed to see if it is was created locally or retrieved from hacker news API.
        News will only be deleted if it is not retrieved from hacker news API It returns a News deleted message. This is best done with a postman app. 
        Sample: DELETE http://127.0.0.1:5000/12345 { {
            "success": true
            }
        }
        Sample: DELETE http://127.0.0.1:5000/32809833 { {
            "error": 422,
            "message": "Could not process request",
            "success": fals
            }
        }
