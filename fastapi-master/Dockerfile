# syntax=docker/dockerfile:1
FROM python:3.9 as builder
ENV DEBIAN_FRONTEND=noninteractive
ENV VIRTUAL_ENV=/venv
WORKDIR /source

RUN apt-get update && \
    apt-get --no-install-recommends install -y gettext locales-all tzdata build-essential gcc curl git

RUN python -m venv $VIRTUAL_ENV
ENV PATH=$VIRTUAL_ENV/bin:$PATH
COPY ./requirements.txt /source/
RUN pip install --no-cache-dir --upgrade -r /source/requirements.txt

FROM python:3.9-slim-bullseye as runner
ENV PYTHONUNBUFFERED 1
ENV USERNAME fa
ENV VIRTUAL_ENV=/venv
WORKDIR /source

COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV
ENV PATH=$VIRTUAL_ENV/bin:$PATH

RUN adduser --disabled-password --gecos ""  $USERNAME && id $USERNAME
RUN echo export PYTHON_PATH=/usr/local/bin/python >> /home/$USERNAME/.profile

COPY ./app /source/app

COPY ./entrypoint.sh /entrypoint.sh
CMD /entrypoint.sh
#CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
