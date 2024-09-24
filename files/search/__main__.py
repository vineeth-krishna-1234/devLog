from linear import LinearSearch
from binary import BinarySearch
from random import randint


if __name__ == "__main__":
    array_sample = [randint(1, 10) for _ in range(20)]
    print(array_sample)

    linear_search = LinearSearch(array_sample)
    binary_search = BinarySearch(array_sample)
    random_value = randint(1, 10)
    print(random_value)
    print(linear_search.search_with_repetition(random_value))
    print(binary_search.search_with_repetition(random_value))
