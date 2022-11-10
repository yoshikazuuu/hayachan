FROM python:3.10
WORKDIR /bot
COPY requirements.txt /bot/
run pip install requirements.txt
COPY . ./bot
CMD python socs_scraping.py
CMD python bot.py