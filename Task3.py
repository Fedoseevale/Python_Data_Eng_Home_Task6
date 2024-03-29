import random
from Task2 import val_queens

def make_pos():
    positions = list(range(1, 9))
    for i in range(4):
        random.shuffle(positions)
        while not val_queens(positions):
            random.shuffle(positions)
        print(positions)