from scripts.__runtime__ import Runtime
from scripts.python_expert.matplotlib.__menu__ import get_statements_with_matplotlib_exercises

if __name__ == "__main__":
    runtime = Runtime(title="MATPLOTLIB")
    runtime.register(practice=get_statements_with_matplotlib_exercises())
    runtime.run()