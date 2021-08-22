FROM python:3.9-slim
LABEL maintainer="manuel.bovo@gmail.com"

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y curl=* git=* \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p /app

WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir -e .
ENTRYPOINT ["./entrypoint.sh"]
