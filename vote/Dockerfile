FROM python:3.12-alpine
RUN adduser -D py
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
USER py
COPY --chown=py:py . .
EXPOSE 8080
CMD ["gunicorn", "app:app", "-c", "gunicorn_config.py"]


