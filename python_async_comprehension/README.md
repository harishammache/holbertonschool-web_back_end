                                                    Python - Async Comprehension

0. Async Generator
    coroutine called async_generator that takes no arguments.

1. Async Comprehensions
    The coroutine will collect 10 random numbers using
    an async comprehensing over async_generator,
    then return the 10 random numbers.

2. Run time for four parallel comprehensions
    Import async_comprehension from the previous file
    and write a measure_runtime
    coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.

