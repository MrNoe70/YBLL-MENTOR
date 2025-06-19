""" Finds the maximum and minimum values in an array of integers. """

def find_max_and_min(numbers):
    """  Parameters:
    numbers: List[int] - A list of integers.

    Time Complexity: O(n) - where n is the number of elements in the list.
    Space Complexity: O(1)

    Examples: 
    >>> find_max_and_min([3, 1, 4, 1, 5, 9])
    (9, 1)
    >>> find_max_and_min([-2, -3, -1])
    (-1, -3)
    >>> find_max_and_min([])
    (None, None)
    """
    if not numbers:
        return None, None

    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers[1:]:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return max_value, min_value

def main():
    """Main function to execute the max and min finder."""
    numbers = input("Enter integers separated by spaces: ")
    try:        
        numbers_list = [int(x) for x in numbers.split()]
        max_value, min_value = find_max_and_min(numbers_list)

        if max_value is not None and min_value is not None:
            print(f"Maximum value: {max_value}")
            print(f"Minimum value: {min_value}")
        else:
            print("The array is empty.")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
