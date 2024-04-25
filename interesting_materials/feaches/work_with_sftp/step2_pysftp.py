# No worked 
import pysftp
import paramiko

host = 'localhost'
username = 'gansiorag'
# username = 'root'
password = 'GANsiBR5668899!'
# password = ''


class My_Connection(pysftp.Connection):
    def __init__(self, *args, **kwargs):
        try:
            if kwargs.get('cnopts') is None:
                kwargs['cnopts'] = pysftp.CnOpts()
                kwargs['cnopts'].hostkeys = None
        except pysftp.HostKeysException as e:
            self._init_error = True
            raise paramiko.ssh_exception.SSHException(str(e))
        else:
            self._init_error = False

        self._sftp_live = False
        self._transport = None
        super().__init__(*args, **kwargs)

    def __del__(self):
        if not self._init_error:
            self.close()


# srv = My_Connection(host=host, username=username, private_key=password)
# srv.chdir('/home/test')  # change directory on remote server
# srv.put('sftp_one.txt')  # To download a file, replace put with get
# lc = srv.listdir()
# print(lc)
# # dd = srv.put('/home/gansiorag/sftp_one.txt')
# dd = srv.getcwd()
# print(dd)
# srv.close()

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(host=host,
                       username=username,
                       password=password,
                       cnopts=cnopts) as sftp:
    print("Connection succesfully stablished")
    sftp.cwd('/home/gansiorag/')  # Switch to a remote directory
    f = sftp.open('new_filename.txt', 'w')
    f.write('proba sdgsgds sdfhsdfh sdhdhf string')
    # directory_structure = sftp.listdir_attr()
    # for attr in directory_structure:
    #     print(attr.filename, attr)
