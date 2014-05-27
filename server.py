#SERVER
import os
import socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

class Server:
    
    def __init__(self,startMessage):
        self.startMessage = startMessage;
        print self.startMessage;
    
    def createServer(self,ipaddr):
        authorizer = DummyAuthorizer();
        
        ''' create a user
            All login information is stored as plaintext right now.
        '''
        authorizer.add_user("user","password", "/users/ryanwilcox/server/user", perm="elradfmwM",
        msg_login = "You are logged in.", msg_quit = "bye.");
        
        authorizer.add_user("user2","passwd","/users/ryanwilcox/server/user2",perm="elradfmwM"
        msg_login = "You are logged in", msg_quit = "bye!.");
        #anon user
        authorizer.add_anonymous("/users/ryanwilcox/server");
    
        handler = FTPHandler;
        handler.authorizer = authorizer;
        handler.banner = "FileTransferProtocol";
    
        server = FTPServer((ipaddr,6066), handler);
    
        #limits on connections to ftp server
        server.max_cons = 256;
        server.max_cons_per_ip = 5;
        server.serve_forever();
        #END OF FUNCTION
 

serv = Server("Start the Server");
servername = socket.gethostname();
serv.createServer(servername);    

        






