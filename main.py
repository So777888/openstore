import redis
import requests
import json

import time

def get_token(userId):
    r = redis.StrictRedis(host="192.168.1.7", port=6379, db=0)
    #获取用户登录的token
    userId = str(userId)
    token_redis = r.get('pp-user-test:token:app_user:' + userId)

    if token_redis is not None:
        print(type(token_redis))
        print(token_redis)
        str_token = str(token_redis,encoding="utf8")
        dict_token = json.loads(str_token)

        token = dict_token["token"]
        print(token)
        return token
    else:
        print("获取的token没有数据")
        exit()




# 定义新增店铺信息的方法

def addstore(phonenumber,userId):

    # 环境的url
    url = 'http://test-zuul.ppwang.com:8107/store/manage/saveStoreInfo'
    token = get_token(userId)

    # 请求头信息
    headers = {
        "Content-Type": "application/json",
        "userId": str(userId),
        "token": token,
        "platform": "Android",
        "versioncode":"189",
        "pea-mg-version":str(1.0),
        "pea-mg-debugCode":str(45747468),
        "pea-mg-debugUserId":str(65),
        "pea-mg-debugToken":"bd1f865df47a83722b7d6bb76c29cf67"
    }


    # pea - mg - timestamp = "1614930051";




    # 请求体内容
    data = {
                "userId" : userId,
                "storeName" : userId,
                "storeLogo":"other/202101/04/C07FF5592372409D8152CE2E80271139.jpg",
                "storeBanner":"other/202101/04/D6B55A5017FF42ADB7CC22909D0569BD.jpg",
                "regionId":477,
                "address":"天河客运站长版东路808",
                "ownerName":"洪小明",
                "tel":phonenumber,
                "syncStoreInfo":1,
                "cateId":77,
                "retailNum":1,
                "packNum":3,
                "wechat":""
            }

    res = requests.session().post(url=url, data=json.dumps(data), headers=headers)

    print("提交店铺信息成功")

    print(res.text)

    return json.loads(res.text)


# app小微店铺进件
def addMicro(phonenumber,userId):

    # 环境的url
    url = 'http://test-zuul.ppwang.com:8107/store/subject/addMicro'
    token = get_token(userId)

    card_1 = time.time()

    # 请求头信息
    headers = {
        "Content-Type": "application/json",
        "userId": str(userId),
        "token": token,
        "platform": "Android",
        "versioncode": "189",
        "pea-mg-version": str(1.0),
        "pea-mg-debugCode": str(45747468),
        "pea-mg-debugUserId": str(65),
        "pea-mg-debugToken": "bd1f865df47a83722b7d6bb76c29cf67"
    }

    # 请求体内容
    data = {
            "storeId": userId,
            "legalPersonName": "洪泽佳",
            "legalPersonCard": card_1,
            "legalPersonPortrait": "store/ED85D508-B0C7-4EE9-88D9-E5683600F692.jpg",
            "legalPersonNational": "store/93A0671C-A402-4F7B-8251-140DC0480BC2.jpg",
            "legalPersonCardValidTime": "2022-02-02",
            "mobile": 13250252197,
            "alipayAccount": phonenumber,
            "wechatAdded": 1
        }

    res = requests.session().post(url=url, data=json.dumps(data), headers=headers)

    print("小微进件提交成功")

    print(res)
    print(res.text)

    # print(json.loads(res.text))

    return json.loads(res.text)



# app个人店铺进件
def addPerson(phonenumber,userId):

    # 环境的url
    url = 'http://test-zuul.ppwang.com:8107/store/subject/addPerson'
    token = get_token(userId)

    # 请求头信息
    headers = {
        "Content-Type": "application/json",
        "userId": str(userId),
        "token": token,
        "platform": "Android",
        "versioncode": "189",
        "pea-mg-version": str(1.0),
        "pea-mg-debugCode": str(45747468),
        "pea-mg-debugUserId": str(65),
        "pea-mg-debugToken": "bd1f865df47a83722b7d6bb76c29cf67"
    }

    # 请求体内容
    data = {
            "storeId": userId,
            "legalPersonName": "花木兰",
            "legalPersonCard": "410702197211052011",
            "legalPersonPortrait": "store/ED85D508-B0C7-4EE9-88D9-E5683600F692.jpg",
            "legalPersonNational": "store/93A0671C-A402-4F7B-8251-140DC0480BC2.jpg",
            "legalPersonCardValidTime": "2023-08-21",
            "businessLicenseType": 1,
            "businessLicense": "store/D59BD928-9BA1-4724-B6F5-85C5B28D4161.jpg",
            "socialCreditCode": "91440101MA9UXA8L0X",
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

    print(res)
    print(res.text)

    # print(json.loads(res.text))

    return json.loads(res.text)



# app企业店铺进件
def addCompany(phonenumber,userId):

    # 环境的url
    url = 'http://test-zuul.ppwang.com:8107/store/subject/addCompany'
    token = get_token(userId)

    # 请求头信息
    headers = {
        "Content-Type": "application/json",
        "userId": str(userId),
        "token": token,
        "platform": "Android",
        "versioncode": "189",
        "pea-mg-version": str(1.0),
        "pea-mg-debugCode": str(45747468),
        "pea-mg-debugUserId": str(65),
        "pea-mg-debugToken": "bd1f865df47a83722b7d6bb76c29cf67"
    }

    # 请求体内容
    data = {
            "storeId": userId,
            "legalPersonName": "洪泽佳",
            "legalPersonCard": "440582199704224876",
            "legalPersonPortrait": "store/ED85D508-B0C7-4EE9-88D9-E5683600F692.jpg",
            "legalPersonNational": "store/93A0671C-A402-4F7B-8251-140DC0480BC2.jpg",
            "legalPersonCardValidTime": "2023-08-21",
            "businessLicenseType": 2,
            "businessLicense": "store/D59BD928-9BA1-4724-B6F5-85C5B28D4161.jpg",
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





if __name__ == '__main__':

    # phonenumber = input("输入手机号:")
    # userId = input("输入店铺ID:")
    phonenumber = 13250230089
    userId = 965202


    addstore(phonenumber,userId)

    # addMicro(phonenumber,userId)

    # addPerson(phonenumber,userId)

    # addCompany(phonenumber,userId)

