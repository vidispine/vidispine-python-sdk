# vidispine.SystemApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version**](SystemApi.md#get_version) | **GET** /version | Retrieve version and license information
[**get_wadl**](SystemApi.md#get_wadl) | **GET** /application.wadl | WADL


# **get_version**
> VersionType get_version()

Retrieve version and license information

Display your license allowance and current system usage.  The `systemInfo` element in the response shows the MAC addresses discovered on the local system. The MAC-address(es) in the license key must match that/those of your system.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import vidispine
from vidispine.rest import ApiException
from pprint import pprint
configuration = vidispine.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = vidispine.SystemApi(vidispine.ApiClient(configuration))

try:
    # Retrieve version and license information
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionType**](VersionType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The version details in a informational text format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wadl**
> str get_wadl()

WADL

Retrieves the application WADL that describes the resources and methods exposed by the VS API.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import vidispine
from vidispine.rest import ApiException
from pprint import pprint
configuration = vidispine.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = vidispine.SystemApi(vidispine.ApiClient(configuration))

try:
    # WADL
    api_response = api_instance.get_wadl()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_wadl: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.sun.wadl+xml, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The application WADL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

