# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR src/
ENV FLASK_APP=importHTML.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]

RUN sudo apt-get install python3-dev libpq-dev
RUN pip3 install psycopg2
RUN sudo apt install -y postgresql postgresql-contrib postgresql-client
RUN sudo -u postgres psql -c "ALTER USER root PASSWORD 'admin';"
RUN sudo passwd postgres
   
FROM node:19-alpine
WORKDIR src/
COPY package.json yarn.lock ./src/
RUN npm install env
COPY . .
RUN yarn install --production
CMD ["node", "index.js"]
EXPOSE 3000

FROM postgres:15.2-bullseye
WORKDIR src/
COPY /database/SEO-UP.sql /database/SEO-UP.sql
RUN service start postgresql15