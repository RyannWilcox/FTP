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
    servername = "xxx.xxx.x.xxx";
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
        print "Press 3 to change directories.";
        print "Press 4 to Quit";
        input = raw_input(); 
        if(input == "4"): # Quit FTP server
            deciding = False;
            ftp.quit();
            print "Goodbye!";
        if(input == "2"): # add a file
            addAFile(ftp);
        if(input == "1"): # download a file
            pickAFile(ftp);
        if(input == "3"):
            changeDirectories(ftp);
    #endloop
#End function

# File will be downloaded into local directory
def pickAFile(theFtp):
    file = raw_input("\nInput file name: ");
    try:
        print "Attempting to locate "+ file + "....";
        theFtp.retrbinary("RETR " + file, open(file,"wb").write);
        print file + " has been downloaded to current directory\n";
    except:
        os.remove(file);
        print "File cannot be found / cannot be read \n ";
        print "\n";
#End function

def addAFile(theFtp):
    #filename = raw_input("\n input file to be added: ");
    filename ="test.txt";
    try:
        file = open(fileName,"rb");
        theFtp.storbinary("STOR %s" % filename,file);
        print "Added" + filename + "to server directory\n\n";
        file.close();
        
    except:
        print "File cannot be found or it cannot be read \n";
        print "\n";
#End function

def changeDirectories(theFtp):
    print "Directory Changed";
#End function
    
connectToFtp(); # try and log in.
    
