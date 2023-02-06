import asyncio
import sys

from fib import main


if __name__ == "__main__": 
    asyncio.run(main(sys.argv[1]))