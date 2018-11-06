# lockss_configuration.AusApi

All URIs are relative to *https://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_au_config**](AusApi.md#delete_au_config) | **DELETE** /aus/{auid} | Delete the configuration of an AU
[**get_all_au_config**](AusApi.md#get_all_au_config) | **GET** /aus | Get the configurations of all AUs
[**get_au_config**](AusApi.md#get_au_config) | **GET** /aus/{auid} | Get the configuration of an AU
[**put_au_config**](AusApi.md#put_au_config) | **PUT** /aus/{auid} | Store the configuration of an AU


# **delete_au_config**
> ConfigExchange delete_au_config(auid)

Delete the configuration of an AU

Delete the configuration of an AU given the AU identifier

### Example
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
    # Delete the configuration of an AU
    api_response = api_instance.delete_au_config(auid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AusApi->delete_au_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auid** | **str**| The identifier of the AU for which the configuration is\\ \\ to be deleted | 

### Return type

[**ConfigExchange**](ConfigExchange.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_au_config**
> ConfigExchange get_all_au_config()

Get the configurations of all AUs

Get the configuration of all AUs

### Example
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

try:
    # Get the configurations of all AUs
    api_response = api_instance.get_all_au_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AusApi->get_all_au_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigExchange**](ConfigExchange.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_au_config**
> ConfigExchange get_au_config(auid)

Get the configuration of an AU

Get the configuration of an AU given the AU identifier

### Example
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
auid = 'auid_example' # str | The identifier of the AU for which the configuration is\\ \\ requested

try:
    # Get the configuration of an AU
    api_response = api_instance.get_au_config(auid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AusApi->get_au_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auid** | **str**| The identifier of the AU for which the configuration is\\ \\ requested | 

### Return type

[**ConfigExchange**](ConfigExchange.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_au_config**
> ConfigExchange put_au_config(auid, config_exchange)

Store the configuration of an AU

Store the configuration of an AU given the AU identifier

### Example
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
auid = 'auid_example' # str | The identifier of the AU for which the configuration is\\ \\ to be stored
config_exchange = lockss_configuration.ConfigExchange() # ConfigExchange | The configuration items to be stored

try:
    # Store the configuration of an AU
    api_response = api_instance.put_au_config(auid, config_exchange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AusApi->put_au_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auid** | **str**| The identifier of the AU for which the configuration is\\ \\ to be stored | 
 **config_exchange** | [**ConfigExchange**](ConfigExchange.md)| The configuration items to be stored | 

### Return type

[**ConfigExchange**](ConfigExchange.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

