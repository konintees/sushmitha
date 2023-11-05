#------------------------------------------------------------
# Name : Susmitha Konintees
# Date : 11-03-2023
# Subject : INTRO TO PROG USING SCRIPTING CS-504-D
# Title :  Algorithm Assignment
#-------------------------------------------------------------------

# Defining the Merge sort function that takes the input as array for implementing the Merge sort algoritham
def mergeSort(array):
    # Implementaing the try and catch to handle the exception
        if len(array) > 1: #Checking the array length is greater that so that array is having elements to sort

        #  r is the  mid point where the array is divided into two subarrays so that we have two subarrays for sorting the elements as per the divide and conqurer policy
        # // is the operator that is used to for interger Division in python
            r = len(array)// 2
            # ":r" --> It is the slicing operator that is used to get the elements form the index 0 to the mid of the array but will not include the inder element 'r' and create a new sublist
            left_sub_array = array[:r]
        # "r"" --> It is the  slicing operator that is used to get the elements form the inder r to the end of the elements of an array
            right_sub_array = array[r:]
        # Calling the merge sort function so that tha will create a new subarrays for implementaing the merge sort for sorting the elements
            mergeSort(left_sub_array)
            mergeSort(right_sub_array)

            i = j = k = 0

            # Until we reach either end of either left_sub_array or right_sub_array, pick larger among
            # elements left_sub_array and right_sub_array and place them in the correct position at A[p..r]
            # comparing the  elements of the both sub arrays and storing in the new elements.
            while i < len(left_sub_array) and j < len(right_sub_array):
                if left_sub_array[i] < right_sub_array[j]: # checking the left_sub_array elements is lessthan and storing the data in new new array in ascending order
                    array[k] = left_sub_array[i] # insterting the elements to new array 
                    i += 1 # incrementing the value of the i to i+1 for the next iteration till the condition fails.
                else:
                    array[k] = right_sub_array[j] # if the value of the i is greater than the right_sub_array then storing the element in the new array
                    j += 1 # incrementing the value of the  j to j+1 for the next iteration.
                k += 1 # incrementing the value of the k to  k+1 for the next iteration.

            # When we run out of elements in either L or M,
            # pick up the remaining elements and put in A[p..r]
            # checking for the remaining elements in the left_sub_array and insterting in the array range from "p to r"
            while i < len(left_sub_array):
                array[k] = left_sub_array[i] # instering the elements of the left sub array to new array 
                i += 1 # incrementing the value of the  i to k+1 for the next iteration.
                k += 1 # incrementing the value of the  i to k+1 for the next iteration.
             # checking for the remaining elements in the right_sub_array and insterting in the array range from "p to r"
            while j < len(right_sub_array):
                array[k] = right_sub_array[j] # instering the elements of the right sub array to new array 
                j += 1 # incrementing the value of the  j to j+1 for the next iteration.
                k += 1 # incrementing the value of the  k to k+1 for the next iteration.
        

# Defining the new defination to print the elements taking a array as input.
def printList(array):
    for i in range(len(array)): # iterating the all elements of the array using for loop
        print(array[i], end=" ") # printing the all elements that are avaliable in the array 
    print() # moving the cursor to new line

# This is a common idiom in Python that checks whether the current script is being run as  part of the main program.
if __name__ == '__main__':
    array = [9,6,14,56,44,32,98,76,4] # creating the unsorted array of elements
    print("Printing the unsorted array:",array) # printing the unsorted elements 

    mergeSort(array) # Calling the function merge sort to sort the elements of an array as userinput

    print("Sorted list in Ascending order : ")
    printList(array)
