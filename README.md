
[![Build Status](https://travis-ci.com/TralahM/pytekcoopbank.svg?branch=master)](https://travis-ci.com/TralahM/pytekcoopbank)
[![Build status](https://ci.appveyor.com/api/projects/status/yvvmq5hyf7hj743a/branch/master?svg=true)](https://ci.appveyor.com/project/TralahM/pytekcoopbank/branch/master)
[![Documentation Status](https://readthedocs.org/projects/pytekcoopbank/badge/?version=latest)](https://pytekcoopbank.readthedocs.io/en/latest/?badge=latest)
[![License: GPLv3](https://img.shields.io/badge/License-GPLV2-green.svg)](https://opensource.org/licenses/GPLV2)
[![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
[![Views](http://hits.dwyl.io/TralahM/pytekcoopbank.svg)](http://dwyl.io/TralahM/pytekcoopbank)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square)](https://github.com/TralahM/pytekcoopbank/pull/)
[![GitHub pull-requests](https://img.shields.io/badge/Issues-pr-red.svg?style=flat-square)](https://github.com/TralahM/pytekcoopbank/pull/)
[![Language](https://img.shields.io/badge/Language-python-3572A5.svg)](https://github.com/TralahM)
<img title="Watching" src="https://img.shields.io/github/watchers/TralahM/pytekcoopbank?label=Watchers&color=blue&style=flat-square">
<img title="Stars" src="https://img.shields.io/github/stars/TralahM/pytekcoopbank?color=red&style=flat-square">
<img title="Forks" src="https://img.shields.io/github/forks/TralahM/pytekcoopbank?color=green&style=flat-square">

# pytekcoopbank

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-black.svg?style=for-the-badge&logo=github)](https://github.com/TralahTek)
[![TralahM](https://img.shields.io/badge/Engineer-TralahM-blue.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)


# Co-operative Bank of Kenya Python SDK
Intuitive Python SDK for the Co-operative Bank of Kenya developer APIs.

## Pre-requisites
### Create an application
Create or login to your account at https://developer.co-opbank.co.ke:9443/store/

On the left panel, you can see a list of menus. Click on Applications to access the list of available applications in which case you can choose to use the default ones or create your own.

### Subscribe to API(s)
* Select the application or create your own application using steps described earlier.
* Click “Subscribe”. A pop up message appears as shown:

### Generate Keys
* Click on “Applications” on the left panel.
* Choose the application for which you want to generate keys
* Choose the appropriate environment from the tabs(production or sandbox ).
* Specify Callback URL and then click “Generate keys”. Leave other fields have default values;

# Installation
#### Via PIP on pypi
```bash
# In terminal do:
$ pip install pytekcoopbank
```

## Building from Source for Developers

```console
$ git clone https://github.com/TralahM/pytekcoopbank.git
$ cd pytekcoopbank
$ python setup.py install
```

# Documentation

[![Documentation](https://img.shields.io/badge/Docs-pytekcoopbank-blue.svg?style=for-the-badge)](https://github.com/TralahM/pytekcoopbank)

## Setup
```python
import tekcoopbank

config=dict(
        env                 = "sandbox",
        consumerKey         = "ss0sD2ANhjvhx_rHU0a6Xf8ROdYa",
        consumerSecret      = "zOfReXCIwn1TfnEYJJJGNP6l3Tka",
        accountNumber       = "54321987654321",
        bankCode            = "011",
        branchCode          = "00011001",
        callbackURL         = "/coop/callback",
        transactionCurrency = "KES",
)

COOP=tekcoopbank.setup_coop(config)

```

## Usage

By default all methods return a `requests.HTTPResponse` object. To get a python
`dict` you can pass a callback to the send functions.

#### Example Callback Function To Pass to Send

```python
callback=lambda x: x.json()
```

### Check Account Balance

```python
balance=COOP.balance.send(messageReference,accountNumber=None,callback=lambda x: x.json())
```

```json

{
    "MessageReference": "wotfhPpsbxWY",
    "MessageDateTime": "2020-10-05 06:20:01",
    "MessageCode": "-8",
    "MessageDescription": "ACCOUNT AUTHORIZATION FAILURE"
}

```

### Check Account Transactions

```python
transactions=COOP.transactions.send(messageReference,accountNumber,NoOfTransactions=2,callback=lambda x: x.json())
```

```json

{
    "MessageReference": "kRaiNxCTtgbV",
    "MessageDateTime": "2020-10-05 06:20:09",
    "MessageCode": "-8",
    "MessageDescription": "ACCOUNT AUTHORIZATION FAILURE"
}

```


### Account MiniStatement

```python
mini_statement=COOP.mini_statement.send(messageReference,accountNumber,callback=lambda x: x.json())
```

```json
{
    "MessageReference": "xdpdBdEdCdYdAdOdudtdDdw",
    "MessageDateTime": "2020-10-05 07:45:54",
    "MessageCode": "-8",
    "MessageDescription": "ACCOUNT AUTHORIZATION FAILURE"
}
```


### Account FullStatement

```python
full_statement=COOP.full_statement.send(messageReference,accountNumber,callback=lambda x: x.json())
```

```json
{
    "MessageReference": "MdKdNdYdzdAdydQdtdpdedH",
    "MessageDateTime": "2020-10-05 07:45:59",
    "MessageCode": "-8",
    "MessageDescription": "ACCOUNT AUTHORIZATION FAILURE"
}
```


### Account Validation

```python
validation=COOP.validation.send(messageReference,accountNumber,callback=lambda x: x.json())
```

```json
{
    "MessageReference": "eDyClhTgirbw",
    "MessageDateTime": "2020-10-05 06:33:04",
    "MessageCode": "-1",
    "MessageDescription": "INVALID ACCOUNT NUMBER"
}
```

### Get Exchange Rates

```python
exchange_rate=COOP.exchange_rate.send(messageReference,
    fromCurrencyCode="KES",
    toCurrencyCode="USD",
    callback=lambda x: x.json())
```

```json
{
    "MessageReference": "HdKdAdidLdtdGdadFdydxdS",
    "MessageDateTime": "2020-10-05 07:33:16",
    "MessageCode": "0",
    "MessageDescription": "Success",
    "FromCurrencyCode": "KES",
    "ToCurrencyCode": "USD",
    "RateType": "SPOT",
    "Rate": "104.35",
    "Tolerance": "23",
    "MultiplyDivide": "D"
}
```

### IFT Account to Account Transfer

```python
ift_to_account=COOP.ift_to_account.send(messageReference,
    accountNumber,
    amount,
    transactionCurrency="KES",
    narration="Payment",
    destinations=[{},],
    callback=lambda x: x.json())
```

```json

{
    "MessageReference": "sdkdddIdUdndpdxdcdedodr",
    "MessageDateTime": "2020-10-05T06:10:29",
    "MessageCode": "-5",
    "MessageDescription": "DEBIT AND CREDITS AMOUNTS NOT BALANCING"
}

```

### PesaLink Account to Account Transfer

```python
pesalink_to_account=COOP.pesalink_to_account.send(messageReference,
    accountNumber,
    amount,
    transactionCurrency="KES",
    narration="Payment",
    destinations=[{},],
    callback=lambda x: x.json())
```

```json
{
    "MessageReference": "rdhdjdvdYdKdidkdQdFdDdg",
    "MessageDateTime": "2020-10-05T07:10:05",
    "MessageCode": "-5",
    "MessageDescription": "DEBIT AND CREDIT(S) AMOUNTS NOT BALANCING"
}
```


### PesaLink Account to Phone Transfer

```python
pesalink_to_phone=COOP.pesalink_to_phone.send(messageReference,
    phoneNumber,
    amount,
    transactionCurrency="KES",
    narration="Payment",
    destinations=[{},],
    callback=lambda x: x.json())
```

```json
{
    "MessageReference": "tdUdXdOdJdVdgdsdNdddhdw",
    "MessageDateTime": "2020-10-05T07:10:09",
    "MessageCode": "-5",
    "MessageDescription": "DEBIT AND CREDIT(S) AMOUNTS NOT BALANCING"
}
```

### Send to Mpesa

```python
to_mpesa=COOP.to_mpesa.send(messageReference,
    mobileNumber,
    amount,
    transactionCurrency="KES",
    narration="Payment",
    destinations=[{},],
    callback=lambda x: x.json())
```

```json
{
    "MessageReference": "gdBdJdPdudOdpdLdndidrdj",
    "MessageDateTime": "2020-10-05T07:10:13",
    "MessageCode": "-5",
    "MessageDescription": "DEBIT AND CREDIT(S) AMOUNTS NOT BALANCING"
}
```


### Transaction Status

```python
transaction_status=COOP.transaction_status.send(messageReference,callback=lambda x: x.json())
```

```json
{
    "MessageReference": "XHJaVzZGOsjB",
    "MessageDateTime": "2020-10-05 06:20:06",
    "MessageCode": -13,
    "MessageDescription": "MESSAGE REFERENCE DOES NOT EXIST",
    "Source": {
        "AccountNumber": null,
        "Amount": null,
        "TransactionCurrency": null,
        "Narration": null,
        "ResponseCode": null,
        "ResponseDescription": null
    },
    "Destinations": null
}

```


## Test Cases

As a developer, the test cases will be available to you for download as you are creating the sandbox app.

The test cases are in place to ensure that you have well understood the API structure for requests and responses for our different APIs. These test cases are in an excel spreadsheet that you should fill in with the results from each of the test scenarios that you want to consume.

As the Test cases will cover all the APIs available, you will only be required to carry out the test cases for the APIs you had initially selected.

## Go - Live

Once you have already tried out the APIs on our platform and have tested these against our test cases provided, you can make a formal request to go to production.

You will need to have the test cases duly filled, then send an email request, together with these filled in test cases, to our support team who will guide you on the next steps to enable you to get to production.

Send the email request and the test cases to digitalbanking@co-opbank.co.ke

# Contributing
[See the Contributing File](CONTRIBUTING.rst)


[See the Pull Request File](PULL_REQUEST_TEMPLATE.md)


# Support

# LICENCE

[Read the license here](LICENSE)


# Self-Promotion

[![](https://img.shields.io/badge/Github-TralahM-green?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![](https://img.shields.io/badge/Twitter-%40tralahtek-red?style=for-the-badge&logo=twitter)](https://twitter.com/TralahM)
[![TralahM](https://img.shields.io/badge/Kaggle-TralahM-purple.svg?style=for-the-badge&logo=kaggle)](https://kaggle.com/TralahM)
[![TralahM](https://img.shields.io/badge/LinkedIn-TralahM-red.svg?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/TralahM)


[![Blog](https://img.shields.io/badge/Blog-tralahm.tralahtek.com-blue.svg?style=for-the-badge&logo=rss)](https://tralahm.tralahtek.com)

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-cyan.svg?style=for-the-badge)](https://org.tralahtek.com)


