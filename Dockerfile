FROM alpine:3.10.3

LABEL maintainer="Claick Oliveira <@gmail.com>" \
      version="0.1.0"

RUN apk add --no-cache bash py3-pip && \
    pip3 install --upgrade pip

RUN adduser -D app
USER app
ENV APP_PATH /home/app
WORKDIR ${APP_PATH}

COPY --chown=app:app python_api ${APP_PATH}
COPY --chown=app:app requirements.txt ${APP_PATH}/requirements.txt

RUN pip3 install --user -r requirements.txt

ENV PATH="${APP_PATH}/.local/bin:${PATH}"

ENTRYPOINT ["gunicorn", "--bind"]

CMD ["0.0.0.0:5000", "wsgi:app"]
