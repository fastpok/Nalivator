# Наливатор
Ориентируемся на этот проект:
https://www.hackster.io/hackershack/smart-bartender-5c430e

## Наш сайт:
https://www.nalivator.tech

## Полезные команды
Запустить сервер
```
# gunicorn --worker-class eventlet -w 1 --certfile /etc/letsencrypt/live/nalivator.tech/fullchain.pem --keyfile /etc/letsencrypt/live/nalivator.tech/privkey.pem -b 0.0.0.0:443 nalivator:app
```
