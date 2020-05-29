# vidispine.ItemLockApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_lock**](ItemLockApi.md#create_item_lock) | **POST** /item/{item-id}/lock | Create a lock
[**delete_item_lock**](ItemLockApi.md#delete_item_lock) | **DELETE** /item/{item-id}/lock | Delete a lock
[**get_item_lock**](ItemLockApi.md#get_item_lock) | **GET** /item/{item-id}/lock | Retrieve a lock
[**update_item_lock_expiration**](ItemLockApi.md#update_item_lock_expiration) | **PUT** /item/{item-id}/lock | Extend the expiration date of a lock


# **create_item_lock**
> create_item_lock(item_id, duration=duration, timestamp=timestamp)

Create a lock

Creates a new lock for the item with an expiration date. The expiration date is the sum of the timestamp and the duration. If no timestamp and no duration is given, the expiration date will be set to 24 hours forward in time.

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
api_instance = vidispine.ItemLockApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
duration = '0' # str | An ISO 8601 duration. (optional) (default to '0')
timestamp = 'timestamp_example' # str | An ISO 8601 timestamp.  Defaults to the current time. (optional)

try:
    # Create a lock
    api_instance.create_item_lock(item_id, duration=duration, timestamp=timestamp)
except ApiException as e:
    print("Exception when calling ItemLockApi->create_item_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **duration** | **str**| An ISO 8601 duration. | [optional] [default to &#39;0&#39;]
 **timestamp** | **str**| An ISO 8601 timestamp.  Defaults to the current time. | [optional] 

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

# **delete_item_lock**
> delete_item_lock(item_id)

Delete a lock

Removes the lock for the item.

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
api_instance = vidispine.ItemLockApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.

try:
    # Delete a lock
    api_instance.delete_item_lock(item_id)
except ApiException as e:
    print("Exception when calling ItemLockApi->delete_item_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 

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

# **get_item_lock**
> LockType get_item_lock(item_id)

Retrieve a lock

Retrieves information about the expiration date and which user that holds the lock.

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
api_instance = vidispine.ItemLockApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.

try:
    # Retrieve a lock
    api_response = api_instance.get_item_lock(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemLockApi->get_item_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 

### Return type

[**LockType**](LockType.md)

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

# **update_item_lock_expiration**
> update_item_lock_expiration(item_id, duration=duration, timestamp=timestamp)

Extend the expiration date of a lock

Sets a new expiration date for the lock. The expiration date is the sum of the timestamp and the duration. If no timestamp and no duration is given, the expiration date will be set to 24 hours forward in time.

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
api_instance = vidispine.ItemLockApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
duration = '0' # str | An ISO 8601 duration. (optional) (default to '0')
timestamp = 'timestamp_example' # str | An ISO 8601 timestamp.  Defaults to the current time. (optional)

try:
    # Extend the expiration date of a lock
    api_instance.update_item_lock_expiration(item_id, duration=duration, timestamp=timestamp)
except ApiException as e:
    print("Exception when calling ItemLockApi->update_item_lock_expiration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **duration** | **str**| An ISO 8601 duration. | [optional] [default to &#39;0&#39;]
 **timestamp** | **str**| An ISO 8601 timestamp.  Defaults to the current time. | [optional] 

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

