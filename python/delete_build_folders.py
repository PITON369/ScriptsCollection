import os
import shutil

def delete_build_folders(root):
    targets = {"bin", "obj", "Debug"}
    for path, dirs, files in os.walk(root, topdown=False):
        for d in dirs:
            if d in targets:
                full_path = os.path.join(path, d)
                shutil.rmtree(full_path, ignore_errors=True)
                print(f"Deleted: {full_path}")

if __name__ == "__main__":
    folder = input("Enter the project path: ").strip('"')
    delete_build_folders(folder)
