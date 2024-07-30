from pathlib import Path
from fastapi import HTTPException


def check_if_file_exists(file_path):
    """
    Raises 404 HTTP Exception in case files don't exist in fs
    """
    if not Path(file_path).exists() or not Path(file_path).is_file():
        raise HTTPException(status_code=404, detail=f"File {file_path} not found")


def check_if_dir_exists(dir_path):
    """
    Raises 404 HTTP Exception in case files don't exist in fs
    """
    if not Path(dir_path).exists() or not Path(dir_path).is_dir():
        raise HTTPException(status_code=404, detail=f"Directory {dir_path} not found")
