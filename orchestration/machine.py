from fabric.context_managers import settings, hide
from fabric.operations import run
import paramiko

# machine absraction

class Machine(object):
    def __init__(self, node):
        self.node = node
        self.public_ip = node.ip
        self.ssh_port = node.ssh_port
        self.splunk_username = node.splunk_username
        self.splunk_password = node.splunk_password
        self.ssh_username = node.ssh_username
        self.ssh_password = node.ssh_password

    @property
    def ssh_host_string(self):
        return "%s:%s" % (self.self.public_ip, self.ssh_port)

    @property
    def is_ssh_accessible(self, timeout=10):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.public_ip, int(self.ssh_port), self.ssH_username, self.ssh_password, timeout=timeout)
            return True
        except Exception, e:
            return False

    def execute_command(self, cmd):
        with settings(hide('warnings', 'running', 'stdout', 'stderr'), host_string=self.ssh_host_string,
                      user=self.ssh_username,
                      password=self.ssh_password, warn_only=True):
            result = run(cmd, shell=True, pty=True)
            return result, result.return_code
