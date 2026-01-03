import os
from pathlib import Path

def project_root() -> Path:
    return Path(__file__).resolve().parents[2]

def data_file(filename: str) -> Path:
    return project_root() / "project" / "data" / filename

def data_file_extra(filename: str):
    root = os.path.dirname(__file__)
    file_path_test = os.path.abspath(os.path.join(root, "..", "data", filename))
    return file_path_test