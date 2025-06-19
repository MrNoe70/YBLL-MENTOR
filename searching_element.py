""" Searching an element in an array using linear search   """

def find_element(arr, target):
    """  Parameters:
    arr: List[int] - A list of integers.
    target: int - The integer to search for.

    Time Complexity: O(n) - where n is the number of elements in the list.
    Space Complexity: O(1)

    Examples:
    >>> find_element([1, 2, 3, 4, 5], 3)
    2
    >>> find_element([1, 2, 3, 4, 5], 6)
    -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 # The target element is not found in the array

if __name__ == "__main__":
    arr = input("Enter integers separated by spaces: ")
    try:
        arr_list = [int(x) for x in arr.split()]
        target = int(input("Enter the integer to search for: "))
        index = find_element(arr_list, target)

        if index != -1:
            print(f"Element found at index: {index}")
        else:
            print("Element not found in the array.")
    except ValueError:
        print("Please enter valid integers.")
