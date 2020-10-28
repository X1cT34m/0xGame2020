FROM python:2.7.9
WORKDIR /app
COPY src /app
COPY requirements.txt /requirements.txt
COPY flag /flag
RUN pip install -i http://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn --upgrade pip && pip install -i http://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn -r /requirements.txt
CMD ["python", "app.py"]
