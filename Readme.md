
```
# create ecosystem
docker-compose -f "docker-compose.yml" up -d --build

# enter to influxdb container
docker exec -it influx-grafana-poc_influxdb_1 bas

# import fake data
influx -import -path=data/Personas_data.txt -precision=s -database=biblioteca_database
```

If you generate new data, you must prepend to Personas_data.txt:
```
# DDL

CREATE DATABASE biblioteca_database

# DML

# CONTEXT-DATABASE: biblioteca_database

```

You should see this message: 
```bash
2020/07/19 22:00:39 Processed 100000 lines.  Time elapsed: 568.695459ms.  Points per second (PPS): 175841
2020/07/19 22:00:40 Processed 200000 lines.  Time elapsed: 1.0388489s.  Points per second (PPS): 192520
2020/07/19 22:00:40 Processed 300000 lines.  Time elapsed: 1.626172345s.  Points per second (PPS): 184482
2020/07/19 22:00:40 Processed 1 commands
2020/07/19 22:00:40 Processed 306721 inserts
2020/07/19 22:00:40 Failed 0 inserts

```

### Resources
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases

https://docs.influxdata.com/influxdb/v1.8/query_language/sample-data/

https://grafana.com/docs/grafana/latest/features/datasources/influxdb/

https://grafana.com/docs/grafana/latest/variables/templates-and-variables/

https://csetutorials.com/influxdb-tutorial.html


### Queries Remotas

Crear base de datos
```
curl -i -XPOST '<url>/query' -u '<user>:<password>' \
 'q=CREATE DATABASE "BibliotecaTest"'
```

Subir desde un archivo
```
curl -i -XPOST '<url>/write?db=BibliotecaTest&precision=s' -u '<user>:<password>' \
 --data-raw @Personas_data.txt
```

Ejecutar Query
```
curl -i -XPOST '<url>/query?pretty=true' -u '<user>:<password>' \
--data-urlencode "db=BibliotecaTest" \
--data-urlencode "q=SELECT * FROM PERSONAS LIMIT 10"
```