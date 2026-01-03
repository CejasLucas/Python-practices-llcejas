from project.utils.__runtime__ import  Runtime
from project.python_expert.venn_diagrams.__menu__ import get_statements_with_venn_diagrams_exercises

if __name__ == "__main__":
    runtime = Runtime(title="VENN DIAGRAMS")
    runtime.register(practice=get_statements_with_venn_diagrams_exercises())
    runtime.run()