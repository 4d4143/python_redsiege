import argparse
import requests


def get_headers(input_url):
    http_request = requests.request('HEAD', input_url)

    return http_request.headers

def check_hsts(headers):
    return 'Strict-Transport-Security' in headers


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL to fetch headers from")
    parser.add_argument("-iL", "--file", help="File with URLs ranges")
    parser.add_argument("-o", "--output", help="Filename for output (In CSV)")

    args = parser.parse_args()
    variables = vars(args)

    query_results = []

    print(check_hsts(get_headers(variables['url'])))



if __name__ == '__main__':
    main()