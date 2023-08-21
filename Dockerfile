FROM python:latest
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app 
EXPOSE 3000
CMD ["python3", "app.py"]
