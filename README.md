# lockss-configuration-python
API of the LOCKSS Configuration REST Service

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.lockss.org/](https://www.lockss.org/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import lockss_configuration 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import lockss_configuration
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import lockss_configuration
from lockss_configuration.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = lockss_configuration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lockss_configuration.AusApi(lockss_configuration.ApiClient(configuration))
auid = 'auid_example' # str | The identifier of the AU for which the configuration is\\ \\ to be deleted

try:
    # Delete the the configuration of an AU
    api_response = api_instance.delete_au_config(auid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AusApi->delete_au_config: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://laaws.lockss.org:443*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AusApi* | [**delete_au_config**](docs/AusApi.md#delete_au_config) | **DELETE** /aus/{auid} | Delete the the configuration of an AU
*AusApi* | [**get_all_au_config**](docs/AusApi.md#get_all_au_config) | **GET** /aus | Get the configurations of all AUs
*AusApi* | [**get_au_config**](docs/AusApi.md#get_au_config) | **GET** /aus/{auid} | Get the configuration of an AU
*AusApi* | [**put_au_config**](docs/AusApi.md#put_au_config) | **PUT** /aus/{auid} | Store the configuration of an AU
*ConfigApi* | [**get_last_update_time**](docs/ConfigApi.md#get_last_update_time) | **GET** /config/lastupdatetime | Get the timestamp when the configuration was last updated
*ConfigApi* | [**get_loaded_url_list**](docs/ConfigApi.md#get_loaded_url_list) | **GET** /config/loadedurls | Get the URLs from which the configuration was loaded
*ConfigApi* | [**get_section_config**](docs/ConfigApi.md#get_section_config) | **GET** /config/file/{sectionName} | Get the named configuration file
*ConfigApi* | [**get_url_config**](docs/ConfigApi.md#get_url_config) | **GET** /config/url | Get the configuration file for a URL
*ConfigApi* | [**put_config**](docs/ConfigApi.md#put_config) | **PUT** /config/file/{sectionName} | Store the named configuration file
*ConfigApi* | [**put_config_reload**](docs/ConfigApi.md#put_config_reload) | **PUT** /config/reload | Request a configuration reload
*StatusApi* | [**get_status**](docs/StatusApi.md#get_status) | **GET** /status | Get the status of the service


## Documentation For Models

 - [ApiStatus](docs/ApiStatus.md)
 - [ConfigExchange](docs/ConfigExchange.md)
 - [ConfigModSpec](docs/ConfigModSpec.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author

lockss-support@lockss.org

