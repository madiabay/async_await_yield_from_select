import httpx
import asyncio


async def send_request(url: str) -> httpx.Response:
    print('hello')
    async with httpx.AsyncClient() as client:
        return await client.get(url)

# async def main():
#     result1 = await asyncio.create_task(send_request('https://example.com'))
#     result2 = await asyncio.create_task(send_request('https://example.com'))
#     result3 = await asyncio.create_task(send_request('https://example.com'))

#     print(result1)
#     print(result2)
#     print(result3)


async def main():
    requests = [send_request('https://example.com') for _ in range(3)]
    responses = await asyncio.gather(*requests)

    print(responses)


asyncio.run(main())