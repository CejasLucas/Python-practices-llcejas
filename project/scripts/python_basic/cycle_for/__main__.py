from project.scripts.__runtime__ import Runtime
from project.scripts.python_basic.cycle_for.__menu__ import get_statements_with_cycle_for_exercises

if __name__ == "__main__":
    runtime = Runtime(title="CYCLE FOR")
    runtime.register(practice=get_statements_with_cycle_for_exercises())
    runtime.run()