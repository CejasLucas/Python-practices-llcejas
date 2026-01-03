import numpy as np

def data():
    return [
        [-44.0, 12.0],
        [12.0, 51.0],
        [1300.0, -5.0]
    ]

def run():
    print("\n⤵️  Perform the following operations:")
    print("- Subtract 5 from the second row of the matrix.")
    print("- Multiply the entire matrix by 2.")
    print("- Divide the first two rows of the matrix by -5.")
    print("- Print the last row of the matrix. \n")

    np.set_printoptions(precision=1, floatmode='fixed', suppress=False)

    matrix_original = np.array(data())
    matrix_copy = matrix_original.copy()

    print(f"Original matrix:\n{matrix_original}\n")

    matrix_copy[1] = matrix_copy[1] - 5
    print(f"Subtract 5 from row two:\n{matrix_copy}\n")

    matrix_copy = matrix_copy * 2
    print(f"Multiply the entire matrix by 2:\n{matrix_copy}\n")

    matrix_copy[0:2] = matrix_copy[0:2] / -5
    print(f"Divide the first two rows by -5:\n{matrix_copy}\n")

    print(f"Last row of the matrix:\n{matrix_copy[-1]}\n")

    print(f"Test matrix:\n{matrix_copy}\n")

    print(f"Original matrix:\n{matrix_original}\n")