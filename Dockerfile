FROM python:3.5
COPY . src/weatherbot
WORKDIR src/weatherbot
RUN pip install -r requirements.txt
RUN python nltk_install.py
RUN python -m src.telegrambot
