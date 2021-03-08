import redis
import requests
import json

import time

# def get_token(userId):
#     r = redis.StrictRedis(host="192.168.1.7", port=6379, db=0)
#     #获取用户登录的token
#     userId = str(userId)
#     token_redis = r.get('pp-user-test:token:app_user:' + userId)
#
#     if token_redis is not None:
#         print(type(token_redis))
#         print(token_redis)
#         str_token = str(token_redis,encoding="utf8")
#         dict_token = json.loads(str_token)
#
#         token = dict_token["token"]
#         print(token)
#         return token
#     else:
#
#         print("获取的token没有数据")
#         exit()




# 定义新增店铺信息的方法

def addstore(phonenumber,userId,token):

    # 环境的url
    url = 'http://rc-zuul.ppwang.com/store/manage/saveStoreInfo'

    # 请求头信息
    headers = {
        "Content-Type": "application/json",
        "userId": str(userId),
        "token": token,
        "platform": "Android"
    }

    # 请求体内容
    data = {
                "userId" : userId,
                "storeName" : userId,
                "storeLogo":"order/202101/05/45b44e950eac35861a0148b5ee500bee.jpg",
                "storeBanner":"order/202101/05/d442d22d7dccce730005e34dba25f364.jpg",
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

    return json.loads(res.text)


# app小微店铺进件
def addMicro(phonenumber,userId,token):

    # 环境的url
    url = 'http://rc-zuul.ppwang.com/store/subject/addMicro'


    card_1 = time.time()

    # 请求头信息
    headers = {
        "Content-Type": "application/json",
        "userId": str(userId),
        "token": token,
        "platform": "Android"
    }

    # 请求体内容
    data = {
            "storeId": userId,
            "legalPersonName": "洪泽佳",
            "legalPersonCard": card_1,
            "legalPersonPortrait": "store/C0E6469F-6445-4A33-99B7-01C0A1543E8B.jpg",
            "legalPersonNational": "store/2116B38C-F4BA-42C8-AB42-D2CF919E0486.jpg",
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
def addPerson(phonenumber,userId,token):

    # 环境的url
    url = 'http://rc-zuul.ppwang.com/store/subject/addPerson'


    # 请求头信息
    headers = {
        "Content-Type": "application/json",
        "userId": str(userId),
        "token": token,
        "platform": "Android"
    }

    # 请求体内容
    data = {
            "storeId": userId,
            "legalPersonName": "花木兰",
            "legalPersonCard": "410702197211052011",
            "legalPersonPortrait": "store/C0E6469F-6445-4A33-99B7-01C0A1543E8B.jpg",
            "legalPersonNational": "store/2116B38C-F4BA-42C8-AB42-D2CF919E0486.jpg",
            "legalPersonCardValidTime": "2023-08-21",
            "businessLicenseType": 1,
            "businessLicense": "store/8140B6C7-272A-46F2-9606-4DB1C2D33CDE.jpg",
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
def addCompany(phonenumber,userId,token):

    # 环境的url
    url = 'http://rc-zuul.ppwang.com/store/subject/addCompany'


    # 请求头信息
    headers = {
        "Content-Type": "application/json",
        "userId": str(userId),
        "token": token,
        "platform": "Android"
    }

    # 请求体内容
    data = {
            "storeId": userId,
            "legalPersonName": "洪泽佳",
            "legalPersonCard": "440582199704224876",
            "legalPersonPortrait": "store/C0E6469F-6445-4A33-99B7-01C0A1543E8B.jpg",
            "legalPersonNational": "store/2116B38C-F4BA-42C8-AB42-D2CF919E0486.jpg",
            "legalPersonCardValidTime": "2023-08-21",
            "businessLicenseType": 2,
            "businessLicense": "store/8140B6C7-272A-46F2-9606-4DB1C2D33CDE.jpg",
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

    return json.loads(res.text)






if __name__ == '__main__':

    # phonenumber = input("输入手机号:")
    # userId = input("输入店铺ID:")
    phonenumber = 18026425112
    userId = 35058699
    token = "cba55d2993b20f3ef085e715d5bb27ed"


    addstore(phonenumber,userId,token)

    addMicro(phonenumber,userId,token)

    # addPerson(phonenumber,userId,token)

    # addCompany(phonenumber,userId,token)

