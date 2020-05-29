# vidispine.VidispineServiceApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_vidispine_service**](VidispineServiceApi.md#disable_vidispine_service) | **PUT** /vidispine-service/service/{service}/disable | Disable a service
[**disable_vidispine_services**](VidispineServiceApi.md#disable_vidispine_services) | **PUT** /vidispine-service/disable | Disable all services
[**enable_vidispine_service**](VidispineServiceApi.md#enable_vidispine_service) | **PUT** /vidispine-service/service/{service}/enable | Enable a service
[**enable_vidispine_services**](VidispineServiceApi.md#enable_vidispine_services) | **PUT** /vidispine-service/enable | Enable all services
[**get_vidispine_service**](VidispineServiceApi.md#get_vidispine_service) | **GET** /vidispine-service/service/{service} | Retrieve a service
[**get_vidispine_service_stack_trace**](VidispineServiceApi.md#get_vidispine_service_stack_trace) | **GET** /vidispine-service/stacktrace | Retrieve service stack trace
[**get_vidispine_services**](VidispineServiceApi.md#get_vidispine_services) | **GET** /vidispine-service | List all services


# **disable_vidispine_service**
> disable_vidispine_service(service)

Disable a service

Disables this service. No instance in the cluster will run this service.

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
api_instance = vidispine.VidispineServiceApi(vidispine.ApiClient(configuration))
service = 'service_example' # str | The service.

try:
    # Disable a service
    api_instance.disable_vidispine_service(service)
except ApiException as e:
    print("Exception when calling VidispineServiceApi->disable_vidispine_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| The service. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_vidispine_services**
> disable_vidispine_services()

Disable all services

Disables all services. No instance in the cluster will run any services.

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
api_instance = vidispine.VidispineServiceApi(vidispine.ApiClient(configuration))

try:
    # Disable all services
    api_instance.disable_vidispine_services()
except ApiException as e:
    print("Exception when calling VidispineServiceApi->disable_vidispine_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_vidispine_service**
> enable_vidispine_service(service)

Enable a service

Enables this service if disabled.

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
api_instance = vidispine.VidispineServiceApi(vidispine.ApiClient(configuration))
service = 'service_example' # str | The service.

try:
    # Enable a service
    api_instance.enable_vidispine_service(service)
except ApiException as e:
    print("Exception when calling VidispineServiceApi->enable_vidispine_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| The service. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_vidispine_services**
> enable_vidispine_services()

Enable all services

Enables all disabled services.

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
api_instance = vidispine.VidispineServiceApi(vidispine.ApiClient(configuration))

try:
    # Enable all services
    api_instance.enable_vidispine_services()
except ApiException as e:
    print("Exception when calling VidispineServiceApi->enable_vidispine_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vidispine_service**
> VidispineServiceListType get_vidispine_service(service, stacktrace=stacktrace)

Retrieve a service

Return a specific Vidispine service and its status and load.

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
api_instance = vidispine.VidispineServiceApi(vidispine.ApiClient(configuration))
service = 'service_example' # str | The service.
stacktrace = False # bool | Return a stack trace for each service (optional) (default to False)

try:
    # Retrieve a service
    api_response = api_instance.get_vidispine_service(service, stacktrace=stacktrace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VidispineServiceApi->get_vidispine_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| The service. | 
 **stacktrace** | **bool**| Return a stack trace for each service | [optional] [default to False]

### Return type

[**VidispineServiceListType**](VidispineServiceListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vidispine_service_stack_trace**
> str get_vidispine_service_stack_trace()

Retrieve service stack trace

Returns a stack trace from the system.

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
api_instance = vidispine.VidispineServiceApi(vidispine.ApiClient(configuration))

try:
    # Retrieve service stack trace
    api_response = api_instance.get_vidispine_service_stack_trace()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VidispineServiceApi->get_vidispine_service_stack_trace: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A stack trace in plain text. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vidispine_services**
> VidispineServiceListType get_vidispine_services(stacktrace=stacktrace)

List all services

Return all Vidispine services and their status and load.

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
api_instance = vidispine.VidispineServiceApi(vidispine.ApiClient(configuration))
stacktrace = False # bool | Return a stack trace for each service (optional) (default to False)

try:
    # List all services
    api_response = api_instance.get_vidispine_services(stacktrace=stacktrace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VidispineServiceApi->get_vidispine_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stacktrace** | **bool**| Return a stack trace for each service | [optional] [default to False]

### Return type

[**VidispineServiceListType**](VidispineServiceListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

