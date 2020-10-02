from os import system, name
from time import sleep


def clear():
    if name == "nt":
        _ = system("cls")


for i in range(4):
    print("Searching for Hackers.")
    sleep(0.5)
    clear()
    sleep(0.15)
    print("Searching for Hackers .")
    sleep(0.5)
    clear()
    sleep(0.15)
    print("Searching for Hackers  .")
    sleep(0.5)
    clear()
    sleep(0.15)

clear()