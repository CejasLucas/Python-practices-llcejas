from project.scripts.python_expert.pandas.pandas_01 import run as ex_01
from project.scripts.python_expert.pandas.pandas_02 import run as ex_02
from project.scripts.python_expert.pandas.pandas_03 import run as ex_03
from project.scripts.python_expert.pandas.pandas_04 import run as ex_04
from project.scripts.python_expert.pandas.pandas_05 import run as ex_05
from project.scripts.python_expert.pandas.pandas_06 import run as ex_06
from project.scripts.python_expert.pandas.pandas_07 import run as ex_07

def get_statements_with_pandas_exercises():
    return [
        {"statement": "Sales discount calculation", "exercise": ex_01},
        {"statement": "Student grades statistics", "exercise": ex_02},
        {"statement": "Monthly balance calculation", "exercise": ex_03},
        {"statement": "Car prices analysis (autos.xlsx)", "exercise": ex_04},
        {"statement": "Internal commerce CSV analysis", "exercise": ex_05},
        {"statement": "Grouping and stats on datasets", "exercise": ex_06},
        {"statement": "Salary database analysis", "exercise": ex_07}
    ]
