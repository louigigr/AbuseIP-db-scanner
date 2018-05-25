>_Forked from https://github.com/mikebanks/AbuseIPdbSCAN_

# AbuseIP DB Scanner

This is a python script that will parse IP addresses from files and interact with AbuseIPDB API. It will return the information about the IP into standard out in tab separated values in standard out.

# New Releases

Visit the [Releases](https://github.com/louigigr/AbuseIP-db-scanner/releases) page to download the [python version](https://github.com/louigigr/AbuseIP-db-scanner/releases/download/v1.0-beta.4/abuseipdb-all.zip) or the [windows binary version](https://github.com/louigigr/AbuseIP-db-scanner/releases/download/v1.0-beta.4/abuseipdb-win.zip) of the script.

## Requirements (Setup)


- Python3 (2.7 may have errors)
- Requests
```
pip3 install Requests
```
- Requests[security]
```
pip3 install requests[security]
```
- AbuseIP DB API Key
In order to use the script you will need an API key and place it in the scrip under the "api_key" variable. API key information can be found here: (https://www.abuseipdb.com/api.html)

## Usage

```
python3 AbuseIPDB.py -f file_to_parse.txt
```

 The options are as follows:

```
-t      outputs items in tab seperated values (Default)

-c      outputs items in comma seperated values
```

## Troubleshooting

- If you are receiving errors, please look at the Issues queue and see if there is already an issue open.

- If you have a unique issue, please create a new Issue, and include the output of your terminal from the bootstrap script down until the error.

