web题目只需要进入相应文件夹，运行：

```bash
docker-compose up -d
```

即可启动环境

close_eyes和just_login需要执行额外的命令：

```bash
cp html/start.sh src/
chmod 777 src/start.sh
docker exec 容器ID /app/start.sh
```

broken_motto请注意session保存路径是否可写问题