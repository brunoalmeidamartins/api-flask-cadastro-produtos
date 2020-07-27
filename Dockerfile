FROM python:3.6.11-stretch
RUN apt-get update && apt-get upgrade -y
RUN mkdir -p /app/
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY api /app/api
COPY config_docker.py /app/config.py
COPY run.py /app/run.py
COPY deploy.sh /app/deploy.sh
RUN chmod +x deploy.sh
EXPOSE 5000
CMD ["sh", "deploy.sh"]