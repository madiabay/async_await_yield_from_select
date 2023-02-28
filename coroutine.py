import asyncio

async def count_to_three():
    print("Веду отсчёт. 1")
    await asyncio.sleep(0)
    print("Веду отсчёт. 2")
    await asyncio.sleep(0)
    print("Веду отсчёт. 3")
    await asyncio.sleep(0)


coroutine_counter = count_to_three()
# print(coroutine_counter)  # <coroutine object count_to_three at 0x7f5a58486a98>
# coroutine_counter.send(None)  # Выведет "Веду отсчёт. 1"
# coroutine_counter.send(None)  # Выведет "Веду отсчёт. 2"
# coroutine_counter.send(None)  # Выведет "Веду отсчёт. 3"

# coroutine_counter.send(None)  # Выбросит ошибку StopIteration

while True:
    try:
        coroutine_counter.send(None)  # В четвёртый раз здесь вылетит StopIteration
    except StopIteration:
        break