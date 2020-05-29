# vidispine.StorageGroupApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_storage_to_storage_group**](StorageGroupApi.md#add_storage_to_storage_group) | **PUT** /storage/storage-group/{group-name}/{storage-id} | Add a storage to a group
[**create_storage_group**](StorageGroupApi.md#create_storage_group) | **PUT** /storage/storage-group/{group-name} | Create a storage group
[**delete_storage_from_storage_group**](StorageGroupApi.md#delete_storage_from_storage_group) | **DELETE** /storage/storage-group/{group-name}/{storage-id} | Remove a storage from a group
[**delete_storage_group**](StorageGroupApi.md#delete_storage_group) | **DELETE** /storage/storage-group/{group-name} | Delete a storage group
[**delete_storage_group_metadata**](StorageGroupApi.md#delete_storage_group_metadata) | **DELETE** /storage/storage-group/{storagegroup-name}/metadata | Delete all key-value pairs
[**delete_storage_group_metadata_key**](StorageGroupApi.md#delete_storage_group_metadata_key) | **DELETE** /storage/storage-group/{storagegroup-name}/metadata/{keypath} | Delete key-value pairs
[**get_storage_group**](StorageGroupApi.md#get_storage_group) | **GET** /storage/storage-group/{group-name} | List all storages within a group
[**get_storage_group_metadata**](StorageGroupApi.md#get_storage_group_metadata) | **GET** /storage/storage-group/{storagegroup-name}/metadata | Retrieve all metadata
[**get_storage_group_metadata_key**](StorageGroupApi.md#get_storage_group_metadata_key) | **GET** /storage/storage-group/{storagegroup-name}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_storage_groups**](StorageGroupApi.md#get_storage_groups) | **GET** /storage/storage-group/ | List all storage groups
[**update_storage_group_metadata**](StorageGroupApi.md#update_storage_group_metadata) | **PUT** /storage/storage-group/{storagegroup-name}/metadata | Create multiple key-value pairs
[**update_storage_group_metadata_key**](StorageGroupApi.md#update_storage_group_metadata_key) | **PUT** /storage/storage-group/{storagegroup-name}/metadata/{keypath} | Set the value for a specific key


# **add_storage_to_storage_group**
> add_storage_to_storage_group(group_name, storage_id)

Add a storage to a group

Adds a storage to a group. If that group already contains the specified storage this operation does nothing.

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Add a storage to a group
    api_instance.add_storage_to_storage_group(group_name, storage_id)
except ApiException as e:
    print("Exception when calling StorageGroupApi->add_storage_to_storage_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **storage_id** | **str**| The storage id. | 

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

# **create_storage_group**
> create_storage_group(group_name)

Create a storage group

Creates a new storage group with the specified name. If the group already exists this operation does nothing.

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Create a storage group
    api_instance.create_storage_group(group_name)
except ApiException as e:
    print("Exception when calling StorageGroupApi->create_storage_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

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

# **delete_storage_from_storage_group**
> delete_storage_from_storage_group(group_name, storage_id)

Remove a storage from a group

Removes a storage from a group.

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Remove a storage from a group
    api_instance.delete_storage_from_storage_group(group_name, storage_id)
except ApiException as e:
    print("Exception when calling StorageGroupApi->delete_storage_from_storage_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **storage_id** | **str**| The storage id. | 

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

# **delete_storage_group**
> delete_storage_group(group_name)

Delete a storage group

Removes the storage group with the given name. Note that this operation does not remove the actual storages contained in the group.

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Delete a storage group
    api_instance.delete_storage_group(group_name)
except ApiException as e:
    print("Exception when calling StorageGroupApi->delete_storage_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

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

# **delete_storage_group_metadata**
> delete_storage_group_metadata(storagegroup_name)

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
storagegroup_name = 'storagegroup_name_example' # str | The storagegroup name.

try:
    # Delete all key-value pairs
    api_instance.delete_storage_group_metadata(storagegroup_name)
except ApiException as e:
    print("Exception when calling StorageGroupApi->delete_storage_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagegroup_name** | **str**| The storagegroup name. | 

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

# **delete_storage_group_metadata_key**
> delete_storage_group_metadata_key(storagegroup_name, keypath)

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
storagegroup_name = 'storagegroup_name_example' # str | The storagegroup name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_storage_group_metadata_key(storagegroup_name, keypath)
except ApiException as e:
    print("Exception when calling StorageGroupApi->delete_storage_group_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagegroup_name** | **str**| The storagegroup name. | 
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

# **get_storage_group**
> StorageGroupType get_storage_group(group_name)

List all storages within a group

Lists all storages belonging to a certain group.

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # List all storages within a group
    api_response = api_instance.get_storage_group(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageGroupApi->get_storage_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

### Return type

[**StorageGroupType**](StorageGroupType.md)

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

# **get_storage_group_metadata**
> SimpleMetadataType get_storage_group_metadata(storagegroup_name)

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
storagegroup_name = 'storagegroup_name_example' # str | The storagegroup name.

try:
    # Retrieve all metadata
    api_response = api_instance.get_storage_group_metadata(storagegroup_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageGroupApi->get_storage_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagegroup_name** | **str**| The storagegroup name. | 

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

# **get_storage_group_metadata_key**
> str get_storage_group_metadata_key(storagegroup_name, keypath)

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
storagegroup_name = 'storagegroup_name_example' # str | The storagegroup name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_storage_group_metadata_key(storagegroup_name, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageGroupApi->get_storage_group_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagegroup_name** | **str**| The storagegroup name. | 
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

# **get_storage_groups**
> StorageGroupListType get_storage_groups()

List all storage groups

Retrieves all storage groups known by the system.

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))

try:
    # List all storage groups
    api_response = api_instance.get_storage_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageGroupApi->get_storage_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StorageGroupListType**](StorageGroupListType.md)

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

# **update_storage_group_metadata**
> update_storage_group_metadata(storagegroup_name, simple_metadata_type)

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
storagegroup_name = 'storagegroup_name_example' # str | The storagegroup name.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_storage_group_metadata(storagegroup_name, simple_metadata_type)
except ApiException as e:
    print("Exception when calling StorageGroupApi->update_storage_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagegroup_name** | **str**| The storagegroup name. | 
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

# **update_storage_group_metadata_key**
> update_storage_group_metadata_key(storagegroup_name, keypath, body)

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
api_instance = vidispine.StorageGroupApi(vidispine.ApiClient(configuration))
storagegroup_name = 'storagegroup_name_example' # str | The storagegroup name.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_storage_group_metadata_key(storagegroup_name, keypath, body)
except ApiException as e:
    print("Exception when calling StorageGroupApi->update_storage_group_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagegroup_name** | **str**| The storagegroup name. | 
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

