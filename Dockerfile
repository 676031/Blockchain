from ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-dev python3-pip

WORKDIR /app

COPY . /app

RUN pip3 install -r requirments.txt

EXPOSE 8000

ENTRYPOINT ["python3"]
CMD ["main.py"]