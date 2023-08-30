from docx2pdf import convert
import datetime
import shutil
import os

def generate_new_filename(base):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%m-%d-%Y-%H:%M")
    new_filename = f"{base}_{formatted_time}.pdf"
    return new_filename

def copy_resume_to_old_resumes(source_path, destination_directory, new_filename):
    dest_path = os.path.join(destination_directory, new_filename)
    shutil.copy(source_path, dest_path)

def main():
    base_filename = "YuvalKerenResume"
    script_directory = os.path.dirname(__file__)

    source_resume_path = os.path.join(script_directory, "..", f"{base_filename}.pdf")
    destination_resumes_directory = os.path.join(script_directory, "..", "OldResumes")

    new_resume_filename = generate_new_filename(base_filename)
    copy_resume_to_old_resumes(source_resume_path, destination_resumes_directory, new_resume_filename)

    docx_path = os.path.join(script_directory, "..", f"{base_filename}.docx")
    pdf_path = os.path.join(script_directory, "..", f"{base_filename}.pdf")
    convert(docx_path, pdf_path)

if __name__ == "__main__":
    main()