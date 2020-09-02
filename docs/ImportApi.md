# vidispine.ImportApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adopt_file**](ImportApi.md#adopt_file) | **POST** /import/placeholder/{item-id}/{component-type}/adopt/{file-id} | Adopt stand-alone files
[**create_placeholder**](ImportApi.md#create_placeholder) | **POST** /import/placeholder | Create a placeholder item
[**create_placeholder_import_passkey**](ImportApi.md#create_placeholder_import_passkey) | **POST** /import/placeholder/{item-id}/raw-passkey | Create passkey for placeholder item
[**delete_default_access_control_for_group**](ImportApi.md#delete_default_access_control_for_group) | **DELETE** /import/access/group/{group-name} | Remove a group from the default access control list
[**get_default_access_controls**](ImportApi.md#get_default_access_controls) | **GET** /import/access | List the default access controls for the current user
[**get_import_storage**](ImportApi.md#get_import_storage) | **GET** /import/storage | Find destination storage
[**get_importables**](ImportApi.md#get_importables) | **GET** /storage/importable | List all files that can be imported
[**get_storage_importables**](ImportApi.md#get_storage_importables) | **GET** /storage/{storage-id}/importable | List all files that can be imported
[**import_file**](ImportApi.md#import_file) | **POST** /file/{file-id}/import | Import a file
[**import_file_asset_map**](ImportApi.md#import_file_asset_map) | **POST** /file/{file-id}/import/assetmap | Import an IMF package
[**import_imf_package**](ImportApi.md#import_imf_package) | **POST** /import/imp | Import an IMF package using a URI
[**import_item**](ImportApi.md#import_item) | **POST** /import | Import using a URI
[**import_item_raw**](ImportApi.md#import_item_raw) | **POST** /import/raw | Import using the request body
[**import_item_raw_passkey**](ImportApi.md#import_item_raw_passkey) | **POST** /import/raw-passkey | Import using a passkey
[**import_placeholder_bulk**](ImportApi.md#import_placeholder_bulk) | **POST** /import/placeholder/{item-id} | Import to a placeholder item in bulk
[**import_placeholder_raw**](ImportApi.md#import_placeholder_raw) | **POST** /import/placeholder/{item-id}/{component-type}/raw | Import to a placeholder item using the request body
[**import_project**](ImportApi.md#import_project) | **POST** /import/project | Import a project
[**import_project_sequence**](ImportApi.md#import_project_sequence) | **POST** /import/project/sequence | Import a sequence
[**import_sidecar**](ImportApi.md#import_sidecar) | **POST** /import/sidecar/{item-id} | Import a sidecar file
[**import_sidecar_raw**](ImportApi.md#import_sidecar_raw) | **POST** /import/sidecar/{item-id}/raw | Import a sidecar file
[**import_storage_definition**](ImportApi.md#import_storage_definition) | **POST** /storage/import | Import a storage definition
[**import_to_placeholder**](ImportApi.md#import_to_placeholder) | **POST** /import/placeholder/{item-id}/{component-type} | Import to a placeholder item
[**update_default_access_control_for_group**](ImportApi.md#update_default_access_control_for_group) | **PUT** /import/access/group/{group-name} | Add a group to the default access control list


# **adopt_file**
> adopt_file(item_id, component_type, file_id, index=index, shape_id=shape_id)

Adopt stand-alone files

Adopt the file as a component in a placeholder item. The value of component-type is one of: `container, audio, video, binary`

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
component_type = 'component_type_example' # str | The component type.
file_id = 'file_id_example' # str | The file id.
index = 56 # int | Index (order) of the component. (optional)
shape_id = 'shape_id_example' # str | Shape id for which shape to receive the content. (optional)

try:
    # Adopt stand-alone files
    api_instance.adopt_file(item_id, component_type, file_id, index=index, shape_id=shape_id)
except ApiException as e:
    print("Exception when calling ImportApi->adopt_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **component_type** | **str**| The component type. | 
 **file_id** | **str**| The file id. | 
 **index** | **int**| Index (order) of the component. | [optional] 
 **shape_id** | **str**| Shape id for which shape to receive the content. | [optional] 

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

# **create_placeholder**
> ItemType create_placeholder(metadata_type, binary=binary, audio=audio, type=type, settings=settings, container=container, video=video, frame_duration=frame_duration, import_tag=import_tag)

Create a placeholder item

Creates an empty item and a shape with components matching the given parameters.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
metadata_type = vidispine.MetadataType() # MetadataType | <em>MetadataDocument</em>, initial metadata that is given to the imported item.
binary = 56 # int | The number of files that contain binary components. (optional)
audio = 56 # int | The number of files that contain audio components. (optional)
type = 'type_example' # str | - `image-sequence`- Image sequence.  - `dpx` - DPX sequence.  Deprecated since version 4. 6: Import image sequences using URIs with file fragments instead. (optional)
settings = 'settings_example' # str | Pre-configured import settings. (optional)
container = 56 # int | The number of files that contain container components. (optional)
video = 56 # int | The number of files that contain video components. (optional)
frame_duration = 'frame_duration_example' # str | duration for each image in the sequence. (optional)
import_tag = ["original"] # list[str] | A list of shape tags that the created shape will be associated with. (optional) (default to ["original"])

try:
    # Create a placeholder item
    api_response = api_instance.create_placeholder(metadata_type, binary=binary, audio=audio, type=type, settings=settings, container=container, video=video, frame_duration=frame_duration, import_tag=import_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->create_placeholder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_type** | [**MetadataType**](MetadataType.md)| &lt;em&gt;MetadataDocument&lt;/em&gt;, initial metadata that is given to the imported item. | 
 **binary** | **int**| The number of files that contain binary components. | [optional] 
 **audio** | **int**| The number of files that contain audio components. | [optional] 
 **type** | **str**| - &#x60;image-sequence&#x60;- Image sequence.  - &#x60;dpx&#x60; - DPX sequence.  Deprecated since version 4. 6: Import image sequences using URIs with file fragments instead. | [optional] 
 **settings** | **str**| Pre-configured import settings. | [optional] 
 **container** | **int**| The number of files that contain container components. | [optional] 
 **video** | **int**| The number of files that contain video components. | [optional] 
 **frame_duration** | **str**| duration for each image in the sequence. | [optional] 
 **import_tag** | [**list[str]**](str.md)| A list of shape tags that the created shape will be associated with. | [optional] [default to [&quot;original&quot;]]

### Return type

[**ItemType**](ItemType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The id of the item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_placeholder_import_passkey**
> URIListType create_placeholder_import_passkey(item_id, shape_id=shape_id)

Create passkey for placeholder item

Creates a new passkey for a specific placeholder item, that can be used to perform imports to this item without requiring authentication.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | Shape id for which shape to receive the content. (optional)

try:
    # Create passkey for placeholder item
    api_response = api_instance.create_placeholder_import_passkey(item_id, shape_id=shape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->create_placeholder_import_passkey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| Shape id for which shape to receive the content. | [optional] 

### Return type

[**URIListType**](URIListType.md)

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

# **delete_default_access_control_for_group**
> delete_default_access_control_for_group(group_name)

Remove a group from the default access control list

Removes the specified group from the default access control list.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Remove a group from the default access control list
    api_instance.delete_default_access_control_for_group(group_name)
except ApiException as e:
    print("Exception when calling ImportApi->delete_default_access_control_for_group: %s\n" % e)
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

# **get_default_access_controls**
> ImportAccessControlListType get_default_access_controls()

List the default access controls for the current user

Lists the access control list that will be applied on imported items.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))

try:
    # List the default access controls for the current user
    api_response = api_instance.get_default_access_controls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->get_default_access_controls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ImportAccessControlListType**](ImportAccessControlListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An &lt;em&gt;ImportAccessControlListDocument&lt;/em&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_storage**
> StorageType get_import_storage(tag=tag, jobmetadata=jobmetadata, item=item)

Find destination storage

Find where imported content would be stored according to current storage rules.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
tag = 'tag_example' # str | Shape tag (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
item = 'item_example' # str | Item id (optional)

try:
    # Find destination storage
    api_response = api_instance.get_import_storage(tag=tag, jobmetadata=jobmetadata, item=item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->get_import_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Shape tag | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **item** | **str**| Item id | [optional] 

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

# **get_importables**
> ImportableFileListType get_importables(storage_type=storage_type, first=first, prefix_first=prefix_first, number=number, storage_group=storage_group, ignorecase=ignorecase, prefix=prefix, exclude_queued=exclude_queued, filter=filter, state=state, algorithm=algorithm, method_type=method_type, prefix_number=prefix_number, method_metadata=method_metadata, storage=storage, scheme=scheme, recursive=recursive, cursor=cursor, auto=auto, id=id, count=count, sort=sort, hash=hash, wildcard=wildcard, path=path)

List all files that can be imported

Retrieves a list of files, together with any found metadata, for files that do not belong to any component.  Same query parameters as for `GET {storage-resource}/file`.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
first = 0 # int | From total list of files, start return list from specified number. (optional) (default to 0)
prefix_first = 0 # int | From total list of prefixes, start return list from specified number.  Note: this parameter has no effect if Elasticsearch is the search backend. (optional) (default to 0)
number = 10 # int | Return a maximum of specified number of files. (optional) (default to 10)
storage_group = 'storage_group_example' # str | Storage group id.  Return only files from storages specified in the storage group (optional)
ignorecase = True # bool | - `true` - Search file path case insensitively - `false` - Search file path case sensitively (optional)
prefix = True # bool | - `true` - Also include file prefixes that matches the criteria - `false` (default) - Do not include file prefixes (optional)
exclude_queued = True # bool | - `true` (default) - Exclude the files that are queued for import - `false` - Do not exclude the files that are queued for import (optional) (default to True)
filter = 'all' # str | - `all` (default) - Return all files - `item` Only return files associated with an item.  - `noitem` Only return files not associated with any item. (optional) (default to 'all')
state = ['state_example'] # list[str] | Filter results by file state.  Can be used multiple times to select several states. (optional)
algorithm = 'algorithm_example' # str | Hash algorithm.  Search for hash values used by specified algorithm (optional)
method_type = 'method_type_example' # str | Return URIs from storage methods with a particular type.  By default, return URLs with empty `methodType`. (optional)
prefix_number = 10 # int | Return a maximum of specified number of prefixes. (optional) (default to 10)
method_metadata = ['method_metadata_example'] # list[str] | metadata used with storage method. (optional)
storage = ['storage_example'] # list[str] | List of storage ids.  Return only files from specific storages.  Same as `storage-id` in URL, but can be specified multiple times (optional)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
recursive = True # bool | - `true` (default) - Return all files in tree.  - `false` - Return only files directly under specified path. (optional) (default to True)
cursor = 'cursor_example' # str | New in version 4. 16.   - `*` - The initial cursor.  - `string-from-search` - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When `cursor` is used, The value of `first` will be ignored.  Only metadata searches in the `generic` interval supports `cursor`. (optional)
auto = False # bool | - `true` - Return files that will be automatically imported due to auto-import rules.  - `false` (default) - Do not return files that will be automatically imported. (optional) (default to False)
id = ['id_example'] # list[str] | If multiple `id` query parameters are specified only those files are returned.  If no ids are specified, all files are returned. (optional)
count = True # bool | - `true` (default) - Return total number of hits in result - `false` - Do not return total number of hits in result, in order to produce results faster (optional) (default to True)
sort = ['sort_example'] # list[str] | Comma-separated list.   - `fileId` [ `asc` (default) | `desc` ] (default) - Order results by file id.  - `size` [ `asc` (default) | `desc` ] - Order results by file size (bytes).  - `state` [ `asc` (default) | `desc` ] - Order results by file state.  - `timestamp` [ `asc` (default) | `desc` ] - Order results by file timestamp.  - `filename` [ `asc` (default) | `desc` ] - Order results by filename.  - `extension` [ `asc` (default) | `desc` ] - Order results by file extension. (optional)
hash = ['hash_example'] # list[str] | List of hash values.  Only return files with specific hash value. (optional)
wildcard = False # bool | - `true` - Allow use of wildcards in path.  - `false` (default) - No wildcard handling of path. (optional) (default to False)
path = '/' # str | - *path* - Return files under this sub-path to storage.  - `/` (default) - Return all files. (optional) (default to '/')

try:
    # List all files that can be imported
    api_response = api_instance.get_importables(storage_type=storage_type, first=first, prefix_first=prefix_first, number=number, storage_group=storage_group, ignorecase=ignorecase, prefix=prefix, exclude_queued=exclude_queued, filter=filter, state=state, algorithm=algorithm, method_type=method_type, prefix_number=prefix_number, method_metadata=method_metadata, storage=storage, scheme=scheme, recursive=recursive, cursor=cursor, auto=auto, id=id, count=count, sort=sort, hash=hash, wildcard=wildcard, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->get_importables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **first** | **int**| From total list of files, start return list from specified number. | [optional] [default to 0]
 **prefix_first** | **int**| From total list of prefixes, start return list from specified number.  Note: this parameter has no effect if Elasticsearch is the search backend. | [optional] [default to 0]
 **number** | **int**| Return a maximum of specified number of files. | [optional] [default to 10]
 **storage_group** | **str**| Storage group id.  Return only files from storages specified in the storage group | [optional] 
 **ignorecase** | **bool**| - &#x60;true&#x60; - Search file path case insensitively - &#x60;false&#x60; - Search file path case sensitively | [optional] 
 **prefix** | **bool**| - &#x60;true&#x60; - Also include file prefixes that matches the criteria - &#x60;false&#x60; (default) - Do not include file prefixes | [optional] 
 **exclude_queued** | **bool**| - &#x60;true&#x60; (default) - Exclude the files that are queued for import - &#x60;false&#x60; - Do not exclude the files that are queued for import | [optional] [default to True]
 **filter** | **str**| - &#x60;all&#x60; (default) - Return all files - &#x60;item&#x60; Only return files associated with an item.  - &#x60;noitem&#x60; Only return files not associated with any item. | [optional] [default to &#39;all&#39;]
 **state** | [**list[str]**](str.md)| Filter results by file state.  Can be used multiple times to select several states. | [optional] 
 **algorithm** | **str**| Hash algorithm.  Search for hash values used by specified algorithm | [optional] 
 **method_type** | **str**| Return URIs from storage methods with a particular type.  By default, return URLs with empty &#x60;methodType&#x60;. | [optional] 
 **prefix_number** | **int**| Return a maximum of specified number of prefixes. | [optional] [default to 10]
 **method_metadata** | [**list[str]**](str.md)| metadata used with storage method. | [optional] 
 **storage** | [**list[str]**](str.md)| List of storage ids.  Return only files from specific storages.  Same as &#x60;storage-id&#x60; in URL, but can be specified multiple times | [optional] 
 **scheme** | **str**| URI scheme to return. | [optional] 
 **recursive** | **bool**| - &#x60;true&#x60; (default) - Return all files in tree.  - &#x60;false&#x60; - Return only files directly under specified path. | [optional] [default to True]
 **cursor** | **str**| New in version 4. 16.   - &#x60;*&#x60; - The initial cursor.  - &#x60;string-from-search&#x60; - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When &#x60;cursor&#x60; is used, The value of &#x60;first&#x60; will be ignored.  Only metadata searches in the &#x60;generic&#x60; interval supports &#x60;cursor&#x60;. | [optional] 
 **auto** | **bool**| - &#x60;true&#x60; - Return files that will be automatically imported due to auto-import rules.  - &#x60;false&#x60; (default) - Do not return files that will be automatically imported. | [optional] [default to False]
 **id** | [**list[str]**](str.md)| If multiple &#x60;id&#x60; query parameters are specified only those files are returned.  If no ids are specified, all files are returned. | [optional] 
 **count** | **bool**| - &#x60;true&#x60; (default) - Return total number of hits in result - &#x60;false&#x60; - Do not return total number of hits in result, in order to produce results faster | [optional] [default to True]
 **sort** | [**list[str]**](str.md)| Comma-separated list.   - &#x60;fileId&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] (default) - Order results by file id.  - &#x60;size&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file size (bytes).  - &#x60;state&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file state.  - &#x60;timestamp&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file timestamp.  - &#x60;filename&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by filename.  - &#x60;extension&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file extension. | [optional] 
 **hash** | [**list[str]**](str.md)| List of hash values.  Only return files with specific hash value. | [optional] 
 **wildcard** | **bool**| - &#x60;true&#x60; - Allow use of wildcards in path.  - &#x60;false&#x60; (default) - No wildcard handling of path. | [optional] [default to False]
 **path** | **str**| - *path* - Return files under this sub-path to storage.  - &#x60;/&#x60; (default) - Return all files. | [optional] [default to &#39;/&#39;]

### Return type

[**ImportableFileListType**](ImportableFileListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An &lt;em&gt;ImportableFileListDocument&lt;/em&gt; describing the job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_importables**
> ImportableFileListType get_storage_importables(storage_id, storage_type=storage_type, first=first, prefix_first=prefix_first, number=number, storage_group=storage_group, ignorecase=ignorecase, prefix=prefix, exclude_queued=exclude_queued, filter=filter, state=state, algorithm=algorithm, method_type=method_type, prefix_number=prefix_number, method_metadata=method_metadata, storage=storage, scheme=scheme, recursive=recursive, cursor=cursor, auto=auto, id=id, count=count, sort=sort, hash=hash, wildcard=wildcard, path=path)

List all files that can be imported

Retrieves a list of files, together with any found metadata, for files that do not belong to any component.  Same query parameters as for `GET {storage-resource}/file`.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
first = 0 # int | From total list of files, start return list from specified number. (optional) (default to 0)
prefix_first = 0 # int | From total list of prefixes, start return list from specified number.  Note: this parameter has no effect if Elasticsearch is the search backend. (optional) (default to 0)
number = 10 # int | Return a maximum of specified number of files. (optional) (default to 10)
storage_group = 'storage_group_example' # str | Storage group id.  Return only files from storages specified in the storage group (optional)
ignorecase = True # bool | - `true` - Search file path case insensitively - `false` - Search file path case sensitively (optional)
prefix = True # bool | - `true` - Also include file prefixes that matches the criteria - `false` (default) - Do not include file prefixes (optional)
exclude_queued = True # bool | - `true` (default) - Exclude the files that are queued for import - `false` - Do not exclude the files that are queued for import (optional) (default to True)
filter = 'all' # str | - `all` (default) - Return all files - `item` Only return files associated with an item.  - `noitem` Only return files not associated with any item. (optional) (default to 'all')
state = ['state_example'] # list[str] | Filter results by file state.  Can be used multiple times to select several states. (optional)
algorithm = 'algorithm_example' # str | Hash algorithm.  Search for hash values used by specified algorithm (optional)
method_type = 'method_type_example' # str | Return URIs from storage methods with a particular type.  By default, return URLs with empty `methodType`. (optional)
prefix_number = 10 # int | Return a maximum of specified number of prefixes. (optional) (default to 10)
method_metadata = ['method_metadata_example'] # list[str] | metadata used with storage method. (optional)
storage = ['storage_example'] # list[str] | List of storage ids.  Return only files from specific storages.  Same as `storage-id` in URL, but can be specified multiple times (optional)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
recursive = True # bool | - `true` (default) - Return all files in tree.  - `false` - Return only files directly under specified path. (optional) (default to True)
cursor = 'cursor_example' # str | New in version 4. 16.   - `*` - The initial cursor.  - `string-from-search` - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When `cursor` is used, The value of `first` will be ignored.  Only metadata searches in the `generic` interval supports `cursor`. (optional)
auto = False # bool | - `true` - Return files that will be automatically imported due to auto-import rules.  - `false` (default) - Do not return files that will be automatically imported. (optional) (default to False)
id = ['id_example'] # list[str] | If multiple `id` query parameters are specified only those files are returned.  If no ids are specified, all files are returned. (optional)
count = True # bool | - `true` (default) - Return total number of hits in result - `false` - Do not return total number of hits in result, in order to produce results faster (optional) (default to True)
sort = ['sort_example'] # list[str] | Comma-separated list.   - `fileId` [ `asc` (default) | `desc` ] (default) - Order results by file id.  - `size` [ `asc` (default) | `desc` ] - Order results by file size (bytes).  - `state` [ `asc` (default) | `desc` ] - Order results by file state.  - `timestamp` [ `asc` (default) | `desc` ] - Order results by file timestamp.  - `filename` [ `asc` (default) | `desc` ] - Order results by filename.  - `extension` [ `asc` (default) | `desc` ] - Order results by file extension. (optional)
hash = ['hash_example'] # list[str] | List of hash values.  Only return files with specific hash value. (optional)
wildcard = False # bool | - `true` - Allow use of wildcards in path.  - `false` (default) - No wildcard handling of path. (optional) (default to False)
path = '/' # str | - *path* - Return files under this sub-path to storage.  - `/` (default) - Return all files. (optional) (default to '/')

try:
    # List all files that can be imported
    api_response = api_instance.get_storage_importables(storage_id, storage_type=storage_type, first=first, prefix_first=prefix_first, number=number, storage_group=storage_group, ignorecase=ignorecase, prefix=prefix, exclude_queued=exclude_queued, filter=filter, state=state, algorithm=algorithm, method_type=method_type, prefix_number=prefix_number, method_metadata=method_metadata, storage=storage, scheme=scheme, recursive=recursive, cursor=cursor, auto=auto, id=id, count=count, sort=sort, hash=hash, wildcard=wildcard, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->get_storage_importables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **first** | **int**| From total list of files, start return list from specified number. | [optional] [default to 0]
 **prefix_first** | **int**| From total list of prefixes, start return list from specified number.  Note: this parameter has no effect if Elasticsearch is the search backend. | [optional] [default to 0]
 **number** | **int**| Return a maximum of specified number of files. | [optional] [default to 10]
 **storage_group** | **str**| Storage group id.  Return only files from storages specified in the storage group | [optional] 
 **ignorecase** | **bool**| - &#x60;true&#x60; - Search file path case insensitively - &#x60;false&#x60; - Search file path case sensitively | [optional] 
 **prefix** | **bool**| - &#x60;true&#x60; - Also include file prefixes that matches the criteria - &#x60;false&#x60; (default) - Do not include file prefixes | [optional] 
 **exclude_queued** | **bool**| - &#x60;true&#x60; (default) - Exclude the files that are queued for import - &#x60;false&#x60; - Do not exclude the files that are queued for import | [optional] [default to True]
 **filter** | **str**| - &#x60;all&#x60; (default) - Return all files - &#x60;item&#x60; Only return files associated with an item.  - &#x60;noitem&#x60; Only return files not associated with any item. | [optional] [default to &#39;all&#39;]
 **state** | [**list[str]**](str.md)| Filter results by file state.  Can be used multiple times to select several states. | [optional] 
 **algorithm** | **str**| Hash algorithm.  Search for hash values used by specified algorithm | [optional] 
 **method_type** | **str**| Return URIs from storage methods with a particular type.  By default, return URLs with empty &#x60;methodType&#x60;. | [optional] 
 **prefix_number** | **int**| Return a maximum of specified number of prefixes. | [optional] [default to 10]
 **method_metadata** | [**list[str]**](str.md)| metadata used with storage method. | [optional] 
 **storage** | [**list[str]**](str.md)| List of storage ids.  Return only files from specific storages.  Same as &#x60;storage-id&#x60; in URL, but can be specified multiple times | [optional] 
 **scheme** | **str**| URI scheme to return. | [optional] 
 **recursive** | **bool**| - &#x60;true&#x60; (default) - Return all files in tree.  - &#x60;false&#x60; - Return only files directly under specified path. | [optional] [default to True]
 **cursor** | **str**| New in version 4. 16.   - &#x60;*&#x60; - The initial cursor.  - &#x60;string-from-search&#x60; - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When &#x60;cursor&#x60; is used, The value of &#x60;first&#x60; will be ignored.  Only metadata searches in the &#x60;generic&#x60; interval supports &#x60;cursor&#x60;. | [optional] 
 **auto** | **bool**| - &#x60;true&#x60; - Return files that will be automatically imported due to auto-import rules.  - &#x60;false&#x60; (default) - Do not return files that will be automatically imported. | [optional] [default to False]
 **id** | [**list[str]**](str.md)| If multiple &#x60;id&#x60; query parameters are specified only those files are returned.  If no ids are specified, all files are returned. | [optional] 
 **count** | **bool**| - &#x60;true&#x60; (default) - Return total number of hits in result - &#x60;false&#x60; - Do not return total number of hits in result, in order to produce results faster | [optional] [default to True]
 **sort** | [**list[str]**](str.md)| Comma-separated list.   - &#x60;fileId&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] (default) - Order results by file id.  - &#x60;size&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file size (bytes).  - &#x60;state&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file state.  - &#x60;timestamp&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file timestamp.  - &#x60;filename&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by filename.  - &#x60;extension&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file extension. | [optional] 
 **hash** | [**list[str]**](str.md)| List of hash values.  Only return files with specific hash value. | [optional] 
 **wildcard** | **bool**| - &#x60;true&#x60; - Allow use of wildcards in path.  - &#x60;false&#x60; (default) - No wildcard handling of path. | [optional] [default to False]
 **path** | **str**| - *path* - Return files under this sub-path to storage.  - &#x60;/&#x60; (default) - Return all files. | [optional] [default to &#39;/&#39;]

### Return type

[**ImportableFileListType**](ImportableFileListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An &lt;em&gt;ImportableFileListDocument&lt;/em&gt; describing the job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_file**
> JobType import_file(file_id, metadata_type, resource_id=resource_id, jobmetadata=jobmetadata, notification_data=notification_data, allow_reimport=allow_reimport, tag=tag, no_transcode=no_transcode, thumbnail_service=thumbnail_service, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, import_tag=import_tag, settings=settings, create_thumbnails=create_thumbnails, create_posters=create_posters, override_fast_start=override_fast_start, id=id, filename=filename, priority=priority, original=original)

Import a file

Starts a an import job that will import the specified file. Only files that do not belong to any components can be imported.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
metadata_type = vidispine.MetadataType() # MetadataType | <em>MetadataDocument</em>, initial metadata that is given to the imported item.
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
allow_reimport = True # bool | - `true` - Import the file to this shape even if the file is already importing or is already part of another item.  - `false` (default) Reject the request if the file with the given id has already been imported or is currently importing. (optional)
tag = ['tag_example'] # list[str] | A list of shape tags to use for transcoding. (optional)
no_transcode = False # bool | - `true` - Will disable transcoding even if the `tags` parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - `false` (default) - Normal transcode. (optional) (default to False)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
import_tag = ["original"] # list[str] | A list of shape tags that the created shape will be associated with. (optional) (default to ["original"])
settings = 'settings_example' # str | Pre-configured import settings. (optional)
create_thumbnails = True # bool | - `true` (default) - Generate thumbnails as per defined by shape tag.  - `false` - Disable thumbnail generation. (optional) (default to True)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)
id = 'id_example' # str | Comma-delimited list of external ids to assign to the item. (optional)
filename = 'filename_example' # str | The original filename of the file. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)

try:
    # Import a file
    api_response = api_instance.import_file(file_id, metadata_type, resource_id=resource_id, jobmetadata=jobmetadata, notification_data=notification_data, allow_reimport=allow_reimport, tag=tag, no_transcode=no_transcode, thumbnail_service=thumbnail_service, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, import_tag=import_tag, settings=settings, create_thumbnails=create_thumbnails, create_posters=create_posters, override_fast_start=override_fast_start, id=id, filename=filename, priority=priority, original=original)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
 **metadata_type** | [**MetadataType**](MetadataType.md)| &lt;em&gt;MetadataDocument&lt;/em&gt;, initial metadata that is given to the imported item. | 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **allow_reimport** | **bool**| - &#x60;true&#x60; - Import the file to this shape even if the file is already importing or is already part of another item.  - &#x60;false&#x60; (default) Reject the request if the file with the given id has already been imported or is currently importing. | [optional] 
 **tag** | [**list[str]**](str.md)| A list of shape tags to use for transcoding. | [optional] 
 **no_transcode** | **bool**| - &#x60;true&#x60; - Will disable transcoding even if the &#x60;tags&#x60; parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - &#x60;false&#x60; (default) - Normal transcode. | [optional] [default to False]
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **import_tag** | [**list[str]**](str.md)| A list of shape tags that the created shape will be associated with. | [optional] [default to [&quot;original&quot;]]
 **settings** | **str**| Pre-configured import settings. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; (default) - Generate thumbnails as per defined by shape tag.  - &#x60;false&#x60; - Disable thumbnail generation. | [optional] [default to True]
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]
 **id** | **str**| Comma-delimited list of external ids to assign to the item. | [optional] 
 **filename** | **str**| The original filename of the file. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_file_asset_map**
> JobType import_file_asset_map(file_id, metadata_type, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, no_transcode=no_transcode, tag=tag, require_fast_start=require_fast_start, notification=notification, override_fast_start=override_fast_start, fast_start_length=fast_start_length, import_tag=import_tag, settings=settings, create_thumbnails=create_thumbnails, create_posters=create_posters, allow_reimport=allow_reimport, id=id, priority=priority, original=original)

Import an IMF package

Starts a an import job that will import an `ASSETMAP` file (SMPTE ST 429-9). Files pointed to by the assetmap (DCP/InterOp or SMPTE) has to be stored in the same directory.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
metadata_type = vidispine.MetadataType() # MetadataType | <em>MetadataDocument</em>, initial metadata that is given to the imported item.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
no_transcode = False # bool | - `true` - Will disable transcoding even if the `tags` parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - `false` (default) - Normal transcode. (optional) (default to False)
tag = ['tag_example'] # list[str] | A list of shape tags to use for transcoding. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
import_tag = ["original"] # list[str] | A list of shape tags that the created shape will be associated with. (optional) (default to ["original"])
settings = 'settings_example' # str | Pre-configured import settings. (optional)
create_thumbnails = True # bool | - `true` (default) - Generate thumbnails as per defined by shape tag.  - `false` - Disable thumbnail generation. (optional) (default to True)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
allow_reimport = True # bool | - `true` - Import the file to this shape even if the file is already importing or is already part of another item.  - `false` (default) Reject the request if the file with the given id has already been imported or is currently importing. (optional)
id = 'id_example' # str | Comma-delimited list of external ids to assign to the item. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)

try:
    # Import an IMF package
    api_response = api_instance.import_file_asset_map(file_id, metadata_type, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, no_transcode=no_transcode, tag=tag, require_fast_start=require_fast_start, notification=notification, override_fast_start=override_fast_start, fast_start_length=fast_start_length, import_tag=import_tag, settings=settings, create_thumbnails=create_thumbnails, create_posters=create_posters, allow_reimport=allow_reimport, id=id, priority=priority, original=original)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_file_asset_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
 **metadata_type** | [**MetadataType**](MetadataType.md)| &lt;em&gt;MetadataDocument&lt;/em&gt;, initial metadata that is given to the imported item. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **no_transcode** | **bool**| - &#x60;true&#x60; - Will disable transcoding even if the &#x60;tags&#x60; parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - &#x60;false&#x60; (default) - Normal transcode. | [optional] [default to False]
 **tag** | [**list[str]**](str.md)| A list of shape tags to use for transcoding. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **import_tag** | [**list[str]**](str.md)| A list of shape tags that the created shape will be associated with. | [optional] [default to [&quot;original&quot;]]
 **settings** | **str**| Pre-configured import settings. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; (default) - Generate thumbnails as per defined by shape tag.  - &#x60;false&#x60; - Disable thumbnail generation. | [optional] [default to True]
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **allow_reimport** | **bool**| - &#x60;true&#x60; - Import the file to this shape even if the file is already importing or is already part of another item.  - &#x60;false&#x60; (default) Reject the request if the file with the given id has already been imported or is currently importing. | [optional] 
 **id** | **str**| Comma-delimited list of external ids to assign to the item. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_imf_package**
> JobType import_imf_package(uri, metadata_type, no_transcode=no_transcode, no_cp_lreimport=no_cp_lreimport, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, xmpfile=xmpfile, create_posters=create_posters, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, require_fast_start=require_fast_start, growing=growing, tag=tag, original=original, storage_id=storage_id, settings=settings, notification=notification, import_tag=import_tag, sidecar=sidecar, resource_id=resource_id, priority=priority, override_fast_start=override_fast_start)

Import an IMF package using a URI

Starts a job that reads the asset map of an IMP (IMF package), and then imports the IMP. Essence files whose UUID is already managed by Vidispine Server are not copied. For more information about jobs, see /job/job. Note that thumbnails and poster frames are only generated if a transcode takes place.  The **importtag** query parameter either be a list of shapes, or on the format `uuid=tag`. The IMF import job accepts certain special **jobMetadata** parameters:

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
uri = 'uri_example' # str | A URI to the asset map that will be imported.  Tracks referenced by the asset map should be located in the same folder.
metadata_type = vidispine.MetadataType() # MetadataType | <em>MetadataDocument</em>, initial metadata that is given to the imported item.
no_transcode = False # bool | - `true` - Will disable transcoding even if the `tags` parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - `false` (default) - Normal transcode. (optional) (default to False)
no_cp_lreimport = False # bool | If `true`, do not allow reimport of CPL with same id (optional) (default to False)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
create_thumbnails = True # bool | - `true` (default) - Generate thumbnails as per defined by shape tag.  - `false` - Disable thumbnail generation. (optional) (default to True)
xmpfile = 'xmpfile_example' # str | URI to a sidecar XMP metadata file. (optional)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
growing = False # bool | - `true` - Specifies that the input file is still written to, so enables growing file support.  - `false` (default) - No growing file handling of import file. (optional) (default to False)
tag = ['tag_example'] # list[str] | A list of shape tags to use for transcoding. (optional)
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
settings = 'settings_example' # str | Pre-configured import settings. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
import_tag = ["original"] # list[str] | A list of shape tags that the created shape will be associated with. (optional) (default to ["original"])
sidecar = 'sidecar_example' # str | URIs or file ids of any sidecar files to import to the item. (optional)
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)

try:
    # Import an IMF package using a URI
    api_response = api_instance.import_imf_package(uri, metadata_type, no_transcode=no_transcode, no_cp_lreimport=no_cp_lreimport, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, xmpfile=xmpfile, create_posters=create_posters, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, require_fast_start=require_fast_start, growing=growing, tag=tag, original=original, storage_id=storage_id, settings=settings, notification=notification, import_tag=import_tag, sidecar=sidecar, resource_id=resource_id, priority=priority, override_fast_start=override_fast_start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_imf_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| A URI to the asset map that will be imported.  Tracks referenced by the asset map should be located in the same folder. | 
 **metadata_type** | [**MetadataType**](MetadataType.md)| &lt;em&gt;MetadataDocument&lt;/em&gt;, initial metadata that is given to the imported item. | 
 **no_transcode** | **bool**| - &#x60;true&#x60; - Will disable transcoding even if the &#x60;tags&#x60; parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - &#x60;false&#x60; (default) - Normal transcode. | [optional] [default to False]
 **no_cp_lreimport** | **bool**| If &#x60;true&#x60;, do not allow reimport of CPL with same id | [optional] [default to False]
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; (default) - Generate thumbnails as per defined by shape tag.  - &#x60;false&#x60; - Disable thumbnail generation. | [optional] [default to True]
 **xmpfile** | **str**| URI to a sidecar XMP metadata file. | [optional] 
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **growing** | **bool**| - &#x60;true&#x60; - Specifies that the input file is still written to, so enables growing file support.  - &#x60;false&#x60; (default) - No growing file handling of import file. | [optional] [default to False]
 **tag** | [**list[str]**](str.md)| A list of shape tags to use for transcoding. | [optional] 
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **settings** | **str**| Pre-configured import settings. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **import_tag** | [**list[str]**](str.md)| A list of shape tags that the created shape will be associated with. | [optional] [default to [&quot;original&quot;]]
 **sidecar** | **str**| URIs or file ids of any sidecar files to import to the item. | [optional] 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_item**
> JobType import_item(uri, metadata_type, no_transcode=no_transcode, url=url, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, xmpfile=xmpfile, create_posters=create_posters, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, require_fast_start=require_fast_start, growing=growing, tag=tag, resource_id=resource_id, thumbnail_service=thumbnail_service, settings=settings, notification=notification, import_tag=import_tag, sidecar=sidecar, original=original, priority=priority, override_fast_start=override_fast_start)

Import using a URI

Starts a job that imports the file, located at the given URI, and creates an item. Note that thumbnails and poster frames are only generated if a transcode takes place.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
uri = 'uri_example' # str | A URI to the file that will be imported.  Make sure to percent encode the URI.
metadata_type = vidispine.MetadataType() # MetadataType | <em>MetadataDocument</em>, initial metadata that is given to the imported item.
no_transcode = False # bool | - `true` - Will disable transcoding even if the `tags` parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - `false` (default) - Normal transcode. (optional) (default to False)
url = 'url_example' # str | A URL to the file that will be imported.  (Deprecated since 4. 2. ) (optional)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
create_thumbnails = True # bool | - `true` (default) - Generate thumbnails as per defined by shape tag.  - `false` - Disable thumbnail generation. (optional) (default to True)
xmpfile = 'xmpfile_example' # str | URI to a sidecar XMP metadata file. (optional)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
growing = False # bool | - `true` - Specifies that the input file is still written to, so enables growing file support.  - `false` (default) - No growing file handling of import file. (optional) (default to False)
tag = ['tag_example'] # list[str] | A list of shape tags to use for transcoding. (optional)
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
settings = 'settings_example' # str | Pre-configured import settings. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
import_tag = ["original"] # list[str] | A list of shape tags that the created shape will be associated with. (optional) (default to ["original"])
sidecar = 'sidecar_example' # str | URIs or file ids of any sidecar files to import to the item. (optional)
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)

try:
    # Import using a URI
    api_response = api_instance.import_item(uri, metadata_type, no_transcode=no_transcode, url=url, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, xmpfile=xmpfile, create_posters=create_posters, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, require_fast_start=require_fast_start, growing=growing, tag=tag, resource_id=resource_id, thumbnail_service=thumbnail_service, settings=settings, notification=notification, import_tag=import_tag, sidecar=sidecar, original=original, priority=priority, override_fast_start=override_fast_start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| A URI to the file that will be imported.  Make sure to percent encode the URI. | 
 **metadata_type** | [**MetadataType**](MetadataType.md)| &lt;em&gt;MetadataDocument&lt;/em&gt;, initial metadata that is given to the imported item. | 
 **no_transcode** | **bool**| - &#x60;true&#x60; - Will disable transcoding even if the &#x60;tags&#x60; parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - &#x60;false&#x60; (default) - Normal transcode. | [optional] [default to False]
 **url** | **str**| A URL to the file that will be imported.  (Deprecated since 4. 2. ) | [optional] 
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; (default) - Generate thumbnails as per defined by shape tag.  - &#x60;false&#x60; - Disable thumbnail generation. | [optional] [default to True]
 **xmpfile** | **str**| URI to a sidecar XMP metadata file. | [optional] 
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **growing** | **bool**| - &#x60;true&#x60; - Specifies that the input file is still written to, so enables growing file support.  - &#x60;false&#x60; (default) - No growing file handling of import file. | [optional] [default to False]
 **tag** | [**list[str]**](str.md)| A list of shape tags to use for transcoding. | [optional] 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **settings** | **str**| Pre-configured import settings. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **import_tag** | [**list[str]**](str.md)| A list of shape tags that the created shape will be associated with. | [optional] [default to [&quot;original&quot;]]
 **sidecar** | **str**| URIs or file ids of any sidecar files to import to the item. | [optional] 
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_item_raw**
> JobType import_item_raw(body, resource_id=resource_id, jobmetadata=jobmetadata, notification_data=notification_data, transfer_priority=transfer_priority, thumbnail_service=thumbnail_service, storage_id=storage_id, settings=settings, require_fast_start=require_fast_start, ids=ids, fast_start_length=fast_start_length, import_tag=import_tag, priority=priority, tag=tag, create_thumbnails=create_thumbnails, original=original, create_posters=create_posters, override_fast_start=override_fast_start, notification=notification, filename=filename, transfer_id=transfer_id, no_transcode=no_transcode)

Import using the request body

Starts a job that reads the raw data from the request body, generates a file, and imports the file.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
body = '/path/to/file' # file | The raw data.
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
transfer_priority = 56 # int | An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
settings = 'settings_example' # str | Pre-configured import settings. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
ids = ['ids_example'] # list[str] | Comma-separated list of external ids to assign to the item. (optional)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
import_tag = ["original"] # list[str] | A list of shape tags that the created shape will be associated with. (optional) (default to ["original"])
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
tag = ['tag_example'] # list[str] | A list of shape tags to use for transcoding. (optional)
create_thumbnails = True # bool | - `true` (default) - Generate thumbnails as per defined by shape tag.  - `false` - Disable thumbnail generation. (optional) (default to True)
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
filename = 'filename_example' # str | The filename to be stored as original filename (optional)
transfer_id = 'transfer_id_example' # str | An id to assign the transfer to be able to refer to it. (optional)
no_transcode = False # bool | - `true` - Will disable transcoding even if the `tags` parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - `false` (default) - Normal transcode. (optional) (default to False)

try:
    # Import using the request body
    api_response = api_instance.import_item_raw(body, resource_id=resource_id, jobmetadata=jobmetadata, notification_data=notification_data, transfer_priority=transfer_priority, thumbnail_service=thumbnail_service, storage_id=storage_id, settings=settings, require_fast_start=require_fast_start, ids=ids, fast_start_length=fast_start_length, import_tag=import_tag, priority=priority, tag=tag, create_thumbnails=create_thumbnails, original=original, create_posters=create_posters, override_fast_start=override_fast_start, notification=notification, filename=filename, transfer_id=transfer_id, no_transcode=no_transcode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_item_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file**| The raw data. | 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **transfer_priority** | **int**| An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **settings** | **str**| Pre-configured import settings. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **ids** | [**list[str]**](str.md)| Comma-separated list of external ids to assign to the item. | [optional] 
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **import_tag** | [**list[str]**](str.md)| A list of shape tags that the created shape will be associated with. | [optional] [default to [&quot;original&quot;]]
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **tag** | [**list[str]**](str.md)| A list of shape tags to use for transcoding. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; (default) - Generate thumbnails as per defined by shape tag.  - &#x60;false&#x60; - Disable thumbnail generation. | [optional] [default to True]
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **filename** | **str**| The filename to be stored as original filename | [optional] 
 **transfer_id** | **str**| An id to assign the transfer to be able to refer to it. | [optional] 
 **no_transcode** | **bool**| - &#x60;true&#x60; - Will disable transcoding even if the &#x60;tags&#x60; parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - &#x60;false&#x60; (default) - Normal transcode. | [optional] [default to False]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job, or no content if the transfer is not finished. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_item_raw_passkey**
> JobType import_item_raw_passkey(transfer_id, metadata_type, resource_id=resource_id, jobmetadata=jobmetadata, notification_data=notification_data, transfer_priority=transfer_priority, thumbnail_service=thumbnail_service, storage_id=storage_id, settings=settings, require_fast_start=require_fast_start, ids=ids, fast_start_length=fast_start_length, import_tag=import_tag, priority=priority, tag=tag, create_thumbnails=create_thumbnails, original=original, create_posters=create_posters, override_fast_start=override_fast_start, notification=notification, filename=filename, no_transcode=no_transcode)

Import using a passkey

Create a job and generates a passkey that can later be used to import an item without being authenticated.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
transfer_id = 'transfer_id_example' # str | An id to assign the transfer to be able to refer to it.
metadata_type = vidispine.MetadataType() # MetadataType | <em>MetadataDocument</em>, initial metadata that is given to the imported item.
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
transfer_priority = 56 # int | An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
settings = 'settings_example' # str | Pre-configured import settings. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
ids = ['ids_example'] # list[str] | Comma-separated list of external ids to assign to the item. (optional)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
import_tag = ["original"] # list[str] | A list of shape tags that the created shape will be associated with. (optional) (default to ["original"])
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
tag = ['tag_example'] # list[str] | A list of shape tags to use for transcoding. (optional)
create_thumbnails = True # bool | - `true` (default) - Generate thumbnails as per defined by shape tag.  - `false` - Disable thumbnail generation. (optional) (default to True)
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
filename = 'filename_example' # str | The filename to be stored as original filename (optional)
no_transcode = False # bool | - `true` - Will disable transcoding even if the `tags` parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - `false` (default) - Normal transcode. (optional) (default to False)

try:
    # Import using a passkey
    api_response = api_instance.import_item_raw_passkey(transfer_id, metadata_type, resource_id=resource_id, jobmetadata=jobmetadata, notification_data=notification_data, transfer_priority=transfer_priority, thumbnail_service=thumbnail_service, storage_id=storage_id, settings=settings, require_fast_start=require_fast_start, ids=ids, fast_start_length=fast_start_length, import_tag=import_tag, priority=priority, tag=tag, create_thumbnails=create_thumbnails, original=original, create_posters=create_posters, override_fast_start=override_fast_start, notification=notification, filename=filename, no_transcode=no_transcode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_item_raw_passkey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **str**| An id to assign the transfer to be able to refer to it. | 
 **metadata_type** | [**MetadataType**](MetadataType.md)| &lt;em&gt;MetadataDocument&lt;/em&gt;, initial metadata that is given to the imported item. | 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **transfer_priority** | **int**| An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **settings** | **str**| Pre-configured import settings. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **ids** | [**list[str]**](str.md)| Comma-separated list of external ids to assign to the item. | [optional] 
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **import_tag** | [**list[str]**](str.md)| A list of shape tags that the created shape will be associated with. | [optional] [default to [&quot;original&quot;]]
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **tag** | [**list[str]**](str.md)| A list of shape tags to use for transcoding. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; (default) - Generate thumbnails as per defined by shape tag.  - &#x60;false&#x60; - Disable thumbnail generation. | [optional] [default to True]
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **filename** | **str**| The filename to be stored as original filename | [optional] 
 **no_transcode** | **bool**| - &#x60;true&#x60; - Will disable transcoding even if the &#x60;tags&#x60; parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - &#x60;false&#x60; (default) - Normal transcode. | [optional] [default to False]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_placeholder_bulk**
> JobType import_placeholder_bulk(item_id, placeholder_import_request_type, jobmetadata=jobmetadata, notification_data=notification_data, tag=tag, storage_id=storage_id, index=index, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, import_tag=import_tag, settings=settings, original=original, growing=growing, override_fast_start=override_fast_start, resource_id=resource_id, shape_id=shape_id, priority=priority, no_transcode=no_transcode)

Import to a placeholder item in bulk

Imports the files and extracts component data based on what type is specified (container, audio, video, binary). No transcoding will take place until all files have been imported.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
placeholder_import_request_type = vidispine.PlaceholderImportRequestType() # PlaceholderImportRequestType | A <em>PlaceholderImportRequestDocument</em> describing the files to import.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
tag = ['tag_example'] # list[str] | A list of shape tags to use for transcoding. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
index = 56 # int | The component index (track) of new component. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
import_tag = ["original"] # list[str] | A list of shape tags that the created shape will be associated with. (optional) (default to ["original"])
settings = 'settings_example' # str | Pre-configured import settings. (optional)
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)
growing = False # bool | - `true` - Specifies that the input file is still written to, so enables growing file support.  - `false` (default) - No growing file handling of import file. (optional) (default to False)
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)
shape_id = 'shape_id_example' # str | Shape id for which shape to receive the content. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
no_transcode = False # bool | - `true` - Will disable transcoding even if the `tags` parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - `false` (default) - Normal transcode. (optional) (default to False)

try:
    # Import to a placeholder item in bulk
    api_response = api_instance.import_placeholder_bulk(item_id, placeholder_import_request_type, jobmetadata=jobmetadata, notification_data=notification_data, tag=tag, storage_id=storage_id, index=index, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, import_tag=import_tag, settings=settings, original=original, growing=growing, override_fast_start=override_fast_start, resource_id=resource_id, shape_id=shape_id, priority=priority, no_transcode=no_transcode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_placeholder_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **placeholder_import_request_type** | [**PlaceholderImportRequestType**](PlaceholderImportRequestType.md)| A &lt;em&gt;PlaceholderImportRequestDocument&lt;/em&gt; describing the files to import. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **tag** | [**list[str]**](str.md)| A list of shape tags to use for transcoding. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **index** | **int**| The component index (track) of new component. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **import_tag** | [**list[str]**](str.md)| A list of shape tags that the created shape will be associated with. | [optional] [default to [&quot;original&quot;]]
 **settings** | **str**| Pre-configured import settings. | [optional] 
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 
 **growing** | **bool**| - &#x60;true&#x60; - Specifies that the input file is still written to, so enables growing file support.  - &#x60;false&#x60; (default) - No growing file handling of import file. | [optional] [default to False]
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 
 **shape_id** | **str**| Shape id for which shape to receive the content. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **no_transcode** | **bool**| - &#x60;true&#x60; - Will disable transcoding even if the &#x60;tags&#x60; parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - &#x60;false&#x60; (default) - Normal transcode. | [optional] [default to False]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_placeholder_raw**
> JobType import_placeholder_raw(item_id, component_type, body, resource_id=resource_id, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, tag=tag, transfer_priority=transfer_priority, index=index, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, priority=priority, storage_id=storage_id, create_thumbnails=create_thumbnails, create_posters=create_posters, override_fast_start=override_fast_start, original=original, shape_id=shape_id, filename=filename, transfer_id=transfer_id, no_transcode=no_transcode)

Import to a placeholder item using the request body

Imports the file and extracts component data based on what type is specified (container, audio, video, binary). No transcoding will take place until all files have been imported.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
component_type = 'component_type_example' # str | The component type.
body = '/path/to/file' # file | The raw data.
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
tag = ['tag_example'] # list[str] | A list of shape tags to use for transcoding. (optional)
transfer_priority = 56 # int | An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. (optional)
index = 56 # int | Index (order) of the component. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
create_thumbnails = True # bool | - `true` (default) - Generate thumbnails as per defined by shape tag.  - `false` - Disable thumbnail generation. (optional) (default to True)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)
shape_id = 'shape_id_example' # str | Shape id for which shape to receive the content. (optional)
filename = 'filename_example' # str | The filename to be stored as original filename (optional)
transfer_id = 'transfer_id_example' # str | An id to assign the transfer to be able to refer to it. (optional)
no_transcode = False # bool | - `true` - Will disable transcoding even if the `tags` parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - `false` (default) - Normal transcode. (optional) (default to False)

try:
    # Import to a placeholder item using the request body
    api_response = api_instance.import_placeholder_raw(item_id, component_type, body, resource_id=resource_id, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, tag=tag, transfer_priority=transfer_priority, index=index, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, priority=priority, storage_id=storage_id, create_thumbnails=create_thumbnails, create_posters=create_posters, override_fast_start=override_fast_start, original=original, shape_id=shape_id, filename=filename, transfer_id=transfer_id, no_transcode=no_transcode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_placeholder_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **component_type** | **str**| The component type. | 
 **body** | **file**| The raw data. | 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **tag** | [**list[str]**](str.md)| A list of shape tags to use for transcoding. | [optional] 
 **transfer_priority** | **int**| An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. | [optional] 
 **index** | **int**| Index (order) of the component. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; (default) - Generate thumbnails as per defined by shape tag.  - &#x60;false&#x60; - Disable thumbnail generation. | [optional] [default to True]
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 
 **shape_id** | **str**| Shape id for which shape to receive the content. | [optional] 
 **filename** | **str**| The filename to be stored as original filename | [optional] 
 **transfer_id** | **str**| An id to assign the transfer to be able to refer to it. | [optional] 
 **no_transcode** | **bool**| - &#x60;true&#x60; - Will disable transcoding even if the &#x60;tags&#x60; parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - &#x60;false&#x60; (default) - Normal transcode. | [optional] [default to False]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job, or no content if the transfer is not finished. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_project**
> URIListType import_project(essence_mappings_type, assign_id=assign_id, collection_id=collection_id, type=type, uri=uri)

Import a project

Creates a new project version containing the clips and sequences found in the given project file. Sequences in the file will be created as items having a Vidispine sequence representation.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
essence_mappings_type = vidispine.EssenceMappingsType() # EssenceMappingsType | 
assign_id = False # bool | True if external ids should be created for the items in this project, using the ids from the project. (optional) (default to False)
collection_id = 'collection_id_example' # str | The id of the project to create a new version for. (optional)
type = 'type_example' # str | The file format. (optional)
uri = 'uri_example' # str | The location of the file to import. (optional)

try:
    # Import a project
    api_response = api_instance.import_project(essence_mappings_type, assign_id=assign_id, collection_id=collection_id, type=type, uri=uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **essence_mappings_type** | [**EssenceMappingsType**](EssenceMappingsType.md)|  | 
 **assign_id** | **bool**| True if external ids should be created for the items in this project, using the ids from the project. | [optional] [default to False]
 **collection_id** | **str**| The id of the project to create a new version for. | [optional] 
 **type** | **str**| The file format. | [optional] 
 **uri** | **str**| The location of the file to import. | [optional] 

### Return type

[**URIListType**](URIListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_project_sequence**
> URIListType import_project_sequence(essence_mappings_type, assign_id=assign_id, type=type, uri=uri, pause_frame=pause_frame)

Import a sequence

Creates a new item with a Vidispine sequence representations of the given file. The file must contain a single sequence.  The item will also have a sequence contain the original data from the file, together with an essence mapping for identifying the items and files referenced by the sequence.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
essence_mappings_type = vidispine.EssenceMappingsType() # EssenceMappingsType | 
assign_id = False # bool | True if external ids should be created for the items in this project, using the ids from the project. (optional) (default to False)
type = 'type_example' # str | The file format. (optional)
uri = 'uri_example' # str | The location of the file to import. (optional)
pause_frame = 56 # int | When a rendering job is started, this parameter determines which frame the job will pause at.  The job will resume when the sequence is updated. (optional)

try:
    # Import a sequence
    api_response = api_instance.import_project_sequence(essence_mappings_type, assign_id=assign_id, type=type, uri=uri, pause_frame=pause_frame)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_project_sequence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **essence_mappings_type** | [**EssenceMappingsType**](EssenceMappingsType.md)|  | 
 **assign_id** | **bool**| True if external ids should be created for the items in this project, using the ids from the project. | [optional] [default to False]
 **type** | **str**| The file format. | [optional] 
 **uri** | **str**| The location of the file to import. | [optional] 
 **pause_frame** | **int**| When a rendering job is started, this parameter determines which frame the job will pause at.  The job will resume when the sequence is updated. | [optional] 

### Return type

[**URIListType**](URIListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_sidecar**
> JobType import_sidecar(item_id, jobmetadata=jobmetadata, notification_data=notification_data, sidecar=sidecar, priority=priority, notification=notification)

Import a sidecar file

Starts a job that imports the sidecar file, located at the given URL, to the specified item.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
sidecar = 'sidecar_example' # str | Either the id of the sidecar file or a URL for locating it. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)

try:
    # Import a sidecar file
    api_response = api_instance.import_sidecar(item_id, jobmetadata=jobmetadata, notification_data=notification_data, sidecar=sidecar, priority=priority, notification=notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_sidecar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **sidecar** | **str**| Either the id of the sidecar file or a URL for locating it. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_sidecar_raw**
> JobType import_sidecar_raw(item_id, body, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, file_extension=file_extension, notification=notification, priority=priority)

Import a sidecar file

Starts a job that imports the sidecar file as HTTP request body. The sidecar file will be saved in one of the Vidispine storages.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
body = '/path/to/file' # file | The raw data.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
storage_id = 'storage_id_example' # str | The id of the storage that the sidecar file will be saved in. (optional)
file_extension = 'file_extension_example' # str | The extension of the file that this sidecar data is from.  Used to identify the sidecar media type.  Example: `srt`. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Import a sidecar file
    api_response = api_instance.import_sidecar_raw(item_id, body, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, file_extension=file_extension, notification=notification, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_sidecar_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **body** | **file**| The raw data. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **storage_id** | **str**| The id of the storage that the sidecar file will be saved in. | [optional] 
 **file_extension** | **str**| The extension of the file that this sidecar data is from.  Used to identify the sidecar media type.  Example: &#x60;srt&#x60;. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_storage_definition**
> import_storage_definition(storage_import_type, path=path)

Import a storage definition

Creates a new storage based on the *StorageImportDocument*. A file entity will be created for each entry in the document, if a file with that ID does not already exist. Finally, a storage method will be added, with the path supplied in the call.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
storage_import_type = vidispine.StorageImportType() # StorageImportType | A <em>StorageImportDocument</em>
path = 'path_example' # str | The file system path to where the files are located. (optional)

try:
    # Import a storage definition
    api_instance.import_storage_definition(storage_import_type, path=path)
except ApiException as e:
    print("Exception when calling ImportApi->import_storage_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_import_type** | [**StorageImportType**](StorageImportType.md)| A &lt;em&gt;StorageImportDocument&lt;/em&gt; | 
 **path** | **str**| The file system path to where the files are located. | [optional] 

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

# **import_to_placeholder**
> JobType import_to_placeholder(item_id, component_type, uri=uri, no_transcode=no_transcode, original=original, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, create_posters=create_posters, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, require_fast_start=require_fast_start, growing=growing, tag=tag, resource_id=resource_id, thumbnail_service=thumbnail_service, settings=settings, notification=notification, file_id=file_id, shape_id=shape_id, allow_reimport=allow_reimport, index=index, priority=priority, override_fast_start=override_fast_start)

Import to a placeholder item

Imports the file and extracts component data based on what type is specified (container, audio, video, binary). No transcoding will take place until all files have been imported.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
component_type = 'component_type_example' # str | The component type.
uri = 'uri_example' # str | A URI to the file that will be imported.  Make sure to percent encode the URI.  Must be specified unless `fileId` is specified. (optional)
no_transcode = False # bool | - `true` - Will disable transcoding even if the `tags` parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - `false` (default) - Normal transcode. (optional) (default to False)
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
create_thumbnails = True # bool | - `true` (default) - Generate thumbnails as per defined by shape tag.  - `false` - Disable thumbnail generation. (optional) (default to True)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
growing = False # bool | - `true` - Specifies that the input file is still written to, so enables growing file support.  - `false` (default) - No growing file handling of import file. (optional) (default to False)
tag = ['tag_example'] # list[str] | A list of shape tags to use for transcoding. (optional)
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
settings = 'settings_example' # str | Pre-configured import settings. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
file_id = 'file_id_example' # str | The id of the file that contains the essence.  Must be specified unless `uri` is specified. (optional)
shape_id = 'shape_id_example' # str | Shape id for which shape to receive the content. (optional)
allow_reimport = True # bool | - `true` - Import the file to this shape even if the file is already importing or is already part of another item.  - `false` (default) Reject the request if the file with the given id has already been imported or is currently importing. (optional)
index = 56 # int | The component index (track) of new component. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)

try:
    # Import to a placeholder item
    api_response = api_instance.import_to_placeholder(item_id, component_type, uri=uri, no_transcode=no_transcode, original=original, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, create_posters=create_posters, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, require_fast_start=require_fast_start, growing=growing, tag=tag, resource_id=resource_id, thumbnail_service=thumbnail_service, settings=settings, notification=notification, file_id=file_id, shape_id=shape_id, allow_reimport=allow_reimport, index=index, priority=priority, override_fast_start=override_fast_start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_to_placeholder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **component_type** | **str**| The component type. | 
 **uri** | **str**| A URI to the file that will be imported.  Make sure to percent encode the URI.  Must be specified unless &#x60;fileId&#x60; is specified. | [optional] 
 **no_transcode** | **bool**| - &#x60;true&#x60; - Will disable transcoding even if the &#x60;tags&#x60; parameter is set.  Rather, the specified tag will be used to determine cropping, scaling etc.  of thumbnails.  - &#x60;false&#x60; (default) - Normal transcode. | [optional] [default to False]
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; (default) - Generate thumbnails as per defined by shape tag.  - &#x60;false&#x60; - Disable thumbnail generation. | [optional] [default to True]
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **growing** | **bool**| - &#x60;true&#x60; - Specifies that the input file is still written to, so enables growing file support.  - &#x60;false&#x60; (default) - No growing file handling of import file. | [optional] [default to False]
 **tag** | [**list[str]**](str.md)| A list of shape tags to use for transcoding. | [optional] 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **settings** | **str**| Pre-configured import settings. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **file_id** | **str**| The id of the file that contains the essence.  Must be specified unless &#x60;uri&#x60; is specified. | [optional] 
 **shape_id** | **str**| Shape id for which shape to receive the content. | [optional] 
 **allow_reimport** | **bool**| - &#x60;true&#x60; - Import the file to this shape even if the file is already importing or is already part of another item.  - &#x60;false&#x60; (default) Reject the request if the file with the given id has already been imported or is currently importing. | [optional] 
 **index** | **int**| The component index (track) of new component. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_access_control_for_group**
> update_default_access_control_for_group(permission, group_name)

Add a group to the default access control list

Sets the permissions for a certain group.

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
api_instance = vidispine.ImportApi(vidispine.ApiClient(configuration))
permission = 'permission_example' # str | The level of permissions to grant the group.
group_name = 'group_name_example' # str | The group name.

try:
    # Add a group to the default access control list
    api_instance.update_default_access_control_for_group(permission, group_name)
except ApiException as e:
    print("Exception when calling ImportApi->update_default_access_control_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The level of permissions to grant the group. | 
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

