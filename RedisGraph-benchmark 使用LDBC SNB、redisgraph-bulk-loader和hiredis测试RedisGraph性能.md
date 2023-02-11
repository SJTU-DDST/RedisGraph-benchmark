# RedisGraph-benchmark: 使用LDBC SNB、redisgraph-bulk-loader和hiredis测试RedisGraph性能

## 1 使用LDBC SNB生成测试数据

### 1.1 安装LDBC SNB

- 下载hadoop

  ```shell
  wget https://repo.huaweicloud.com/apache/hadoop/common/hadoop-2.9.2/hadoop-2.9.2.tar.gz
  tar -zxvf hadoop-2.9.2.tar.gz
  # 添加环境变量
  # 我一般加在~/.bashrc中
  export HADOOP_HOME=/..../hadoop-2.9.2
  # 根据具体情况，配置使用内存容量
  export HADOOP_CLIENT_OPTS="-Xmx8G"
  ```

- 下载LDBC SNB源码

  ```shell
  git clone https://github.com/ldbc/ldbc_snb_datagen.git -b v0.3.2
  # 添加环境变量
  # 我一般加在~/.bashrc中
  export LDBC_SNB_DATAGEN_HOME=/..../ldbc_snb_datagen
  source ~/.bashrc
  ```

- 安装jdk与maven

### 1.2 生成测试数据

- 配置`params.ini`

  LDBC SNB支持生成不同规模的图数据集，generator.scaleFactor参数各取值对应的点边数目如下表：

  ![](https://user-images.githubusercontent.com/83715643/217151639-44cf7819-49ec-4c2b-9d3c-3d6265f7ba4d.png)

  ```shell
  cd $LDBC_SNB_DATAGEN_HOME
  cp params-csv-basic.ini params.ini
  # 修改params.ini，设置generator.scaleFactor=0.1
  # 修改后的params.ini第1行内容
  ldbc.snb.datagen.generator.scaleFactor:snb.interactive.0.1
  ```

- 修改`run.sh`

  ```shell
  # 修改后的run.sh
  DEFAULT_HADOOP_HOME=/..../hadoop-2.9.2 #change to your hadoop folder
  ```

- 执行程序

  ```shell
  ./run.sh
  ```

  生成的数据在`$LDBC_SNB_DATAGEN_HOME/social_network`和`$LDBC_SNB_DATAGEN_HOME/substitution_parameters`两个目录下。`social_network`存储的是表单数据，`substitution_parameters`存储的是测试数据。

## 2 使用redisgraph-bulk-loader将测试数据导入RedisGraph

- 下载`RedisGraph-benchmark`

  ```shell
  git clone https://github.com/SJTU-DDST/RedisGraph-benchmark.git
  cd ./loader-bulk
  ```

- 安装`redisgraph-bulk-loader`

  ```shell
  pip install redisgraph-bulk-loader
  ```

- 拷贝测试数据

  ```shell
  cp -r $LDBC_SNB_DATAGEN_HOME/social_network/static/. ./loader-bulk/social_network_0_1
  cp -r $LDBC_SNB_DATAGEN_HOME/social_network/dynamic/. ./loader-bulk/social_network_0_1
  ```

- 将测试数据导入至redisgraph

  ```shell
  # 对CSV输入文件进行预处理：
  ./convert-csv.sh
  # 向RedisGraph server中导入数据：
  ./build_social_network_0_1.sh 127.0.0.1 6379
  ```

## 3 使用hiredis测试RedisGraph的吞吐量

- 安装`hiredis`

  ```shell
  git clone https://github.com/redis/hiredis.git
  make
  make install
  ```

- compile

  ```shell
  gcc -o redis_graph_test redis_graph_test.c -I /usr/local/include/hiredis -lhiredis -pthread
  ```

- 执行程序

  ```shell
  # 向RedisGraph server发送query，测试吞吐量：
  # 测得的吞吐量一共有两种：
  # no pipeline:仅开启1个连接线程，顺序发送query
  # pipelined: 同时开启64个连接线程，每个线程以batch的形式发送query
  ./redis_graph_test -h 127.0.0.1 -p 6379
  ```

  

