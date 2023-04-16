#!/usr/bin/python3

# import library
import traceback
from bs4 import BeautifulSoup
from flask import request
import requests
import re
from collections import Counter
from pytrends.request import TrendReq
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def status():
    return "Hello world", 200

@app.route("/api/webscraper/parse", methods=["POST"])
def parse_website():
    try:
        payload = request.get_json()
        if payload == None:
            return "", 400
        url = payload.get("url")
        if url == None:
            return "", 400
        pytrends = TrendReq(hl="en-US", tz=360)
        # Request to website and download HTML contents
        req = requests.get(url)
        req.raise_for_status()
        soup = BeautifulSoup(req.text, "lxml")
        titleWords = Counter()
        if soup.head:
            title = (
                soup.title.string
                if soup.title != None and soup.title.string != None
                else ""
            )
            wordOutput = re.findall(r"\w+", title)
            for word in wordOutput:
                titleWords[word] += 1
        if soup.body:
            paragraphWords = Counter()
            for paragraph in soup.find_all("p"):
                wordOutput = re.findall(r"\w+", paragraph.text)
                for word in wordOutput:
                    paragraphWords[word] += 1
        print(titleWords, flush=True)
        return {"words": titleWords}, 200

    except Exception:
        error = traceback.format_exc()
        print(error, flush=True)
        return "", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
