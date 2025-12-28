import pandas as pd

# Dictionary of students: DNI -> (Name, Grade)
data = {
    "44264079": ("Dominguez", 8.05),
    "41445789": ("Diaz", 9.55),
    "40745789": ("Rodriguez", 5.25),
    "39745789": ("Covey", 7.55),
    "35745789": ("Martins", 9.85),
    "34745789": ("Lopez", 4.33),
    "43645789": ("Paz", 2.5),
    "42745789": ("Messi", 1.75),
    "42645789": ("Cerro", 3.55),
    "41645789": ("Gutierrez", 6),
    "35445789": ("Sosa", 6.75)
}

def calculate_pandas_series(grades):
    """Receives a pandas Series of grades and returns summary statistics."""
    return pd.Series(
        [grades.min(), grades.max(), grades.mean(), grades.std()],
        index=["Minimum", "Maximum", "Average", "Standard Deviation"]
    )

def run_exercise_2():
    print("\nWrite a function that receives a dictionary")
    print("with students' grades and returns a Series with the")
    print("minimum, maximum, mean, and standard deviation.\n")

    # Convert dictionary to a pandas Series (ID -> (Name, Grade))
    students = pd.Series(data.values(), index=data.keys())

    print("=" * 45)
    print(f"{'🎓  Students and their grades':^45}")
    print("=" * 45)
    print(students)
    print("-" * 45)

    # Extract only the grades
    grades = pd.Series([grade for _, grade in data.values()], index=data.keys())

    # Calculate statistics
    stats = calculate_pandas_series(grades)

    print("\n" * 2 + "=" * 45)
    print(f"{'📊  Calculated statistics':^45}")
    print("=" * 45)
    print(stats)
    print("-" * 45)