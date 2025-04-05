FROM python:3.9-slim

   WORKDIR /app
   COPY . .

   RUN pip install -r requirements.txt

   CMD gunicorn --bind 0.0.0.0:$PORT app:app & python3 main.py
