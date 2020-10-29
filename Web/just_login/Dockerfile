FROM tutum/lamp
COPY ./html /app
RUN chmod 777 /app/start.sh
ENTRYPOINT /run.sh&&/app/start.sh
