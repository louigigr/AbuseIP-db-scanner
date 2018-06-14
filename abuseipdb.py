import codecs
import argparse
import re
import sys
import requests
import ipaddress
import socket
import time
import os

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="""
    AbuseIPDB query system by Quadrant Global Limited.\n\nPart of the Quadrant Global Security Toolset.\n\n
    This program uses the AbuseIPDB.com API in order to perform queries and detect malicious IP addresses.\n
    The input can be any text file in any form, the IP addresses are parsed and recognised automatically.
    """
)
required = parser.add_argument_group('required arguments')
required.add_argument(
    "-f",
    "--file",
    help="parses IP Addresses from a single given file",
    action="store",
    required=True)
required.add_argument(
    "-d",
    "--days",
    help="Number of days to look back in history for alerts",
    action="store",
    required=False)

parser.add_argument("-t", "--tsv", help="outputs items in tab separated values (Default)", action="store_true")
parser.add_argument("-c", "--csv", help="outputs items in comma separated values", action="store_true")

args = parser.parse_args()


def createfile(filename, key):
    filetocreate = open(filename, "w+")
    filetocreate.write(key)
    filetocreate.close()


def get_file(infile):
    with codecs.open(infile, "r", encoding='utf-8', errors='ignore') as filetoget:
        return filetoget.read()


def get_cat(x):
    return {
        3: 'Fraud_Orders',
        4: 'DDoS_Attack',
        5: 'FTP_Brute-Force',
        6: 'Ping of Death',
        7: 'Phishing',
        8: 'Fraud VoIP',
        9: 'Open_Proxy',
        10: 'Web_Spam',
        11: 'Email_Spam',
        12: 'Blog_Spam',
        13: 'VPN IP',
        14: 'Port_Scan',
        15: 'Hacking',
        16: 'SQL Injection',
        17: 'Spoofing',
        18: 'Brute_Force',
        19: 'Bad_Web_Bot',
        20: 'Exploited_Host',
        21: 'Web_App_Attack',
        22: 'SSH',
        23: 'IoT_Targeted',
    }.get(
        x,
        'UNK CAT, ***REPORT TO MAINTAINER***OPEN AN ISSUE ON GITHUB w/ IP***')


def get_report(i_p):
    # noofdays=input("Please enter number of days to look back in history for alerts: ")
    global data, log
    if not args.days:
        print("Setting days to default: 30")
        noofdays = 30
    else:
        noofdays = args.days
    try:
        pass
    except ValueError:
        print("\nYou must specify an integer between 1 and 365.\n")
        sys.exit()
    if int(noofdays) <= int(0) or int(noofdays) > int(365):
        print("\nYou must specify an integer between 1 and 365.\n")
        sys.exit()
    request = 'https://www.abuseipdb.com/check/%s/json?key=%s&days=%s' % (i_p, api_key, noofdays)
    # DEBUG
    # print(request)
    r = requests.get(request)
    # DEBUG
    # print(r.json())
    try:
        data = r.json()
        if not data:
            print("%s:  No Abuse Reports" % i_p)
        else:
            for record in data:
                log = []
                ip_address = ("Alert for %s:" % i_p)
                # ip_address = record['ip']
                country = record['country']
                # iso_code = record['isoCode']
                category = record['category']
                created = record['created']
                log.append(ip_address)
                log.append(country)
                # log.append(iso_code)
                log.append(created)
                for cat in category:
                    temp_cat = get_cat(cat)
                    log.append(temp_cat)
                    if args.csv:
                        print(','.join(log))
                    else:
                        print('\t'.join(log))
                    log.remove(temp_cat)
    except (ValueError, KeyError, TypeError):
        # log = []
        ip_address = ("Alert for %s:" % i_p)
        # ip_address = record['ip']
        country = data['country']
        # iso_code = record['isoCode']
        category = data['category']
        created = data['created']
        log.append(ip_address)
        log.append(country)
        # log.append(iso_code)
        log.append(created)
        for cat in category:
            temp_cat = get_cat(cat)
            log.append(temp_cat)
            if args.csv:
                print(','.join(log))
            else:
                print('\t'.join(log))
            log.remove(temp_cat)


def deduplicate(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


def main():
    if args.file:
        fileexists = get_file(args.file)
        found = deduplicate(re.findall(
            r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', fileexists))

        list(set(found))

        print("Abuse IP Database REPORT:")
        count = 0
        for ip in found:
            try:
                socket.inet_aton(ip)
            except socket.error:
                continue

            if ipaddress.ip_address(ip).is_private is False:
                if count == 59:
                    time.sleep(60)
                    count = 0
                get_report(ip)
                count += 1


if __name__ == '__main__':
    scriptdir = os.path.dirname(os.path.realpath(__file__)) + "\\"
    scriptfile = scriptdir + "my.api"
    if os.path.exists(scriptfile):

        if os.stat(scriptfile).st_size == 0:
            my_api = input("The file my.api does not contain and key or data. Please enter your API key now: ")
            createfile(scriptfile, str(my_api))
            sys.exit()
        with open(scriptfile) as f:
            first_line = f.readline()
        api_key = first_line
    else:
        print("No API file exists, creating...")
        try:
            # open(scriptdir + "my.api", 'x')
            my_api = input("The file my.api does not contain and key or data. Please enter your API key now: ")
            createfile(scriptfile, str(my_api))
        except FileExistsError:
            pass

        sys.exit()
    main()
