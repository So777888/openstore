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
            self.legalPersonPortrait = "/store/3E1B4EA5DF420A7B7F36922D18346002.jpg"
            self.legalPersonNational = "/store/334B51031866926C98597F561DFECF0E.jpg"
            self.businessLicense = "/store/4DB9BF38DB481AF8A63DAF5FF047D0E3.jpg"

        self.phonenumber = phonenumber
        self.userId = userId
        self.pea_mg_debugUserId = pea_mg_debugUserId
        self.pea_mg_debugToken = pea_mg_debugToken

    def get_token(self, userId):

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
            "versioncode": "189",
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
        print(url)
        token = self.get_token(userId)
        card_1 = "410222197701163011"
        print(self.storeBanner)
        pr = self.storeBanner
        print(pr)

        # 请求头信息
        headers = {
            "Content-Type": "application/json",
            "userId": str(userId),
            "token": token,
            "platform": "Android",
            "versioncode": "189",
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
        return json.loads(res.text)


    # app个人店铺进件
    def addPerson(self):
        # 环境的url
        url = self.url + '/store/subject/addPerson'
        print(url)
        token = self.get_token(userId)

        # 请求头信息
        headers = {
            "Content-Type": "application/json",
            "userId": str(userId),
            "token": token,
            "platform": "Android",
            "versioncode": "189",
            "pea-mg-version": str(1.0),
            "pea-mg-debugCode": str(45747468),
            "pea-mg-debugUserId": self.pea_mg_debugUserId,
            "pea-mg-debugToken": self.pea_mg_debugToken
        }

        # 请求体内容
        data = {
            "storeId": userId,
            "legalPersonName": "花木兰",
            "legalPersonCard": "410702197211052011",
            "legalPersonPortrait": self.legalPersonPortrait,
            "legalPersonNational": self.legalPersonNational,
            "legalPersonCardValidTime": "2023-08-21",
            "businessLicenseType": 1,
            "businessLicense": self.businessLicense,
            "socialCreditCode": "92420105MA4KNXGN84",
            "businessLicenseValidTime": "长期",
            "merchantName": "esigntest批批网实名测试企业",
            "mobile": phonenumber,
            "alipayType": 1,
            "alipayAccount": "100000@qq.com",
            "operatorName": "花木兰",
            "email": "100000@qq.com"
        }

        res = requests.session().post(url=url, data=json.dumps(data), headers=headers)
        print("个人进件提交成功")
        print(res.text)
        return json.loads(res.text)


    # app企业店铺进件
    def addCompany(self):
        # 环境的url
        url = self.url + '/store/subject/addCompany'
        print(url)
        token = self.get_token(userId)

        # 请求头信息
        headers = {
            "Content-Type": "application/json",
            "userId": str(userId),
            "token": token,
            "platform": "Android",
            "versioncode": "189",
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
            "legalPersonPortrait": self.legalPersonPortrait,
            "legalPersonNational": self.legalPersonNational,
            "legalPersonCardValidTime": "2023-08-21",
            "businessLicenseType": 2,
            "businessLicense": self.businessLicense,
            "socialCreditCode": "912388479846526897",
            "businessLicenseValidTime": "长期",
            "merchantName": "esigntest批批网实名测试企业",
            "mobile": 13250252197,
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
    url_select = 'TEST'
    pea_mg_debugUserId = 65
    pea_mg_debugToken = '3354ac6a6e90b140c69bc02c1c800701'
    phonenumber = 18026426127
    userId = 965308

    creat_store_message = creat_store(url_select,str(pea_mg_debugUserId),str(pea_mg_debugToken),phonenumber,userId)

    # creat_store_message.addstore()
    creat_store_message.addMicro()
    # creat_store_message.addPerson()
    # creat_store_message.addCompany()


