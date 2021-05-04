"""
    This file takes care of the client side of the peer to peer network
    This file takes care of the file being downloaded on to the machine
"""

from server_client.constants import *
import pickle


class Client: 

    def __init__(self, addr, hashlist):
        try:
            # set up the socket
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # this allows python to use the recently closed socket
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # set up socket connection
            self.s.connect((addr, PORT))
            # establish DHT variables
            self.hashlist = hashlist
            self.hashes = {} # these will be the file hashes paired with IP addresses
            
            # update and output all the hashes for the files in the shared folder
            j_thread = threading.Thread(target=self.update_hashes())
            j_thread.daemon = True
            j_thread.start()

            # create to work on a different thread
            i_thread = threading.Thread(target=self.send_message)
            i_thread.daemon = True
            i_thread.start()


            # send the message requesting data so that it is constantly listening
            while True:

                r_thread = threading.Thread(target=self.recieve_message)
                r_thread.start()
                r_thread.join()

                data = self.recieve_message()

                if not data:
                    # means the server has failed
                    print("-" * 21 + " Server failed " + "-" * 21)
                    break

                elif data[0:1] == b'\x11':
                    print("Got peers")
                    # first byte is the byte '\x11 we added to make sure that we have peers
                    self.update_peers(data[1:])
        except Exception as e:
            sys.exit()

    """
        This thread will deal with printing the recieved message
    """
    def recieve_message(self):
        try:
            while True:
                print("Recieving -------")
                data = self.s.recv(BYTE_SIZE)
                if not data:
                    break
                print("\nRecieved message on the client side is:")
                d = pickle.loads(data)
                print(d)
                excluded_files = self.compare_hashes(d)


            #for file in hashes:
             #   file_exists = False
                
            """
            if self.previous_data != data:
                fileIO.create_file(data)
                self.previous_data = data
            # TODO download the file to the computer
            """
            return data
        except KeyboardInterrupt:
           self.send_disconnect_signal()

    def compare_hashes(self,data):
        print(data)
        exc_list = []
        for i in data:
            print(i)
            if self.hashes.has_key(i):
                print(HOST,"has",i)
            else:
                exc_list.append(i)
                print(HOST,"does not have",i)
        return exc_list

    """
        This method will append the list of file hashes to the hash table
        and output the final hash table of values
    """
    def update_hashes(self):
        for i in self.hashlist:
           self.hashes[i].append(HOST)
           print("Have appended",i,"to",HOST)
        

        print("The hash table of files is the following:")
        hash_items = self.hashes.items()
        for item in hash_items:
            print(item)



    """
        This method updates the list of peers
    """
    def update_peers(self, peers):
        # our peers list would lool like 127.0.0.1, 192.168.1.1, 
        # we do -1 to remove the last value which would be None
        p2p.peers = str(peers, "utf-8").split(',')[:-1]
    

    """
        This method is used to send the message
        :param: msg -> The optional message to send 
    """
    def send_message(self):
        try:
            #while True:
                # encode the message into bytes
                # other code will run when this happens as the thread is busy
                # request to download the file
            self.s.send(REQUEST_STRING.encode('utf-8'))

        except KeyboardInterrupt as e:
            # If a user turns the server off due to KeyboardInterrupt
            self.send_disconnect_signal()
            return

    def send_disconnect_signal(self):
       print("Disconnected from server")
       # signal the server that the connection has closed
       self.s.send("q".encode('utf-8'))
       sys.exit()
