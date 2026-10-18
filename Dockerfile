FROM python:3.11-slim

RUN apt-get update && apt-get install -y python3-tk tk xvfb && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

CMD ["xvfb-run", "-a", "python", "customer_login.py"]