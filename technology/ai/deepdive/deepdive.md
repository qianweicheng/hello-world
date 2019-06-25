# Deepdive
## Quickstart
http://deepdive.stanford.edu/quickstart
- 帮助脚本:`bash <(curl -fsSL git.io/getdeepdive)`
- 启动数据库
```
    docker run -d --name deepdive-database \
                -p 5432:5432 \
                -e "POSTGRES_USER=deepdive" \
                -e "POSTGRES_DB=deepdive" \
                -e "POSTGRES_DB=deepdive" \
                postgres:latest
```
- Load input: `deepdive compile`
- `deepdive load articles input/articles-1000.tsv.bz2`
- Adds some useful NLP markups to the English text:`deepdive do sentences` and `deepdive do spouse_candidate`
- Run the model: `deepdive do probabilities`