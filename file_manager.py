"""Util for sorting files by extensions"""

import sys
from pathlib import Path
from shutil import copyfile
from colorama import Fore, Style

DEFAULT_TARGET_PATH = Path.cwd() / "dist"
GAP = "   "
ICO_DIR = "\U0001F4C1"
ICO_FILE = "\U0001F5CB"


def file_system_print(source_path: Path, target_path: Path, level: int):
    """Print file system tree"""

    for e in source_path.iterdir():
        if e.is_dir():
            print(GAP * level, ICO_DIR, Fore.WHITE + e.name + Style.RESET_ALL)
            file_system_print(e, target_path, level + 1)
        else:
            print(
                GAP * level,
                Fore.LIGHTBLACK_EX + ICO_FILE,
                e.name,
                Fore.RED,
                " >> сopied",
                Style.RESET_ALL,
            )
            file_name, file_extension = e.name, e.suffix
            storage_directory = target_path / file_extension
            if not (storage_directory.exists() and storage_directory.is_dir()):
                storage_directory.mkdir(exist_ok=True, parents=True)
            copyfile(e, storage_directory / file_name)


def check_path() -> tuple:
    """Checks if the specified paths are correct"""
    is_folder, source_path, target_path = False, Path(), Path(DEFAULT_TARGET_PATH)
    args = sys.argv
    if len(args) < 2:
        print("The script requires at least one parameter")
    else:
        source_path = Path(args[1])
        if source_path.exists() and source_path.is_dir():
            is_folder = True
            if len(args) > 2:
                target_path = Path(args[2])
            if not (target_path.exists() and target_path.is_dir()):
                target_path.mkdir(exist_ok=True, parents=True)
        else:
            print("The specified source path is not a directory or does not exist")
    return (is_folder, source_path, target_path)


def main():
    """App runtime"""
    is_folder, source_path, target_path = check_path()
    if is_folder:
        file_system_print(source_path, target_path, 0)


if __name__ == "__main__":
    main()
