from common import configDB as configDB
from common import common
import json
#连接mysql数据库

localsql = common.get_sql("loancore", "t_ba_iou","01")
localsql_update = common.get_sql("loancore", "t_ba_iou","02")
databasenumber = common.get_database_from_xml("loancore")
print(localsql_update)
print(localsql)
print(databasenumber)
#修改借据状态为7008
data1 = configDB.MyDB.update(localsql_update,databasenumber)
#查询借据状态
data = configDB.MyDB.query(localsql,databasenumber)
for i in range(len(data)):
    print (data[i])

    print ("变更后的借据状态IOU_STATE:"+ data[i][5])

'''
localsql_update = common.get_sql("loanquota", "t_lq_user_scene_base_info","02")
localsql = common.get_sql("loanquota", "t_lq_user_scene_base_info","01")
databasenumber = common.get_database_from_xml("loanquota")
print(localsql_update)
print(localsql)
print(databasenumber)
#修改借据状态为7008
data2 = configDB.MyDB.query(localsql,databasenumber)
data1 = configDB.MyDB.update(localsql_update,databasenumber)
#data1 = configDB.MyDB.update(localsql_update)
#查询借据状态
data = configDB.MyDB.query(localsql,databasenumber)
for i in range(len(data)):
    print (data[i])

    print ("变更后的状态VALIDATE_STATE:"+ data[i][0])
'''
