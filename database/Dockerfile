FROM mysql:8.0
ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE=ans_dados

COPY ./scripts/create_tables.sql /docker-entrypoint-initdb.d/
