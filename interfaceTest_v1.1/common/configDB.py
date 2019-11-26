import pymysql
import readConfig as readConfig
from common import common
from common.Log import MyLog as Log

#localReadConfig = readConfig.ReadConfig()

class MyDB:
    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None
    def query(sql,databasenumber):
        #连接mysql数据库，获取数据库配置文件信息
         '''
         db = pymysql.connect(localReadConfig.get_db("host"),
                         localReadConfig.get_db("username"), localReadConfig.get_db("password"),
                         localReadConfig.get_db("database"),
                         int(localReadConfig.get_db("port")))
         '''
         db = pymysql.connect( databasenumber['host'],
                               databasenumber['username'],
                               databasenumber['password'],
                               databasenumber['database'],
                               int(databasenumber['port']))
         #创建游标
         cursor = db.cursor()
         #执行sql
         cursor.execute(sql)
         #获取全部数据，fetchone获取第一条数据
         data = cursor.fetchall()
         #关闭数据库连接
         db.close()
         return data

    def update(sql,databasenumber):
         '''
         db = pymysql.connect(localReadConfig.get_db("host"),
                         localReadConfig.get_db("username"), localReadConfig.get_db("password"),
                         localReadConfig.get_db("database"),
                         int(localReadConfig.get_db("port")))
         '''
         db = pymysql.connect( databasenumber['host'],
                               databasenumber['username'],
                               databasenumber['password'],
                               databasenumber['database'],
                               int(databasenumber['port']))
         cursor = db.cursor()
         try:
             # 执行SQL语句
             cursor.execute(sql)
             # 提交到数据库执行
             db.commit()
         except:
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
            db.close()


    def delete(sql,databasenumber):
         db = pymysql.connect( databasenumber['host'],
                               databasenumber['username'],
                               databasenumber['password'],
                               databasenumber['database'],
                               int(databasenumber['port']))
         cursor = db.cursor()

         try:
             # 执行sql语句
             cursor.execute(sql)
             # 提交到数据库执行
             db.commit()
         except:
             # Rollback in case there is any error
             print ("sql报错，回滚")
             db.rollback()

        #关闭数据库连接
             db.close()


if __name__ == "__main__":
    sql = "SELECT * " \
          "FROM yx_cust_info_bc LEFT JOIN yx_per_cust_bc " \
          "ON yx_cust_info_bc.id = yx_per_cust_bc.id " \
          "LEFT JOIN yx_business_bc " \
          " ON yx_per_cust_bc.id = yx_business_bc.yxPerCustBc_id "\
          "where yx_business_bc.clueId = '%s'" % "402811da5d86e849015d87f0512c0376"

    # print sql
    data = MyDB.search(sql)
    # print data
    for i in range(len(data)):
        print (data[i])