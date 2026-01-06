from project.scripts.__runtime__ import Runtime
from project.scripts.python_basic.cycle_while.__menu__ import get_statements_with_cycle_while_exercises

if __name__ == "__main__":
    runtime = Runtime(title="CYCLE WHILE")
    runtime.register(practice=get_statements_with_cycle_while_exercises())
    runtime.run()