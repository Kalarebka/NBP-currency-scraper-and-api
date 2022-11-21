FROM python:3.10

RUN useradd --create-home celery
USER celery
ENV PATH="/home/celery/.local/bin:${PATH}"

WORKDIR /home/celery
ADD requirements.txt .
RUN pip install -r requirements.txt

COPY ./currency_scraper ./currency_scraper
COPY celeryconfig.py .