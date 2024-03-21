from fsspec.implementations.sftp import SFTPFileSystem

host = 'localhost'
username = ''
password = ''

fs = SFTPFileSystem(host=host, username=username, password=password)

# list a directory
fs.ls("/")

# # open a file
# with fs.open('sftp_one.txt', 'w') as file:
#     content = file.write('sgsg sgsdg sgsdg sgsggs')

# open a file
with fs.open('sftp_one.txt', 'r') as file:
    content = file.read()
print(content)
