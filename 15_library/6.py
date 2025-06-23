# You have directory called all files that contains python file & doc file at same place. Write a program to separate these files into folders program and document. You need to display total file count before and after separation
import os
import shutil


def organize_files(directory):

    program_dir = os.path.join(directory, "program")
    document_dir = os.path.join(directory, "document")

    for folder in [program_dir, document_dir]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    all_files = [
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    ]
    print(f"Total files before separation: {len(all_files)}")

    moved_files = 0
    for filename in all_files:
        file_path = os.path.join(directory, filename)

        if filename.endswith(".py"):
            shutil.move(file_path, os.path.join(program_dir, filename))
            moved_files += 1
        elif filename.endswith(".doc") or filename.endswith(".docx"):
            shutil.move(file_path, os.path.join(document_dir, filename))
            moved_files += 1

    remaining_files = [
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    ]
    program_files = [
        f
        for f in os.listdir(program_dir)
        if os.path.isfile(os.path.join(program_dir, f))
    ]
    document_files = [
        f
        for f in os.listdir(document_dir)
        if os.path.isfile(os.path.join(document_dir, f))
    ]

    print("\nAfter separation:")
    print(f"Files in program folder: {len(program_files)}")
    print(f"Files in document folder: {len(document_files)}")
    print(f"Files not moved: {len(remaining_files)}")
    print(f"Total files moved: {moved_files}")


if __name__ == "__main__":
    target_directory = r"C:\Users\Lenovo\OneDrive\Desktop\python\all_files"
    print(f"Organizing files in: {target_directory}")
    organize_files(target_directory)
    print("\nFile organization complete!")
