## lottery
manage data about lottery[mark six,lotto mark], predict future values.

基于双色球、大乐透数据预测出奖号码， 定时收集最新出奖号码并评审。

### dao

数据管理， 历史数据存储及查询,  实时数据定时获取。

api:

按日期获取大乐透中奖号码 GET

/dao/big-lotto/<yyyy-mm-dd>



获取大乐透最新几期的中奖号码 GET

/dao/big-lotto/latest/<int>



按日期获取双色球中奖号码 GET

/dao/two-color-balls/<yyyy-mm-dd>



获取大乐透最新几期的中奖号码 GET

/dao/two-color-balls/latest/<int>

...

### predict

基于历史数据预测下期号码

api:

...

## 运行服务

```
cd /opt/lottery
sh start.sh
```

