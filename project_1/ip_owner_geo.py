import ipaddress
import whois
import argparse
import sys
import csv


def query_ip(ip_input):
    try:
        if "/" in ip_input:
            ip_to_lookup = ipaddress.ip_address(ip_input)
        else:
            ip_to_lookup = ipaddress.ip_network(ip_input)
        query = whois.whois(ip_input)
        return query
    except:
        print(f'{ip_input} is not a valid IP or IP range!')


def load_file(ip_list_file):
    ips_list = []

    with open(ip_list_file, 'r') as ip_list:
        lines = ip_list.readlines()
        for line in lines:
            ip_list.append(line)

    return ips_list


def output_findings(query_array):
    print(query_array)


def save_findings():
    pass


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="Single IP or CIDR range")
    parser.add_argument("-iL", "--file", help="File with IPs or CIDR ranges")
    parser.add_argument("-o", "--output", help="Filename for output (In CSV)")

    args = parser.parse_args()
    variables = vars(args)

    query_results = []

    if variables['ip']:
        query_results.append(query_ip(variables['ip']))

    if variables['file']:
        ips_list = load_file(variables['file'])

        for ip in ips_list:
            query_results.append(ip)

    if (not variables['ip'] or not variables['file'] and variables['output']):
        print("Please provide an IP or a list of IPs!")
        sys.exit(0)

    output_findings(query_results)

    if variables['output']:
        save_findings(query_results)

if __name__ == '__main__':
    main()