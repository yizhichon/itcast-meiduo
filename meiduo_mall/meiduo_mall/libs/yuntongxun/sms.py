# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from .CCPRestSDK import REST

# 主帐号
accountSid = '8aaf0708647cfd080164eb7c11210278'

# 主帐号Token
accountToken = '606aa8f65803412e8349c7c937f9919b'

# 应用Id
appId = '8aaf0708647cfd080164eb7c11490279'

# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'


# 发送模板短信
# @param to 手机号码
# @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
# @param $tempId 模板Id

# 单例模式
class CCP(object):
    instance = None  # 类属性,用来保存这个类的单例

    def __new__(cls):
        if cls.instance is None:
            # 表示类中没有实例,创建实例
            ccp_obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            ccp_obj.rest = REST(serverIP, serverPort, softVersion)
            ccp_obj.rest.setAccount(accountSid, accountToken)
            ccp_obj.rest.setAppId(appId)

            cls.instance = ccp_obj

        return cls.instance

    def send_tempate_sms(self, to, datas, tempId):
        result = self.rest.sendTemplateSMS(to, datas, tempId)
        # result 是一个字典
        status_code = result.get("statusCode")
        if status_code == "000000":
            # 表示发送短信成功
            return 0
        else:
            # 表示发送失败
            return -1


# sendTemplateSMS(手机号码,内容数据,模板Id)

if __name__ == '__main__':
    ccp = CCP()
    ccp.send_tempate_sms("15802077709", ["1234", "5"], 1)
