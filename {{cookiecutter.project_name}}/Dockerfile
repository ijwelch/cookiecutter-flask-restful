FROM python:3.7-alpine3.8

# install environment dependencies
# RUN apt-get update -yqq \
#   && apt-get install -yqq --no-install-recommends \
#     netcat \
#   && apt-get -q clean

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add app
COPY . /usr/src/app

RUN set -e; \
  apk add --no-cache --virtual .build-deps \
  gcc \
  libc-dev \
  linux-headers \
  ; \
  pip install pipenv && \
  pipenv install --system --deploy; \
  apk del .build-deps;

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# run server
CMD ["./entrypoint.sh"]
