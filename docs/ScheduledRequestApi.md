# vidispine.ScheduledRequestApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scheduled_request**](ScheduledRequestApi.md#delete_scheduled_request) | **DELETE** /scheduled-request/{request-id} | Delete a scheduled request
[**delete_scheduled_requests**](ScheduledRequestApi.md#delete_scheduled_requests) | **DELETE** /scheduled-request/ | Delete all scheduled requests
[**get_scheduled_request**](ScheduledRequestApi.md#get_scheduled_request) | **GET** /scheduled-request/{request-id} | Retrieve a scheduled request
[**get_scheduled_request_response**](ScheduledRequestApi.md#get_scheduled_request_response) | **GET** /scheduled-request/{request-id}/response | Retrieve the response body
[**get_scheduled_requests**](ScheduledRequestApi.md#get_scheduled_requests) | **GET** /scheduled-request | List all scheduled requests


# **delete_scheduled_request**
> delete_scheduled_request(request_id)

Delete a scheduled request

Deletes the scheduled request with the specified id.

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
api_instance = vidispine.ScheduledRequestApi(vidispine.ApiClient(configuration))
request_id = 'request_id_example' # str | The request id.

try:
    # Delete a scheduled request
    api_instance.delete_scheduled_request(request_id)
except ApiException as e:
    print("Exception when calling ScheduledRequestApi->delete_scheduled_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The request id. | 

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

# **delete_scheduled_requests**
> delete_scheduled_requests()

Delete all scheduled requests

Deletes all scheduled requests for the current user.

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
api_instance = vidispine.ScheduledRequestApi(vidispine.ApiClient(configuration))

try:
    # Delete all scheduled requests
    api_instance.delete_scheduled_requests()
except ApiException as e:
    print("Exception when calling ScheduledRequestApi->delete_scheduled_requests: %s\n" % e)
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

# **get_scheduled_request**
> ScheduledRequestType get_scheduled_request(request_id)

Retrieve a scheduled request

Retrieves the request that matches the specified id.

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
api_instance = vidispine.ScheduledRequestApi(vidispine.ApiClient(configuration))
request_id = 'request_id_example' # str | The request id.

try:
    # Retrieve a scheduled request
    api_response = api_instance.get_scheduled_request(request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledRequestApi->get_scheduled_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The request id. | 

### Return type

[**ScheduledRequestType**](ScheduledRequestType.md)

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

# **get_scheduled_request_response**
> str get_scheduled_request_response(request_id)

Retrieve the response body

Retrieves the response body of the scheduled request. This can only be called if the state of the request is either SUCCESS or BAD_REQUEST. The content-type is the same that was returned when the request was processed.

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
api_instance = vidispine.ScheduledRequestApi(vidispine.ApiClient(configuration))
request_id = 'request_id_example' # str | The request id.

try:
    # Retrieve the response body
    api_response = api_instance.get_scheduled_request_response(request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledRequestApi->get_scheduled_request_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The request id. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The response body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_requests**
> ScheduledRequestListType get_scheduled_requests(state=state)

List all scheduled requests

Retrieves all known scheduled requests for the current user.

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
api_instance = vidispine.ScheduledRequestApi(vidispine.ApiClient(configuration))
state = 'state_example' # str | Retrieve requests belonging to a certain state. (optional)

try:
    # List all scheduled requests
    api_response = api_instance.get_scheduled_requests(state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledRequestApi->get_scheduled_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Retrieve requests belonging to a certain state. | [optional] 

### Return type

[**ScheduledRequestListType**](ScheduledRequestListType.md)

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

