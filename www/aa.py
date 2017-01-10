
import asyncio,sys
import orm
import orm
from models import User, Blog, Comment

if __name__=="__main__":
    loop = asyncio.get_event_loop()

    @asyncio.coroutine
    def test():

        yield from orm.create_pool(loop=loop,host='172.18.108.118', port=3306, user='root', password='1234', db='awesome')
        u = User(name='Test', email='0test@example.com', passwd='1234567890', image='about:blank')

        yield from u.save()
        yield from orm.destroy_pool()

    loop.run_until_complete(test())
    loop.close()
    if loop.is_closed():
        sys.exit(0)