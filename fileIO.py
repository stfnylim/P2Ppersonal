"""
    This file deals with all the functions related to file IO 
"""
import os
import hashlib
from server_client.constants import *

cwd = os.getcwd()
uploadedfilesdir = os.path.join(cwd,'sharedfolder')
filelistdir = os.path.join(uploadedfilesdir,'.filelist')

def convert_to_bytes(file_path):
    read_data = None
    with open(file_path, 'r') as file:
        read_data = file.read()
    return read_data.encode("utf-8")



def create_file(data):
    data = data.decode('utf-8')
    print("Writing to file")
    with open("new_file.txt", 'w') as file:
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

    if (os.path.isdir(uploadedfilesdir)):
        print("shared folder is already made")
    else:
        os.mkdir(uploadedfilesdir)
        print("have just made the shared folder")
    if(os.path.isdir(filelistdir)):
        print("file list folder is already made")
    else:
        os.mkdir(filelistdir)
        print("have just made the file list folder")
    print("You may now start uploading files or downloading files in your peer to peer network.")

"""
    this method will be responsible for hashing all the files within the
    shared folder and return a list of all the hashes
"""
def update_uploaded_files():
    uploadedfiles = os.listdir(os.path.join(cwd, 'sharedfolder'))
    print('These are the uploaded files in the following shared folder:')
    hashlist = []
    for i in uploadedfiles:
        # this is to hash the file at the specified location
        print(i)
        if(i != '.filelist'):
            path_to_file = os.path.join(uploadedfilesdir, i)
            file_hash = hashlib.md5()
            with open(path_to_file, 'rb') as afile:
                buf = afile.read()
                file_hash.update(buf)
            hex = file_hash.hexdigest()
            print("file hash for", i,":\n",hex)
            hashlist.append(hex) # adds the hash to the list
    # after finishing adding the list of hashes return the list
    print("The final list of hashes is:")
    print(*hashlist, sep = "\n")
    return hashlist



if __name__ == "__main__":
    main()
