# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /src
ENV FLASK_APP=importHTML.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
   
FROM node:19-alpine
WORKDIR /src
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000