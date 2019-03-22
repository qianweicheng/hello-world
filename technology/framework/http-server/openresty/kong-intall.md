# Kong API Gateway
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
- Konga
```
docker run -p 1337:1337 \
             --network kong-net \
             --name konga \
             -e "NODE_ENV=development" \
             -e "TOKEN_SECRET=1234567890" \
             pantsel/konga
```
- PGBI/kong-dashboard
```
    docker run -d --name kong-dashboard --network=kong-net --rm -p 8080:8080 pgbi/kong-dashboard start --kong-url http://kong:8001
```
Dashboard|Kong|Node
-|-|-
3.3.x, 3.4.x|>= 0.9, <0.14|>= 6.0.0
3.5.x|>= 0.9, <0.15|>= 6.0.0
3.6.x|>= 0.9, <2.0.0|>= 6.0.0
Case|Result
-|-
Kong: 0.14.1 Dashboard: 3.5.0| OK
Kong: 1.0.3  Dashboard: 3.6.0| Failed
## 企业版安装
URL: https://bintray.com/login?forwardedFrom=kong
Username: edisontech_eval_weicheng-qian@kong
Password: 712ade9a1f5ea018fdcddb571422b7531964890b
Your software access and license is valid until 2019-03-26.
- 登陆：
    `docker login -u edisontech_eval_weicheng-qian@kong -p 712ade9a1f5ea018fdcddb571422b7531964890b kong-docker-kong-enterprise-edition-docker.bintray.io`
- 下载image: 
    `docker pull kong-docker-kong-enterprise-edition-docker.bintray.io/kong-enterprise-edition`
- Tag:
    `docker tag kong-docker-kong-enterprise-edition-docker.bintray.io/kong-enterprise-edition kong-ee`
- database
    ```
    docker run -d --name kong-ee-database \
    --network=kong-net \
    -p 5432:5432 \
    -e "POSTGRES_USER=kong" \
    -e "POSTGRES_DB=kong" \
    postgres:9.6
    ```
-  license key:
```
export KONG_LICENSE_DATA='{"license":{"signature":"c10a042a23fab3b6d39fd796df28792cfe8cbb8612652f1f951baab0e812b9341df563cc94be864a2e23dab5a49457ffd6f84e80ae5ab7d2168d5c2acd0739c2","payload":{"customer":"Edisontech_Eval","license_creation_date":"2019-02-25","product_subscription":"Kong Enterprise Edition","admin_seats":"5","support_plan":"None","license_expiration_date":"2019-03-26","license_key":"0011K000024n6xYQAQ_a1V1K000006SvBnUAK"},"version":1}}'
```
- Run kong migrations:
```
 docker run --rm --network=kong-net \
   -e "KONG_DATABASE=postgres" -e "KONG_PG_HOST=kong-ee-database" \
   -e "KONG_CASSANDRA_CONTACT_POINTS=kong-ee-database" \
   -e "KONG_LICENSE_DATA=$KONG_LICENSE_DATA" \
   kong-ee kong migrations up
```
- Run kong
```
docker run -d --name kong-ee --network=kong-net \
  -e "KONG_DATABASE=postgres" \
  -e "KONG_PG_HOST=kong-ee-database" \
  -e "KONG_CASSANDRA_CONTACT_POINTS=kong-ee-database" \
  -e "KONG_PROXY_ACCESS_LOG=/dev/stdout" \
  -e "KONG_ADMIN_ACCESS_LOG=/dev/stdout" \
  -e "KONG_PROXY_ERROR_LOG=/dev/stderr" \
  -e "KONG_ADMIN_ERROR_LOG=/dev/stderr" \
  -e "KONG_ADMIN_LISTEN=0.0.0.0:8001" \
  -e "KONG_PORTAL=on" \
  -e "KONG_PORTAL_GUI_PROTOCOL=http" \
  -e "KONG_PORTAL_GUI_HOST=127.0.0.1:8003" \
  -e "KONG_LICENSE_DATA=$KONG_LICENSE_DATA" \
  -p 8000:8000 \
  -p 8443:8443 \
  -p 8001:8001 \
  -p 8444:8444 \
  -p 8002:8002 \
  -p 8445:8445 \
  -p 8003:8003 \
  -p 8004:8004 \
  kong-ee
  ```