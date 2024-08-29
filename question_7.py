"""module containing code for implementing 
a recursive search algorithm that searches
for a number entered by user in a list of numbers
"""

def recursive_binary_search(arr, target, low, high):
    # Base case: if the range is invalid, the target is not in the list
    if low > high:
        return False
    
    # Find the middle index
    mid = (low + high) // 2
    
    # Check if the middle element is the target
    if arr[mid] == target:
        return True
    
    # If the target is smaller than the middle element, search the left half
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)
    
    # If the target is larger than the middle element, search the right half
    else:
        return recursive_binary_search(arr, target, mid + 1, high)

# Driver function
def search_number_in_list():
    # List of sorted numbers
    numbers = [1, 2, 4, 7, 10, 15, 20, 25, 30, 35, 40]
    
    # Prompt the user to enter a number
    target = int(input("Enter a number to search for: "))
    
    # Call the recursive binary search function
    result = recursive_binary_search(numbers, target, 0, len(numbers) - 1)
    
    # Print the result
    if result:
        print(f"{target} was found in the list.")
    else:
        print(f"{target} was not found in the list.")

# Call the search function
search_number_in_list()
