# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from .CCPRestSDK import REST

# ���ʺ�
accountSid = '8aaf0708647cfd080164eb7c11210278'

# ���ʺ�Token
accountToken = '606aa8f65803412e8349c7c937f9919b'

# Ӧ��Id
appId = '8aaf0708647cfd080164eb7c11490279'

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP = 'app.cloopen.com'

# ����˿�
serverPort = '8883'

# REST�汾��
softVersion = '2013-12-26'


# ����ģ�����
# @param to �ֻ�����
# @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
# @param $tempId ģ��Id

# ����ģʽ
class CCP(object):
    instance = None  # ������,�������������ĵ���

    def __new__(cls):
        if cls.instance is None:
            # ��ʾ����û��ʵ��,����ʵ��
            ccp_obj = super(CCP, cls).__new__(cls)

            # ��ʼ��REST SDK
            ccp_obj.rest = REST(serverIP, serverPort, softVersion)
            ccp_obj.rest.setAccount(accountSid, accountToken)
            ccp_obj.rest.setAppId(appId)

            cls.instance = ccp_obj

        return cls.instance

    def send_tempate_sms(self, to, datas, tempId):
        result = self.rest.sendTemplateSMS(to, datas, tempId)
        # result ��һ���ֵ�
        status_code = result.get("statusCode")
        if status_code == "000000":
            # ��ʾ���Ͷ��ųɹ�
            return 0
        else:
            # ��ʾ����ʧ��
            return -1


# sendTemplateSMS(�ֻ�����,��������,ģ��Id)

if __name__ == '__main__':
    ccp = CCP()
    ccp.send_tempate_sms("15802077709", ["1234", "5"], 1)
