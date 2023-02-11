# load-bulk
## Requirements

`redisgraph-bulk-loader`是一个Python程序，用于从CSV输入构建RedisGraph数据库。`redisgraph-bulk-loader`可以将数据批量快速导入RedisGraph数据库。

The bulk loader can be installed using pip:

```shell
pip install redisgraph-bulk-loader
```

Or

```shell
pip install git+https://github.com/RedisGraph/redisgraph-bulk-loader.git@master
```

## run

对CSV输入文件进行预处理：

```shell
./convert-csv.sh
```

向RedisGraph server中导入数据：

```shell
./build_social_network_0_1.sh 127.0.0.1 6379
```

