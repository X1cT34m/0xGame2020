FROM vulhub/flask:1.1.1

WORKDIR /usr/app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt /usr/requirements.txt
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /usr/requirements.txt

COPY ./src/ /usr/app/
CMD ["flask", "run"]
