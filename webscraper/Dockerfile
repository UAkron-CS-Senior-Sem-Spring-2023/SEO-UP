# Setup python and clear cache
FROM python:3.10-bullseye as base
WORKDIR /app
RUN python -m pip install --no-cache --upgrade pip pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv lock && pipenv --clear && pipenv --rm
RUN pipenv install --clear --system

COPY *.py /app/

FROM base as dev
CMD ["python", "-u", "app.py"]
