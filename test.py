from main import find_smallest_absolute_diff
import random
from time import time


def create_sample_data(min_number: int, max_number: int, sample_range: int):
    a_list = random.sample(range(min_number, max_number), sample_range)
    return a_list


A_list = create_sample_data(1, 1000000000000, 10000000)
A_list.sort()
B_list = create_sample_data(1, 2000000000, 5000)
B_list.sort(reverse=True)


start = time()

min_diff = find_smallest_absolute_diff(A_list, B_list)

time_it_takes = round((time()-start), 5)

print(f"Finding the smallest difference took {time_it_takes}")
print("The smallest absolute diff is", min_diff)
