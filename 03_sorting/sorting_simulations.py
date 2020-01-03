import numpy as np
import time
from tqdm import tqdm
from random import shuffle
from matplotlib import pyplot as plt

# Function copied from
# https://stackabuse.com/sorting-algorithms-in-python/

def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True

def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each half
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)


# main
N = 500 # Simulations
bubble_time = list()
insertion_time = list()
merge_time = list()

for simulation in tqdm(range(N)):
    numbers = np.arange(simulation)
    # Bubble Sort
    shuffle(numbers)
    t_bubble = time.time()
    bubble_sort(numbers)
    bubble_time.append(1000*(time.time() - t_bubble))
    # Insertion Sort
    shuffle(numbers)
    t_insertion = time.time()
    insertion_sort(numbers)
    insertion_time.append(1000*(time.time() - t_insertion))
    # Merge Sort
    shuffle(numbers)
    t_merge = time.time()
    merge_sort(numbers)
    merge_time.append(1000*(time.time() - t_merge))

plt.plot(bubble_time, label='bubble_time')
plt.plot(insertion_time, label='insertion_time')
plt.plot(merge_time, label='merge_time')
plt.legend()
plt.title('Sorting of random numbers')
plt.ylabel('Time to sort in ms')
plt.xlabel('Amount of numbers to be sorted'.format(N))
plt.show()
