FROM python:3
ENV PYTHONUNBUFFERED 0
RUN pip install --upgrade pip
COPY .. /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD flask run --host=0.0.0.0 --port=5000