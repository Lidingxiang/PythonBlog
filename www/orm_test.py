

import asyncio
import logging

from orm import create_pool
from models import User


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    async def test():

        await create_pool(loop=loop, user='root', password='1234', db='awesome', host='172.18.108.118', port=3306)

        # 新增记录
        # u = User(name='Test', email='2test@example.com',
        #          passwd='1234567890', image='about:blank')
        # await u.save()

        # 测试select语句
        users = await User.findAll(orderBy='created_at')
        for user in users:
            logging.info('name: %s, passwd: %s' % (user.name, user.passwd))

    loop.run_until_complete(test())
    loop.close()
