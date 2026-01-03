from project.utils.__runtime__ import Runtime
from project.python_basic.dictionaries.__menu__ import get_statements_with_dictionaries_exercises

if __name__ == "__main__":
    runtime = Runtime(title="DICTIONARIES")
    runtime.register(practice=get_statements_with_dictionaries_exercises())
    runtime.run()