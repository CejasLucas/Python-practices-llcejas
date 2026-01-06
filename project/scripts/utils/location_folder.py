import os
from pathlib import Path

# 4 Levels: .../project/scripts/utils/location_folder → root

def project_root() -> Path:
    return Path(__file__).resolve().parents[3]

def file_path_using_pathlib(folder_name: str, file_name: str) -> Path:
    return project_root() / "project" / folder_name / file_name

def file_path_using_with_os(folder_name: str, file_name: str):
    root = os.path.dirname(__file__)
    folder_path = os.path.abspath(os.path.join(root, "..", folder_name, file_name))
    return folder_path