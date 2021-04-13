import random
import string
from datetime import date

import redis
import requests
import json
import time


class creat_store(object):

    def __init__(self, url_select,pea_mg_debugUserId,pea_mg_debugToken,phonenumber, userId):

        if url_select == 'TEST':
            self.url = 'http://test-zuul.ppwang.com:8107'
            self.storeBanner = "other/202101/04/C07FF5592372409D8152CE2E80271139.jpg"
            self.storeLogo = "other/202101/04/D6B55A5017FF42ADB7CC22909D0569BD.jpg"
            self.legalPersonPortrait = "store/ED85D508-B0C7-4EE9-88D9-E5683600F692.jpg"
            self.legalPersonNational = "store/93A0671C-A402-4F7B-8251-140DC0480BC2.jpg"
            self.businessLicense = "store/D59BD928-9BA1-4724-B6F5-85C5B28D4161.jpg"

        else:
            self.url = 'http://rc-zuul.ppwang.com'
            self.storeBanner = "order/202104/01/db3131be055de3f7184013fdaa38c0fb.jpg"
            self.storeLogo = "order/202104/01/aec242fee56a87b592dd092d2dd275ba.jpg"
            self.legalPersonPortrait = "store/3E1B4EA5DF420A7B7F36922D18346002.jpg"
            self.legalPersonNational = "store/334B51031866926C98597F561DFECF0E.jpg"
            self.businessLicense = "store/4DB9BF38DB481AF8A63DAF5FF047D0E3.jpg"

        self.phonenumber = phonenumber
        self.userId = userId
        self.pea_mg_debugUserId = pea_mg_debugUserId
        self.pea_mg_debugToken = pea_mg_debugToken

    def get_token(self, userId):

        if  url_select == 'TEST':

            r = redis.StrictRedis(host="192.168.1.7", port=6379, db=0)
            # 获取用户登录的token
            userId = str(userId)
            token_redis = r.get('pp-user-test:token:app_user:' + userId)

            if token_redis is not None:
                str_token = str(token_redis, encoding="utf8")
                dict_token = json.loads(str_token)

                token = dict_token["token"]
                print(token)

                return token

            else:
                print("获取的token没有数据")
                exit()

        else:
            token = '0000000000f1ce9fd97e8f8a1786bc10'
            return token

    # 随机创建身份证号
    def creat_identity(self):
        maxage = 60
        minage = 20
        now = date.today()
        birth = now.year - int(minage)
        mon = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        mon_days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
        age = int(maxage) - int(minage)
        y = str(birth - random.randint(1, age))
        index1 = random.randint(0, 11)
        m = str(mon[index1])
        m = m.zfill(2)
        maxDay = int(mon_days[index1])
        d = str(random.randint(1, maxDay))
        d = d.zfill(2)
        s = y + m + d
        area_1 = ["11", "12", "13", "14", "15", "21", "22", "23", "31", "32", "33", "34", "35", "36", "37", "41", "42", "43", "44","45", "46", "50", "51", "52", "53", "54", "61", "62", "63", "64", "65", "71", "81", "82", "91"]
        area = random.choice(area_1)
        print(type(area))

        # area = ["11"]
        print("shenfenzhang  zhuangt type")
        print(type(area))
        id = random.choice(area) + ''.join(random.choice(string.digits) for i in range(4)) + s + ''.join(
            random.choice(string.digits) for i in range(3))
        identity_id = id[0:17]
        lid = list(id)
        temp = 0
        for nn in range(2, 19):
            a = int(lid[18 - nn])  # 17到1的数
            w = (2 ** (nn - 1)) % 11  # 17到1的系数
            temp += a * w  # temp = temp+a*w 17位数字和系数相乘的结果相加
        temp = (12 - temp % 11) % 11
        if temp >= 0 and temp <= 9:
            identity_id += str(temp)
        elif temp == 10:
            identity_id += 'X'
        return identity_id

    # 定义新增店铺信息的方法
    def addstore(self):
        url = self.url + '/store/manage/saveStoreInfo'
        print(url)
        token = self.get_token(userId)


        # 请求头信息
        headers = {
            "Content-Type": "application/json",
            "userId": str(userId),
            "token": token,
            "platform": "Android",
            "versioncode": "210",
            "pea-mg-version": str(1.0),
            "pea-mg-debugCode": str(45747468),
            "pea-mg-debugUserId": self.pea_mg_debugUserId,
            "pea-mg-debugToken": self.pea_mg_debugToken
        }

        # 请求体内容
        data = {
            "userId": userId,
            "storeName": userId,
            "storeLogo": self.storeLogo,
            "storeBanner": self.storeBanner,
            "regionId": 477,
            "address": "天河客运站长版东路808",
            "ownerName": "洪小明",
            "tel": phonenumber,
            "syncStoreInfo": 1,
            "cateId": 77,
            "retailNum": 1,
            "packNum": 3,
            "wechat": ""
        }
        print(data)
        res = requests.session().post(url=url, data=json.dumps(data), headers=headers)
        print("提交店铺信息成功")
        print(res.text)
        return json.loads(res.text)


    # app小微店铺进件
    def addMicro(self):
        # 环境的url
        url = self.url + '/store/subject/addMicro'
        token = self.get_token(userId)
        # card_1 = "112031197402081311"
        card_1 = self.creat_identity()


        # 请求头信息
        headers = {
            "Content-Type": "application/json",
            "userId": str(userId),
            "token": token,
            "platform": "Android",
            "versioncode": "210",
            "pea-mg-version": str(1.0),
            "pea-mg-debugCode": str(45747468),
            "pea-mg-debugUserId": self.pea_mg_debugUserId,
            "pea-mg-debugToken": self.pea_mg_debugToken
        }

        print(headers)
        # 请求体内容
        data = {
            "storeId": userId,
            "legalPersonName": "洪泽佳",
            "legalPersonCard": card_1,
            "legalPersonPortrait": self.legalPersonPortrait,
            "legalPersonNational": self.legalPersonNational,
            "legalPersonCardValidTime": "2022-02-02",
            "mobile": 13250252197,
            "alipayAccount": phonenumber,
            "wechatAdded": 1
        }
        print(data)
        res = requests.session().post(url=url, data=json.dumps(data), headers=headers)
        print("小微进件提交成功")
        print(res)
        print(res.text)
        res_text = eval(res.text)
        message = res_text["message"]

        print(message)

        if message == "该身份证资料已申请开启其他店铺。请更换经营者资料后，重新提交。":
            print("重新调用生成小微进件信息")
            self.addMicro()




        return json.loads(res.text)


    # app个人店铺进件
    def addPerson(self):
        # 环境的url
        url = self.url + '/store/subject/addPersonV2'
        print(url)
        token = self.get_token(userId)

        # 请求头信息
        headers = {
            "Content-Type": "application/json",
            "userId": str(userId),
            "token": token,
            "platform": "Android",
            "versioncode": "210",
            "pea-mg-version": str(1.0),
            "pea-mg-debugCode": str(45747468),
            "pea-mg-debugUserId": self.pea_mg_debugUserId,
            "pea-mg-debugToken": self.pea_mg_debugToken
        }

        # 请求体内容
        data = {
            # "storeId": userId,
            # "legalPersonName": "黄芝华",
            # "legalPersonCard": "420111198310055541",
            # "legalPersonPortrait": self.legalPersonPortrait,
            # "legalPersonNational": self.legalPersonNational,
            # "legalPersonCardValidTime": "2023-08-21",
            # "businessLicenseType": 2,
            # "businessLicense": self.businessLicense,
            # "businessLicenseStartTime": "2019-01-16",
            # "socialCreditCode": "92420105MA4KNXGN84",
            # "businessLicenseValidTime": "长期",
            # "merchantName": "武汉市汉阳区影子时尚服装工作室",
            # "mobile": phonenumber,
            # "alipayType": 1,
            # "alipayAccount": "100000@qq.com",
            # "operatorName": "黄芝华",
            # "email": "100000@qq.com"

            "storeId": userId,
            "legalPersonName": "王彦成",
            "legalPersonCard": "41052319680617003X",
            "legalPersonPortrait": self.legalPersonPortrait,
            "legalPersonNational": self.legalPersonNational,
            "legalPersonCardValidTime": "2023-08-21",
            "businessLicenseType": 2,
            "businessLicense": self.businessLicense,
            "businessLicenseStartTime": "2019-01-16",
            "socialCreditCode": "92321081MA1XT24WXW",
            "businessLicenseValidTime": "长期",
            "merchantName": "仪征市刘集镇花丫丫百货店",
            "mobile": phonenumber,
            "alipayType": 1,
            "alipayAccount": "100000@qq.com",
            "operatorName": "王彦成",
            "email": "100000@qq.com"

        }

        res = requests.session().post(url=url, data=json.dumps(data), headers=headers)
        print("个人进件提交成功")
        print(res.text)
        return json.loads(res.text)


    # app企业店铺进件
    def addCompany(self):
        # 环境的url
        url = self.url + '/store/subject/addCompanyV2'
        print(url)
        token = self.get_token(userId)

        # 请求头信息
        headers = {
            "Content-Type": "application/json",
            "userId": str(userId),
            "token": token,
            "platform": "Android",
            "versioncode": "210",
            "pea-mg-version": str(1.0),
            "pea-mg-debugCode": str(45747468),
            "pea-mg-debugUserId": self.pea_mg_debugUserId,
            "pea-mg-debugToken": self.pea_mg_debugToken
        }

        # 请求体内容
        data = {
            "storeId": userId,
            "legalPersonName": "洪泽佳",
            "legalPersonCard": "440582199704224876",
            "mobile": 13250252197,
            # "legalPersonName": "梁春榕",
            # "legalPersonCard": "452128199312161021",
            # "mobile": 15626202858,
            "legalPersonPortrait": self.legalPersonPortrait,
            "legalPersonNational": self.legalPersonNational,
            "legalPersonCardValidTime": "2023-08-21",
            "businessLicenseType": 2,
            "businessLicense": self.businessLicense,
            "businessLicenseStartTime": "2019-01-16",
            "socialCreditCode": "912388479846526897",
            "businessLicenseValidTime": "长期",
            "merchantName": "esigntest批批网实名测试企业",
            "alipayType": 1,
            "alipayAccount": "100000@qq.com",
            "operatorName": "花木兰",
            "email": "100000@qq.com"

        }

        res = requests.session().post(url=url, data=json.dumps(data), headers=headers)
        print("企业进件提交成功")
        print(res)
        print(res.text)
        return json.loads(res.text)


# def add_address(userId):
#     # 环境的url
#     url = 'https://test-api2.ppwang.com/index.php?c=goods'
#     token = get_token(userId)
#
#     # 请求头信息
#     headers = {
#         "Content-Type": "application/json",
#         # "userId": str(userId),
#         # "token": token,
#         "platform": "Android",
#         "versioncode": "189",
#         # "pea-mg-version": str(1.0),
#         # "pea-mg-debugCode": str(45747468),
#         # "pea-mg-debugUserId": str(65),
#         # "pea-mg-debugToken": "bd1f865df47a83722b7d6bb76c29cf67"
#     }
#
#     # 请求体内容
#     data = {
#     "json": [{
#            "address" : "天河客运站",
#             "region_id" : "477",
#             "editType" : 0,
#             "consignee" : "洪小明",
#             "zipcode" : "123456",
#             "token" : "e87cc2898d7f007215d177a306ddee74",
#             "cmd" : "7100",
#             "phone_mob" : "13250252197",
#             "user_id" : userId,
#             "isSelected" : "false",
#             "index" : 0
# }]
# }
#
#     res = requests.session().post(url=url, data=json.dumps(data), headers=headers)
#
#
#
#     print(res)
#     print(res.text)
#
#     # print(json.loads(res.text))
#
#     return json.loads(res.text)


if __name__ == '__main__':
    # phonenumber = input("输入手机号:")
    # userId = input("输入店铺ID:")、
    # url_select = 'TEST'
    # pea_mg_debugUserId = 65
    # pea_mg_debugToken = 'e5a8e33a7559f20b57ad06a2d8b0f0a3'

    url_select = 'RC'
    pea_mg_debugUserId = 234
    pea_mg_debugToken = '46b5f36f43e79e7df926e34e0e4ffd90'
    phonenumber = 18026426150
    userId = 966076

    creat_store_message = creat_store(url_select,str(pea_mg_debugUserId),str(pea_mg_debugToken),phonenumber,userId)

    creat_store_message.addstore()
    # creat_store_message.addMicro()
    # creat_store_message.addPerson()
    creat_store_message.addCompany()



