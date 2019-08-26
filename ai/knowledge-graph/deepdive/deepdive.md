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
- Compile the DeepDive application : `deepdive compile`
- Load input: `deepdive load articles input/articles-1000.tsv.bz2` or 全量`deepdive do articles`
- Adds some useful NLP markups to the English text:`deepdive do sentences` and `deepdive do spouse_candidate`
- Run the model: `deepdive do probabilities`
- Start the UI: `mindbender search update` and `mindbender search gui`
  
## 加速
- copy `udf/bazaar` folder and run `sbt/sbt stage`
## 其他概念
- 实体抽取(Relation extraction)
- factor graph(variables, factors)
## DDlog
文档: `http://deepdive.stanford.edu/writing-dataflow-ddlog`
- Normal
    `Q(x, y) :- R(x, y), S(y).`表示`R`和`S` 通过`inner join`产生结果返回给`Q`
- Expressions
    ```
        a(k int).
        b(k int, p text, q text, r int).
        c(s text, n int, t text).

        Q("test", f(123), id) :- a(id), b(id, x,y,z), c(x || y,10,"foo").

        R(TRUE, power(abs(x-z), 2)) :- a(x), b(y, _, _, _).

        S(if l > 10 then TRUE
        else if l < 10 then FALSE
        else NULL end) :- R ( _, l).
    ```
- Constant literals

- Disjunctions
    ```
        Q(x, y) :- R(x, y), S(y).
        Q(x, y) :- T(x, y).
    ```
    ```
        Q(x, y) :- R(x, y), S(y); T(x, y).
    ```
- Aggregation: 只返回一行
    `Q(a,b,MAX(c)) :- R(a,b,c).`
- Select distinct
    `Q(x,y) *:- R(x, y).`
- Quantifiers
    ```
        P(a) :- R(a, _), EXISTS[S(a, _)].
        Q(a) :- R(a, b),    ALL[S(a, c), c > b].
    ```
- Optional
    ```
        Q(a, c) :- R(a, b), OPTIONAL[S(a, c), c > b].
    ```
- Select distinct
    `*:=`
- Quantifiers
- A question mark after the relation name indicates that it is a variable relation containing random variables rather than a normal relation used for loading or processing data to be later used by the model. 
    `has_spouse?(p1_id text, p2_id text).`