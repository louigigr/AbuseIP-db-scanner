>_Forked from https://github.com/mikebanks/AbuseIPdbSCAN_

# AbuseIP DB Scanner

This is a **python3** script that will parse any text file containg IP addresses and return relevant threat information using the AbuseIPDB API.

# New Releases

Visit the **[Latest Releases](https://github.com/louigigr/AbuseIP-db-scanner/releases/latest)** page to download the [python version](https://github.com/louigigr/AbuseIP-db-scanner/releases/download/v1.0-stable/abuseipdb-generic.zip) or the [windows binary version](https://github.com/louigigr/AbuseIP-db-scanner/releases/download/v1.0-stable/abuseipdb-win-v1.0.zip) of the script.

## Download and use binary

- Download the [windows binary](https://github.com/louigigr/AbuseIP-db-scanner/releases/download/v1.0-stable/abuseipdb-win-v1.0.zip) from the [releases](https://github.com/louigigr/AbuseIP-db-scanner/releases) page

>![alt text](https://cdn.els-cdn.com/sd/img/sprite_parts/warning_a.gif "Important!") **Important! The binary should work fine on Windows 10, in any other case you need to download  [Windows 10 Universal C Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=48234)**![alt text](https://cdn.els-cdn.com/sd/img/sprite_parts/warning_a.gif "Important!")

- Unzip the downloaded file to a folder of your choice _(e.g C:\users\user\programs\)_
- Open windows terminal _(windows key + R and type CMD)_
- Change to the desired directory _(cd \users\user\programs\)_

> ![alt text](http://www.happystove.com/images/starYellow.png "Optional") Optional: _You can add the directory to your PATH environment variable or copy the script inside C:\Windows\System32\ directory in order for it to be available to you at any time while on the terminal._![alt text](http://www.happystove.com/images/starYellow.png "Optional")
- Run the script with ``` abuseipdb  ```
- You will be prompted to enter your api key ``` Please enter your abuseipdb.com API key here: ``` _1234567_
- The key is stored in registry and you can change it at any time using the **-a** switch
- To properly use the program you need to have a text file _(e.g alerts.log)_ that contains IP addresses in any form. The file is parsed and all non-local IP addresses are extracted and deduplicated. In order to execute the script just type: 
``` abuseipdb -f {FileWithIPs} ```
e.g. ``` abuseipdb -f alert.log ```

> Optional: To save to a file you can apend > {filename} after the command e.g ``` abuseipdb -f alert.log > ThreatReport.txt ```

- Specify the number of days you wish to search and display alerts for by using the -d or --days switch.
e.g. ``` abuseipdb -f myip.txt -d 60 ```

  - Accepted range is 1 to 365
  - If no switch is specified the script uses a default value of _30_
  - Contains a really simple failsafe so the script won't break, really helps with the binary version
- To get help type abuseipdb -h

## Setup and Usage with python

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

-d      specifies number of days
```


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

## Troubleshooting

- If you are receiving errors, please look at the Issues queue and see if there is already an issue open.

- If you have a unique issue, please create a new Issue, and include the output of your terminal from the bootstrap script down until the error.

