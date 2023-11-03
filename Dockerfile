FROM python:3.9-slim-buster

# Install binutils package
RUN apt-get update && apt-get install -y binutils

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["pyinstaller", "switcher.py"]