from docx2pdf import convert
import datetime
import shutil
import os

## generate new file name
current_time = datetime.datetime.now()
base = "YuvalKerenResume"
full = base + str(current_time.month) + "-" + str(current_time.day) + "-" + str(current_time.year)
full += "-" + str(current_time.hour) + ":" + str(current_time.minute) + ".pdf"
print(full)

## copy current resume pdf into OldResumes folder w/ new name
script_directory = os.path.dirname(__file__)
src = os.path.join(script_directory, "..", base + ".pdf")
dest = os.path.join(script_directory, "..", "OldResumes", full)

shutil.copy(src, dest)

## replace YuvalKerenResume with new .docx version
convert("../" + base + ".docx", "../" + base + ".pdf")