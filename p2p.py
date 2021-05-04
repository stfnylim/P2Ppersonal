
from server_client.constants import *
from server_client.client import Client
from server_client.server import Server
import hashlib
import fileIO
import pickle
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
    # msg = fileIO.convert_to_bytes("read_file.txt")
    # TODO: Then we must compare the hash tables between different nodes in the system
    # with a for loop and update the files associated with the missing hashes in the hash tables

    # This will create shared folder so that it can start hashing the uploaded files
    fileIO.create_folder()
    hashlist = fileIO.update_uploaded_files()


    msg = pickle.dumps(hashlist)

    recd = pickle.loads(msg)
    print(recd)

    """
    for item in hashlist:
        print(item)
    dbfile.close()
    """
    #msg = bytes(f'{len(msg):<{10}}', "utf-8") + msg
    print(msg)
    #msg = msg.decode('utf-8')
    d = pickle.load(msg)
    print(d)
    # print(msg.decode("utf-8"))
    while True:
        try:
            print("-" * 21 + "Trying to connect" + "-" * 21)
            # sleep a random time between 1 -5 seconds
            time.sleep(randint(RAND_TIME_START,RAND_TIME_END))
            for peer in p2p.peers:
                try:
                    client = Client(peer,hashlist)
                    
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
