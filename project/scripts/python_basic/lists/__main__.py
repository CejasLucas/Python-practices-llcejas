from scripts.__runtime__ import Runtime
from scripts.python_basic.lists.__menu__ import get_statements_with_lists_exercises

if __name__ == "__main__":
    runtime = Runtime(title="LISTS")
    runtime.register(practice=get_statements_with_lists_exercises())
    runtime.run()