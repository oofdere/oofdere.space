from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/visit")
def visits():
    # TODO: Count each request to visits() and return the total
    return {"not yet implemented": "not yet implemented"}

@app.get("/quote")
def quote():
    # TODO: Return a random quote
    return {"not yet implemented": "not yet implemented"}

@app.get("/status")
def status():
    # TODO: Query last.fm for the song I'm listening to at the moment
    return {"not yet implemented": "not yet implemented"}