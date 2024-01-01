import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine, max_execution_time: float) -> None:
    # Функция принимает на вход корутину, которую необходимо запустить, однако иногда она выполняется
    # слишком долго, это время необходимо ограничить переданным на вход количеством секунд.
    #
    # Тест проверяет, что каждая переданная корутина была запущена, и все они завершились за заданное
    # время.
    #
    # YOUR CODE GOES HERE
    try:
        await asyncio.wait_for(coro, max_execution_time)
    except:
        pass


async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    try:
        await asyncio.wait_for(asyncio.gather(*coros), max_execution_time)
    except:
        pass

