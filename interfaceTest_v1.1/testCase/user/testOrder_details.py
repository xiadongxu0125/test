import time
import unittest
import paramunittest
import readConfig as readConfig
from common import common
from common import configHttp
from common.Log import MyLog
import hashlib
import json
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
local000001_xls = common.get_xls("test000001.xlsx", "Order_details")
#H5前端查看全部借据接口LB0094

@paramunittest.parametrized(*local000001_xls)
class testOrder_details(unittest.TestCase):


    def setParameters(self, case_name, method,cookie ,appKey,apiCode,bizCode, data, result, code, msg,retCode,retMessage):
        """
        set params
        :param case_name:
        :param method:
        :param cookie:
        :param appKey:
        :param data1:
        :param apiCode:
        :param bizCode:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.cookie = str(cookie)
        self.appKey = str(appKey)
        self.apiCode = str(apiCode)
        self.bizCode = str(bizCode)
        #data 反序列化 loads只能完成反序列化 ，将包含str类型的JSON文档反序列化为一个python对象"""
        self.data = json.loads(data)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
        self.retCode = str(retCode)
        self.retMessage = str(retMessage)
        self.response = None
        self.info = None
        self.cookie = cookie
        #timestamp1 = lambda: int(round(time.time() * 1000))（生成13位时间戳)
        #系统时间戳10位后加000，所以乘以1000
        timestamp1 = int(time.time())*1000
        self.timestamp = timestamp1
        self.appSecret ='E14DE753-9EC6-4986-B7CB-A793DF2A13A5'
        '''
        sign 开发源码生成规则
        const baseVerifyCode =function (apicode, bizcode) {
  var timestamp = Date.parse(new Date());
  var parmasstr = appsectet+'apiCode' + apicode + 'appKey' + appkey + 'bizCode' + bizcode + 'timestamp' + timestamp+ appsectet;
  var nowcode = 'appKey=' + appkey + '&apiCode=' + apicode + '&bizCode=' + bizcode + '&timestamp=' + timestamp + '&sign=' + md5(parmasstr)
  return nowcode

        '''
        sign1 = self.appSecret + 'apiCode' + str(apiCode) + 'appKey' + str(appKey) + 'bizCode' + str(bizCode) + 'timestamp' + str(self.timestamp) + self.appSecret
        self.sign = hashlib.md5(sign1.encode()).hexdigest()

    def description(self):
        """

        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
         #login
        #self.cookie = businessCommon.login()

    def testorder_details(self):

        """
        test body
        :return:
        """
        # set url
        self.url = common.get_url_from_xml('Order_details')
        localConfigHttp.set_url(self.url)

        # set header

        if self.cookie == '0':
            cookie = self.cookie
        else:
            cookie = self.cookie
        header = {'content-type':'application/json','cookie': cookie}
        localConfigHttp.set_headers(header)

        # set param
        #param 参数已字典格式无顺序传值
        param = {"appKey": self.appKey, "apiCode": self.apiCode, "bizCode": self.bizCode,
                 'timestamp': self.timestamp, 'sign': self.sign}
        #param 拼接而成按顺序传值
        #param = 'appKey=' + self.appKey + '&apiCode=' + self.apiCode + '&bizCode=' + self.bizCode + '&timestamp=' + str(self.timestamp) +'&sign=' + self.sign

        localConfigHttp.set_params(param)
        # set data
        #data = {"mobileNo": self.mobileNo}
        data = self.data
        localConfigHttp.set_data(data)

        # test interface
        self.response = localConfigHttp.post()

        # check result
        self.checkResult()

    def tearDown(self):
        """

        :return:
        """
        # logout
        #businessCommon.logout(self.login_token)
        self.log.build_case_line(self.case_name, self.info['info'], self.info['message'])

    def checkResult(self):
        self.info = self.response.json()
        common.show_return_msg(self.response)

        if self.result == '0':
            self.assertEqual(self.info['responseHeader']["code"], self.code)
            self.assertEqual(self.info['responseHeader']["message"], self.msg)
            print("接口调用成功！")
            self.assertEqual(self.info['result']["retCode"], self.retCode)
            self.assertEqual(self.info['result']["retMessage"], self.retMessage)
            print("查看全部借据成功！")

            #result = self.info['info'].get('result')
            #self.assertEqual(result, 1)

        if self.result == '1':
            self.assertEqual(self.info['responseHeader']["code"], self.code)
            self.assertEqual(self.info['responseHeader']["message"], self.msg)
            print("接口调用成功！")
            self.assertEqual(self.info['result']["retCode"], self.retCode)
            self.assertEqual(self.info['result']["retMessage"], self.retMessage)
            print("查看全部借据失败："+ self.retMessage)
