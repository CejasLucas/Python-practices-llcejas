from scripts.__runtime__ import Runtime
from scripts.python_basic.tuples.__menu__ import get_statements_with_tuples_exercises

if __name__ == "__main__":
    runtime = Runtime(title="TUPLES")
    runtime.register(practice=get_statements_with_tuples_exercises())
    runtime.run()