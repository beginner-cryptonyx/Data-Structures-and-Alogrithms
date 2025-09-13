from random import randint
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation


def make_data(size):
    return_array = []
    for _ in range(size):
        return_array.append(randint(0, 2**10))
    return return_array


if __name__ == "__main__":
    # array = make_data(10)
    array = [10, 20, 30, 40, 50]
    fig, ax = plt.subplots()
    graph = ax.bar([i for i in range(len(array))], [element for element in array], color="g")

    def update(frame):
        global array
        ax.set(xticks="")
        array[1] -= 1

    amin = FuncAnimation(fig, update, frames=None)
    plt.show()
