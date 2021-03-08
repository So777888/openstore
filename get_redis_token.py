import redis
import json



r = redis.StrictRedis(host="192.168.1.7", port=6379, db=0)
def add_redis():
    r = redis.Redis(host="192.168.1.7", port=6379, password="123", db=0)
    with r.pipeline(transaction=False) as p:

        for value in range(1,13000):
            # print(value)
            mapping = {value:value}
            r.zadd("Pp-RelationStoreFans_961948", mapping)
        p.execute()



def get_redis_token(userId):
    token_redis = r.get('pp-user-test:token:app_user:' + userId)
    if token_redis is not None:
        print(type(token_redis))
        print(token_redis)
        str_token = str(token_redis, encoding="utf8")
        dict_token = json.loads(str_token)

        token = dict_token["token"]
        print(token)
        return token
    else:

        print("获取的token没有数据")
        exit()




if __name__ == '__main__':
    # add_redis()
    userId = input("输入userId:")

    get_redis_token(userId)

