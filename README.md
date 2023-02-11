# RedisGraph-benchmark

## loader-bulk

`redisgraph-bulk-loader`是一个Python程序，用于从CSV输入构建RedisGraph数据库。`redisgraph-bulk-loader`可以将数据批量快速导入RedisGraph数据库。

具体使用见`./loader-bulk/README.md`

## loader-py

`redisgraph-loader-py`是一个Python程序，用于从CSV输入构建RedisGraph数据库。`redisgraph-loader-py`的功能与`redisgraph-bulk-loader`相同，缺点是导入数据速度较慢。

具体使用见`./loader-py/README.md`

## query-hiredis

使用`redisgraph-bulk-loader`或者`redisgraph-loader-py`将数据导入redisgraph后，使用`query-hiredis`测试redisgraph的吞吐量。

具体使用见`./query-hiredis/README.md`

## 详细教程

见`RedisGraph-benchmark 使用LDBC SNB、redisgraph-bulk-loader和hiredis测试RedisGraph性能.md`
