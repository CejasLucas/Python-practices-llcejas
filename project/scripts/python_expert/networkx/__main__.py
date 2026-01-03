from scripts.__runtime__ import Runtime
from scripts.python_expert.networkx.__menu__ import get_statements_with_networkx_exercises

if __name__ == "__main__":
    runtime = Runtime(title="NETWORKX")
    runtime.register(practice=get_statements_with_networkx_exercises())
    runtime.run()