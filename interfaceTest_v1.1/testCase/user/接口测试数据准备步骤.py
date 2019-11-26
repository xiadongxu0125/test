'''
1.抓包，或者看接口文档获取接口相关信息：如
POST /loanapi/biz/lb/bigdata/notify/v1?
appKey=000001&apiCode=LB0106&bizCode=LBN106&timestamp=1563850054000&sign=3d09c5beced07f5c686d0f6dae20b3df HTTP/1.1

data{"mobileNo":"17600121987","partnerCode":"C01","decisionCode":"1379","channelSource":"H5","productTypeCode":"02"}

返回报文：
请求返回值：
{
    "info": "成功",
    "message": "成功",
    "responseHeader": {
        "accessNumber": "b1e7d50cd96d47e2bfbd86601381b69c",
        "code": "0000",
        "message": "成功",
        "serviceBeginTime": "20190723111621376",
        "serviceEndTime": "20190723111621801"
    },
    "result": {
        "decisionCode": "1381",
        "productTypeCode": "02",
        "retCode": "0000",
        "retMessage": "操作成功"
    },
    "status": "20000108",
    "timestamp": 1563851781801
2.新增测试案例user目录下
3.修改testfile 下case 中 test000001.xlsx中新增新接口Sheet页，按原有接口中对应的测试项修改
4.img下interfaceURL.xml中新增接口路径
5.修改local000001_xls = common.get_xls("test000001.xlsx", "Application_quota")获取接口信息路径，修改sheet页对应的名称
6.修改self.url = common.get_url_from_xml('Application_quota')获取url信息路径，修改新增接口对应的url路径名称
7.如有sql执行需要修改img中sql.xml,获取数据库名称，表名称，执行顺序，修改脚本中需要传入数据库名称，还有获取数据库地址参数参见
  testApplication_euota.py中数据库相关脚本设置！
8.如有sql执行需要修改DATABAS.xml中的数据库名称以及数据库链接
9.执行新增脚本验证返回接口
'''