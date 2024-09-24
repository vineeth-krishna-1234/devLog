from bubble import Bubble
from selection import Selection
import sys
from random import randint
import argparse


sort_algorithms = {"bubble": Bubble, "selection": Selection}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort the list.")

    # Add positional argument
    parser.add_argument(
        "--type", type=str, help="type of the algorithm to use", default="all"
    )
    parser.add_argument(
        "--size", type=int, help="size of the sample list to use", default=10
    )
    # Parse the arguments
    args = parser.parse_args()
    array_sample = [randint(1, 1000) for _ in range(args.size)]
    print(f"Sample Array: {array_sample}")
    print("")

    if args.type == "all":
        for algorithm, function in sort_algorithms.items():
            print(f"Sorting with {algorithm}")
            instance = function(array_sample)
            instance.sort()
            print(f"ASCENDING :{instance.get_data()}")
            instance.set_direction(False)
            instance.sort()
            print(f"DECENDING :{instance.get_data()}")
            print("")
        sys.exit()
    if args.type not in sort_algorithms.keys():
        print("Algorithm Not Found")
        sys.exit()

    print(f"Sorting with {args.type}")
    instance = sort_algorithms.get(args.type)(array_sample)
    instance.sort()
    print(f"ASCENDING :{instance.get_data()}")
    instance.set_direction(False)
    instance.sort()
    print(f"DECENDING :{instance.get_data()}")
