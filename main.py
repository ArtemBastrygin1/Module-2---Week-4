import multiprocessing


def compute_squares(data):
    for i in data:
        print(i ** 2)

    processes = []
    for i in len(data):
        p = multiprocessing.Process(target=compute_squares, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join(1)


compute_squares(list(range(5)))
