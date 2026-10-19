FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY web_app.py .

EXPOSE 6080

CMD ["python", "web_app.py"]