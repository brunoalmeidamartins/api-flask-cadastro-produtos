FROM python:3.6.11-stretch
RUN apt-get update && apt-get upgrade -y
COPY api /var/www/
COPY migrations /var/www/
COPY config_docker.py /var/www/config.py
COPY requirements.txt /var/www/requirements.txt
COPY run.py /var/www/run.py
WORKDIR /var/www
RUN pip install -r /var/www/requirements.txt
RUN export FLASK_API=/var/www/api/__init__.py && flask db init && flask db migrate && flask db upgrade
EXPOSE 5000
CMD ["python", "run.py"]