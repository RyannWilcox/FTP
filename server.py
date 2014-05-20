#SERVER
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def createServer(ipaddr,username,password):
    authorizer = DummyAuthorizer();
    # create a user
    authorizer.add_user(username, password, "?", perm="elradfmwM",
    msg_login = "You are logged in.", msg_quit = "bye.");
    
    #anon user
    authorizer.add_anonymous("?");
    
    handler = FTPHandler;
    handler.authorizer = authorizer;
    handler.banner = "FileTransferProtocol";
    
    server = FTPServer((ipaddr,6066), handler);
    
    #limits on connections to ftp server
    server.max_cons = 256;
    server.max_cons_per_ip = 5;
    server.serve_forever();
#END OF FUNCTION


createServer("xxx.xxx.x.xxx","user","password");    
        






