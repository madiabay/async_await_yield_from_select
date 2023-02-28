import asyncio


async def say_hello():
    print('hello')
    await asyncio.sleep(2)
    print('bye')


async def main():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_hello())
    await task1
    await task2


asyncio.run(main())