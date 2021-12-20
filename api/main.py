from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = False,
)

@app.get("/quote")
def quote():
    # TODO: Return a random quote
    quote = random.choice(open('quotes.txt').readlines())
    url = None
    attrib = None
    if " - " in quote:
        split = quote.split(" - ")
        quote = split[0]
        if "http" in split[1]:
            url = split[1]
        else:
            attrib = split[1]
    return {"quote": quote, "url": url, "attrib": attrib}

@app.get("/visit")
def visits():
    # TODO: Count each request to visits() and return the total
    return {"not yet implemented": "not yet implemented"}

@app.get("/status")
def status():
    # TODO: Query last.fm for the song I'm listening to at the moment
    return {"not yet implemented": "not yet implemented"}