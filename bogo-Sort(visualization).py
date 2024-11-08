import random
from matplotlib import pyplot

def bogo_sort(a):
    n = len(a)
    is_sorted = False
    while not is_sorted:
        # swap two elements
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        a[i], a[j] = a[j], a[i]
        yield a

        # check if sorted
        is_sorted = all(a[i] <= a[i + 1] for i in range(n - 1))


def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                yield a


def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        yield a


def radix_sort(a):
    # Radix Sort
    def counting_sort(a, exp):
        n = len(a)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = a[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = a[i] // exp
            output[count[index % 10] - 1] = a[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            a[i] = output[i]
            yield a

    n = len(a)
    max_value = max(a)
    exp = 1
    while max_value // exp > 0:
        yield from counting_sort(a, exp)
        exp *= 10


def counting_sort(a):
    # Counting Sort
    n = len(a)
    output = [0] * n
    count = [0] * (max(a) + 1)

    for i in range(n):
        count[a[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        output[count[a[i]] - 1] = a[i]
        count[a[i]] -= 1
        i -= 1
        yield output

    for i in range(n):
        a[i] = output[i]
        yield a


def bucket_sort(a):
    # Bucket Sort
    n = len(a)
    buckets = [[] for _ in range(n)]

    for num in a:
        index = int(num * n)
        buckets[index].append(num)

    for i in range(n):
        buckets[i].sort()
        yield [item for sublist in buckets[:i + 1] for item in sublist]

    for i in range(n):
        a[i] = buckets[i][0]
        yield a


def merge_sort(a):
    # Merge Sort
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def _merge_sort(a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = _merge_sort(a[:mid])
        right = _merge_sort(a[mid:])
        return merge(left, right)

    result = _merge_sort(a)
    yield result

    for i in range(len(a)):
        a[i] = result[i]
        yield a


def quick_sort(a, low, high):
    # Quick Sort
    if low < high:
        pivot_index = partition(a, low, high)
        yield a
        yield from quick_sort(a, low, pivot_index - 1)
        yield from quick_sort(a, pivot_index + 1, high)




def heap_sort(a):
    # Heap Sort
    def heapify(a, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and a[left] > a[largest]:
            largest = left

        if right < n and a[right] > a[largest]:
            largest = right

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            yield a
            yield from heapify(a, n, largest)

    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        yield a
        yield from heapify(a, i, 0)



def visualize(sorting_algorithm1, sorting_algorithm2, n):
    # create array
    a = [1, 43, 5, 23]

    # generate sorting process for algorithm 1
    sorting_process1 = sorting_algorithm1(a)
    # generate sorting process for algorithm 2
    sorting_process2 = sorting_algorithm2(a)

    # track whether each algorithm has finished
    finished1 = False
    finished2 = False

    # visualize sorting process for both algorithms
    while not finished1 or not finished2:
        # Sorting Algorithm 1
        if not finished1:
            next_a1 = next(sorting_process1, None)
            if next_a1 is not None:
                # subplot for algorithm 1
                pyplot.subplot(1, 2, 1)
                pyplot.bar(x=range(1, len(a) + 1), height=next_a1, color='blue')
                pyplot.title('Algorithm 1 - Current State')
                pyplot.axis("off")

                # check if algorithm 1 has finished
                if next_a1 is None:
                    finished1 = True
                    pyplot.subplot(1, 2, 1)
                    pyplot.bar(x=range(1, len(a) + 1), height=a, color='blue')
                    pyplot.title('Algorithm 1 - Final State')
                    pyplot.axis("off")

        # Sorting Algorithm 2
        if not finished2:
            next_a2 = next(sorting_process2, None)
            if next_a2 is not None:
                # subplot for algorithm 2
                pyplot.subplot(1, 2, 2)
                pyplot.bar(x=range(1, len(a) + 1), height=next_a2, color='orange')
                pyplot.title('Algorithm 2 - Current State')
                pyplot.axis("off")

                # check if algorithm 2 has finished
                if next_a2 is None:
                    finished2 = True
                    pyplot.subplot(1, 2, 2)
                    pyplot.bar(x=range(1, len(a) + 1), height=a, color='orange')
                    pyplot.title('Algorithm 2 - Final State')
                    pyplot.axis("off")

        pyplot.pause(0.6)
        pyplot.clf()

    pyplot.show()

# Example: Visualize Bogo Sort and Bubble Sort
visualize(heap_sort, bubble_sort, n=4)
