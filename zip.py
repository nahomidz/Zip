from zipfile import ZipFile

test_file_name = "respaldo.zip"

with ZipFile(test_file_name, 'r') as zip:
    zip.printdir()
    zip.extractall() 