###
# Solution of step one can be adapted to step two using startswith("000000")
# Just wanted to test out threading in Python (Implementation is far from good)
###

# Imports
import hashlib
import threading
import time
import sys

#########STEP ONE#########
def step_one(string: str) -> int:
    cpt = 0

    while True:
        message = f"{string}{cpt}"
        md5_hash = hashlib.md5(message.encode()).hexdigest()
        if md5_hash.startswith("00000"):
            return cpt
        cpt += 1

#########STEP TWO#########
def step_two(original_string) -> int:
    class myThread(threading.Thread):
        def __init__(self, name, counter):
            threading.Thread.__init__(self)
            self.name = name
            self.counter = counter
        def run(self):
            print ("Starting " + self.name)
            calculating_hash(self.name, self.counter, original_string)
            print ("Exiting " + self.name)

    def calculating_hash(threadName, cpt, original_string):
        original_string = "iwrupvqb"
        string = "iwrupvqb"

        while True:
            count = 0
            hashed = hashlib.md5(string.encode())

            for i in range(6):
                if hashed.hexdigest()[i] == "0":
                    count += 1
            if count == 6:
                print("MD5 found:",hashed.hexdigest())
                print("Corresponding string:",cpt)
                sys.exit()
            else:
                count = 0
                cpt += 1
                string = original_string
                string += str(cpt)
                # print("String:", threadName,string)

    thread1 = myThread("Thread-1", -1)
    thread2 = myThread("Thread-2", 6000000)
    thread3 = myThread("Thread-3", 7000000)
    thread4 = myThread("Thread-4", 8000000)
    thread5 = myThread("Thread-5", 9000000)
    thread6 = myThread("Thread-6", 10000000)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    print ("Exiting Main Thread")

def main() -> None:
    start_time = time.time()
    string = "iwrupvqb"
    print("Result of Part One:", step_one(string))
    print("Result of Part Two:", step_two(string))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    sys.exit(main())