FROM ubuntu:18.04

RUN apt-get update -y  && apt-get install -y python3 python3-pip

COPY . .

WORKDIR /app

RUN pip3 install Flask && python3 -m pip install requests

COPY ./src /app

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["proxy.py"]
