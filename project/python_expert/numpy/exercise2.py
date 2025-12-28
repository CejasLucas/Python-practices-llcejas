import numpy as np

def data():
    return [
        [-44.0, 12.0],
        [12.0, 51.0],
        [1300.0, -5.0]
    ]

def add_elements(matrix):
    amount = 0
    for row in matrix:
        for element in row:
            amount += element
    return amount

def average_of_the_first_two_rows(matrix):
    amount = 0
    counter = 0
    for row in matrix[0:2]:
        for element in row:
            amount += element
            counter += 1
    return amount / counter

def run_exercise_2():
    print("\n⤵️  Using NumPy:")
    print("- Compute the sum of all elements of a from the ")
    print("  previous exercise using two nested for loops")
    print("- Compute the sum of all elements of a using np.sum")
    print("- Compute the average of the elements in the ")
    print("  first two rows of a using two nested for loops.")
    print("- Compute the same average using slices (:) and np.mean \n")

    matrix = np.array(data())

    print(f"Original matrix:\n{matrix}\n")

    print(f"Add elements using nested loops: {add_elements(matrix)}\n")

    print(f"Add elements using NumPy sum function: {np.sum(matrix)}\n")

    print(f"Average of elements in the first two rows using loops: {average_of_the_first_two_rows(matrix)}\n")

    print(f"Average of elements in the first two rows using NumPy: {np.mean(matrix[0:2])}\n")