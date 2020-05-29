# vidispine.StorageApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_storage_evacuation**](StorageApi.md#abort_storage_evacuation) | **DELETE** /storage/{storage-id}/evacuate | Cancel evacuation of a storage
[**create_storage**](StorageApi.md#create_storage) | **POST** /storage | Create a storage
[**delete_storage**](StorageApi.md#delete_storage) | **DELETE** /storage/{storage-id} | Delete a storage
[**delete_storage_metadata**](StorageApi.md#delete_storage_metadata) | **DELETE** /storage/{storage-id}/metadata | Delete all key-value pairs
[**delete_storage_metadata_key**](StorageApi.md#delete_storage_metadata_key) | **DELETE** /storage/{storage-id}/metadata/{keypath} | Delete key-value pairs
[**evacuate_storage**](StorageApi.md#evacuate_storage) | **PUT** /storage/{storage-id}/evacuate | Evacuate a storage
[**get_storage**](StorageApi.md#get_storage) | **GET** /storage/{storage-id} | Retrieve a storage
[**get_storage_free_space**](StorageApi.md#get_storage_free_space) | **GET** /storage/{storage-id}/freespace | Retrieve the amount of free space on a storage
[**get_storage_import_document**](StorageApi.md#get_storage_import_document) | **GET** /storage/{storage-id}/export | Export a storage definition
[**get_storage_metadata**](StorageApi.md#get_storage_metadata) | **GET** /storage/{storage-id}/metadata | Retrieve all metadata
[**get_storage_metadata_key**](StorageApi.md#get_storage_metadata_key) | **GET** /storage/{storage-id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_storage_status**](StorageApi.md#get_storage_status) | **GET** /storage/{storage-id}/status | Retrieve the storage status
[**get_storages**](StorageApi.md#get_storages) | **GET** /storage | List all storages
[**rescan_storage**](StorageApi.md#rescan_storage) | **POST** /storage/{storage-id}/rescan | Rescan a storage
[**update_storage**](StorageApi.md#update_storage) | **PUT** /storage/{storage-id} | Update a storage
[**update_storage_metadata**](StorageApi.md#update_storage_metadata) | **PUT** /storage/{storage-id}/metadata | Create multiple key-value pairs
[**update_storage_metadata_key**](StorageApi.md#update_storage_metadata_key) | **PUT** /storage/{storage-id}/metadata/{keypath} | Set the value for a specific key
[**update_storage_type**](StorageApi.md#update_storage_type) | **PUT** /storage/{storage-id}/type/{type} | Update the storage type


# **abort_storage_evacuation**
> abort_storage_evacuation(storage_id)

Cancel evacuation of a storage

Cancel the evacuation process on a storage.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Cancel evacuation of a storage
    api_instance.abort_storage_evacuation(storage_id)
except ApiException as e:
    print("Exception when calling StorageApi->abort_storage_evacuation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **create_storage**
> StorageType create_storage(storage_type)

Create a storage

Creates a new storage.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_type = vidispine.StorageType() # StorageType | 

try:
    # Create a storage
    api_response = api_instance.create_storage(storage_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->create_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_type** | [**StorageType**](StorageType.md)|  | 

### Return type

[**StorageType**](StorageType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Storage id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage**
> delete_storage(storage_id, safe=safe)

Delete a storage

Deletes the storage. All files in storage will remain after call, but the Vidispine system will no longer manage them.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
safe = False # bool | - `true` - Storage will only be deleted if there are no files connected to items on the storage.  - `false` (default) - Storage will be deleted, and any file entities will be disconnected from items and deleted. (optional) (default to False)

try:
    # Delete a storage
    api_instance.delete_storage(storage_id, safe=safe)
except ApiException as e:
    print("Exception when calling StorageApi->delete_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **safe** | **bool**| - &#x60;true&#x60; - Storage will only be deleted if there are no files connected to items on the storage.  - &#x60;false&#x60; (default) - Storage will be deleted, and any file entities will be disconnected from items and deleted. | [optional] [default to False]

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

# **delete_storage_metadata**
> delete_storage_metadata(storage_id)

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Delete all key-value pairs
    api_instance.delete_storage_metadata(storage_id)
except ApiException as e:
    print("Exception when calling StorageApi->delete_storage_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_storage_metadata_key**
> delete_storage_metadata_key(storage_id, keypath)

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_storage_metadata_key(storage_id, keypath)
except ApiException as e:
    print("Exception when calling StorageApi->delete_storage_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
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

# **evacuate_storage**
> evacuate_storage(storage_id)

Evacuate a storage

Trigger evacuation of a storage.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Evacuate a storage
    api_instance.evacuate_storage(storage_id)
except ApiException as e:
    print("Exception when calling StorageApi->evacuate_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_storage**
> StorageType get_storage(storage_id)

Retrieve a storage

Retrieves a specific storage.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Retrieve a storage
    api_response = api_instance.get_storage(storage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 

### Return type

[**StorageType**](StorageType.md)

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

# **get_storage_free_space**
> str get_storage_free_space(storage_id)

Retrieve the amount of free space on a storage

Retrieves the amount of free space on the storage.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Retrieve the amount of free space on a storage
    api_response = api_instance.get_storage_free_space(storage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_storage_free_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 

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
**0** | Amount of free space as decimal number, between 0 and 100, inclusive |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_import_document**
> StorageImportType get_storage_import_document(storage_id)

Export a storage definition

Creates a *StorageImportDocument* that describes every file on the storage. This should be saved to a file which can later be used to import the storage definition.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Export a storage definition
    api_response = api_instance.get_storage_import_document(storage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_storage_import_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 

### Return type

[**StorageImportType**](StorageImportType.md)

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

# **get_storage_metadata**
> SimpleMetadataType get_storage_metadata(storage_id)

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_storage_metadata(storage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_storage_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 

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

# **get_storage_metadata_key**
> str get_storage_metadata_key(storage_id, keypath)

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_storage_metadata_key(storage_id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_storage_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
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

# **get_storage_status**
> str get_storage_status(storage_id)

Retrieve the storage status

Retrieves the status of the storage.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Retrieve the storage status
    api_response = api_instance.get_storage_status(storage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_storage_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 

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
**0** | Status string |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storages**
> StorageListType get_storages(usedbytes=usedbytes, freebytes=freebytes, files=files, freeamount=freeamount, storagegroup=storagegroup, url=url, status=status, size=size)

List all storages

Retrieves the storages that have been configured.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
usedbytes = '-' # str | Range of bytes, in format *s1*`-`*s2*.  Returns storages with used space that is in that range.  Either number can be omitted to not specify lower/upper limit.  Size units can be used. (optional) (default to '-')
freebytes = '-' # str | Range of bytes, in format *s1*`-`*s2*.  Returns storages with free space that is in that range.  Either number can be omitted to not specify lower/upper limit.  Size units can be used. (optional) (default to '-')
files = '-' # str | Range of files as integers, in format *s1*`-`*s2*.  Returns storages with number of files that is in that range.  Either number can be omitted to not specify lower/upper limit. (optional) (default to '-')
freeamount = '-' # str | Range of percent as integers, in format *s1*`-`*s2*.  Returns storages with used space that is in that range.  Either number can be omitted to not specify lower/upper limit. (optional) (default to '-')
storagegroup = ['storagegroup_example'] # list[str] | List of storage groups.   - *storage-group* - Returned storage is member of specified storage group.  - `-`*storage-group* - Returned storage is not member of specified storage group.  Default is to return all storages. (optional)
url = 'url_example' # str | Returns storages with a method matching this URL.  May include wildcards `*` and `?`. (optional)
status = ['status_example'] # list[str] | List of storage status.   - *status* - Returned storage has this status.  - `-`*status* - Returned storage does not have this status.  Default is to return all storages. (optional)
size = '-' # str | Range of bytes, in format *s1*`-`*s2*.  Returns storages with nominal size that is in that range.  Either number can be omitted to not specify lower/upper limit.  Size units can be used. (optional) (default to '-')

try:
    # List all storages
    api_response = api_instance.get_storages(usedbytes=usedbytes, freebytes=freebytes, files=files, freeamount=freeamount, storagegroup=storagegroup, url=url, status=status, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_storages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usedbytes** | **str**| Range of bytes, in format *s1*&#x60;-&#x60;*s2*.  Returns storages with used space that is in that range.  Either number can be omitted to not specify lower/upper limit.  Size units can be used. | [optional] [default to &#39;-&#39;]
 **freebytes** | **str**| Range of bytes, in format *s1*&#x60;-&#x60;*s2*.  Returns storages with free space that is in that range.  Either number can be omitted to not specify lower/upper limit.  Size units can be used. | [optional] [default to &#39;-&#39;]
 **files** | **str**| Range of files as integers, in format *s1*&#x60;-&#x60;*s2*.  Returns storages with number of files that is in that range.  Either number can be omitted to not specify lower/upper limit. | [optional] [default to &#39;-&#39;]
 **freeamount** | **str**| Range of percent as integers, in format *s1*&#x60;-&#x60;*s2*.  Returns storages with used space that is in that range.  Either number can be omitted to not specify lower/upper limit. | [optional] [default to &#39;-&#39;]
 **storagegroup** | [**list[str]**](str.md)| List of storage groups.   - *storage-group* - Returned storage is member of specified storage group.  - &#x60;-&#x60;*storage-group* - Returned storage is not member of specified storage group.  Default is to return all storages. | [optional] 
 **url** | **str**| Returns storages with a method matching this URL.  May include wildcards &#x60;*&#x60; and &#x60;?&#x60;. | [optional] 
 **status** | [**list[str]**](str.md)| List of storage status.   - *status* - Returned storage has this status.  - &#x60;-&#x60;*status* - Returned storage does not have this status.  Default is to return all storages. | [optional] 
 **size** | **str**| Range of bytes, in format *s1*&#x60;-&#x60;*s2*.  Returns storages with nominal size that is in that range.  Either number can be omitted to not specify lower/upper limit.  Size units can be used. | [optional] [default to &#39;-&#39;]

### Return type

[**StorageListType**](StorageListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of storage ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rescan_storage**
> rescan_storage(storage_id)

Rescan a storage

Triggers a rescan of a single storage.  The `scanInterval` property can be used to control how often (in seconds) a storage is scanned. Default is `60`. By setting `scanInterval` to `-1` storage scans will be disabled. By calling `/rescan`, the system is forced to rescan a storage without delay.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Rescan a storage
    api_instance.rescan_storage(storage_id)
except ApiException as e:
    print("Exception when calling StorageApi->rescan_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **update_storage**
> StorageType update_storage(storage_id, storage_type)

Update a storage

Updates an existing storage.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
storage_type = vidispine.StorageType() # StorageType | 

try:
    # Update a storage
    api_response = api_instance.update_storage(storage_id, storage_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->update_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **storage_type** | [**StorageType**](StorageType.md)|  | 

### Return type

[**StorageType**](StorageType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Storage id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_metadata**
> update_storage_metadata(storage_id, simple_metadata_type)

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_storage_metadata(storage_id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling StorageApi->update_storage_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
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

# **update_storage_metadata_key**
> update_storage_metadata_key(storage_id, keypath, body)

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_storage_metadata_key(storage_id, keypath, body)
except ApiException as e:
    print("Exception when calling StorageApi->update_storage_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
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

# **update_storage_type**
> update_storage_type(storage_id, type)

Update the storage type

Sets the type of the storage.

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
api_instance = vidispine.StorageApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
type = 'type_example' # str | The type.

try:
    # Update the storage type
    api_instance.update_storage_type(storage_id, type)
except ApiException as e:
    print("Exception when calling StorageApi->update_storage_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **type** | **str**| The type. | 

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

