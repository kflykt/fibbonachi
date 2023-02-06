import asyncio
import random
import sys


# Was the intention to make fib function async? Algorithm is sync so we await at every turn
async def fib(value, function_id):
    if value == 0:
        return 0, function_id
    if value == 1:
        return 1, function_id
    result_1 = await fib(value - 1, function_id)
    result_2 = await fib(value - 2, function_id)
    return result_1[0] + result_2[0], function_id


# I understood that we just want to randomly wait before running function, so I created wrapper for sleep.
# Would this being async be enough to fulfill requirements of async
async def run_after_sleep(fib_function, id, value):
    wait_time = random.uniform(0, 1)
    await asyncio.sleep(wait_time)
    # return wait_time for testing
    return {'function_result': await fib_function(value, id), 'wait_time': wait_time}


def show_result(result_list):
    first_result = result_list[0]["function_result"]
    print("function that completed first:", first_result[1])
    print("fib value: ", first_result[0])


async def run_fib_as_async(value):
    # https://docs.python.org/3.8/library/asyncio-task.html#running-tasks-concurrently
    tasks = [run_after_sleep(fib, 1, value), run_after_sleep(fib, 2, value)]
    task_order_list = []
    for task in asyncio.as_completed(tasks):
        task_order_list.append(await task)

    return task_order_list


async def main(argv):
    if not argv.isdigit():
        print("Input has to be positive integer")
        return False

    number_value = int(argv)

    show_result(await run_fib_as_async(number_value))
