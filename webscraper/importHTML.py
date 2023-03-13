#!/usr/bin/python3

# import library
from bs4 import BeautifulSoup
import requests
import os.path
from os import path
import re
from collections import Counter
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

# Request to website and download HTML contents
url='https://www.etsy.com/?utm_source=google&utm_medium=cpc&utm_term=etsy_e&utm_campaign=Search_US_Brand_GGL_ENG_General-Brand_Core_All_Exact&utm_ag=A1&utm_custom1=_k_Cj0KCQiAi8KfBhCuARIsADp-A54MzODz8nRIxO2LnGcB8Ezc3_q40IQk9HygcSzz9fPmPWnrITz8InQaAt5oEALw_wcB_k_&utm_content=go_227553629_16342445429_536666953103_kwd-1818581752_c_&utm_custom2=227553629&gclid=Cj0KCQiAi8KfBhCuARIsADp-A54MzODz8nRIxO2LnGcB8Ezc3_q40IQk9HygcSzz9fPmPWnrITz8InQaAt5oEALw_wcB'

with requests.get(url) as req:
	req.raise_for_status()
	soup = BeautifulSoup(req.text, 'lxml')
	file = open("testOutput.txt", "w")
	file.write(soup.prettify())
	if (head := soup.head):
		titleWords = Counter()
		wordOutput = re.findall(r'\w+', soup.title.string)
		for word in wordOutput:
			titleWords[word] += 1
	if (body := soup.body):
		paragraphWords = Counter()
		for paragraph in soup.find_all('p'):
			wordOutput = re.findall(r'\w+', paragraph.text)
			for word in wordOutput:
				paragraphWords[word] += 1
	print(titleWords)