from urllib.request import urlopen
import json

from fastapi import FastAPI, Request, Form
from fastapi.responses import Response
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI()

# Example route: returns JSON
@app.post("/stock")
def post_form(request: Request, symbol: str = Form(...)):
    # define API key
    """
    INSTANTIATE THIS VARIABLE WITH YOUR API KEY
    """
    api_key = "fea958093b903a386e10fae9328e6f4d"

  # create url link
    url = 'https://financialmodelingprep.com/api/v3/profile/' + symbol + '?apikey=' + api_key


    # store the response of URL
    response = urlopen(url)


    # store the JSON response from URL
    data_json = json.loads(response.read())


    # check if empty thus invalid stock symbol
    if len(data_json) == 0:
        return {}


    # return json data
    return data_json


# Example route: return a HTML page
@app.get("/", response_class=HTMLResponse)

def get_html() -> HTMLResponse:
    with open("index.html") as html:
        return HTMLResponse(content=html.read())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)
