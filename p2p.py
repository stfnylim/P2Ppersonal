
from server_client.constants import *
from server_client.client import Client
from server_client.server import Server
import fileIO
import hashlib

"""
    This class will take care of converting client to server
"""
class p2p:
    # make ourself the default peer
    peers = [HOST]

def main():
    # if the server breks we try to make a client a new server

    # TODO After hashing, we store the hash with a key of IP addresses locally into the client or server
    # TODO Also, to parse through the list of hashes that are stored in the hash table

    # test directories
    cwd = os.getcwd()
    path_to_file = os.path.join(cwd, "read_file.txt") # temporary for file path of new
    new_file_path = os.path.join(cwd, "new_file.txt") # temporary for new storage

    msg = fileIO.convert_to_bytes(path_to_file)

    # this is to hash the file at the specified location
    file_hash = hashlib.sha256()
    with open(path_to_file, 'rb') as f:
        fb = f.read(BYTE_SIZE)
        while len(fb) >0:
            fb = f.read(BYTE_SIZE)
    print("file hash hex: ",file_hash.hexdigest())
    hex = file_hash.hexdigest()

    # this is to store it in the hash table
    
    hash = {'hex':HOST}
    
    # TODO: Then we must compare the hash tables between different nodes in the system
    # with a for loop and update the files associated with the missing hashes in the hash tables




    while True:
        try:
            print("-" * 21 + "Trying to connect" + "-" * 21)
            # sleep a random time between 1 -5 seconds
            time.sleep(randint(RAND_TIME_START,RAND_TIME_END))
            for peer in p2p.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass

                # become the server
                try:
                    server = Server(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)

if __name__ == "__main__":
    main()
