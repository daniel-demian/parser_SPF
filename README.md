# SPF Checker Script

This Python script checks the SPF policy in the DNS of a given domain and lists all IP addresses that are allowed to send emails on behalf of that domain. It parses the IP addresses from the SPF record and any included domains recursively.

## Features

- Fetches SPF record for a given domain
- Parses IP addresses from the SPF record
- Recursively handles included domains in the SPF record
- Prevents re-processing of already visited domains

## Prerequisites

- Python 3.x
- `dnspython` library

You can install the `dnspython` library using pip:

```sh
pip install dnspython
