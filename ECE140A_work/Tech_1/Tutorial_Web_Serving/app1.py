# Necessary Imports
from fastapi import FastAPI                   # The main FastAPI import
from fastapi.responses import HTMLResponse    # Used for returning HTML responses
from fastapi.staticfiles import StaticFiles   # Used for serving static files
import uvicorn                                # Used for running the app

# Configuration
app = FastAPI()                   # Specify the "app" that will run the routing
 # Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Example route: return a static HTML page
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
  with open("index.html") as html:
    return HTMLResponse(content=html.read())


# Example route: returning just JSON
@app.get("/json/{name}")
def get_json(name:str) -> dict:
  return {"Hello": name}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)
