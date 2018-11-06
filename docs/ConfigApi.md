# lockss_configuration.ConfigApi

All URIs are relative to *https://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_last_update_time**](ConfigApi.md#get_last_update_time) | **GET** /config/lastupdatetime | Get the timestamp when the configuration was last updated
[**get_loaded_url_list**](ConfigApi.md#get_loaded_url_list) | **GET** /config/loadedurls | Get the URLs from which the configuration was loaded
[**get_section_config**](ConfigApi.md#get_section_config) | **GET** /config/file/{sectionName} | Get the named configuration file
[**get_url_config**](ConfigApi.md#get_url_config) | **GET** /config/url | Get the configuration file for a URL
[**put_config**](ConfigApi.md#put_config) | **PUT** /config/file/{sectionName} | Store the named configuration file
[**put_config_reload**](ConfigApi.md#put_config_reload) | **PUT** /config/reload | Request a configuration reload


# **get_last_update_time**
> datetime get_last_update_time()

Get the timestamp when the configuration was last updated

Get the timestamp when the configuration was last updated

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
api_instance = lockss_configuration.ConfigApi(lockss_configuration.ApiClient(configuration))

try:
    # Get the timestamp when the configuration was last updated
    api_response = api_instance.get_last_update_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_last_update_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**datetime**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loaded_url_list**
> list[str] get_loaded_url_list()

Get the URLs from which the configuration was loaded

Get the URLs from which the configuration was actually\\ \\ loaded, reflecting any failover to local copies

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
api_instance = lockss_configuration.ConfigApi(lockss_configuration.ApiClient(configuration))

try:
    # Get the URLs from which the configuration was loaded
    api_response = api_instance.get_loaded_url_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_loaded_url_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_config**
> file get_section_config(section_name, accept, if_match=if_match, if_modified_since=if_modified_since, if_none_match=if_none_match, if_unmodified_since=if_unmodified_since)

Get the named configuration file

Get the configuration file stored for a given name

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
api_instance = lockss_configuration.ConfigApi(lockss_configuration.ApiClient(configuration))
section_name = 'section_name_example' # str | The name of the section for which the configuration file\\ \\ is requested
accept = 'accept_example' # str | The Accept header
if_match = 'if_match_example' # str | The If-Match header (optional)
if_modified_since = 'if_modified_since_example' # str | The If-Match header (optional)
if_none_match = 'if_none_match_example' # str | The If-Match header (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | The If-Match header (optional)

try:
    # Get the named configuration file
    api_response = api_instance.get_section_config(section_name, accept, if_match=if_match, if_modified_since=if_modified_since, if_none_match=if_none_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_section_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_name** | **str**| The name of the section for which the configuration file\\ \\ is requested | 
 **accept** | **str**| The Accept header | 
 **if_match** | **str**| The If-Match header | [optional] 
 **if_modified_since** | **str**| The If-Match header | [optional] 
 **if_none_match** | **str**| The If-Match header | [optional] 
 **if_unmodified_since** | **str**| The If-Match header | [optional] 

### Return type

[**file**](file.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_url_config**
> file get_url_config(url, accept, if_match=if_match, if_modified_since=if_modified_since, if_none_match=if_none_match, if_unmodified_since=if_unmodified_since)

Get the configuration file for a URL

Get the configuration file stored for a given URL

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
api_instance = lockss_configuration.ConfigApi(lockss_configuration.ApiClient(configuration))
url = 'url_example' # str | The URL for which the configuration is requested
accept = 'accept_example' # str | The Accept header
if_match = 'if_match_example' # str | The If-Match header (optional)
if_modified_since = 'if_modified_since_example' # str | The If-Match header (optional)
if_none_match = 'if_none_match_example' # str | The If-Match header (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | The If-Match header (optional)

try:
    # Get the configuration file for a URL
    api_response = api_instance.get_url_config(url, accept, if_match=if_match, if_modified_since=if_modified_since, if_none_match=if_none_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_url_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| The URL for which the configuration is requested | 
 **accept** | **str**| The Accept header | 
 **if_match** | **str**| The If-Match header | [optional] 
 **if_modified_since** | **str**| The If-Match header | [optional] 
 **if_none_match** | **str**| The If-Match header | [optional] 
 **if_unmodified_since** | **str**| The If-Match header | [optional] 

### Return type

[**file**](file.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config**
> put_config(section_name, config_file, if_match=if_match, if_modified_since=if_modified_since, if_none_match=if_none_match, if_unmodified_since=if_unmodified_since)

Store the named configuration file

Store the configuration file for a given name

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
api_instance = lockss_configuration.ConfigApi(lockss_configuration.ApiClient(configuration))
section_name = 'section_name_example' # str | The name of the section for which the configuration file\\ \\ is to be stored
config_file = '/path/to/file.txt' # file | The configuration file to be stored
if_match = 'if_match_example' # str | The If-Match header (optional)
if_modified_since = 'if_modified_since_example' # str | The If-Match header (optional)
if_none_match = 'if_none_match_example' # str | The If-Match header (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | The If-Match header (optional)

try:
    # Store the named configuration file
    api_instance.put_config(section_name, config_file, if_match=if_match, if_modified_since=if_modified_since, if_none_match=if_none_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling ConfigApi->put_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_name** | **str**| The name of the section for which the configuration file\\ \\ is to be stored | 
 **config_file** | **file**| The configuration file to be stored | 
 **if_match** | **str**| The If-Match header | [optional] 
 **if_modified_since** | **str**| The If-Match header | [optional] 
 **if_none_match** | **str**| The If-Match header | [optional] 
 **if_unmodified_since** | **str**| The If-Match header | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config_reload**
> put_config_reload()

Request a configuration reload

Request that the stored configuration is reloaded

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
api_instance = lockss_configuration.ConfigApi(lockss_configuration.ApiClient(configuration))

try:
    # Request a configuration reload
    api_instance.put_config_reload()
except ApiException as e:
    print("Exception when calling ConfigApi->put_config_reload: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

