
import ftplib

HOSTNAME = " ftp.dlptest.com/"  
USERNAME = "dlpuser" 
PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"  

# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

# Enter File Name with Extension
filename = "share.txt" 

# Read file in binary mode
with open(filename, "a") as file:
    ftp_server.storbinary(f"STORE {filename}", file)

# Get list of files
ftp_server.dir()

# Close the Connection
ftp_server.quit()