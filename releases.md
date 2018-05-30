## Release v1.0
First stable release of AbuseIP-db-scanner 

> Windows binaries and Python3 version available

## Download

> [Python version](https://github.com/louigigr/AbuseIP-db-scanner/releases/download/v1.0-stable/abuseipdb-generic.zip)

> [Windows binary version](https://github.com/louigigr/AbuseIP-db-scanner/releases/download/v1.0-stable/abuseipdb-win-v1.0.zip)

_You can also visit the [Repository Releases page ](https://github.com/louigigr/AbuseIP-db-scanner/releases)_

**_The windows binary should work fine in Windows 10. In any other case you may need to download [Windows 10 Universal C Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=48234)_**

## What's New!
* Save API Key to a file
* Added -d or --days switch to keep generic script as a complete CLI solution which might be better for automation
* Retrieve Reports by specifying number of days. If no number of days is specified the default value of _30_ is used


### Features

* Registry API key Storage (Windows only)
* Input Key on first run
* Store API Key to file (python version)
* Export to CSV
* Export to Tab Seperated Values
* IP parser that will automatically:
  * Grab all IP addresses in the file no matter the formatting
  * Detect and remove duplicate IP addresses
  * Detect and remove local subnet IP addresses _(192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8)_



## Generic Release

The generic release uses the file method to store your API key.
