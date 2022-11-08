FROM python:3.10
WORKDIR /bot
COPY requriments.txt /bot/
run pip install requriments.txt
COPY . ./bot
CMD python socs_scraping.py
CMD python bot.py