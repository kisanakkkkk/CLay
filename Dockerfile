FROM python:3.11.5

RUN apt update

ADD . /CLay/

WORKDIR /CLay

RUN pip install . --no-cache-dir 

ENTRYPOINT ["CLay"]
