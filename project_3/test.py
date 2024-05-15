import paramiko
import paramiko.client
import argparse

command = "whoami"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="IP to connect to")
parser.add_argument("-u", "--user", help="Username")
parser.add_argument("-p", "--pass", help="Password")

args = parser.parse_args()
variables = vars(args)

#Convert each string char to hex to debug what is being sent to server
print(':'.join(hex(ord(x)) for x in variables['pass']))

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(variables['ip'], username=variables['user'], password=variables['pass'])
if client:
    print("connected!")
_stdin, _stdout, _stderr = client.exec_command(command)
_stdin.close()
print(_stdout.read().decode())
client.close()
