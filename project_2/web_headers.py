import argparse
import requests


def get_headers(input_url):
    http_request = requests.request('HEAD', input_url)

    return http_request.headers


def check_hsts(headers):
    return 'Strict-Transport-Security' in headers


def check_csp(headers):
    return 'Content-Security-Policy' in headers


def check_xframe_options(headers):
    return 'X-Frame-Options' in headers


def check_server(headers):
    if 'Server' in headers:
        return headers['Server']
    else:
        return False


def check_headers(urls_list):
    results = []

    for url in urls_list:
        sub_result = {}
        headers = get_headers(url)
        sub_result['url'] = url
        sub_result['has_hsts'] = check_hsts(headers)
        sub_result['has_xframe_options'] = check_xframe_options(headers)
        sub_result['has_csp'] = check_csp(headers)
        sub_result['has_server'] = check_server(headers)
        results.append(sub_result)

    return results


def load_file(urls_file):
    urls = []

    with open(urls_file, 'r') as urls_list:
        lines = urls_list.readlines()
        for line in lines:
            urls.append(line)

    return urls


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