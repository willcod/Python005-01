import redis
import datetime

from .mymodule.redis_instance import get_redis_instance

client = get_redis_instance()

def sendsms(telephone_number: int, content: str, key=None):
    print(f"Send to {telephone_number} \n" +
          "the content is:\n" +
          content
          )
    now = datetime.datetime.now().strftime("%Y%m%d%H%M")
    countkey = str(telephone_number) + now
    hashkey = "Key"+countkey
    value = client.hget(hashkey, 'count')

    if value:
        count = value.decode()
        if count >= '5':
            print("1 分钟内发送次数超过 5 次, 请等待 1 分钟")
            return

    client.incr(countkey)
    inc = client.get(countkey).decode()
    client.hset(hashkey, 'count', inc)

    print("发送成功")


sendsms(123456789, 'hello')
sendsms(123456789, 'hello')
sendsms(123456789, 'hello')
sendsms(123456789, 'hello')
sendsms(123456789, 'hello')
sendsms(123456789, 'hello')
