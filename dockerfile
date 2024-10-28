
ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}-slim

SHELL ["/bin/bash", "-c"]

RUN mkdir -p /opt/lambda/src

RUN apt update && \
  apt install curl \
  nano \
  zip \
  unzip \
  tzdata \
  sudo -y 

WORKDIR /opt/lambda/src

COPY ./requirements.txt /opt/lambda

RUN pip install -U pip --no-cache-dir && \
  pip install --no-cache-dir -r /opt/lambda/requirements.txt

CMD ["tail", "-f", "/dev/null"]
