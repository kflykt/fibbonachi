import pytest
from fib import run_fib_as_async, fib, main, run_after_sleep

@pytest.mark.asyncio
@pytest.mark.parametrize("input,expected", [(3, 2), (5, 5), (6, 8), (13, 233)])
async def test_fib(input, expected):
    value, id = await fib(input, 1)
    assert value == expected

@pytest.mark.asyncio
async def test_fib_error():
    with pytest.raises(TypeError):
        value, _ = await fib("3", 1)


@pytest.mark.asyncio
async def test_fib_with_sleep():
    result = await run_after_sleep(fib, 1, 3)

    assert result["function_result"][0] == 2
    assert isinstance(result["wait_time"], float)


# this can pass even just out of luck
# Giving sleep value as parameter would solve this problem
@pytest.mark.asyncio
async def test_fib_execute_order():
    result = await run_fib_as_async(3)
    assert result[0]["wait_time"] < result[1]["wait_time"]
