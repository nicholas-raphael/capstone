FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update &&\
    apt-get install -y libpq-dev python3-dev --no-install-recommends &&\ 
    apt-get clean &&\ 
    rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app

#copy files
COPY __init__.py /app/__init__.py
COPY requirements /app/requirements
COPY main.py /app/main.py
COPY deployment.yml deployment.yml
COPY entrypoint.sh /app/entrypoint.sh

# install dependencies
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements/base.txt

RUN useradd --create-home --shell /bin/bash user
USER user

## Step 5:
# Run app.py at container launch
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

#ENTRYPOINT ["sh", "entrypoint.sh"]