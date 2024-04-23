#!/usr/bin/env python3
"""
    Take the code from wait_n and alter it into
    a new function task_wait_n.
    The code is nearly identical to wait_n except
    task_wait_random is being called.
"""
from typing import List
from asyncio.tasks import Task
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Crée et retourne une liste d'objets asyncio.Task pour
        les coroutines wait_random.

        Paramètres :
            n (int) : Le nombre de fois d'appeler task_wait_random.
            max_delay (int) : Le délai maximal en secondes
            pour chaque appel task_wait_random.

        Retourne :
            List[float] : Une liste contenant les résultats des coroutines.
    """
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    return results
