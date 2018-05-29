>_Forked from https://github.com/mikebanks/AbuseIPdbSCAN_

# AbuseIP DB Scanner

This is a **python3** script that will parse any text file containg IP addresses and return relevant threat information using the AbuseIPDB API.

# New Releases

Visit the [Releases](https://github.com/louigigr/AbuseIP-db-scanner/releases) page to download the [python version](https://github.com/louigigr/AbuseIP-db-scanner/releases/download/v1.0-beta.4/abuseipdb-all.zip) or the [windows binary version](https://github.com/louigigr/AbuseIP-db-scanner/releases/download/v1.0-beta.4/abuseipdb-win.zip) of the script.

## What's New!

- Save API Key to a file
- Added -d or --days switch to keep generic script as a complete CLI solution which might be better for automation
- Retrieve Reports by specifying number of days. If no number of days is specified the default value of _30_ is used

## Requirements (Setup) and Usage

### Setup

- Python3 (_2.7 may have errors_)
- Requests
```
pip3 install Requests
```
- Requests[security]
```
pip3 install requests[security]
```

### Usage:

In order to use the script you will need an API key. The API key is stored in a file _my.api_ in the same directory as the script. In order for the script to work make sure you edit the file _my.api_ and enter your API Key. API key information can be found here: (https://www.abuseipdb.com/api.html)

To use type:

```
python3 abuseipdb.py -f file_to_parse.txt
```

 The options are as follows:

```
-t      outputs items in tab seperated values (Default)

-c      outputs items in comma seperated values
```
_Specify the number of days you wish to search and display alerts for. Accepted range is **1 to 365**._


## Setup and use with PIPENV

### Setup PIPENV and AbuseIP-db-scanner

* Requirements
  * Python3
  * Pipenv _(install with pip install pipenv)_
  * Requests

```
cd ~
git clone https://github.com/louigigr/AbuseIP-db-scanner.git
cd AbuseIP-db-scanner
pipenv install --python 3.6
pipenv shell
pipenv install requests
```

### Usage

To use type:

```
python abuseipdb.py
```

_Specify the number of days you wish to search and display alerts for. Accepted range is **1 to 365**._


