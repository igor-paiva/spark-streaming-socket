FROM python:3.7-slim
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

WORKDIR /code

COPY . ./

RUN pip3 install essential-generators

CMD python3 main.py
