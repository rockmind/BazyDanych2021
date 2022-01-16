FROM postgres:14.1-alpine

ADD https://raw.githubusercontent.com/pthom/northwind_psql/master/northwind.sql /docker-entrypoint-initdb.d/
RUN chmod 754 /docker-entrypoint-initdb.d/northwind.sql

ENV PGDATA=/data/pgdata
ENV POSTGRES_USER=mylovelyuser
ENV POSTGRES_PASSWORD=mysecretpassword
ENV POSTGRES_DB=northwind