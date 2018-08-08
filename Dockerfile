FROM ubuntu:16.04

LABEL maintainer="nithoalif@bukalapak.com" \
      description="vitess test environment"

ENV VTTOP="/vt" \
    VTROOT="/vt" \
    USER="vitess" \
    MYSQL_FLAVOR="MySQL56"

COPY vt /vt

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python2.7-minimal python-pip mysql-server-5.7 libmysqlclient-dev && \
    mkdir -p /vt/sbin /vt/lib && \
    ln -s /usr/bin/mysql* /vt/sbin && \
    ln -s /usr/sbin/mysqld /vt/sbin && \
    ln -s /usr/lib/mysql /vt/lib/mysql && \
    pip install protobuf mysql-python && \
    cd /vt/py && python /vt/py/setup.py build install && \
    groupadd -r $USER && \
    useradd -m -r -g $USER $USER && \
    chown -R $USER:$USER /vt

USER $USER:$USER

EXPOSE 12345 12346 12347 12348

ENTRYPOINT ["/vt/start.sh"]
