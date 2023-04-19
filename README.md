### 1 Scenario1

#### 1.1 The description of data model

![](https://user-images.githubusercontent.com/83715643/232994420-43e7ce89-2642-4f05-9778-e950649ec7b9.png)

- 2张表，1条Path(T10预置，T7更新)，N(64K):1；

- 表项规格：xxxK -> xM ；

- Host：T7 1个应用，1个线程；

- 业务流程：查主键（命中） -> T7 Tuple更新->T7 索引更新 -> 图更新 -> 图查找。

#### 1.1 How to use?

```shell
cd scenario1
# generate router.csv and relation.csv
python generator_scenario1.py
# build the graph using redisgraph-bulk-loader
# in other words, load the data into redisgraph database
sh build_graph_scenario1.sh 127.0.0.1 6379
```

#### 1.2 Test using redis-cli

You can interact with RedisGraph using redis-cli, obtaining the information of graph you just built.

```sh
./redis-cli -h 127.0.0.1 -p 6379
127.0.0.1:6379> GRAPH.QUERY scenario1 "MATCH (r)-[]->(t) WHERE r.id >= 0 AND r.id < 10 RETURN t.ip"
1) 1) "t.ip"
2)  1) 1) "0.11.51.112"
    2) 1) "0.127.107.109"
    3) 1) "0.32.16.195"
    4) 1) "0.100.46.252"
    5) 1) "0.113.208.226"
    6) 1) "0.11.51.112"
    7) 1) "0.127.107.109"
    8) 1) "0.120.233.9"
    9) 1) "0.120.233.9"
   10) 1) "0.32.46.196"
3) 1) "Cached execution: 0"
   2) "Query internal execution time: 245.734096 milliseconds"
```

### 2 Scenario2

#### 2.1 The description of data model

![](https://user-images.githubusercontent.com/83715643/233010850-7038fdf6-5cb5-42aa-b671-d7b581ef011b.png)

- 9张表，1条Path(T7预置，T10-T80插入)，1:1

- 表项规格：xxxK -> xM 

- Host：T10-T80 8个应用，8个线程

- 业务流程：查主键（Miss） -> T10-T80 Tuple插入->T10-T80 索引插入-> 图更新 -> 图查找


#### 2.2 How to use?

```shell
cd scenario2
# generate router.csv and relation.csv
python generator_scenario2.py
# build the graph using redisgraph-bulk-loader
# in other words, load the data into redisgraph database
sh build_graph_scenario2.sh 127.0.0.1 6379
```

#### 2.3 Test using redis-cli

You can interact with RedisGraph using redis-cli, obtaining the information of graph you just built.

```sh
./redis-cli -h 127.0.0.1 -p 6379
127.0.0.1:6279> GRAPH.QUERY scenario2 "MATCH (r)-[]->(t1)-[]->(t2)-[]->(t3)-[]->(t4) WHERE r.id >= 0 AND r.id < 4 RETURN t1.ip,t2.ip,t3.ip,t4.ip"
1) 1) "t1.ip"
   2) "t2.ip"
   3) "t3.ip"
   4) "t4.ip"
2) 1) 1) "4.189.198.237"
      2) "0.99.24.144"
      3) "6.19.79.82"
      4) "3.0.154.66"
   2) 1) "5.78.99.78"
      2) "4.132.63.49"
      3) "4.133.60.90"
      4) "1.249.66.57"
   3) 1) "3.15.56.99"
      2) "7.159.139.211"
      3) "7.222.202.113"
      4) "0.134.121.121"
   4) 1) "3.51.220.158"
      2) "1.7.93.53"
      3) "3.48.241.230"
      4) "6.119.99.19"
3) 1) "Cached execution: 0"
   2) "Query internal execution time: 5128.089778 milliseconds"
```
