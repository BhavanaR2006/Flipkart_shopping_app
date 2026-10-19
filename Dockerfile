FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk tk xvfb x11vnc novnc websockify fluxbox procps \
    && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 6080

CMD ["bash", "-c", "export DISPLAY=:1; Xvfb :1 -screen 0 1280x800x24 & sleep 2; fluxbox & sleep 2; x11vnc -display :1 -forever -shared -nopw -listen 0.0.0.0 -rfbport 5900 -noxdamage & sleep 2; websockify --web=/usr/share/novnc/ 0.0.0.0:6080 127.0.0.1:5900 & exec python customer_login.py"]