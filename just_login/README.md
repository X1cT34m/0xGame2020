启动之后需要把html文件夹下的start.sh拷贝到src目录，然后

```
docker exec 容器ID chmod 777 /app/start.sh
docker exec 容器ID /app/start.sh
```

