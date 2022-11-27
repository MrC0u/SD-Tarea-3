
# Hadoop
## Iniciar Container de Hadoop
```bash
docker build -t hadoop .
docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
```

## Ingresar al container de Hadoop
```bash
docker exec -it hadoop bash
```

## Creacion Carpetas Hadoop
```bash
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hduser
hdfs dfs -mkdir input	
```

## Ingresar archivo input a Hadoop
```bash
hdfs dfs -put <file-name>.txt input
```

## Funcion WordCounter
```bash
mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output /user/hduser/output -mapper ./mapper.py -reducer ./reducer.py
```

## Visualizar resultado
```bash
hdfs dfs -cat /user/hduser/output/*
```

Otra forma de ver los resultados (Mostrado en el video) es ingresando en [Hadoop](http://localhost:9870/explorer.html#/user/hduser) , luego descargar el archivo llamado  ``` part_00000 ```, y abrirlo con un editor/visualizador de texto.
  
# Video Demostracion
[![Video](https://img.youtube.com/vi/AYM--7cPCuU/0.jpg)](https://youtu.be/AYM--7cPCuU/)
  
