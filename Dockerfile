# Dockerfile

## Base Image
FROM python:3.12

## Working Directory
WORKDIR <dir-name>

## Copy
COPY . <dir-name>

## Run
RUN pip install -r requirements.txt

## Port
EXPOSE <port-nums>

## Command 
CMD <command-to-run-application>