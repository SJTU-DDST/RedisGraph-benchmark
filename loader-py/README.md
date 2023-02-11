# load-py

`redisgraph-loader-py`是一个Python程序，用于从CSV输入构建RedisGraph数据库。`redisgraph-loader-py`的功能与`redisgraph-bulk-loader`相同，缺点是导入数据速度较慢。

## requirement

```shell
pip install -r requirements.txt
```

## run

向RedisGraph server中导入数据：

```shell
python3 social_demo.py -h 127.0.0.1 -p 6379
```

