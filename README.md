![Square logo]

# Square Connect Python SDK - RETIRED

---

[![Build Status](https://travis-ci.org/square/connect-python-sdk.svg?branch=master)](https://travis-ci.org/square/connect-python-sdk)
[![PyPI version](https://badge.fury.io/py/squareconnect.svg)](https://badge.fury.io/py/squareconnect)
[![Apache-2 license](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)
==================

## NOTICE: Square Connect Python SDK retired

The Square Connect Python SDK is retired (EOL) as of 2019-08-15 and will no
longer receive bug fixes or product updates. To continue receiving API and SDK
improvements, please follow the instructions below to migrate to the new
[Square Python SDK].

The old Connect SDK documentation is available under the
[`/docs` folder](./docs/README.md).

<br/>

---

* [Migrate to the Square Python SDK](#migrate-to-the-square-python-sdk)
* [Example code migration](#example-code-migration)
* [Ask the community](#ask-the-community)

---

<br/>

## Migrate to the Square Python SDK

Follow the instructions below to migrate your apps from the deprecated
`squareconnect` library to the new `square` library.


### Install the new library

Install the latest [Square Python SDK] using pip:

```python
pip install squareup
```


### Update your code

1. Change all instances of `import 'squareconnect'` to `import 'square'`.
1. Replace models with plain Python dictionary equivalents.
1. Update client instantiation to follow the method outlined below.
1. Update code for accessing response data to follow the method outlined below.
1. Check `response.is_success` or `response.is_error` rather than rescuing
   exceptions for flow control.

To simplify your code, we also recommend that you use method chaining to access
APIs instead of explicitly instantiating multiple clients.


#### Client instantiation

```python
from square.client import Client

square = Client(access_token='YOUR ACCESS TOKEN')

response = square.API.ENDPOINT(body=BODY)
```

#### Accessing response data

```python
if response.is_success():
  print({response.body})
elif response.is_error():
  print({response.errors})
```

### An example code migration

As a specific example, consider the following code for creating a new customer
from this dictionary:

```python
new_customer = {
  'given_name': 'Ava',
  'address': {
    'address_line_1': '555 Electric Ave',
    'locality': 'Los Angeles',
    'country': 'US'
  }
}
```

With the deprecated `squareconnect` library, this is how you instantiate a
client for the Customers API, format the request, and call the endpoint:

```python
from squareconnect import ApiClient
from squareconnect.rest import ApiException
from squareconnect.apis.customers_api import CustomersApi
from squareconnect.models.create_customer_request import CreateCustomerRequest

# Instantiate and initialize the client
api_client = ApiClient()
api_client.configuration.access_token = 'YOUR ACCESS TOKEN'

# Get an instance of the Square API you want call
api_instance = CustomersApi(api_client)

# Build the request
create_customer_request = CreateCustomerRequest(
  given_name=new_customer['given_name'],
  address=new_customer['address'],
)

# Call create_customer method to create a new customer and handle the response
try:
  api_response = api_instance.create_customer(create_customer_request)
  print(f"Success: {api_response.customer}")
except ApiException as err:
  print(f"Exception when calling CustomersApi->create_customer: {err}")
```

Now consider equivalent code using the new `square` library:

```python
from square.client import Client

# Instantiate the client
client = Client(access_token='YOUR ACCESS TOKEN')

# Call create_customer method to create a new customer
result = client.customers.create_customer(new_customer)

# Handle the result
if result.is_success():
  # Display the response as text
  print(f"Success: {result.text}")
# Call the error method to see if the call failed
elif result.is_error():
  print(f"Errors: {result.errors}")
```

That's it! What was once a multi-block process can be handled in 2 lines of code
and an `if/elif` block. Migrating to the `square` library reduces boilerplate
and lets you can focus on the parts of your code that really matter.


<br/>

---

<br/>

## Ask the community

Please join us in our [Square developer community] if you have any questions!


[//]: # "Link anchor definitions"
[Square Logo]: https://docs.connect.squareup.com/images/github/github-square-logo.svg
[Square Python SDK]: https://github.com/square/square-python-sdk
[Square developer community]: https://squ.re/slack
[Square Python SDK](https://github.com/square/square-python-sdk)
