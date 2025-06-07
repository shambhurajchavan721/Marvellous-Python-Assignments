import threading
import multiprocessing
import time

def main():
    normal_sum()
    threading_sum()
    multiprocessing_sum()

def calculate_sum(start, end, result, index):
    total = 0
    for i in range(start, end + 1):
        total = total + i
    result[index] = total

def normal_sum():
    start_time = time.time()
    total = 0
    for i in range(1, 10000001):
        total = total + i
    print("normal Sum:", total)

    end_time = time.time
    print("Time for normal sum:",end_time - start_time)

def threading_sum():
    start_time = time.time()
    result = [0, 0]

    t1 = threading.Thread(target=calculate_sum, args=(1, 5000000, result, 0))
    t2 = threading.Thread(target=calculate_sum, args=(5000001, 10000000, result, 1))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Threading Sum:", result[0] + result[1])

    end_time = time.time
    print("Time for Threading sum:", end_time - start_time)

def multiprocessing_sum():
    start_time = time.time()
    manager = multiprocessing.Manager()
    result = manager.list([0, 0])

    p1 = multiprocessing.Process(target=calculate_sum, args=(1, 5000000, result, 0))
    p2 = multiprocessing.Process(target=calculate_sum, args=(5000001, 10000000, result, 1))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Multiprocessing Sum:", result[0] + result[1])

    end_time = time.time
    print("Time for Multiprocessing sum:", end_time - start_time)

if __name__ == "__main__":
    main()