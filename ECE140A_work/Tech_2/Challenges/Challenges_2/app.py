# Necessary Imports
from urllib.request import Request, urlopen
from fastapi import FastAPI, Request, Form
import json
from fastapi import FastAPI                   # The main FastAPI import
from fastapi.responses import HTMLResponse    # Used for returning HTML responses
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles   # Used for serving static files
import uvicorn                                # Used for running the app


'''
Company name    companyName
Industry        industry
Sector          sector
Stock price     price
'''




# Configuration
app = FastAPI()                   # Specify the "app" that will run the routing

 # Mount the static directory
app.mount("/public", StaticFiles(directory="public"), name="static")


# Example route: return a static HTML page
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("index.html") as html:
        return HTMLResponse(content=html.read())


@app.post("/stock")
def post_form(request: Request, 
stock1: str = Form(...), 
stock2: str = Form(...), 
stock3: str = Form(...) ):

    # define API key
    """
    INSTANTIATE THIS VARIABLE WITH YOUR API KEY
    """
    api_key = "fea958093b903a386e10fae9328e6f4d"

    # create url link
    url1 = 'https://financialmodelingprep.com/api/v3/profile/' + stock1 + '?apikey=' + api_key
    url2 = 'https://financialmodelingprep.com/api/v3/profile/' + stock2 + '?apikey=' + api_key
    url3 = 'https://financialmodelingprep.com/api/v3/profile/' + stock3 + '?apikey=' + api_key

    # store the response of URL
    stock1response = urlopen(url1)
    stock2response= urlopen(url2)
    stock3response = urlopen(url3)

    # store the JSON response from URL
    data_json1 = json.loads(stock1response.read())
    data_json2 = json.loads(stock2response.read())
    data_json3 = json.loads(stock3response.read())


    # make 3 len conditions for stocks 
    # check if empty thus invalid stock symbol
    if len(data_json1) == 0:
        return {}


    # return 3 json data sets for parsing 
    # return json data
    # app state for storing global variables 
    return data_json



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)