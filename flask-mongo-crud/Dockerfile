FROM python:3.9

RUN mkdir -p /app 
WORKDIR /app
COPY . .

# Set the timezone to Philippines
RUN echo "Asia/Manila" > /etc/timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Manila /etc/localtime

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
