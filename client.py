#CLIENT

from ftplib import FTP

'''this does not work yet....'''

def connectToFtp():
    #Get all information from the user.
    servername = raw_input("input the servers name: ");
    username = raw_input("input username..");
    password = raw_input("input password..");
    
    #attempt login to FTP
    ftp = FTP(servername);
    ftp.login(username,password);


connectToFtp(); # try and log in.
    
