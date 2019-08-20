FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /procode
WORKDIR /procode
COPY requirements.txt /procode/
RUN pip install -r requirements.txt
COPY . /procode/


