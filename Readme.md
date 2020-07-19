
```
# create ecosystem
docker-compose -f "docker-compose.yml" up -d --build

# enter to influxdb container
docker exec -it influx-grafana-poc_influxdb_1 bas

# import fake data
influx -import -path=Personas_data.txt -precision=s -database=Personas
```

### Resources
https://grafana.com/docs/grafana/latest/features/datasources/influxdb/

https://grafana.com/docs/grafana/latest/variables/templates-and-variables/
