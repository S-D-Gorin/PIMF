
# Chat Police

FROM python:3.11

COPY ./bot /opt/bot
WORKDIR /opt/bot
RUN pip install --no-cache-dir -r requirements.txt
ADD ./bot /opt

CMD ["python", "bot.py"]