# No worked 
import pysftp
import paramiko

host = 'localhost'
# username = 'gansiorag'
username = 'root'
password = 'gansiorag'
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


srv = My_Connection(host=host, username=username, private_key='sftp_one.txt')
# srv.chdir('/home/test')  # change directory on remote server
# srv.put('sftp_one.txt')  # To download a file, replace put with get
lc = srv.listdir()
print(lc)
dd = srv.get('sftp_one.txt')
print(dd)
srv.close()
