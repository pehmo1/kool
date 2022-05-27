FROM ubuntu

RUN apt update && apt install -y python3 python3-pip
RUN pip3 install -U autopep8 requests
COPY ./main.py /opt

WORKDIR /opt