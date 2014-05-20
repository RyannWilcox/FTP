#CLIENT
import os
from ftplib import FTP


def connectToFtp():
    #Get all information from the user.
    #Will use this when everything works.
    ''''
    servername = raw_input("input the servers name: ");
    username = raw_input("input username: ");
    password = raw_input("input password: ");
    '''
    
    # For testing purposes.
    servername = "?";
    username = "user";
    password = "password";
    
    #attempt login to FTP
    ftp = FTP();
    ftp.connect(servername,6066);
    
    if(ftp.login(username,password)):
        print "You are logged in."
        files = ftp.dir();
        print files;
    else:
        print "Could not log in.";
     #endif
     
     # Desicions on what to do while connected
    input = 0; 
    deciding = True;
    while(deciding):
        print "What would you like to do?";
        print "Press 1 to retrieve a file.";
        print "Press 2 to store a file.";
        print "Press 3 to Quit";
        input = raw_input(); 
        if(input == "3"): # Quit FTP server
            deciding = False;
            ftp.quit();
            print "Goodbye!";
        if(input == "2"): # add a fo;e
            print "You picked 2";   
        if(input == "1"): # download a file
            pickAFile(ftp);
    #endloop
#End function

# File will be downloaded into local directory
def pickAFile(theFtp):
    file =raw_input("\nInput file name: ");
    try:
        print "Attempting to locate "+ file + "....";
        theFtp.retrbinary("RETR " + file, open(file,"wb").write);
        print file + " has been downloaded to current directory";
    except:
        os.remove(file);
        print "File cannot be found / cannot be read \n ";
        print "\n";
#End function

connectToFtp(); # try and log in.
    
