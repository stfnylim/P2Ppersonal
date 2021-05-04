"""
    This file deals with all the functions related to file IO 
"""
import os
import hashlib


def convert_to_bytes(file_path):
    read_data = None
    with open(file_path, 'r') as file:
        read_data = file.read()
    return read_data.encode("utf-8")



def create_file(data):
    data = data.decode("utf-8")
    print("Writing to file")
    with open(new_file_path, 'w') as file:
        file.write(data)
    return True


def main():

    data = convert_to_bytes("read_file.txt")
    create_file(data)

    
"""
This method is for checking if the "shared folder" exists in the directory
and if it doesnt, then it will create the folder so that it can sync files with
the other nodes
"""

def create_folder():
        
        os.mkdir(uploadedfilesdir)
        os.mkdir(fileslistdir)
        print("have made the shared and uploaded files folder")

def update_uploaded_files():
    uploadedfiles = os.listdir(os.path.join(cwd, 'sharedfolder'))
    print('These are the uploaded files in the following shared folder:')
    for i in uploadedfiles:
        print(i)



if __name__ == "__main__":
    main()
