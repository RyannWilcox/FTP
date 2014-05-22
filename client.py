#CLIENT
import os
import socket
from ftplib import FTP

class Client:
    def __init__(self,message):
        ''''
        self.username = raw_input("input username: ");
        self.password = raw_input("input password: ");
        '''
        self.message = message;
        print message;
        self.servername = raw_input("input the servers name: ");
        self.username = "user";
        self.password = "password";
           
    def connectToFtp(self):
        #attempt login to FTP
        ftp = FTP();
        ftp.connect(self.servername,6066);
    
        if(ftp.login(self.username,self.password)):
            print "You are logged in."
        else:
            print "Could not log in.";
        #endif
         # Desicions on what to do while connected
        deciding = True;
        input = 0;
        while(deciding):
            print ftp.pwd();
            print ftp.dir();
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
                self.addAFile(ftp);
            if(input == "1"): # download a file
                self.pickAFile(ftp);
            if(input == "3"): # change server directories
                self.changeDirectories(ftp);
        #endloop
#End function

    # File will be downloaded into local directory
    def pickAFile(self,theFtp):
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

#File is uploaded from current directory to ftp server directory
    def addAFile(self,theFtp):
        fileName = raw_input("\nInput name of file to be uploaded: ");
        try:
            file = open(fileName,"rb");
            theFtp.storbinary("STOR %s" % fileName,file);
            print "Added " + fileName + " to server directory\n\n";
            file.close();    
        except:
            print "File cannot be found or it cannot be read \n";
            print "\n";
#End function

#Change directories in the 
    def changeDirectories(self,theFtp):
        # Get the current directory for output
        curDirectory = theFtp.pwd();
        print "current directory: " + curDirectory;
        dirCh = raw_input("Input directory to change to:");
        try:
            #Change to inputted directory
            theFtp.cwd(dirCh);
        except:
            print "Could not change to that directory..";
#End function
 
theClient = Client("Start the client..");   
theClient.connectToFtp(); # try and log in.
    
