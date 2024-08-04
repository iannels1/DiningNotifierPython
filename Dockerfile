FROM python:3.11-slim
LABEL authors="Ian Nelson"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "DiningNotifier/main.py"]
