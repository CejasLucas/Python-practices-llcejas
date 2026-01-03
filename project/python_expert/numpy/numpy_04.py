import numpy as np

def square_matrix_with_values_between_five_and_fifteen():
    return np.random.uniform(5, 15, size=(5, 5))

def square_matrix_with_values_between_zero_and_one():
    return np.random.rand(5, 5)

def elements_greater_than(matrix, number):
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            value = matrix[i][j]
            if value > number:
                print(f"Matrix[{i}][{j}] = {value}")


def run():
    print("\n⤵️ Create two 5×5 square matrices using NumPy:")
    print("- One matrix with random values between 5 and 15.")
    print("- Another matrix with random values between 0 and 1.")
    print("\n♻️  [Then] ")
    print("Iterate through the second matrix (values between 0 and 1)")
    print("using two nested loops, and print the row and column positions")
    print("along with the values of all elements greater than 0.5 \n")

    first_matrix = square_matrix_with_values_between_five_and_fifteen()
    second_matrix = square_matrix_with_values_between_zero_and_one()

    print("\n" + "=" * 65)
    print(f"{'First matrix (5-15)':^65}")
    print("=" * 65)
    print(first_matrix)
    print("=" * 65)

    print("\n" + "=" * 65)
    print(f"{'Second matrix (0-1)':^65}")
    print("=" * 65)
    print(second_matrix)
    print("=" * 65)

    print("\n" + "-" * 40)
    print(f"{'Elements > 0.5 in second matrix':^40}")
    print("-" * 40)
    elements_greater_than(second_matrix, 0.5)
    print("-" * 40)