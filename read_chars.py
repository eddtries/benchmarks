import timeit


def read_file(path):
    text = []
    with open(path) as file:
        for line in file.readlines():
            for c in line:
                text.append(c)

    return text


def solution_one(input_str):
    d = {}
    for i in input_str:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d


def solution_two(input_str):
    d = {}
    for i in input_str:
        d[i] = d.get(i, 0) + 1
    return d


if __name__ == '__main__':
    text = read_file('./odyssey.txt')
    starttime = timeit.default_timer()
    for i in range(1, 10000):
        solution_one(text)
    print("Solution A:",
          timeit.default_timer() - starttime)

    starttime = timeit.default_timer()
    for i in range(1, 10000):
        solution_two(text)
    print("Solution B:",
          timeit.default_timer() - starttime)

    # Solution A: 21.370537624985445
    # Solution B: 19.468167208018713
