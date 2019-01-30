# Kong API Gateway
官网: https://konghq.com/
https://hub.docker.com/_/kong/
https://github.com/PGBI/kong-dashboard
https://blog.csdn.net/li396864285/article/details/77371385

## Install 
1. Create the network: `docker network create kong-net`
2. Start your database
    ```
    docker run -d --name kong-database \
                --network=kong-net \
                -p 5432:5432 \
                -e "POSTGRES_USER=kong" \
                -e "POSTGRES_DB=kong" \
                postgres:9.6
    ```
3. Prepare your database
    ```
        docker run --rm \
        --network=kong-net \
        -e "KONG_DATABASE=postgres" \
        -e "KONG_PG_HOST=kong-database" \
        -e "KONG_CASSANDRA_CONTACT_POINTS=kong-database" \
        kong:latest kong migrations up
     ```
4. Start Kong
    ```
    docker run -d --name kong \
     --network=kong-net \
     -e "KONG_DATABASE=postgres" \
     -e "KONG_PG_HOST=kong-database" \
     -e "KONG_CASSANDRA_CONTACT_POINTS=kong-database" \
     -e "KONG_PROXY_ACCESS_LOG=/dev/stdout" \
     -e "KONG_ADMIN_ACCESS_LOG=/dev/stdout" \
     -e "KONG_PROXY_ERROR_LOG=/dev/stderr" \
     -e "KONG_ADMIN_ERROR_LOG=/dev/stderr" \
     -e "KONG_ADMIN_LISTEN=0.0.0.0:8001, 0.0.0.0:8444 ssl" \
     -p 8000:8000 \
     -p 8443:8443 \
     -p 8001:8001 \
     -p 8444:8444 \
     kong:latest
     ```


5. Start Dashboard
```
    docker run --name kong-dashboard --network=kong-net --rm -p 8080:8080 pgbi/kong-dashboard start --kong-url http://kong:8001
```