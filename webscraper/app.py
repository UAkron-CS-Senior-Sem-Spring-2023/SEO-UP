#!/usr/bin/python3

# import library
import traceback
import psycopg2
from bs4 import BeautifulSoup
from flask import request
import requests
import re
from pytrends.request import TrendReq

from flask import Flask

app = Flask(__name__)

@app.route("/")
def status():
    return "Hello world", 200

def connect(word):
    """ Connect to the PostgreSQL database server """

    conn = None
    try:
    # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(user="admin", database="postgres", password="admin", host="postgres", port=5432)
        conn.autocommit = True

    # create a cursor
        cur = conn.cursor() 
        
    # execute a statement
    # write to table
        print('Connected to Database. Executing Query: ')
        
    # delete exisitng table, create, insert, show that it is inserted
        cur.execute("DROP TABLE IF EXISTS keywords;")
        cur.execute("CREATE TABLE IF NOT EXISTS keywords(first_keyword CHAR (45));")
        cur.execute("INSERT INTO keywords VALUES(%s);", (word,))
        cur.execute("SELECT * FROM keywords;")
        database = cur.fetchall()

    # close the communication with the PostgreSQL
        cur.close()

        for x in database:
            print(x)
        
        return word

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.\n')

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
        try:
            req = requests.get(url)
            req.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error while fetching URL: {e}", flush=True)
            return "", 500
        soup = BeautifulSoup(req.text, "lxml")
        words = []
        if soup.head:
            title = (
                soup.title.string
                if soup.title != None and soup.title.string != None
                else ""
            )
            wordOutput = re.findall(r"\w+", title)
            for word in wordOutput:
                if word not in words:
                    words.append(word)
                    connect(word)
        if soup.body:
            for paragraph in soup.find_all("p"):
                wordOutput = re.findall(r"\w+", paragraph.text)
                for word in wordOutput:
                    if word not in words:
                        words.append(word)
        for word in words.copy():
            if re.match(r'^\d+$', word) or len(word) < 3:
                words.remove(word)
        trendMean = [];
        for index, word in zip(range(50), words):
            kw_list = [word]
            pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='', gprop='')
            data = pytrends.interest_over_time()
            trendMean.append(int(data.mean().values[0]))
        return {"words": words, "trendMean": trendMean}, 200

    except Exception:
        error = traceback.format_exc()
        print(error, flush=True)
        return "", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
