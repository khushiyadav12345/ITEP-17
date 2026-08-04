from threading import Thread
class FirstThread(Thread):
    def run(self):
        for _ in range(5):
            print("Hello...")