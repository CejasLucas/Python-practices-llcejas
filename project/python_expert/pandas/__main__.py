from project.utils.__runtime__ import Runtime
from project.python_expert.pandas.__menu__ import get_statements_with_pandas_exercises

if __name__ == "__main__":
    runtime = Runtime(title="PANDAS")
    runtime.register(get_statements_with_pandas_exercises())
    runtime.run()