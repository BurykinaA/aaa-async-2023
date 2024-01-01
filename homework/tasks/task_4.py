result = ""

async def task_1(i: int):
    global result
    result += "1"
    if i == 0:
        return

    if i > 5:
        await task_2(i // 2)
    else:
        await task_2(i - 1)


async def task_2(i: int):
    global result
    result += "2"
    if i == 0:
        return

    if i % 2 == 0:
        await task_1(i // 2)
    else:
        await task_2(i - 1)


async def coroutines_execution_order(i: int = 42) -> int:
    global result
    result = ""
    await task_1(i)
    return int(result)
