#! python3
# backupToZip.py - Copies an entire folder and its contents into a zip file whose filename increments.

import zipfile, os, logging
logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")

def backupToZip(folder):
    # Back up the entire contents of "folder into a zip file."
    logging.debug(f"backupToZip({folder}) is running...")

    folder = os.path.abspath(folder) # make sure the folder is absolute
    logging.debug(f"folder = {folder}")

    # Figure out the filename this code should use based on what files already exist.

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        logging.debug(f"zipFilename = {zipFilename}")
        if not os.path.exists(zipFilename):
            logging.debug(f"{zipFilename} does not exist.")
            break
        number = number + 1
        logging.debug(f"number = {number}")

    # Create the zip file.
    logging.debug(f"Creating {zipFilename}...")
    backupZip = zipfile.ZipFile(zipFilename, "w")

    # Walk the entire folder tree and compress the files in each folder.
    for folderName, subfolders, filenames in os.walk(folder):
        logging.debug(f"Adding files in {folderName}...")
        # Add the current folder to the zip file.
        backupZip.write(folderName)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue # don't back up the backup ZIP files.
            backupZip.write(os.path.join(folderName, filename))
    logging.debug("End of program.")

logging.debug("Start of program.")
backupToZip("E:\\tutorials")
