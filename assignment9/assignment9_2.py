import multiprocessing

def square(sublist, result_list):
    for num in sublist:
        result_list.append(num * num)

def main():
    Data = [23,57,45,695,5455,456585,4556655,55666355,456566565,4565632]

    mid = len(Data) // 2
    part1 = Data[:mid]
    part2 = Data[mid:]

    manager = multiprocessing.Manager()
    result = manager.list()

    p1 = multiprocessing.Process(target=square, args=(part1, result))
    p2 = multiprocessing.Process(target=square, args=(part2, result))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Squares:", list(result))

if __name__ == "__main__":
    main()