#main.py
from utils.file_utils import read_file

def main():
    data = read_file("utils/sample.txt")
    print(data)
    
if __name__ == "__main__":
    main()  
    