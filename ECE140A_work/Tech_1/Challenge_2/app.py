# Necessary Imports
from fastapi import FastAPI                 # The main FastAPI import
from fastapi.responses import HTMLResponse  # Used for returning responses
import uvicorn                              # Used for running the app
from fastapi.staticfiles import StaticFiles

# Configuration
app = FastAPI()               # Specify the "app" that will run the routing
# Mount the static directory
app.mount("/public", StaticFiles(directory="public"), name="static")

# Example route: return a simple static webpage
# Example route: return a static HTML page
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
  with open("index.html") as html:
    return HTMLResponse(content=html.read())

# Running the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)
