from huey import RedisHuey
import os


huey = RedisHuey("whois", host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])
