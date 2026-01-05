from project.scripts.__runtime__ import Runtime
from project.scripts.python_expert.numpy.__menu__ import get_statements_with_numpy_exercises

if __name__ == "__main__":
    runtime = Runtime(title="NUMPY")
    runtime.register(get_statements_with_numpy_exercises())
    runtime.run()