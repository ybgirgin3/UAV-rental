FROM postgres:16.0-alpine

WORKDIR /db

ADD ./init.sql /docker-entrypoint-initdb.d/

RUN echo "CREATE DATABASE uav;" >> init.sql
RUN echo "CREATE USER admin WITH PASSWORD 'admin';" >> init.sql
RUN echo "GRANT ALL PRIVILEGES ON DATABASE uav TO admin;" >> init.sql

CMD [ "postgres" ]