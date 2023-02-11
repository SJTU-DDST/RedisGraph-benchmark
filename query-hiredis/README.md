# query-hiredis
## Requirements

Hiredis is a minimalistic C client library for the Redis database.

Hiredis can be installed:

```shell
git clone https://github.com/redis/hiredis.git
make
make install
```

## compile

```shell
gcc -o redis_graph_test redis_graph_test.c -I /usr/local/include/hiredis -lhiredis -pthread
```

## run

向RedisGraph server发送query，测试吞吐量：

```shell
./redis_graph_test -h 127.0.0.1 -p 6379
```

