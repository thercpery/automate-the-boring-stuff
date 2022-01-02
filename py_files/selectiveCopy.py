#! python3

import os, logging, shutil
from pathlib import Path
logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")

def selectiveCopy(folder):
    logging.debug(f"Start of selectiveCopy({folder})...")
    text_files_path = Path(folder/"text_files")
    logging.debug(f"text_files_path = {text_files_path}")
    py_files_path = Path(folder/"py_files")
    logging.debug(f"py_files_path = {py_files_path}")
    if not os.path.exists(text_files_path) and not os.path.exists(py_files_path):
        os.makedirs(text_files_path)
        os.makedirs(py_files_path)
    for foldername, subfolders, filenames in os.walk(folder):
        logging.debug(f"The current folder is {Path(foldername)}")

        for subfolder in subfolders:
            logging.debug(f"SUBFOLDER OF {foldername}: {subfolder}")

        for filename in filenames:
            logging.debug(f"FILE INSIDE {foldername}: {filename}")
            logging.debug(f"Path : {Path(foldername , filename)}")
            if filename.endswith(".txt"):
                logging.debug(f"{filename} is a text file.")
                if not os.path.exists(Path(text_files_path, filename)):
                    shutil.copy(Path(foldername, filename) , text_files_path)
                    logging.debug(f"Copied {Path(foldername, filename)} to {text_files_path}.")
                else:
                    logging.debug(f"{filename} exists in {text_files_path}")
            elif filename.endswith(".py"):
                logging.debug(f"{filename} is a Python file.")
                if not os.path.exists(Path(py_files_path, filename)):
                    shutil.copy(Path(foldername, filename) , py_files_path)
                    logging.debug(f"Copied {Path(foldername, filename)} to {py_files_path}.")
                else:
                    logging.debug(f"{filename} exists in {py_files_path}")

logging.debug("Start of program.")
logging.debug(f"Path.cwd() = {Path.cwd()}")
selectiveCopy(Path.cwd())
