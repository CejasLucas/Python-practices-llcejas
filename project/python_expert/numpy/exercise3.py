import numpy as np

def data():
    return (
        [[0] * 9 for _ in range(3)] +
        [[0.5] * 8 + [0.7]] +
        [[1] * 9 for _ in range(3)]
    )

def run_exercise_3():
    print("\n⤵️  Generate a 7×9 matrix where:")
    print("- The first 3 columns contain the value 0")
    print("- The fourth column contains 0.5")
    print("  (Except for the last element, which is 0.7)")
    print("- The remaining columns contain 1")
    print("- Then print the matrix and the average of the last row \n")

    matrix = np.array(data())
    last_row = matrix[-1]
    average = np.mean(last_row)

    print(f"This is the whole matrix:\n {matrix} \n")
    print(f"Last row selected: {last_row} \n")
    print(f"Average of the last row: {average} \n")