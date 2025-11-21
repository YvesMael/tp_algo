import matplotlib.pyplot as plt
from timeit import timeit
from collections.abc import Callable, Iterator, Iterable
import functools
import random
from stupidsort import stupidsort, insertionsort

def input_arrays(n: int=1_000, N: int=1_000, repl: bool=True) -> Iterator[list[int]]:
    if not repl:
        for i in range(n):
            yield random.sample([el for el in range(N)], k=i)
    else: 
        for i in range(n):
            yield random.choices([el for el in range(N)], k=i)  


def plot_array(array: list[float], title: str, log: bool = False) -> None:
    plt.title(title)
    plt.semilogy(array) if log else plt.plot(array)
    plt.show()


def timeit_batch(fun: Callable, inputs: Iterable, setup: str='pass', cumul: int = 10) -> list[float]:
    return [timeit( f'{fun.__name__}({arg})',
                    setup=setup,
                    globals=globals(),
                    number=cumul) for arg in inputs]


def sum_reduce(t):
    return functools.reduce(lambda x, y: x + y, t, 0)


if __name__ == '__main__':
    # "scénario jouet" de parangonnage, à adapter au fur et à mesure du TP
    # result: list[float] = timeit_batch(sum, input_arrays(), cumul=4)
    # result_reduce: list[float] = timeit_batch(sum_reduce, input_arrays(), cumul=4)
    # print(result_reduce)
    # plot_array(array=result, title="sum", log=False)
    # plot_array(array=result_reduce, title="sum_reduce", log=False)

    liste = [5,4,10,7,1,6,2,100,50,20,70,0,3,40]
    print(insertionsort(liste))