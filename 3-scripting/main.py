import os

def main():
    print(f"The name of this module is: {__name__}")
    for root, directories, files in os.walk("../"):
        # print(f"Root: {root}")
        # print(f"Directories: {directories}")
        # print(f"Files: {files}")
        for _file in files:
            absolute_path = os.path.join(root, _file)
            print(f"File path: {absolute_path}")
if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(Exception)


