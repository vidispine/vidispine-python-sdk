# vidispine.MetadataLockApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_lock_field**](MetadataLockApi.md#add_metadata_lock_field) | **PUT** /{type}/{id}/metadata-lock/{lock-id} | Update a locking container
[**create_metadata_lock**](MetadataLockApi.md#create_metadata_lock) | **POST** /{type}/{id}/metadata-lock | Create a locking container
[**delete_metadata_lock**](MetadataLockApi.md#delete_metadata_lock) | **DELETE** /{type}/{id}/metadata-lock/{lock-id} | Delete a locking container
[**get_metadata_lock**](MetadataLockApi.md#get_metadata_lock) | **GET** /{type}/{id}/metadata-lock/{lock-id} | Retrieve a locking container
[**get_metadata_locks**](MetadataLockApi.md#get_metadata_locks) | **GET** /{type}/{id}/metadata-lock | List all locking containers


# **add_metadata_lock_field**
> MetadataLockType add_metadata_lock_field(type, id, lock_id, field=field, timeout=timeout)

Update a locking container

Add new fields to the locking container and/or updates the expiry time.

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
api_instance = vidispine.MetadataLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
id = 'id_example' # str | The id.
lock_id = 'lock_id_example' # str | The lock id.
field = ['field_example'] # list[str] | Comma-separated list of fields to lock. (optional)
timeout = 60 # int | Time-out in seconds. (optional) (default to 60)

try:
    # Update a locking container
    api_response = api_instance.add_metadata_lock_field(type, id, lock_id, field=field, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataLockApi->add_metadata_lock_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **id** | **str**| The id. | 
 **lock_id** | **str**| The lock id. | 
 **field** | [**list[str]**](str.md)| Comma-separated list of fields to lock. | [optional] 
 **timeout** | **int**| Time-out in seconds. | [optional] [default to 60]

### Return type

[**MetadataLockType**](MetadataLockType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Locking id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metadata_lock**
> MetadataLockType create_metadata_lock(type, id, field=field, timeout=timeout)

Create a locking container

Creates a new locking container, optionally with initial locks.

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
api_instance = vidispine.MetadataLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
id = 'id_example' # str | The id.
field = ['field_example'] # list[str] | Comma-separated list of fields to lock. (optional)
timeout = 60 # int | Time-out in seconds. (optional) (default to 60)

try:
    # Create a locking container
    api_response = api_instance.create_metadata_lock(type, id, field=field, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataLockApi->create_metadata_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **id** | **str**| The id. | 
 **field** | [**list[str]**](str.md)| Comma-separated list of fields to lock. | [optional] 
 **timeout** | **int**| Time-out in seconds. | [optional] [default to 60]

### Return type

[**MetadataLockType**](MetadataLockType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Locking id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_lock**
> delete_metadata_lock(type, id, lock_id)

Delete a locking container

Remove the locking container and all locks associated with it.

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
api_instance = vidispine.MetadataLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
id = 'id_example' # str | The id.
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Delete a locking container
    api_instance.delete_metadata_lock(type, id, lock_id)
except ApiException as e:
    print("Exception when calling MetadataLockApi->delete_metadata_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **id** | **str**| The id. | 
 **lock_id** | **str**| The lock id. | 

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

# **get_metadata_lock**
> MetadataLockType get_metadata_lock(type, id, lock_id)

Retrieve a locking container

Returns information about specified locking container.

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
api_instance = vidispine.MetadataLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
id = 'id_example' # str | The id.
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Retrieve a locking container
    api_response = api_instance.get_metadata_lock(type, id, lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataLockApi->get_metadata_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **id** | **str**| The id. | 
 **lock_id** | **str**| The lock id. | 

### Return type

[**MetadataLockType**](MetadataLockType.md)

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

# **get_metadata_locks**
> MetadataLockListType get_metadata_locks(type, id)

List all locking containers

Returns all locking containers.

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
api_instance = vidispine.MetadataLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
id = 'id_example' # str | The id.

try:
    # List all locking containers
    api_response = api_instance.get_metadata_locks(type, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataLockApi->get_metadata_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **id** | **str**| The id. | 

### Return type

[**MetadataLockListType**](MetadataLockListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of locking ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

