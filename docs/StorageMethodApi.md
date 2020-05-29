# vidispine.StorageMethodApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_storage_method**](StorageMethodApi.md#delete_storage_method) | **DELETE** /storage/{storage-id}/method/{method-id} | Delete a storage method
[**delete_storage_method_metadata**](StorageMethodApi.md#delete_storage_method_metadata) | **DELETE** /storage/{storage-id}/method/{method-id}/metadata | Delete all key-value pairs
[**delete_storage_method_metadata_key**](StorageMethodApi.md#delete_storage_method_metadata_key) | **DELETE** /storage/{storage-id}/method/{method-id}/metadata/{keypath} | Delete key-value pairs
[**get_storage_method**](StorageMethodApi.md#get_storage_method) | **GET** /storage/{storage-id}/method/{method-id} | Retrieve a storage method
[**get_storage_method_metadata**](StorageMethodApi.md#get_storage_method_metadata) | **GET** /storage/{storage-id}/method/{method-id}/metadata | Retrieve all metadata
[**get_storage_method_metadata_key**](StorageMethodApi.md#get_storage_method_metadata_key) | **GET** /storage/{storage-id}/method/{method-id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_storage_methods**](StorageMethodApi.md#get_storage_methods) | **GET** /storage/{storage-id}/method | List storage methods
[**update_or_create_storage_method**](StorageMethodApi.md#update_or_create_storage_method) | **PUT** /storage/{storage-id}/method | Update or create a storage method
[**update_storage_method**](StorageMethodApi.md#update_storage_method) | **PUT** /storage/{storage-id}/method/{method-id} | Create/update a storage method
[**update_storage_method_metadata**](StorageMethodApi.md#update_storage_method_metadata) | **PUT** /storage/{storage-id}/method/{method-id}/metadata | Create multiple key-value pairs
[**update_storage_method_metadata_key**](StorageMethodApi.md#update_storage_method_metadata_key) | **PUT** /storage/{storage-id}/method/{method-id}/metadata/{keypath} | Set the value for a specific key


# **delete_storage_method**
> delete_storage_method(storage_id, method_id, url=url)

Delete a storage method

Removes an access method from a storage.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
method_id = 'method_id_example' # str | The method id.
url = 'url_example' # str | Method is accessed through this URL (optional)

try:
    # Delete a storage method
    api_instance.delete_storage_method(storage_id, method_id, url=url)
except ApiException as e:
    print("Exception when calling StorageMethodApi->delete_storage_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **method_id** | **str**| The method id. | 
 **url** | **str**| Method is accessed through this URL | [optional] 

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

# **delete_storage_method_metadata**
> delete_storage_method_metadata(storage_id, method_id)

Delete all key-value pairs

Clears all key-value pairs for the specified entity.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
method_id = 'method_id_example' # str | The method id.

try:
    # Delete all key-value pairs
    api_instance.delete_storage_method_metadata(storage_id, method_id)
except ApiException as e:
    print("Exception when calling StorageMethodApi->delete_storage_method_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **method_id** | **str**| The method id. | 

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

# **delete_storage_method_metadata_key**
> delete_storage_method_metadata_key(storage_id, method_id, keypath)

Delete key-value pairs

Deletes the key-value pair with the specified key. If a key path is given, it may include wildcards for deleting multiple keys.  Key paths can also be specified as well as specific keys.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
method_id = 'method_id_example' # str | The method id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_storage_method_metadata_key(storage_id, method_id, keypath)
except ApiException as e:
    print("Exception when calling StorageMethodApi->delete_storage_method_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **method_id** | **str**| The method id. | 
 **keypath** | **str**| The keypath. | 

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

# **get_storage_method**
> StorageMethodListType get_storage_method(storage_id, method_id)

Retrieve a storage method

Retrieves a specific access method to storage.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
method_id = 'method_id_example' # str | The method id.

try:
    # Retrieve a storage method
    api_response = api_instance.get_storage_method(storage_id, method_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageMethodApi->get_storage_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **method_id** | **str**| The method id. | 

### Return type

[**StorageMethodListType**](StorageMethodListType.md)

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

# **get_storage_method_metadata**
> SimpleMetadataType get_storage_method_metadata(storage_id, method_id)

Retrieve all metadata

Retrieves all key-value pairs associated with the specified entity.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
method_id = 'method_id_example' # str | The method id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_storage_method_metadata(storage_id, method_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageMethodApi->get_storage_method_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **method_id** | **str**| The method id. | 

### Return type

[**SimpleMetadataType**](SimpleMetadataType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;SimpleMetadataDocument&lt;/em&gt; containing all key-value pairs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_method_metadata_key**
> str get_storage_method_metadata_key(storage_id, method_id, keypath)

Retrieve the metadata for a specific key

Retrieves the value of a specific key. If a key path is specified, exactly one key-value pair must match the key path, else an error is returned.  Key paths can also be specified as well as specific keys.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
method_id = 'method_id_example' # str | The method id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_storage_method_metadata_key(storage_id, method_id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageMethodApi->get_storage_method_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **method_id** | **str**| The method id. | 
 **keypath** | **str**| The keypath. | 

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
**0** | The raw string value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_methods**
> StorageMethodListType get_storage_methods(storage_id, browse=browse, write=write, url=url, read=read)

List storage methods

Retrieves the access methods configured on a specific storage.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
browse = False # bool | - `true` - Only return methods which have file browse capability.  - `false` (default) - Return methods regardless of file browse capability. (optional) (default to False)
write = False # bool | - `true` - Only return methods which have file write capability.  - `false` (default) - Return methods regardless of file write capability. (optional) (default to False)
url = 'url_example' # str | Only return methods with this URL.  Wildcards (`?`, `*`) can be used, for example `http:*`. (optional)
read = False # bool | - `true` - Only return methods which have file read capability.  - `false` (default) - Return methods regardless of file read capability. (optional) (default to False)

try:
    # List storage methods
    api_response = api_instance.get_storage_methods(storage_id, browse=browse, write=write, url=url, read=read)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageMethodApi->get_storage_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **browse** | **bool**| - &#x60;true&#x60; - Only return methods which have file browse capability.  - &#x60;false&#x60; (default) - Return methods regardless of file browse capability. | [optional] [default to False]
 **write** | **bool**| - &#x60;true&#x60; - Only return methods which have file write capability.  - &#x60;false&#x60; (default) - Return methods regardless of file write capability. | [optional] [default to False]
 **url** | **str**| Only return methods with this URL.  Wildcards (&#x60;?&#x60;, &#x60;*&#x60;) can be used, for example &#x60;http:*&#x60;. | [optional] 
 **read** | **bool**| - &#x60;true&#x60; - Only return methods which have file read capability.  - &#x60;false&#x60; (default) - Return methods regardless of file read capability. | [optional] [default to False]

### Return type

[**StorageMethodListType**](StorageMethodListType.md)

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

# **update_or_create_storage_method**
> str update_or_create_storage_method(url, storage_id, read=read, type=type, browse=browse, bandwidth=bandwidth, write=write)

Update or create a storage method

Adds a new access method to the storage. If URL matches an existing method, a new method is not created, instead the existing one is updated.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
url = 'url_example' # str | Method is accessed through this URL
storage_id = 'storage_id_example' # str | The storage id.
read = True # bool | - `true` (default) - Method has file read capability - `false` - Method does not have file read capability (optional) (default to True)
type = 'type_example' # str | method type.  Default is empty. (optional)
browse = True # bool | - `true` (default) - Method has file browse capability - `false` - Method does not have file browse capability (optional) (default to True)
bandwidth = 56 # int | The bandwidth of this method in bytes per second.  Default `0`. (optional)
write = True # bool | - `true` (default) - Method has file write capability - `false` - Method does not have file write capability (optional) (default to True)

try:
    # Update or create a storage method
    api_response = api_instance.update_or_create_storage_method(url, storage_id, read=read, type=type, browse=browse, bandwidth=bandwidth, write=write)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageMethodApi->update_or_create_storage_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Method is accessed through this URL | 
 **storage_id** | **str**| The storage id. | 
 **read** | **bool**| - &#x60;true&#x60; (default) - Method has file read capability - &#x60;false&#x60; - Method does not have file read capability | [optional] [default to True]
 **type** | **str**| method type.  Default is empty. | [optional] 
 **browse** | **bool**| - &#x60;true&#x60; (default) - Method has file browse capability - &#x60;false&#x60; - Method does not have file browse capability | [optional] [default to True]
 **bandwidth** | **int**| The bandwidth of this method in bytes per second.  Default &#x60;0&#x60;. | [optional] 
 **write** | **bool**| - &#x60;true&#x60; (default) - Method has file write capability - &#x60;false&#x60; - Method does not have file write capability | [optional] [default to True]

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
**0** | TabbedTuple : id, URL, status string of method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_method**
> str update_storage_method(url, storage_id, method_id, read=read, type=type, browse=browse, bandwidth=bandwidth, write=write)

Create/update a storage method

Updates access method to the storage.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
url = 'url_example' # str | Method is accessed through this URL
storage_id = 'storage_id_example' # str | The storage id.
method_id = 'method_id_example' # str | The method id.
read = True # bool | - `true` - Method has file read capability.  - `false` - Method does not have file read capability. (optional)
type = 'type_example' # str | method type. (optional)
browse = True # bool | - `true` - Method has file browse capability.  - `false` - Method does not have file browse capability. (optional)
bandwidth = 56 # int | The bandwidth of this method in bytes per second.  Default `0`. (optional)
write = True # bool | - `true` - Method has file write capability.  - `false` - Method does not have file write capability. (optional)

try:
    # Create/update a storage method
    api_response = api_instance.update_storage_method(url, storage_id, method_id, read=read, type=type, browse=browse, bandwidth=bandwidth, write=write)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageMethodApi->update_storage_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Method is accessed through this URL | 
 **storage_id** | **str**| The storage id. | 
 **method_id** | **str**| The method id. | 
 **read** | **bool**| - &#x60;true&#x60; - Method has file read capability.  - &#x60;false&#x60; - Method does not have file read capability. | [optional] 
 **type** | **str**| method type. | [optional] 
 **browse** | **bool**| - &#x60;true&#x60; - Method has file browse capability.  - &#x60;false&#x60; - Method does not have file browse capability. | [optional] 
 **bandwidth** | **int**| The bandwidth of this method in bytes per second.  Default &#x60;0&#x60;. | [optional] 
 **write** | **bool**| - &#x60;true&#x60; - Method has file write capability.  - &#x60;false&#x60; - Method does not have file write capability. | [optional] 

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
**0** | TabbedTuple : id, URL, status string of method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_method_metadata**
> update_storage_method_metadata(storage_id, method_id, simple_metadata_type)

Create multiple key-value pairs

Sets all the specified key-value pairs.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
method_id = 'method_id_example' # str | The method id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_storage_method_metadata(storage_id, method_id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling StorageMethodApi->update_storage_method_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **method_id** | **str**| The method id. | 
 **simple_metadata_type** | [**SimpleMetadataType**](SimpleMetadataType.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_method_metadata_key**
> update_storage_method_metadata_key(storage_id, method_id, keypath, body)

Set the value for a specific key

Sets the value for a specific key. The key path may not contain wildcards.

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
api_instance = vidispine.StorageMethodApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
method_id = 'method_id_example' # str | The method id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_storage_method_metadata_key(storage_id, method_id, keypath, body)
except ApiException as e:
    print("Exception when calling StorageMethodApi->update_storage_method_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **method_id** | **str**| The method id. | 
 **keypath** | **str**| The keypath. | 
 **body** | **str**| The raw string value. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

