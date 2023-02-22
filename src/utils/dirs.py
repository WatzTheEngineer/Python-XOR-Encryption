import os
from pathlib import Path


def checkdirs():
    Path("dcr").mkdir(parents=True, exist_ok=True)
    Path("ecr").mkdir(parents=True, exist_ok=True)
    Path("keys").mkdir(parents=True, exist_ok=True)


def filelist(folder: str) -> list[str]:
    files = []
    for element in os.listdir(folder):
        if os.path.isfile(folder + "/" + element):
            files.append(element)
    return files


def dir_contains_files(folder: str) -> bool:
    if len(filelist(folder)) > 0:
        return True
    return False
