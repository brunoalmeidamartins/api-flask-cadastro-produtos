FROM python:3.6.11-stretch
RUN apt-get update && apt-get upgrade -y
RUN mkdir -p /app/
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY api /app/api
#COPY migrations /app/migrations
COPY config_docker.py /app/config.py
COPY run.py /app/run.py
COPY wait-for-it.sh /app/wait-for-it.sh
COPY deploy.sh /app/deploy.sh
RUN chmod +x wait-for-it.sh && chmod +x deploy.sh
#ENV FLASK_APP=/app/api/__init__.py
#RUN flask routes
#RUN flask db migrate && flask db upgrade
#ENTRYPOINT [ "sh", "/app/wait-for-it.sh", "--host=mysqlsrv", "--port:3306", "--", "./app//migrate.sh" ]
#ENTRYPOINT [ "sh", "/app/migrate.sh" ]
EXPOSE 5000
CMD ["sh", "deploy.sh"]