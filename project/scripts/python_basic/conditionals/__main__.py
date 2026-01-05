from project.scripts.__runtime__ import Runtime
from project.scripts.python_basic.conditionals.__menu__ import get_statements_with_conditional_exercises

if __name__ == "__main__":
    runtime = Runtime(title="CONDITIONALS")
    runtime.register(practice=get_statements_with_conditional_exercises())
    runtime.run()