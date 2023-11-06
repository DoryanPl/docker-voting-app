# gunicorn_config.py
bind = "0.0.0.0:8080"
errorlog = "-"
accesslog = "-"
workers = 4
keepalive = 0
