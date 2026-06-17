import threading
import time


def walk_dog(name):
    time.sleep(8)
    print(f"You walk {name}")

def take_trash_out():
    time.sleep(2)
    print("You take the trash out")

def get_clothes():
    time.sleep(4)
    print("You clean clothes")


thread1 = threading.Thread(target = walk_dog, args = ("Scooby",))
thread1.start()

thread2 = threading.Thread(target = take_trash_out)
thread2.start()

thread3 = threading.Thread(target = get_clothes)
thread3.start()

