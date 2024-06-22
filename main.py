# Server
import uvicorn
from fastapi import FastAPI
from country_guesser import country_guess
from fastapi.responses import HTMLResponse

app = FastAPI()

IMAGE_PATH = "pictures\\sample 01.jpg"
HTML_CONTENT = "<b>I'm a bold text<b>"


@app.get("/guess_country/")
def guess_country():
    result =  country_guess(IMAGE_PATH)
    return {"country_guess": result}


@app.get("/geo_genie/", response_class=HTMLResponse)
def serve_html():
    return HTMLResponse(content=HTML_CONTENT)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
