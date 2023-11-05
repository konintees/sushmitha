#------------------------------------------------------------
# Name : Susmitha Konintees
# Date : 11-03-2023
# Subject : INTRO TO PROG USING SCRIPTING CS-504-D
# Title : Algorithm Assignment
#-------------------------------------------------------------------

# Defining the Merge  function that takes the left and right as parameters.
def merge(left, right):
    merged = []  # Initialize an empty list to store the merged result
    left_index, right_index = 0, 0  # Initialize indices for the left and right with zero 

    # Compare and merge elements from left and right lists
    # Iteraing the loop till the elements in both the left and right subarrays to be merged.
    while left_index < len(left) and right_index < len(right):
        # checking the left_index elements is greater than right_index  and storing the data in new new array for modified in descending order
        if left[left_index] > right[right_index]:  
            merged.append(left[left_index])  # Append the larger element from the left list
            left_index += 1 # incrementing the value of the i to i+1 for the next iteration till the condition fails.
        else:
            merged.append(right[right_index])  # Append the larger element from the right list
            right_index += 1 # incrementing the value of the i to i+1 for the next iteration till the condition fails.

    # If there are remaining elements in the left or right lists, extend the merged list with them.
    merged.extend(left[left_index:])  # Append any remaining elements from the left list
    merged.extend(right[right_index:])  # Append any remaining elements from the right list

    return merged  # Return the merged and sorted list


# Defining the Merge sort function that takes the input as array for implementing the Merge sort algoritham in descending order
def merge_sort_descending(arr):
    # Convert the input list into a list of lists with single elements from the original
    sorted_lists = [[x] for x in arr]
    # The while loop continues as long as there are more than one sorted sublist to merge.
    while len(sorted_lists) > 1:
        new_sorted_lists = [] # Defining the new empyt list for storing the elements that are sorted

        # Merge adjacent pairs of sorted lists
        # Generating a sequence of numbers range starting from 0 to the lenght of the sorted list with the step of 2 but not the lenth of the sorted list
        for i in range(0, len(sorted_lists), 2):
            if i + 1 < len(sorted_lists): # checking the element wiht index is i+1 is lessthan the length of the sorted list
                merged = merge(sorted_lists[i], sorted_lists[i + 1])  # Merging the two adjacent sorted list
                new_sorted_lists.append(merged) # adding the the elements of the merged lists into new_sorted_lists list created.
            else:
                new_sorted_lists.append(sorted_lists[i])  # we are adding the remaining elements to the list.

        sorted_lists = new_sorted_lists   # Adding the list of mergerd elements into the sorted list.

    return sorted_lists[0]  # Returing  the final sorted list after completing the sorting of the elements.

# Take user input for a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
# split() is function that is used to spilt the string into substirng
#convering the substring into intergers.
user_list = list(map(int, user_input.split()))  

# Sort the user input in descending order iteratively using the merge_sort_descending function
sorted_user_list = merge_sort_descending(user_list) # Calling the merge_sort_descending function to implement the sort on user input.
#Printing the elemetns in the descending order 
print("Sorted in descending order:", sorted_user_list)
