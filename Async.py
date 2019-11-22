import asyncio
import random
import time


async def count(id):
    for i in range(1, 20):  # does not include 20
        print(str(id) + ' ' + str(i))
        await asyncio.sleep(random.randrange(4))
        print(str(id) + ' ' + str(i * i))


async def main():
    await asyncio.gather(count(1), count(2), count(3))


'''
async def rand_sleep():
    time.sleep(random.randrange(4))
    return 1
'''

if __name__ == '__main__':
    asyncio.run(main())
