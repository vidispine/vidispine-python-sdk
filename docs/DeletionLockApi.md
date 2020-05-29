# vidispine.DeletionLockApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_deletion_lock**](DeletionLockApi.md#create_entity_deletion_lock) | **POST** /{type}/{entity-id}/deletion-lock | Create a lock
[**create_entity_type_deletion_lock**](DeletionLockApi.md#create_entity_type_deletion_lock) | **POST** /{type}/deletion-lock | Create a lock
[**delete_deletion_lock**](DeletionLockApi.md#delete_deletion_lock) | **DELETE** /deletion-lock/{lock-id} | Delete a lock
[**delete_deletion_lock_metadata**](DeletionLockApi.md#delete_deletion_lock_metadata) | **DELETE** /deletion-lock/{lock-id}/metadata | Delete all key-value pairs
[**delete_deletion_lock_metadata_key**](DeletionLockApi.md#delete_deletion_lock_metadata_key) | **DELETE** /deletion-lock/{lock-id}/metadata/{keypath} | Delete key-value pairs
[**delete_entity_deletion_lock_metadata**](DeletionLockApi.md#delete_entity_deletion_lock_metadata) | **DELETE** /{type}/{entity-id}/deletion-lock/{lock-id}/metadata | Delete all key-value pairs
[**delete_entity_deletion_metadata_key**](DeletionLockApi.md#delete_entity_deletion_metadata_key) | **DELETE** /{type}/{entity-id}/deletion-lock/{lock-id}/metadata/{keypath} | Delete key-value pairs
[**delete_entity_type_deletion_lock_metadata**](DeletionLockApi.md#delete_entity_type_deletion_lock_metadata) | **DELETE** /{type}/deletion-lock/{lock-id}/metadata | Delete all key-value pairs
[**delete_entity_type_deletion_lock_metadata_key**](DeletionLockApi.md#delete_entity_type_deletion_lock_metadata_key) | **DELETE** /{type}/deletion-lock/{lock-id}/metadata/{keypath} | Delete key-value pairs
[**get_deletion_lock**](DeletionLockApi.md#get_deletion_lock) | **GET** /deletion-lock/{lock-id} | Retrieve a lock
[**get_deletion_lock_metadata**](DeletionLockApi.md#get_deletion_lock_metadata) | **GET** /deletion-lock/{lock-id}/metadata | Retrieve all metadata
[**get_deletion_lock_metadata_key**](DeletionLockApi.md#get_deletion_lock_metadata_key) | **GET** /deletion-lock/{lock-id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_deletion_locks**](DeletionLockApi.md#get_deletion_locks) | **GET** /deletion-lock | List all locks
[**get_entity_deletion_lock**](DeletionLockApi.md#get_entity_deletion_lock) | **GET** /{type}/{entity-id}/deletion-lock/{lock-id} | Retrieve a lock for an entity
[**get_entity_deletion_lock_metadata**](DeletionLockApi.md#get_entity_deletion_lock_metadata) | **GET** /{type}/{entity-id}/deletion-lock/{lock-id}/metadata | Retrieve all metadata
[**get_entity_deletion_lock_metadata_key**](DeletionLockApi.md#get_entity_deletion_lock_metadata_key) | **GET** /{type}/{entity-id}/deletion-lock/{lock-id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_entity_deletion_locks**](DeletionLockApi.md#get_entity_deletion_locks) | **GET** /{type}/{entity-id}/deletion-lock | List all locks for an entity
[**get_entity_type_deletion_lock**](DeletionLockApi.md#get_entity_type_deletion_lock) | **GET** /{type}/deletion-lock/{lock-id} | Retrieve a lock for an entity
[**get_entity_type_deletion_lock_metadata**](DeletionLockApi.md#get_entity_type_deletion_lock_metadata) | **GET** /{type}/deletion-lock/{lock-id}/metadata | Retrieve all metadata
[**get_entity_type_deletion_lock_metadata_key**](DeletionLockApi.md#get_entity_type_deletion_lock_metadata_key) | **GET** /{type}/deletion-lock/{lock-id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_entity_type_deletion_locks**](DeletionLockApi.md#get_entity_type_deletion_locks) | **GET** /{type}/deletion-lock | List all locks for an entity
[**update_deletion_lock**](DeletionLockApi.md#update_deletion_lock) | **PUT** /deletion-lock/{lock-id} | Update a lock
[**update_deletion_lock_metadata**](DeletionLockApi.md#update_deletion_lock_metadata) | **PUT** /deletion-lock/{lock-id}/metadata | Create multiple key-value pairs
[**update_deletion_lock_metadata_key**](DeletionLockApi.md#update_deletion_lock_metadata_key) | **PUT** /deletion-lock/{lock-id}/metadata/{keypath} | Set the value for a specific key
[**update_entity_deletion_lock**](DeletionLockApi.md#update_entity_deletion_lock) | **PUT** /{type}/{entity-id}/deletion-lock/{lock-id} | Update a lock
[**update_entity_deletion_lock_metadata**](DeletionLockApi.md#update_entity_deletion_lock_metadata) | **PUT** /{type}/{entity-id}/deletion-lock/{lock-id}/metadata | Create multiple key-value pairs
[**update_entity_deletion_lock_metadata_key**](DeletionLockApi.md#update_entity_deletion_lock_metadata_key) | **PUT** /{type}/{entity-id}/deletion-lock/{lock-id}/metadata/{keypath} | Set the value for a specific key
[**update_entity_type_deletion_lock**](DeletionLockApi.md#update_entity_type_deletion_lock) | **PUT** /{type}/deletion-lock/{lock-id} | Update a lock
[**update_entity_type_deletion_lock_metadata**](DeletionLockApi.md#update_entity_type_deletion_lock_metadata) | **PUT** /{type}/deletion-lock/{lock-id}/metadata | Create multiple key-value pairs
[**update_entity_type_deletion_lock_metadata_key**](DeletionLockApi.md#update_entity_type_deletion_lock_metadata_key) | **PUT** /{type}/deletion-lock/{lock-id}/metadata/{keypath} | Set the value for a specific key


# **create_entity_deletion_lock**
> DeletionLockType create_entity_deletion_lock(type, entity_id, deletion_lock_type)

Create a lock

Creates new deletion lock based on the information in the *DeletionLockDocument*.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
deletion_lock_type = vidispine.DeletionLockType() # DeletionLockType | 

try:
    # Create a lock
    api_response = api_instance.create_entity_deletion_lock(type, entity_id, deletion_lock_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->create_entity_deletion_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **deletion_lock_type** | [**DeletionLockType**](DeletionLockType.md)|  | 

### Return type

[**DeletionLockType**](DeletionLockType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity_type_deletion_lock**
> DeletionLockType create_entity_type_deletion_lock(type, deletion_lock_type)

Create a lock

Creates new deletion lock based on the information in the *DeletionLockDocument*.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
deletion_lock_type = vidispine.DeletionLockType() # DeletionLockType | 

try:
    # Create a lock
    api_response = api_instance.create_entity_type_deletion_lock(type, deletion_lock_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->create_entity_type_deletion_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **deletion_lock_type** | [**DeletionLockType**](DeletionLockType.md)|  | 

### Return type

[**DeletionLockType**](DeletionLockType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deletion_lock**
> delete_deletion_lock(lock_id)

Delete a lock

Delete a lock that was explicitly set on this entity.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Delete a lock
    api_instance.delete_deletion_lock(lock_id)
except ApiException as e:
    print("Exception when calling DeletionLockApi->delete_deletion_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_deletion_lock_metadata**
> delete_deletion_lock_metadata(lock_id)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Delete all key-value pairs
    api_instance.delete_deletion_lock_metadata(lock_id)
except ApiException as e:
    print("Exception when calling DeletionLockApi->delete_deletion_lock_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_deletion_lock_metadata_key**
> delete_deletion_lock_metadata_key(lock_id, keypath)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
lock_id = 'lock_id_example' # str | The lock id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_deletion_lock_metadata_key(lock_id, keypath)
except ApiException as e:
    print("Exception when calling DeletionLockApi->delete_deletion_lock_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **str**| The lock id. | 
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

# **delete_entity_deletion_lock_metadata**
> delete_entity_deletion_lock_metadata(type, entity_id, lock_id)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
entity_id = 'entity_id_example' # str | The entity id.
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Delete all key-value pairs
    api_instance.delete_entity_deletion_lock_metadata(type, entity_id, lock_id)
except ApiException as e:
    print("Exception when calling DeletionLockApi->delete_entity_deletion_lock_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **entity_id** | **str**| The entity id. | 
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

# **delete_entity_deletion_metadata_key**
> delete_entity_deletion_metadata_key(type, entity_id, lock_id, keypath)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
entity_id = 'entity_id_example' # str | The entity id.
lock_id = 'lock_id_example' # str | The lock id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_entity_deletion_metadata_key(type, entity_id, lock_id, keypath)
except ApiException as e:
    print("Exception when calling DeletionLockApi->delete_entity_deletion_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **entity_id** | **str**| The entity id. | 
 **lock_id** | **str**| The lock id. | 
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

# **delete_entity_type_deletion_lock_metadata**
> delete_entity_type_deletion_lock_metadata(type, lock_id)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Delete all key-value pairs
    api_instance.delete_entity_type_deletion_lock_metadata(type, lock_id)
except ApiException as e:
    print("Exception when calling DeletionLockApi->delete_entity_type_deletion_lock_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
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

# **delete_entity_type_deletion_lock_metadata_key**
> delete_entity_type_deletion_lock_metadata_key(type, lock_id, keypath)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
lock_id = 'lock_id_example' # str | The lock id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_entity_type_deletion_lock_metadata_key(type, lock_id, keypath)
except ApiException as e:
    print("Exception when calling DeletionLockApi->delete_entity_type_deletion_lock_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **lock_id** | **str**| The lock id. | 
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

# **get_deletion_lock**
> DeletionLockType get_deletion_lock(lock_id)

Retrieve a lock

Returns a specific lock.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Retrieve a lock
    api_response = api_instance.get_deletion_lock(lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_deletion_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **str**| The lock id. | 

### Return type

[**DeletionLockType**](DeletionLockType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | XML/JSON, schema &lt;em&gt;DeletionLockDocument&lt;/em&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deletion_lock_metadata**
> SimpleMetadataType get_deletion_lock_metadata(lock_id)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_deletion_lock_metadata(lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_deletion_lock_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **str**| The lock id. | 

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

# **get_deletion_lock_metadata_key**
> str get_deletion_lock_metadata_key(lock_id, keypath)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
lock_id = 'lock_id_example' # str | The lock id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_deletion_lock_metadata_key(lock_id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_deletion_lock_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **str**| The lock id. | 
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

# **get_deletion_locks**
> DeletionLockListType get_deletion_locks(only_effective=only_effective, first=first, entity_types=entity_types, username=username, number=number, metadata=metadata, range=range)

List all locks

Retrieves a list of deletion locks.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
only_effective = False # bool | - `true` - Only return the effective lock of the entity.  - `false` (default) - Return all deletion locks applied on the entity. (optional) (default to False)
first = 1 # int | Return locks starting from the specified offset. (optional) (default to 1)
entity_types = ['entity_types_example'] # list[str] | Comma-separated list.  Only return locks set explicitly on the specified entity type(s). (optional)
username = 'username_example' # str | Comma-separated user names.  Filter only locks created by the specified user(s). (optional)
number = 100 # int | Return at most the specified number of locks. (optional) (default to 100)
metadata = ['metadata_example'] # list[str] | Filter out only the locks that has metadata according to the filter criteria.   - *key* `=` *value* - Multiple query parameters can be specified.  Note that `=` is part of the query parameter, and has to be encoded (`%3d`). (optional)
range = 'range_example' # str | Filter out locks whose expiry time is within the specified range.  The range format is `[d. . d]`, `(d. . d)`, `[d. . d)`, `(d. . d]`, `(*. . d]`, `[d. . *)`, or `(*. . *)`.  `d` is a date and time in the ISO 8601 format. (optional)

try:
    # List all locks
    api_response = api_instance.get_deletion_locks(only_effective=only_effective, first=first, entity_types=entity_types, username=username, number=number, metadata=metadata, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_deletion_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **only_effective** | **bool**| - &#x60;true&#x60; - Only return the effective lock of the entity.  - &#x60;false&#x60; (default) - Return all deletion locks applied on the entity. | [optional] [default to False]
 **first** | **int**| Return locks starting from the specified offset. | [optional] [default to 1]
 **entity_types** | [**list[str]**](str.md)| Comma-separated list.  Only return locks set explicitly on the specified entity type(s). | [optional] 
 **username** | **str**| Comma-separated user names.  Filter only locks created by the specified user(s). | [optional] 
 **number** | **int**| Return at most the specified number of locks. | [optional] [default to 100]
 **metadata** | [**list[str]**](str.md)| Filter out only the locks that has metadata according to the filter criteria.   - *key* &#x60;&#x3D;&#x60; *value* - Multiple query parameters can be specified.  Note that &#x60;&#x3D;&#x60; is part of the query parameter, and has to be encoded (&#x60;%3d&#x60;). | [optional] 
 **range** | **str**| Filter out locks whose expiry time is within the specified range.  The range format is &#x60;[d. . d]&#x60;, &#x60;(d. . d)&#x60;, &#x60;[d. . d)&#x60;, &#x60;(d. . d]&#x60;, &#x60;(*. . d]&#x60;, &#x60;[d. . *)&#x60;, or &#x60;(*. . *)&#x60;.  &#x60;d&#x60; is a date and time in the ISO 8601 format. | [optional] 

### Return type

[**DeletionLockListType**](DeletionLockListType.md)

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

# **get_entity_deletion_lock**
> DeletionLockType get_entity_deletion_lock(type, entity_id, lock_id)

Retrieve a lock for an entity

Returns a specific lock.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Retrieve a lock for an entity
    api_response = api_instance.get_entity_deletion_lock(type, entity_id, lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_entity_deletion_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **lock_id** | **str**| The lock id. | 

### Return type

[**DeletionLockType**](DeletionLockType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | XML/JSON, schema &lt;em&gt;DeletionLockDocument&lt;/em&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_deletion_lock_metadata**
> SimpleMetadataType get_entity_deletion_lock_metadata(type, entity_id, lock_id)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
entity_id = 'entity_id_example' # str | The entity id.
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_entity_deletion_lock_metadata(type, entity_id, lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_entity_deletion_lock_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **entity_id** | **str**| The entity id. | 
 **lock_id** | **str**| The lock id. | 

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

# **get_entity_deletion_lock_metadata_key**
> str get_entity_deletion_lock_metadata_key(type, entity_id, lock_id, keypath)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
entity_id = 'entity_id_example' # str | The entity id.
lock_id = 'lock_id_example' # str | The lock id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_entity_deletion_lock_metadata_key(type, entity_id, lock_id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_entity_deletion_lock_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **entity_id** | **str**| The entity id. | 
 **lock_id** | **str**| The lock id. | 
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

# **get_entity_deletion_locks**
> DeletionLockListType get_entity_deletion_locks(type, entity_id, only_effective=only_effective, first=first, username=username, number=number, metadata=metadata, range=range)

List all locks for an entity

Retrieves a list of deletion locks on the entity.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
only_effective = False # bool | - `true` - Only return the effective lock of the entity.  - `false` (default) - Return all deletion locks applied on the entity. (optional) (default to False)
first = 1 # int | Return locks starting from the specified offset. (optional) (default to 1)
username = 'username_example' # str | Comma-separated user names.  Filter only locks created by the specified user(s). (optional)
number = 100 # int | Return at most the specified number of locks. (optional) (default to 100)
metadata = ['metadata_example'] # list[str] | Filter out only the locks that has metadata according to the filter criteria.   - *key* `=` *value* - Multiple query parameters can be specified.  Note that `=` is part of the query parameter, and has to be encoded (`%3d`). (optional)
range = 'range_example' # str | Filter out locks whose expiry time is within the specified range.  The range format is `[d. . d]`, `(d. . d)`, `[d. . d)`, `(d. . d]`, `(*. . d]`, `[d. . *)`, or `(*. . *)`.  `d` is a date and time in the ISO 8601 format. (optional)

try:
    # List all locks for an entity
    api_response = api_instance.get_entity_deletion_locks(type, entity_id, only_effective=only_effective, first=first, username=username, number=number, metadata=metadata, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_entity_deletion_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **only_effective** | **bool**| - &#x60;true&#x60; - Only return the effective lock of the entity.  - &#x60;false&#x60; (default) - Return all deletion locks applied on the entity. | [optional] [default to False]
 **first** | **int**| Return locks starting from the specified offset. | [optional] [default to 1]
 **username** | **str**| Comma-separated user names.  Filter only locks created by the specified user(s). | [optional] 
 **number** | **int**| Return at most the specified number of locks. | [optional] [default to 100]
 **metadata** | [**list[str]**](str.md)| Filter out only the locks that has metadata according to the filter criteria.   - *key* &#x60;&#x3D;&#x60; *value* - Multiple query parameters can be specified.  Note that &#x60;&#x3D;&#x60; is part of the query parameter, and has to be encoded (&#x60;%3d&#x60;). | [optional] 
 **range** | **str**| Filter out locks whose expiry time is within the specified range.  The range format is &#x60;[d. . d]&#x60;, &#x60;(d. . d)&#x60;, &#x60;[d. . d)&#x60;, &#x60;(d. . d]&#x60;, &#x60;(*. . d]&#x60;, &#x60;[d. . *)&#x60;, or &#x60;(*. . *)&#x60;.  &#x60;d&#x60; is a date and time in the ISO 8601 format. | [optional] 

### Return type

[**DeletionLockListType**](DeletionLockListType.md)

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

# **get_entity_type_deletion_lock**
> DeletionLockType get_entity_type_deletion_lock(type, lock_id)

Retrieve a lock for an entity

Returns a specific lock.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Retrieve a lock for an entity
    api_response = api_instance.get_entity_type_deletion_lock(type, lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_entity_type_deletion_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **lock_id** | **str**| The lock id. | 

### Return type

[**DeletionLockType**](DeletionLockType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | XML/JSON, schema &lt;em&gt;DeletionLockDocument&lt;/em&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_type_deletion_lock_metadata**
> SimpleMetadataType get_entity_type_deletion_lock_metadata(type, lock_id)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
lock_id = 'lock_id_example' # str | The lock id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_entity_type_deletion_lock_metadata(type, lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_entity_type_deletion_lock_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **lock_id** | **str**| The lock id. | 

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

# **get_entity_type_deletion_lock_metadata_key**
> str get_entity_type_deletion_lock_metadata_key(type, lock_id, keypath)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
lock_id = 'lock_id_example' # str | The lock id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_entity_type_deletion_lock_metadata_key(type, lock_id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_entity_type_deletion_lock_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **lock_id** | **str**| The lock id. | 
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

# **get_entity_type_deletion_locks**
> DeletionLockListType get_entity_type_deletion_locks(type, only_effective=only_effective, first=first, username=username, number=number, metadata=metadata, range=range)

List all locks for an entity

Retrieves a list of deletion locks on the entity.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
only_effective = False # bool | - `true` - Only return the effective lock of the entity.  - `false` (default) - Return all deletion locks applied on the entity. (optional) (default to False)
first = 1 # int | Return locks starting from the specified offset. (optional) (default to 1)
username = 'username_example' # str | Comma-separated user names.  Filter only locks created by the specified user(s). (optional)
number = 100 # int | Return at most the specified number of locks. (optional) (default to 100)
metadata = ['metadata_example'] # list[str] | Filter out only the locks that has metadata according to the filter criteria.   - *key* `=` *value* - Multiple query parameters can be specified.  Note that `=` is part of the query parameter, and has to be encoded (`%3d`). (optional)
range = 'range_example' # str | Filter out locks whose expiry time is within the specified range.  The range format is `[d. . d]`, `(d. . d)`, `[d. . d)`, `(d. . d]`, `(*. . d]`, `[d. . *)`, or `(*. . *)`.  `d` is a date and time in the ISO 8601 format. (optional)

try:
    # List all locks for an entity
    api_response = api_instance.get_entity_type_deletion_locks(type, only_effective=only_effective, first=first, username=username, number=number, metadata=metadata, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->get_entity_type_deletion_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **only_effective** | **bool**| - &#x60;true&#x60; - Only return the effective lock of the entity.  - &#x60;false&#x60; (default) - Return all deletion locks applied on the entity. | [optional] [default to False]
 **first** | **int**| Return locks starting from the specified offset. | [optional] [default to 1]
 **username** | **str**| Comma-separated user names.  Filter only locks created by the specified user(s). | [optional] 
 **number** | **int**| Return at most the specified number of locks. | [optional] [default to 100]
 **metadata** | [**list[str]**](str.md)| Filter out only the locks that has metadata according to the filter criteria.   - *key* &#x60;&#x3D;&#x60; *value* - Multiple query parameters can be specified.  Note that &#x60;&#x3D;&#x60; is part of the query parameter, and has to be encoded (&#x60;%3d&#x60;). | [optional] 
 **range** | **str**| Filter out locks whose expiry time is within the specified range.  The range format is &#x60;[d. . d]&#x60;, &#x60;(d. . d)&#x60;, &#x60;[d. . d)&#x60;, &#x60;(d. . d]&#x60;, &#x60;(*. . d]&#x60;, &#x60;[d. . *)&#x60;, or &#x60;(*. . *)&#x60;.  &#x60;d&#x60; is a date and time in the ISO 8601 format. | [optional] 

### Return type

[**DeletionLockListType**](DeletionLockListType.md)

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

# **update_deletion_lock**
> DeletionLockType update_deletion_lock(lock_id, deletion_lock_type)

Update a lock

Updates a lock based on the information in the *DeletionLockDocument*.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
lock_id = 'lock_id_example' # str | The lock id.
deletion_lock_type = vidispine.DeletionLockType() # DeletionLockType | 

try:
    # Update a lock
    api_response = api_instance.update_deletion_lock(lock_id, deletion_lock_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->update_deletion_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **str**| The lock id. | 
 **deletion_lock_type** | [**DeletionLockType**](DeletionLockType.md)|  | 

### Return type

[**DeletionLockType**](DeletionLockType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deletion_lock_metadata**
> update_deletion_lock_metadata(lock_id, simple_metadata_type)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
lock_id = 'lock_id_example' # str | The lock id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_deletion_lock_metadata(lock_id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling DeletionLockApi->update_deletion_lock_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **str**| The lock id. | 
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

# **update_deletion_lock_metadata_key**
> update_deletion_lock_metadata_key(lock_id, keypath, body)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
lock_id = 'lock_id_example' # str | The lock id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_deletion_lock_metadata_key(lock_id, keypath, body)
except ApiException as e:
    print("Exception when calling DeletionLockApi->update_deletion_lock_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_id** | **str**| The lock id. | 
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

# **update_entity_deletion_lock**
> DeletionLockType update_entity_deletion_lock(type, entity_id, lock_id, deletion_lock_type)

Update a lock

Updates a lock based on the information in the *DeletionLockDocument*.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
lock_id = 'lock_id_example' # str | The lock id.
deletion_lock_type = vidispine.DeletionLockType() # DeletionLockType | 

try:
    # Update a lock
    api_response = api_instance.update_entity_deletion_lock(type, entity_id, lock_id, deletion_lock_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->update_entity_deletion_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **lock_id** | **str**| The lock id. | 
 **deletion_lock_type** | [**DeletionLockType**](DeletionLockType.md)|  | 

### Return type

[**DeletionLockType**](DeletionLockType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_deletion_lock_metadata**
> update_entity_deletion_lock_metadata(type, entity_id, lock_id, simple_metadata_type)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
entity_id = 'entity_id_example' # str | The entity id.
lock_id = 'lock_id_example' # str | The lock id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_entity_deletion_lock_metadata(type, entity_id, lock_id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling DeletionLockApi->update_entity_deletion_lock_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **entity_id** | **str**| The entity id. | 
 **lock_id** | **str**| The lock id. | 
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

# **update_entity_deletion_lock_metadata_key**
> update_entity_deletion_lock_metadata_key(type, entity_id, lock_id, keypath, body)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
entity_id = 'entity_id_example' # str | The entity id.
lock_id = 'lock_id_example' # str | The lock id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_entity_deletion_lock_metadata_key(type, entity_id, lock_id, keypath, body)
except ApiException as e:
    print("Exception when calling DeletionLockApi->update_entity_deletion_lock_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **entity_id** | **str**| The entity id. | 
 **lock_id** | **str**| The lock id. | 
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

# **update_entity_type_deletion_lock**
> DeletionLockType update_entity_type_deletion_lock(type, lock_id, deletion_lock_type)

Update a lock

Updates a lock based on the information in the *DeletionLockDocument*.

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
lock_id = 'lock_id_example' # str | The lock id.
deletion_lock_type = vidispine.DeletionLockType() # DeletionLockType | 

try:
    # Update a lock
    api_response = api_instance.update_entity_type_deletion_lock(type, lock_id, deletion_lock_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeletionLockApi->update_entity_type_deletion_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **lock_id** | **str**| The lock id. | 
 **deletion_lock_type** | [**DeletionLockType**](DeletionLockType.md)|  | 

### Return type

[**DeletionLockType**](DeletionLockType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_type_deletion_lock_metadata**
> update_entity_type_deletion_lock_metadata(type, lock_id, simple_metadata_type)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
lock_id = 'lock_id_example' # str | The lock id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_entity_type_deletion_lock_metadata(type, lock_id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling DeletionLockApi->update_entity_type_deletion_lock_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **lock_id** | **str**| The lock id. | 
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

# **update_entity_type_deletion_lock_metadata_key**
> update_entity_type_deletion_lock_metadata_key(type, lock_id, keypath, body)

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
api_instance = vidispine.DeletionLockApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
lock_id = 'lock_id_example' # str | The lock id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_entity_type_deletion_lock_metadata_key(type, lock_id, keypath, body)
except ApiException as e:
    print("Exception when calling DeletionLockApi->update_entity_type_deletion_lock_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **lock_id** | **str**| The lock id. | 
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

