import redis
from .mymodule.redis_instance import get_redis_instance

client = get_redis_instance()
client.delete(1001)
client.delete(1002)

def counter(video_id : int):
    client.incr(video_id)


counter(1001)
print(client.get(1001))

counter(1001)
print(client.get(1001))

counter(1002)
print(client.get(1002))

counter(1001)
print(client.get(1001))

counter(1002)
print(client.get(1002))