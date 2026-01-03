from scripts.__runtime__ import Runtime
from scripts.python_basic.sets.__menu__ import get_statements_with_sets_exercises

if __name__ == "__main__":
    runtime = Runtime(title="SETS")
    runtime.register(practice=get_statements_with_sets_exercises())
    runtime.run()