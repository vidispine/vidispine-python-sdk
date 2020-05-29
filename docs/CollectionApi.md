# vidispine.CollectionApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_collection**](CollectionApi.md#add_to_collection) | **PUT** /collection/{collection-id}/{id} | Add an item, library or collection to a collection
[**create_collection**](CollectionApi.md#create_collection) | **POST** /collection | Create a collection
[**create_collection_export_job**](CollectionApi.md#create_collection_export_job) | **POST** /collection/{collection-id}/export | Start an export job for a collection or a library
[**create_collection_to_folder_mapping**](CollectionApi.md#create_collection_to_folder_mapping) | **PUT** /collection/{collection-id}/map-to-folder | Mark a collection as folder mapped
[**delete_collection**](CollectionApi.md#delete_collection) | **DELETE** /collection/{collection-id} | Delete a collection
[**delete_collection_to_folder_mapping**](CollectionApi.md#delete_collection_to_folder_mapping) | **DELETE** /collection/{collection-id}/map-to-folder | Unmark a collection as folder mapped
[**delete_collections**](CollectionApi.md#delete_collections) | **DELETE** /collection | Delete multiple collections
[**get_collection**](CollectionApi.md#get_collection) | **GET** /collection/{collection-id} | Retrieve a collection
[**get_collection_ancestors**](CollectionApi.md#get_collection_ancestors) | **GET** /collection/{collection-id}/ancestor | Retrieve the ancestors of a collection
[**get_collection_items**](CollectionApi.md#get_collection_items) | **GET** /collection/{collection-id}/item | Retrieve the items of a collection
[**get_collection_search_history**](CollectionApi.md#get_collection_search_history) | **GET** /collection/history | Retrieve the search history
[**get_collections**](CollectionApi.md#get_collections) | **GET** /collection | List all collections
[**remove_from_collection**](CollectionApi.md#remove_from_collection) | **DELETE** /collection/{collection-id}/{id} | Remove an item, library or collection from a collection
[**reorder_collection_elements**](CollectionApi.md#reorder_collection_elements) | **POST** /collection/{collection-id}/order | Reorder collection elements
[**search_collections**](CollectionApi.md#search_collections) | **PUT** /collection | Search for collections
[**search_items_in_collection**](CollectionApi.md#search_items_in_collection) | **PUT** /collection/{collection-id}/item | Search for items within a collection
[**update_collection**](CollectionApi.md#update_collection) | **PUT** /collection/{collection-id} | Update a collection
[**update_collection_folder_name**](CollectionApi.md#update_collection_folder_name) | **PUT** /collection/{collection-id}/folder-name | Report that the folder name has changed on disk
[**update_collection_name**](CollectionApi.md#update_collection_name) | **PUT** /collection/{collection-id}/rename | Update collection name


# **add_to_collection**
> add_to_collection(collection_id, id, type=type, metadata=metadata, add_items=add_items)

Add an item, library or collection to a collection

Adds an item, library or collection with the id `id`, to the collection with the id `collection-id`. If `id` is already present within the collection, this is a no-op, except if the query parameter metadata is used. In that case, metadata is updated for the specified entity.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.
id = 'id_example' # str | The id.
type = 'item' # str | - `collection` - The object identified by `id` is a collection.  - `item` (default) - The object identified by `id` is an item.  - `library` - The object identified by `id` is a library. (optional) (default to 'item')
metadata = ['metadata_example'] # list[str] | - *key* `=` *value* - Set or add metadata field to the relation between the collection and entity.  Can be used multiple times to add several fields.  The key cannot be empty or start with a minus sign.  To delete a field enter the same key with a minus sign at the beginning.  Note that `=` is part of the query parameter, and has to be encoded (`%3d`). (optional)
add_items = True # bool | - `true` - Library items will be added individually.  Only has any effect when `type=library`.  - `false` - Library will be added to collection, not specific items. (optional)

try:
    # Add an item, library or collection to a collection
    api_instance.add_to_collection(collection_id, id, type=type, metadata=metadata, add_items=add_items)
except ApiException as e:
    print("Exception when calling CollectionApi->add_to_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 
 **id** | **str**| The id. | 
 **type** | **str**| - &#x60;collection&#x60; - The object identified by &#x60;id&#x60; is a collection.  - &#x60;item&#x60; (default) - The object identified by &#x60;id&#x60; is an item.  - &#x60;library&#x60; - The object identified by &#x60;id&#x60; is a library. | [optional] [default to &#39;item&#39;]
 **metadata** | [**list[str]**](str.md)| - *key* &#x60;&#x3D;&#x60; *value* - Set or add metadata field to the relation between the collection and entity.  Can be used multiple times to add several fields.  The key cannot be empty or start with a minus sign.  To delete a field enter the same key with a minus sign at the beginning.  Note that &#x60;&#x3D;&#x60; is part of the query parameter, and has to be encoded (&#x60;%3d&#x60;). | [optional] 
 **add_items** | **bool**| - &#x60;true&#x60; - Library items will be added individually.  Only has any effect when &#x60;type&#x3D;library&#x60;.  - &#x60;false&#x60; - Library will be added to collection, not specific items. | [optional] 

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

# **create_collection**
> CollectionType create_collection(collection_type, name=name, settings=settings, external_id=external_id)

Create a collection

Generates a new collection and returns the id associated with that collection.  This resource accepts a collection document that can contain both metadata that should be set for the collection and the entities that it should contain.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_type = vidispine.CollectionType() # CollectionType | 
name = 'name_example' # str | Name of the collection. (optional)
settings = 'settings_example' # str | Pre-configured import settings. (optional)
external_id = 'external_id_example' # str | An external identifier to assign to the collection. (optional)

try:
    # Create a collection
    api_response = api_instance.create_collection(collection_type, name=name, settings=settings, external_id=external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->create_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_type** | [**CollectionType**](CollectionType.md)|  | 
 **name** | **str**| Name of the collection. | [optional] 
 **settings** | **str**| Pre-configured import settings. | [optional] 
 **external_id** | **str**| An external identifier to assign to the collection. | [optional] 

### Return type

[**CollectionType**](CollectionType.md)

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

# **create_collection_export_job**
> JobType create_collection_export_job(collection_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, tag=tag, all=all, projection=projection, use_original_component_filename=use_original_component_filename, notification=notification, priority=priority, version=version, uri=uri, metadata=metadata, template=template, location_name=location_name)

Start an export job for a collection or a library

Creates a new export job that will copy all matching files in the collection/library to a remote location.  A shape tag can be specified to decide which shapes that will be exported. The files will retain their original names and the URI should therefore point to the folder where the files should be placed.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
track = ["*"] # list[str] | Comma-separated list of item track ids.  Can include wildcards, e. g.  `A*`.  Can also contain component ids. (optional) (default to ["*"])
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
use_original_filename = False # bool | If set to `true`, the file(s) will be exported with their original filename if available. (optional) (default to False)
tag = 'tag_example' # str | Finds a shape with the specified tag and uses that for export.  If not specified, the system will attempt to use the original shape. (optional)
all = True # bool | - `true` (default) - Fail the job if not all files from the selected shapes could be exported.  - `false` - Don't export lost or unavailable files. (optional) (default to True)
projection = 'projection_example' # str | Defines the projection to use when exporting the metadata. (optional)
use_original_component_filename = True # bool | If set to `true`, the file(s) will be exported with their original component filename if available. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
version = 'latest' # str | - *essence-version-id* - Return shapes for a specified version.  - `all` - Return shapes for all versions.  - `latest` (default) - Return shapes for the latest version.  - `latest-per-shapetag` - Return shapes with the highest essence version number per shape tag. (optional) (default to 'latest')
uri = 'uri_example' # str | A URI to the destination of the file. (optional)
metadata = False # bool | - `true` - Metadata will also be exported to side-car XML file.  - `false` (default) - No metadata is exported. (optional) (default to False)
template = 'template_example' # str | export template to use. (optional)
location_name = 'location_name_example' # str | The name of an export location. (optional)

try:
    # Start an export job for a collection or a library
    api_response = api_instance.create_collection_export_job(collection_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, tag=tag, all=all, projection=projection, use_original_component_filename=use_original_component_filename, notification=notification, priority=priority, version=version, uri=uri, metadata=metadata, template=template, location_name=location_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->create_collection_export_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **track** | [**list[str]**](str.md)| Comma-separated list of item track ids.  Can include wildcards, e. g.  &#x60;A*&#x60;.  Can also contain component ids. | [optional] [default to [&quot;*&quot;]]
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **use_original_filename** | **bool**| If set to &#x60;true&#x60;, the file(s) will be exported with their original filename if available. | [optional] [default to False]
 **tag** | **str**| Finds a shape with the specified tag and uses that for export.  If not specified, the system will attempt to use the original shape. | [optional] 
 **all** | **bool**| - &#x60;true&#x60; (default) - Fail the job if not all files from the selected shapes could be exported.  - &#x60;false&#x60; - Don&#39;t export lost or unavailable files. | [optional] [default to True]
 **projection** | **str**| Defines the projection to use when exporting the metadata. | [optional] 
 **use_original_component_filename** | **bool**| If set to &#x60;true&#x60;, the file(s) will be exported with their original component filename if available. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **version** | **str**| - *essence-version-id* - Return shapes for a specified version.  - &#x60;all&#x60; - Return shapes for all versions.  - &#x60;latest&#x60; (default) - Return shapes for the latest version.  - &#x60;latest-per-shapetag&#x60; - Return shapes with the highest essence version number per shape tag. | [optional] [default to &#39;latest&#39;]
 **uri** | **str**| A URI to the destination of the file. | [optional] 
 **metadata** | **bool**| - &#x60;true&#x60; - Metadata will also be exported to side-car XML file.  - &#x60;false&#x60; (default) - No metadata is exported. | [optional] [default to False]
 **template** | **str**| export template to use. | [optional] 
 **location_name** | **str**| The name of an export location. | [optional] 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection_to_folder_mapping**
> create_collection_to_folder_mapping(collection_id)

Mark a collection as folder mapped

Marks collection `collection-id` as mapped to folder. Files in child items will be moved to the corresponding folder in the storages.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.

try:
    # Mark a collection as folder mapped
    api_instance.create_collection_to_folder_mapping(collection_id)
except ApiException as e:
    print("Exception when calling CollectionApi->create_collection_to_folder_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 

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

# **delete_collection**
> delete_collection(collection_id)

Delete a collection

Delete specified collection.  Note that the actual items and libraries that are contained within the collection are not modified.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.

try:
    # Delete a collection
    api_instance.delete_collection(collection_id)
except ApiException as e:
    print("Exception when calling CollectionApi->delete_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 

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

# **delete_collection_to_folder_mapping**
> delete_collection_to_folder_mapping(collection_id)

Unmark a collection as folder mapped

Marks collection `collection-id` as *not* mapped to folder. Files in child items will be moved to the root directory in the storages.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.

try:
    # Unmark a collection as folder mapped
    api_instance.delete_collection_to_folder_mapping(collection_id)
except ApiException as e:
    print("Exception when calling CollectionApi->delete_collection_to_folder_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 

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

# **delete_collections**
> delete_collections(id)

Delete multiple collections

Delete multiple collections.  Note that the actual items and libraries that are contained within the collection are not modified.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
id = ['id_example'] # list[str] | Comma-separated list of collection ids or external ids.

try:
    # Delete multiple collections
    api_instance.delete_collections(id)
except ApiException as e:
    print("Exception when calling CollectionApi->delete_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| Comma-separated list of collection ids or external ids. | 

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

# **get_collection**
> CollectionType get_collection(collection_id, language=language, track=track, children=children, conflict=conflict, merged_extradata=merged_extradata, content=content, terse=terse, merged_permission=merged_permission, sample_rate=sample_rate, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, interval=interval, group=group, field=field, include=include, revision=revision, include_values=include_values)

Retrieve a collection

Return the ids of the objects contained within the collection, that has the id `collection-id`.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
children = ['children_example'] # list[str] | Comma-separated list of types to include in the result.  Default is to return everything.   - `collection` - Return collections contained in this collection.  - `item` - Return items contained in this collection.  - `library` - Return libraries contained in this collection.  New in version 4. 16. 6. (optional)
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
merged_extradata = 'merged_extradata_example' # str | Any possible extra data. (optional)
content = ['content_example'] # list[str] | Comma-separated list of additional content to retrieve. (optional)
terse = 'no' # str | - `yes` - Return metadata in terse format.  - `no` (default) - Return metadata in verbose format. (optional) (default to 'no')
merged_permission = 'merged_permission_example' # str | The lowest required permission level. (optional)
sample_rate = 'sample_rate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
include_transient_metadata = True # bool | - `true` (default) - Include transient metadata.  - `false` - Do not include transient metadata in response. (optional) (default to True)
merged_type = 'merged_type_example' # str | The type of operation to check for. (optional)
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = 'include_example' # str | A list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)
revision = 'revision_example' # str | Specifying what revision of metadata to display.  Only used if requesting a single item or collection. (optional)
include_values = True # bool | Return the value enumeration for each metadata field. (optional)

try:
    # Retrieve a collection
    api_response = api_instance.get_collection(collection_id, language=language, track=track, children=children, conflict=conflict, merged_extradata=merged_extradata, content=content, terse=terse, merged_permission=merged_permission, sample_rate=sample_rate, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, interval=interval, group=group, field=field, include=include, revision=revision, include_values=include_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **track** | [**list[str]**](str.md)| Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is &#x60;A2&#x60;.  - *track-type* *t1* &#x60;-&#x60; *t2* - Return metadata for specified track interval, e. g.  &#x60;A2-4&#x60;.  - *track-type* &#x60;*&#x60; - Return metadata for all tracks of specified type, e. g.  &#x60;A*&#x60;.  - &#x60;generic&#x60; - Return all non-tracked metadata.  - &#x60;all&#x60; (default) - All metadata, with or without track specification, are returned. | [optional] [default to [&quot;all&quot;]]
 **children** | [**list[str]**](str.md)| Comma-separated list of types to include in the result.  Default is to return everything.   - &#x60;collection&#x60; - Return collections contained in this collection.  - &#x60;item&#x60; - Return items contained in this collection.  - &#x60;library&#x60; - Return libraries contained in this collection.  New in version 4. 16. 6. | [optional] 
 **conflict** | **str**| - &#x60;yes&#x60; (default) - Include all metadata conflicts, unresolved.  - &#x60;no&#x60; - Return conflicts resolved according to field rules. | [optional] [default to &#39;yes&#39;]
 **merged_extradata** | **str**| Any possible extra data. | [optional] 
 **content** | [**list[str]**](str.md)| Comma-separated list of additional content to retrieve. | [optional] 
 **terse** | **str**| - &#x60;yes&#x60; - Return metadata in terse format.  - &#x60;no&#x60; (default) - Return metadata in verbose format. | [optional] [default to &#39;no&#39;]
 **merged_permission** | **str**| The lowest required permission level. | [optional] 
 **sample_rate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **include_transient_metadata** | **bool**| - &#x60;true&#x60; (default) - Include transient metadata.  - &#x60;false&#x60; - Do not include transient metadata in response. | [optional] [default to True]
 **merged_type** | **str**| The type of operation to check for. | [optional] 
 **default_value** | **bool**| - &#x60;true&#x60; - For unset fields, return default values.  - &#x60;false&#x60; (default) - Do not return default values. | [optional] [default to False]
 **interval** | [**list[str]**](str.md)| Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - &#x60;generic&#x60; - Return all non-timed metadata.  - &#x60;all&#x60; (default) - Return all metadata, same as &#x60;interval&#x3D;generic,-INF-+INF&#x60; | [optional] [default to [&quot;all&quot;]]
 **group** | [**list[str]**](str.md)| Comma-separated list.   - *group-name* - Return specified group.  - *group-name* &#x60;+&#x60; - Return specified group and subgroups.  - *group-name* &#x60;:&#x60; *new-name* - Return specified group, renamed to a new name in return value.  - &#x60;-&#x60; *group-name* - Exclude specified group.  - (default) - Return all groups. | [optional] 
 **field** | [**list[str]**](str.md)| Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \&quot;:\&quot; *new-name* - Return specified field, renamed to a new name in return value.  - \&quot;-\&quot; *field-name* - Exclude specified field.  - (default) - Return all fields. | [optional] 
 **include** | **str**| A list of keys.   Includes additional field specific data.  Additionally, if set to &#x60;type&#x60; the type definition of the field will be retrieved. | [optional] 
 **revision** | **str**| Specifying what revision of metadata to display.  Only used if requesting a single item or collection. | [optional] 
 **include_values** | **bool**| Return the value enumeration for each metadata field. | [optional] 

### Return type

[**CollectionType**](CollectionType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_ancestors**
> URIListType get_collection_ancestors(collection_id)

Retrieve the ancestors of a collection

Retrieves the ids of all ancestors of the collection.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.

try:
    # Retrieve the ancestors of a collection
    api_response = api_instance.get_collection_ancestors(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get_collection_ancestors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 

### Return type

[**URIListType**](URIListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_items**
> ItemListType get_collection_items(collection_id, language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, update_frequency=update_frequency, number=number, interval=interval, group=group, merged_permission=merged_permission, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, uri_type=uri_type, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, q=q, p=p, library=library, base_uri=base_uri, merged_extradata=merged_extradata, result=result, storage=storage, revision=revision, url=url, scheme=scheme, auto_refresh=auto_refresh, version=version, cursor=cursor, include_values=include_values, sample_rate=sample_rate, library_id=library_id, count=count, save=save, noauth_url=noauth_url, update_mode=update_mode)

Retrieve the items of a collection

Retrieves only the items of the collection.  Queries on collection items will now return items in creation order by default. See `indexCollectionItemOrder` on how to revert back to using the insert/custom collection item ordering.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
first = 1 # int | From the resulting list of items, start return list from specified offset. (optional) (default to 1)
closed_files = True # bool | A URI parameter:  - `true` (default) - Return only URIs that point to closed files.  - `false` - Return all URIs. (optional) (default to True)
terse = 'no' # str | - `yes` - Return metadata in terse format.  - `no` (default) - Return metadata in verbose format. (optional) (default to 'no')
method_metadata = 'method_metadata_example' # str | Metadata used with storage method. (optional)
update_frequency = 'update_frequency_example' # str | When creating a library, use this update frequency.  Defaults to no periodic updates. (optional)
number = 100 # int | The number of entities to fetch. (optional) (default to 100)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
merged_permission = 'merged_permission_example' # str | The lowest required permission level. (optional)
storage_group = 'storage_group_example' # str | Storage group id.  Return only files from storages specified in the storage group. (optional)
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
starttc = False # bool | - `true` - Interval is given relative to start timecode of item.  - `false` (default) - Interval is 0-based. (optional) (default to False)
content = ['content_example'] # list[str] | Comma-separated list of the types of content to retrieve. (optional)
uri_type = ['uri_type_example'] # list[str] | Comma-separated list of format types (container format) to return. (optional)
include_transient_metadata = True # bool | - `true` (default) - Include transient metadata.  - `false` - Do not include transient metadata in response. (optional) (default to True)
merged_type = 'merged_type_example' # str | The type of operation to check for. (optional)
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
tag = 'tag_example' # str | A URI parameter: Comma-separated list of shape tags to return. (optional)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = 'include_example' # str | A list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)
method_type = 'method_type_example' # str | Access method.   - `AUTO` - Gives an APInoauth URI to the media.  Access to file is tunneled through Vidispine.  - `AZURE_SAS` - If the storage schema is azure:// you can get direct access to the media.  The resulting URI will not tunnel through Vidispine but rather point directly to the media location at the azure storage. (optional)
q = 'q_example' # str | XML/JSON, *ItemSearchDocument*.  Only with GET. (optional)
p = ['p_example'] # list[str] | Comma-separated list of paths specifying the content to include.  Overrides the content and filter parameters. (optional)
library = '*' # str | Restricts search to within library, identifier. (optional) (default to '*')
base_uri = 'base_uri_example' # str | Which base URI to use for the thumbnail URLs. (optional)
merged_extradata = 'merged_extradata_example' # str | Any possible extra data. (optional)
result = 'list' # str | - `list` (default) - Return a list of items.  - `library` - Create a library with the matching items. (optional) (default to 'list')
storage = ['storage_example'] # list[str] | List of storage ids.  Return only files from specific storages.  Can be specified multiple times. (optional)
revision = 'revision_example' # str | Specifying which metadata revision to display.  Only used if requesting a single item or collection. (optional)
url = False # bool | - `true` - Return list of URLs.  - `false` (default) - Return list of ids. (optional) (default to False)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
auto_refresh = False # bool | When creating a library, make it self-refresh. (optional) (default to False)
version = 'version_example' # str | Specifying which essence version to return for shapes.  If special value `all`, display all versions.  If special value `latest` (default), display latest version of shapes. (optional)
cursor = 'cursor_example' # str | New in version 4. 16.   - `*` - The initial cursor.  - `string-from-search` - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When `cursor` is used, The value of `first` will be ignored.  Only metadata searches in the `generic` interval supports `cursor`. (optional)
include_values = True # bool | Return the value enumeration for each metadata field. (optional)
sample_rate = 'sample_rate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
library_id = 'library_id_example' # str | If set, the library identified by this id will be used instead of creating a new library. (optional)
count = True # bool | - `true` (default) - Return hits in result.  - `false` - Do not return hits in result, in order to produce results faster. (optional) (default to True)
save = True # bool | - `true` - Returns a `303 See Other`, with a `Location` header containing an URI to fetch the search result - `false` (default) - Returns a regular search result (optional)
noauth_url = True # bool | - `true` Return URIs that do not need authentication.  - `false` (default) Return normal URIs (optional)
update_mode = 'MERGE' # str | When creating a library, use this update mode. (optional) (default to 'MERGE')

try:
    # Retrieve the items of a collection
    api_response = api_instance.get_collection_items(collection_id, language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, update_frequency=update_frequency, number=number, interval=interval, group=group, merged_permission=merged_permission, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, uri_type=uri_type, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, q=q, p=p, library=library, base_uri=base_uri, merged_extradata=merged_extradata, result=result, storage=storage, revision=revision, url=url, scheme=scheme, auto_refresh=auto_refresh, version=version, cursor=cursor, include_values=include_values, sample_rate=sample_rate, library_id=library_id, count=count, save=save, noauth_url=noauth_url, update_mode=update_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **first** | **int**| From the resulting list of items, start return list from specified offset. | [optional] [default to 1]
 **closed_files** | **bool**| A URI parameter:  - &#x60;true&#x60; (default) - Return only URIs that point to closed files.  - &#x60;false&#x60; - Return all URIs. | [optional] [default to True]
 **terse** | **str**| - &#x60;yes&#x60; - Return metadata in terse format.  - &#x60;no&#x60; (default) - Return metadata in verbose format. | [optional] [default to &#39;no&#39;]
 **method_metadata** | **str**| Metadata used with storage method. | [optional] 
 **update_frequency** | **str**| When creating a library, use this update frequency.  Defaults to no periodic updates. | [optional] 
 **number** | **int**| The number of entities to fetch. | [optional] [default to 100]
 **interval** | [**list[str]**](str.md)| Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - &#x60;generic&#x60; - Return all non-timed metadata.  - &#x60;all&#x60; (default) - Return all metadata, same as &#x60;interval&#x3D;generic,-INF-+INF&#x60; | [optional] [default to [&quot;all&quot;]]
 **group** | [**list[str]**](str.md)| Comma-separated list.   - *group-name* - Return specified group.  - *group-name* &#x60;+&#x60; - Return specified group and subgroups.  - *group-name* &#x60;:&#x60; *new-name* - Return specified group, renamed to a new name in return value.  - &#x60;-&#x60; *group-name* - Exclude specified group.  - (default) - Return all groups. | [optional] 
 **merged_permission** | **str**| The lowest required permission level. | [optional] 
 **storage_group** | **str**| Storage group id.  Return only files from storages specified in the storage group. | [optional] 
 **track** | [**list[str]**](str.md)| Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is &#x60;A2&#x60;.  - *track-type* *t1* &#x60;-&#x60; *t2* - Return metadata for specified track interval, e. g.  &#x60;A2-4&#x60;.  - *track-type* &#x60;*&#x60; - Return metadata for all tracks of specified type, e. g.  &#x60;A*&#x60;.  - &#x60;generic&#x60; - Return all non-tracked metadata.  - &#x60;all&#x60; (default) - All metadata, with or without track specification, are returned. | [optional] [default to [&quot;all&quot;]]
 **conflict** | **str**| - &#x60;yes&#x60; (default) - Include all metadata conflicts, unresolved.  - &#x60;no&#x60; - Return conflicts resolved according to field rules. | [optional] [default to &#39;yes&#39;]
 **starttc** | **bool**| - &#x60;true&#x60; - Interval is given relative to start timecode of item.  - &#x60;false&#x60; (default) - Interval is 0-based. | [optional] [default to False]
 **content** | [**list[str]**](str.md)| Comma-separated list of the types of content to retrieve. | [optional] 
 **uri_type** | [**list[str]**](str.md)| Comma-separated list of format types (container format) to return. | [optional] 
 **include_transient_metadata** | **bool**| - &#x60;true&#x60; (default) - Include transient metadata.  - &#x60;false&#x60; - Do not include transient metadata in response. | [optional] [default to True]
 **merged_type** | **str**| The type of operation to check for. | [optional] 
 **default_value** | **bool**| - &#x60;true&#x60; - For unset fields, return default values.  - &#x60;false&#x60; (default) - Do not return default values. | [optional] [default to False]
 **tag** | **str**| A URI parameter: Comma-separated list of shape tags to return. | [optional] 
 **field** | [**list[str]**](str.md)| Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \&quot;:\&quot; *new-name* - Return specified field, renamed to a new name in return value.  - \&quot;-\&quot; *field-name* - Exclude specified field.  - (default) - Return all fields. | [optional] 
 **include** | **str**| A list of keys.   Includes additional field specific data.  Additionally, if set to &#x60;type&#x60; the type definition of the field will be retrieved. | [optional] 
 **method_type** | **str**| Access method.   - &#x60;AUTO&#x60; - Gives an APInoauth URI to the media.  Access to file is tunneled through Vidispine.  - &#x60;AZURE_SAS&#x60; - If the storage schema is azure:// you can get direct access to the media.  The resulting URI will not tunnel through Vidispine but rather point directly to the media location at the azure storage. | [optional] 
 **q** | **str**| XML/JSON, *ItemSearchDocument*.  Only with GET. | [optional] 
 **p** | [**list[str]**](str.md)| Comma-separated list of paths specifying the content to include.  Overrides the content and filter parameters. | [optional] 
 **library** | **str**| Restricts search to within library, identifier. | [optional] [default to &#39;*&#39;]
 **base_uri** | **str**| Which base URI to use for the thumbnail URLs. | [optional] 
 **merged_extradata** | **str**| Any possible extra data. | [optional] 
 **result** | **str**| - &#x60;list&#x60; (default) - Return a list of items.  - &#x60;library&#x60; - Create a library with the matching items. | [optional] [default to &#39;list&#39;]
 **storage** | [**list[str]**](str.md)| List of storage ids.  Return only files from specific storages.  Can be specified multiple times. | [optional] 
 **revision** | **str**| Specifying which metadata revision to display.  Only used if requesting a single item or collection. | [optional] 
 **url** | **bool**| - &#x60;true&#x60; - Return list of URLs.  - &#x60;false&#x60; (default) - Return list of ids. | [optional] [default to False]
 **scheme** | **str**| URI scheme to return. | [optional] 
 **auto_refresh** | **bool**| When creating a library, make it self-refresh. | [optional] [default to False]
 **version** | **str**| Specifying which essence version to return for shapes.  If special value &#x60;all&#x60;, display all versions.  If special value &#x60;latest&#x60; (default), display latest version of shapes. | [optional] 
 **cursor** | **str**| New in version 4. 16.   - &#x60;*&#x60; - The initial cursor.  - &#x60;string-from-search&#x60; - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When &#x60;cursor&#x60; is used, The value of &#x60;first&#x60; will be ignored.  Only metadata searches in the &#x60;generic&#x60; interval supports &#x60;cursor&#x60;. | [optional] 
 **include_values** | **bool**| Return the value enumeration for each metadata field. | [optional] 
 **sample_rate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **library_id** | **str**| If set, the library identified by this id will be used instead of creating a new library. | [optional] 
 **count** | **bool**| - &#x60;true&#x60; (default) - Return hits in result.  - &#x60;false&#x60; - Do not return hits in result, in order to produce results faster. | [optional] [default to True]
 **save** | **bool**| - &#x60;true&#x60; - Returns a &#x60;303 See Other&#x60;, with a &#x60;Location&#x60; header containing an URI to fetch the search result - &#x60;false&#x60; (default) - Returns a regular search result | [optional] 
 **noauth_url** | **bool**| - &#x60;true&#x60; Return URIs that do not need authentication.  - &#x60;false&#x60; (default) Return normal URIs | [optional] 
 **update_mode** | **str**| When creating a library, use this update mode. | [optional] [default to &#39;MERGE&#39;]

### Return type

[**ItemListType**](ItemListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of ids or URLs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_search_history**
> SearchHistoryListType get_collection_search_history(max_results=max_results, username=username, start=start)

Retrieve the search history

Retrieves a list of searches made by a particular user, include \"Collection search \" and \"Item and collection search\". The results are ordered according to timestamp, with the latest searches being first. Duplicate queries will not be retrieved.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
max_results = 10 # int | The maximum number of searches that will be retrieved.  The value must be between 1 and 50. (optional) (default to 10)
username = 'username_example' # str | The name of the user that has performed the searched.  If not specified, the user performing the request will be selected. (optional)
start = 'start_example' # str | If set, only searches made after this date will be retrieved. (optional)

try:
    # Retrieve the search history
    api_response = api_instance.get_collection_search_history(max_results=max_results, username=username, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get_collection_search_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_results** | **int**| The maximum number of searches that will be retrieved.  The value must be between 1 and 50. | [optional] [default to 10]
 **username** | **str**| The name of the user that has performed the searched.  If not specified, the user performing the request will be selected. | [optional] 
 **start** | **str**| If set, only searches made after this date will be retrieved. | [optional] 

### Return type

[**SearchHistoryListType**](SearchHistoryListType.md)

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

# **get_collections**
> CollectionListType get_collections(language=language, track=track, conflict=conflict, merged_extradata=merged_extradata, first=first, content=content, interval=interval, cursor=cursor, merged_permission=merged_permission, sample_rate=sample_rate, include_transient_metadata=include_transient_metadata, merged_type=merged_type, terse=terse, default_value=default_value, number=number, count=count, group=group, field=field, include=include, revision=revision, include_values=include_values)

List all collections

Retrieves a list of all known collections.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
merged_extradata = 'merged_extradata_example' # str | Any possible extra data. (optional)
first = 1 # int | From the resulting list of items, start return list from specified offset. (optional) (default to 1)
content = ['content_example'] # list[str] | Comma-separated list of additional content to retrieve. (optional)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
cursor = 'cursor_example' # str | New in version 4. 16.   - `*` - The initial cursor.  - `string-from-search` - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When `cursor` is used, The value of `first` will be ignored.  Only metadata searches in the `generic` interval supports `cursor`. (optional)
merged_permission = 'merged_permission_example' # str | The lowest required permission level. (optional)
sample_rate = 'sample_rate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
include_transient_metadata = True # bool | - `true` (default) - Include transient metadata.  - `false` - Do not include transient metadata in response. (optional) (default to True)
merged_type = 'merged_type_example' # str | The type of operation to check for. (optional)
terse = 'no' # str | - `yes` - Return metadata in terse format.  - `no` (default) - Return metadata in verbose format. (optional) (default to 'no')
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
number = 100 # int | The number of entities to fetch. (optional) (default to 100)
count = True # bool | - `true` (default) - Return hits in result.  - `false` - Do not return hits in result, in order to produce results faster. (optional) (default to True)
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = 'include_example' # str | A list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)
revision = 'revision_example' # str | Specifying what revision of metadata to display.  Only used if requesting a single item or collection. (optional)
include_values = True # bool | Return the value enumeration for each metadata field. (optional)

try:
    # List all collections
    api_response = api_instance.get_collections(language=language, track=track, conflict=conflict, merged_extradata=merged_extradata, first=first, content=content, interval=interval, cursor=cursor, merged_permission=merged_permission, sample_rate=sample_rate, include_transient_metadata=include_transient_metadata, merged_type=merged_type, terse=terse, default_value=default_value, number=number, count=count, group=group, field=field, include=include, revision=revision, include_values=include_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **track** | [**list[str]**](str.md)| Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is &#x60;A2&#x60;.  - *track-type* *t1* &#x60;-&#x60; *t2* - Return metadata for specified track interval, e. g.  &#x60;A2-4&#x60;.  - *track-type* &#x60;*&#x60; - Return metadata for all tracks of specified type, e. g.  &#x60;A*&#x60;.  - &#x60;generic&#x60; - Return all non-tracked metadata.  - &#x60;all&#x60; (default) - All metadata, with or without track specification, are returned. | [optional] [default to [&quot;all&quot;]]
 **conflict** | **str**| - &#x60;yes&#x60; (default) - Include all metadata conflicts, unresolved.  - &#x60;no&#x60; - Return conflicts resolved according to field rules. | [optional] [default to &#39;yes&#39;]
 **merged_extradata** | **str**| Any possible extra data. | [optional] 
 **first** | **int**| From the resulting list of items, start return list from specified offset. | [optional] [default to 1]
 **content** | [**list[str]**](str.md)| Comma-separated list of additional content to retrieve. | [optional] 
 **interval** | [**list[str]**](str.md)| Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - &#x60;generic&#x60; - Return all non-timed metadata.  - &#x60;all&#x60; (default) - Return all metadata, same as &#x60;interval&#x3D;generic,-INF-+INF&#x60; | [optional] [default to [&quot;all&quot;]]
 **cursor** | **str**| New in version 4. 16.   - &#x60;*&#x60; - The initial cursor.  - &#x60;string-from-search&#x60; - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When &#x60;cursor&#x60; is used, The value of &#x60;first&#x60; will be ignored.  Only metadata searches in the &#x60;generic&#x60; interval supports &#x60;cursor&#x60;. | [optional] 
 **merged_permission** | **str**| The lowest required permission level. | [optional] 
 **sample_rate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **include_transient_metadata** | **bool**| - &#x60;true&#x60; (default) - Include transient metadata.  - &#x60;false&#x60; - Do not include transient metadata in response. | [optional] [default to True]
 **merged_type** | **str**| The type of operation to check for. | [optional] 
 **terse** | **str**| - &#x60;yes&#x60; - Return metadata in terse format.  - &#x60;no&#x60; (default) - Return metadata in verbose format. | [optional] [default to &#39;no&#39;]
 **default_value** | **bool**| - &#x60;true&#x60; - For unset fields, return default values.  - &#x60;false&#x60; (default) - Do not return default values. | [optional] [default to False]
 **number** | **int**| The number of entities to fetch. | [optional] [default to 100]
 **count** | **bool**| - &#x60;true&#x60; (default) - Return hits in result.  - &#x60;false&#x60; - Do not return hits in result, in order to produce results faster. | [optional] [default to True]
 **group** | [**list[str]**](str.md)| Comma-separated list.   - *group-name* - Return specified group.  - *group-name* &#x60;+&#x60; - Return specified group and subgroups.  - *group-name* &#x60;:&#x60; *new-name* - Return specified group, renamed to a new name in return value.  - &#x60;-&#x60; *group-name* - Exclude specified group.  - (default) - Return all groups. | [optional] 
 **field** | [**list[str]**](str.md)| Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \&quot;:\&quot; *new-name* - Return specified field, renamed to a new name in return value.  - \&quot;-\&quot; *field-name* - Exclude specified field.  - (default) - Return all fields. | [optional] 
 **include** | **str**| A list of keys.   Includes additional field specific data.  Additionally, if set to &#x60;type&#x60; the type definition of the field will be retrieved. | [optional] 
 **revision** | **str**| Specifying what revision of metadata to display.  Only used if requesting a single item or collection. | [optional] 
 **include_values** | **bool**| Return the value enumeration for each metadata field. | [optional] 

### Return type

[**CollectionListType**](CollectionListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_from_collection**
> remove_from_collection(collection_id, id, type=type)

Remove an item, library or collection from a collection

Attempts to remove specific content with the id, `id`, from a collection with the id `collection-id`.  Note that the object corresponding to the id is not altered.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.
id = 'id_example' # str | The id.
type = 'item' # str | - `collection` - The object identified by `id` is a collection.  - `item` (default) - The object identified by `id` is an item.  - `library` - The object identified by `id` is a library. (optional) (default to 'item')

try:
    # Remove an item, library or collection from a collection
    api_instance.remove_from_collection(collection_id, id, type=type)
except ApiException as e:
    print("Exception when calling CollectionApi->remove_from_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 
 **id** | **str**| The id. | 
 **type** | **str**| - &#x60;collection&#x60; - The object identified by &#x60;id&#x60; is a collection.  - &#x60;item&#x60; (default) - The object identified by &#x60;id&#x60; is an item.  - &#x60;library&#x60; - The object identified by &#x60;id&#x60; is a library. | [optional] [default to &#39;item&#39;]

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

# **reorder_collection_elements**
> CollectionType reorder_collection_elements(collection_id, collection_reorder_type)

Reorder collection elements

Changes the order of the elements. Note that the reordering elements are parsed and applied in the sequence that they are supplied.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.
collection_reorder_type = vidispine.CollectionReorderType() # CollectionReorderType | <em>CollectionReorderDocument</em> containing the changes to the order.

try:
    # Reorder collection elements
    api_response = api_instance.reorder_collection_elements(collection_id, collection_reorder_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->reorder_collection_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 
 **collection_reorder_type** | [**CollectionReorderType**](CollectionReorderType.md)| &lt;em&gt;CollectionReorderDocument&lt;/em&gt; containing the changes to the order. | 

### Return type

[**CollectionType**](CollectionType.md)

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

# **search_collections**
> CollectionListType search_collections(item_search_type, language=language, track=track, conflict=conflict, merged_extradata=merged_extradata, first=first, content=content, interval=interval, cursor=cursor, merged_permission=merged_permission, sample_rate=sample_rate, include_transient_metadata=include_transient_metadata, merged_type=merged_type, terse=terse, default_value=default_value, number=number, count=count, group=group, field=field, include=include, revision=revision, include_values=include_values)

Search for collections

Searches for collections that matches the query.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
item_search_type = vidispine.ItemSearchType() # ItemSearchType | 
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
merged_extradata = 'merged_extradata_example' # str | Any possible extra data. (optional)
first = 1 # int | The index of the first collection. (optional) (default to 1)
content = ['content_example'] # list[str] | Comma-separated list of additional content to retrieve. (optional)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
cursor = 'cursor_example' # str | New in version 4. 16.   - `*` - The initial cursor.  - `string-from-search` - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When `cursor` is used, The value of `first` will be ignored.  Only metadata searches in the `generic` interval supports `cursor`. (optional)
merged_permission = 'merged_permission_example' # str | The lowest required permission level. (optional)
sample_rate = 'sample_rate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
include_transient_metadata = True # bool | - `true` (default) - Include transient metadata.  - `false` - Do not include transient metadata in response. (optional) (default to True)
merged_type = 'merged_type_example' # str | The type of operation to check for. (optional)
terse = 'no' # str | - `yes` - Return metadata in terse format.  - `no` (default) - Return metadata in verbose format. (optional) (default to 'no')
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
number = 100 # int | The number of collections to retrieve. (optional) (default to 100)
count = True # bool | - `true` (default) - Return hits in result.  - `false` - Do not return hits in result, in order to produce results faster. (optional) (default to True)
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = 'include_example' # str | A list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)
revision = 'revision_example' # str | Specifying what revision of metadata to display.  Only used if requesting a single item or collection. (optional)
include_values = True # bool | Return the value enumeration for each metadata field. (optional)

try:
    # Search for collections
    api_response = api_instance.search_collections(item_search_type, language=language, track=track, conflict=conflict, merged_extradata=merged_extradata, first=first, content=content, interval=interval, cursor=cursor, merged_permission=merged_permission, sample_rate=sample_rate, include_transient_metadata=include_transient_metadata, merged_type=merged_type, terse=terse, default_value=default_value, number=number, count=count, group=group, field=field, include=include, revision=revision, include_values=include_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->search_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_search_type** | [**ItemSearchType**](ItemSearchType.md)|  | 
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **track** | [**list[str]**](str.md)| Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is &#x60;A2&#x60;.  - *track-type* *t1* &#x60;-&#x60; *t2* - Return metadata for specified track interval, e. g.  &#x60;A2-4&#x60;.  - *track-type* &#x60;*&#x60; - Return metadata for all tracks of specified type, e. g.  &#x60;A*&#x60;.  - &#x60;generic&#x60; - Return all non-tracked metadata.  - &#x60;all&#x60; (default) - All metadata, with or without track specification, are returned. | [optional] [default to [&quot;all&quot;]]
 **conflict** | **str**| - &#x60;yes&#x60; (default) - Include all metadata conflicts, unresolved.  - &#x60;no&#x60; - Return conflicts resolved according to field rules. | [optional] [default to &#39;yes&#39;]
 **merged_extradata** | **str**| Any possible extra data. | [optional] 
 **first** | **int**| The index of the first collection. | [optional] [default to 1]
 **content** | [**list[str]**](str.md)| Comma-separated list of additional content to retrieve. | [optional] 
 **interval** | [**list[str]**](str.md)| Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - &#x60;generic&#x60; - Return all non-timed metadata.  - &#x60;all&#x60; (default) - Return all metadata, same as &#x60;interval&#x3D;generic,-INF-+INF&#x60; | [optional] [default to [&quot;all&quot;]]
 **cursor** | **str**| New in version 4. 16.   - &#x60;*&#x60; - The initial cursor.  - &#x60;string-from-search&#x60; - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When &#x60;cursor&#x60; is used, The value of &#x60;first&#x60; will be ignored.  Only metadata searches in the &#x60;generic&#x60; interval supports &#x60;cursor&#x60;. | [optional] 
 **merged_permission** | **str**| The lowest required permission level. | [optional] 
 **sample_rate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **include_transient_metadata** | **bool**| - &#x60;true&#x60; (default) - Include transient metadata.  - &#x60;false&#x60; - Do not include transient metadata in response. | [optional] [default to True]
 **merged_type** | **str**| The type of operation to check for. | [optional] 
 **terse** | **str**| - &#x60;yes&#x60; - Return metadata in terse format.  - &#x60;no&#x60; (default) - Return metadata in verbose format. | [optional] [default to &#39;no&#39;]
 **default_value** | **bool**| - &#x60;true&#x60; - For unset fields, return default values.  - &#x60;false&#x60; (default) - Do not return default values. | [optional] [default to False]
 **number** | **int**| The number of collections to retrieve. | [optional] [default to 100]
 **count** | **bool**| - &#x60;true&#x60; (default) - Return hits in result.  - &#x60;false&#x60; - Do not return hits in result, in order to produce results faster. | [optional] [default to True]
 **group** | [**list[str]**](str.md)| Comma-separated list.   - *group-name* - Return specified group.  - *group-name* &#x60;+&#x60; - Return specified group and subgroups.  - *group-name* &#x60;:&#x60; *new-name* - Return specified group, renamed to a new name in return value.  - &#x60;-&#x60; *group-name* - Exclude specified group.  - (default) - Return all groups. | [optional] 
 **field** | [**list[str]**](str.md)| Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \&quot;:\&quot; *new-name* - Return specified field, renamed to a new name in return value.  - \&quot;-\&quot; *field-name* - Exclude specified field.  - (default) - Return all fields. | [optional] 
 **include** | **str**| A list of keys.   Includes additional field specific data.  Additionally, if set to &#x60;type&#x60; the type definition of the field will be retrieved. | [optional] 
 **revision** | **str**| Specifying what revision of metadata to display.  Only used if requesting a single item or collection. | [optional] 
 **include_values** | **bool**| Return the value enumeration for each metadata field. | [optional] 

### Return type

[**CollectionListType**](CollectionListType.md)

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

# **search_items_in_collection**
> ItemListType search_items_in_collection(collection_id, item_search_type, language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, update_frequency=update_frequency, number=number, interval=interval, group=group, merged_permission=merged_permission, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, uri_type=uri_type, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, q=q, p=p, library=library, base_uri=base_uri, merged_extradata=merged_extradata, result=result, storage=storage, revision=revision, url=url, scheme=scheme, auto_refresh=auto_refresh, version=version, cursor=cursor, include_values=include_values, sample_rate=sample_rate, library_id=library_id, count=count, save=save, noauth_url=noauth_url, update_mode=update_mode)

Search for items within a collection

Performs a search among the items in the specified collection.  Queries on collection items will now return items in creation order by default. See `indexCollectionItemOrder` on how to revert back to using the insert/custom collection item ordering.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.
item_search_type = vidispine.ItemSearchType() # ItemSearchType | 
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
first = 1 # int | From the resulting list of items, start return list from specified offset. (optional) (default to 1)
closed_files = True # bool | A URI parameter:  - `true` (default) - Return only URIs that point to closed files.  - `false` - Return all URIs. (optional) (default to True)
terse = 'no' # str | - `yes` - Return metadata in terse format.  - `no` (default) - Return metadata in verbose format. (optional) (default to 'no')
method_metadata = 'method_metadata_example' # str | Metadata used with storage method. (optional)
update_frequency = 'update_frequency_example' # str | When creating a library, use this update frequency.  Defaults to no periodic updates. (optional)
number = 100 # int | The number of entities to fetch. (optional) (default to 100)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
merged_permission = 'merged_permission_example' # str | The lowest required permission level. (optional)
storage_group = 'storage_group_example' # str | Storage group id.  Return only files from storages specified in the storage group. (optional)
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
starttc = False # bool | - `true` - Interval is given relative to start timecode of item.  - `false` (default) - Interval is 0-based. (optional) (default to False)
content = ['content_example'] # list[str] | Comma-separated list of the types of content to retrieve. (optional)
uri_type = ['uri_type_example'] # list[str] | Comma-separated list of format types (container format) to return. (optional)
include_transient_metadata = True # bool | - `true` (default) - Include transient metadata.  - `false` - Do not include transient metadata in response. (optional) (default to True)
merged_type = 'merged_type_example' # str | The type of operation to check for. (optional)
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
tag = 'tag_example' # str | A URI parameter: Comma-separated list of shape tags to return. (optional)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = 'include_example' # str | A list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)
method_type = 'method_type_example' # str | Access method.   - `AUTO` - Gives an APInoauth URI to the media.  Access to file is tunneled through Vidispine.  - `AZURE_SAS` - If the storage schema is azure:// you can get direct access to the media.  The resulting URI will not tunnel through Vidispine but rather point directly to the media location at the azure storage. (optional)
q = 'q_example' # str | XML/JSON, *ItemSearchDocument*.  Only with GET. (optional)
p = ['p_example'] # list[str] | Comma-separated list of paths specifying the content to include.  Overrides the content and filter parameters. (optional)
library = '*' # str | Restricts search to within library, identifier. (optional) (default to '*')
base_uri = 'base_uri_example' # str | Which base URI to use for the thumbnail URLs. (optional)
merged_extradata = 'merged_extradata_example' # str | Any possible extra data. (optional)
result = 'list' # str | - `list` (default) - Return a list of items.  - `library` - Create a library with the matching items. (optional) (default to 'list')
storage = ['storage_example'] # list[str] | List of storage ids.  Return only files from specific storages.  Can be specified multiple times. (optional)
revision = 'revision_example' # str | Specifying which metadata revision to display.  Only used if requesting a single item or collection. (optional)
url = False # bool | - `true` - Return list of URLs.  - `false` (default) - Return list of ids. (optional) (default to False)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
auto_refresh = False # bool | When creating a library, make it self-refresh. (optional) (default to False)
version = 'version_example' # str | Specifying which essence version to return for shapes.  If special value `all`, display all versions.  If special value `latest` (default), display latest version of shapes. (optional)
cursor = 'cursor_example' # str | New in version 4. 16.   - `*` - The initial cursor.  - `string-from-search` - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When `cursor` is used, The value of `first` will be ignored.  Only metadata searches in the `generic` interval supports `cursor`. (optional)
include_values = True # bool | Return the value enumeration for each metadata field. (optional)
sample_rate = 'sample_rate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
library_id = 'library_id_example' # str | If set, the library identified by this id will be used instead of creating a new library. (optional)
count = True # bool | - `true` (default) - Return hits in result.  - `false` - Do not return hits in result, in order to produce results faster. (optional) (default to True)
save = True # bool | - `true` - Returns a `303 See Other`, with a `Location` header containing an URI to fetch the search result - `false` (default) - Returns a regular search result (optional)
noauth_url = True # bool | - `true` Return URIs that do not need authentication.  - `false` (default) Return normal URIs (optional)
update_mode = 'MERGE' # str | When creating a library, use this update mode. (optional) (default to 'MERGE')

try:
    # Search for items within a collection
    api_response = api_instance.search_items_in_collection(collection_id, item_search_type, language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, update_frequency=update_frequency, number=number, interval=interval, group=group, merged_permission=merged_permission, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, uri_type=uri_type, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, q=q, p=p, library=library, base_uri=base_uri, merged_extradata=merged_extradata, result=result, storage=storage, revision=revision, url=url, scheme=scheme, auto_refresh=auto_refresh, version=version, cursor=cursor, include_values=include_values, sample_rate=sample_rate, library_id=library_id, count=count, save=save, noauth_url=noauth_url, update_mode=update_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->search_items_in_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 
 **item_search_type** | [**ItemSearchType**](ItemSearchType.md)|  | 
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **first** | **int**| From the resulting list of items, start return list from specified offset. | [optional] [default to 1]
 **closed_files** | **bool**| A URI parameter:  - &#x60;true&#x60; (default) - Return only URIs that point to closed files.  - &#x60;false&#x60; - Return all URIs. | [optional] [default to True]
 **terse** | **str**| - &#x60;yes&#x60; - Return metadata in terse format.  - &#x60;no&#x60; (default) - Return metadata in verbose format. | [optional] [default to &#39;no&#39;]
 **method_metadata** | **str**| Metadata used with storage method. | [optional] 
 **update_frequency** | **str**| When creating a library, use this update frequency.  Defaults to no periodic updates. | [optional] 
 **number** | **int**| The number of entities to fetch. | [optional] [default to 100]
 **interval** | [**list[str]**](str.md)| Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - &#x60;generic&#x60; - Return all non-timed metadata.  - &#x60;all&#x60; (default) - Return all metadata, same as &#x60;interval&#x3D;generic,-INF-+INF&#x60; | [optional] [default to [&quot;all&quot;]]
 **group** | [**list[str]**](str.md)| Comma-separated list.   - *group-name* - Return specified group.  - *group-name* &#x60;+&#x60; - Return specified group and subgroups.  - *group-name* &#x60;:&#x60; *new-name* - Return specified group, renamed to a new name in return value.  - &#x60;-&#x60; *group-name* - Exclude specified group.  - (default) - Return all groups. | [optional] 
 **merged_permission** | **str**| The lowest required permission level. | [optional] 
 **storage_group** | **str**| Storage group id.  Return only files from storages specified in the storage group. | [optional] 
 **track** | [**list[str]**](str.md)| Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is &#x60;A2&#x60;.  - *track-type* *t1* &#x60;-&#x60; *t2* - Return metadata for specified track interval, e. g.  &#x60;A2-4&#x60;.  - *track-type* &#x60;*&#x60; - Return metadata for all tracks of specified type, e. g.  &#x60;A*&#x60;.  - &#x60;generic&#x60; - Return all non-tracked metadata.  - &#x60;all&#x60; (default) - All metadata, with or without track specification, are returned. | [optional] [default to [&quot;all&quot;]]
 **conflict** | **str**| - &#x60;yes&#x60; (default) - Include all metadata conflicts, unresolved.  - &#x60;no&#x60; - Return conflicts resolved according to field rules. | [optional] [default to &#39;yes&#39;]
 **starttc** | **bool**| - &#x60;true&#x60; - Interval is given relative to start timecode of item.  - &#x60;false&#x60; (default) - Interval is 0-based. | [optional] [default to False]
 **content** | [**list[str]**](str.md)| Comma-separated list of the types of content to retrieve. | [optional] 
 **uri_type** | [**list[str]**](str.md)| Comma-separated list of format types (container format) to return. | [optional] 
 **include_transient_metadata** | **bool**| - &#x60;true&#x60; (default) - Include transient metadata.  - &#x60;false&#x60; - Do not include transient metadata in response. | [optional] [default to True]
 **merged_type** | **str**| The type of operation to check for. | [optional] 
 **default_value** | **bool**| - &#x60;true&#x60; - For unset fields, return default values.  - &#x60;false&#x60; (default) - Do not return default values. | [optional] [default to False]
 **tag** | **str**| A URI parameter: Comma-separated list of shape tags to return. | [optional] 
 **field** | [**list[str]**](str.md)| Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \&quot;:\&quot; *new-name* - Return specified field, renamed to a new name in return value.  - \&quot;-\&quot; *field-name* - Exclude specified field.  - (default) - Return all fields. | [optional] 
 **include** | **str**| A list of keys.   Includes additional field specific data.  Additionally, if set to &#x60;type&#x60; the type definition of the field will be retrieved. | [optional] 
 **method_type** | **str**| Access method.   - &#x60;AUTO&#x60; - Gives an APInoauth URI to the media.  Access to file is tunneled through Vidispine.  - &#x60;AZURE_SAS&#x60; - If the storage schema is azure:// you can get direct access to the media.  The resulting URI will not tunnel through Vidispine but rather point directly to the media location at the azure storage. | [optional] 
 **q** | **str**| XML/JSON, *ItemSearchDocument*.  Only with GET. | [optional] 
 **p** | [**list[str]**](str.md)| Comma-separated list of paths specifying the content to include.  Overrides the content and filter parameters. | [optional] 
 **library** | **str**| Restricts search to within library, identifier. | [optional] [default to &#39;*&#39;]
 **base_uri** | **str**| Which base URI to use for the thumbnail URLs. | [optional] 
 **merged_extradata** | **str**| Any possible extra data. | [optional] 
 **result** | **str**| - &#x60;list&#x60; (default) - Return a list of items.  - &#x60;library&#x60; - Create a library with the matching items. | [optional] [default to &#39;list&#39;]
 **storage** | [**list[str]**](str.md)| List of storage ids.  Return only files from specific storages.  Can be specified multiple times. | [optional] 
 **revision** | **str**| Specifying which metadata revision to display.  Only used if requesting a single item or collection. | [optional] 
 **url** | **bool**| - &#x60;true&#x60; - Return list of URLs.  - &#x60;false&#x60; (default) - Return list of ids. | [optional] [default to False]
 **scheme** | **str**| URI scheme to return. | [optional] 
 **auto_refresh** | **bool**| When creating a library, make it self-refresh. | [optional] [default to False]
 **version** | **str**| Specifying which essence version to return for shapes.  If special value &#x60;all&#x60;, display all versions.  If special value &#x60;latest&#x60; (default), display latest version of shapes. | [optional] 
 **cursor** | **str**| New in version 4. 16.   - &#x60;*&#x60; - The initial cursor.  - &#x60;string-from-search&#x60; - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When &#x60;cursor&#x60; is used, The value of &#x60;first&#x60; will be ignored.  Only metadata searches in the &#x60;generic&#x60; interval supports &#x60;cursor&#x60;. | [optional] 
 **include_values** | **bool**| Return the value enumeration for each metadata field. | [optional] 
 **sample_rate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **library_id** | **str**| If set, the library identified by this id will be used instead of creating a new library. | [optional] 
 **count** | **bool**| - &#x60;true&#x60; (default) - Return hits in result.  - &#x60;false&#x60; - Do not return hits in result, in order to produce results faster. | [optional] [default to True]
 **save** | **bool**| - &#x60;true&#x60; - Returns a &#x60;303 See Other&#x60;, with a &#x60;Location&#x60; header containing an URI to fetch the search result - &#x60;false&#x60; (default) - Returns a regular search result | [optional] 
 **noauth_url** | **bool**| - &#x60;true&#x60; Return URIs that do not need authentication.  - &#x60;false&#x60; (default) Return normal URIs | [optional] 
 **update_mode** | **str**| When creating a library, use this update mode. | [optional] [default to &#39;MERGE&#39;]

### Return type

[**ItemListType**](ItemListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of ids or URLs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection**
> CollectionType update_collection(collection_id, collection_type, clear=clear)

Update a collection

Updates the content of the collection with the id `collection-id` as specified in the document. It is also possible to change the name of the collection  and metadata of the collection-entity relations.  Either all or no entities must have a mode specified. If no entities have a mode specified and the document contains an entity that does not exist in the collection, then the entity will be added.  When no entities have a mode specified the entities will get the same position as they are ordered in the document.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
collection_id = 'collection_id_example' # str | The collection id.
collection_type = vidispine.CollectionType() # CollectionType | <em>CollectionDocument</em> that contains the entity ids.
clear = True # bool | - `true` (default) - All entities that are in the collection but not specified in the document will be removed.  Only has any effect when no entities have a mode specified.  - `false` - All entities in the document will be appended to the collection.  If an entity already exist in the collection then the position is determined by the document.  Only has any effect when no entities have a mode specified. (optional) (default to True)

try:
    # Update a collection
    api_response = api_instance.update_collection(collection_id, collection_type, clear=clear)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->update_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 
 **collection_type** | [**CollectionType**](CollectionType.md)| &lt;em&gt;CollectionDocument&lt;/em&gt; that contains the entity ids. | 
 **clear** | **bool**| - &#x60;true&#x60; (default) - All entities that are in the collection but not specified in the document will be removed.  Only has any effect when no entities have a mode specified.  - &#x60;false&#x60; - All entities in the document will be appended to the collection.  If an entity already exist in the collection then the position is determined by the document.  Only has any effect when no entities have a mode specified. | [optional] [default to True]

### Return type

[**CollectionType**](CollectionType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;CollectionDocument&lt;/em&gt; containing the collection name and the entities in order. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection_folder_name**
> str update_collection_folder_name(name, collection_id)

Report that the folder name has changed on disk

If the folder name has been changed by a user or an external program, it can be reported to Vidispine with this command. The affected file entities in the database will then be updated with the new path, and the collection name will be changed.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The new name of the folder.
collection_id = 'collection_id_example' # str | The collection id.

try:
    # Report that the folder name has changed on disk
    api_response = api_instance.update_collection_folder_name(name, collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->update_collection_folder_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The new name of the folder. | 
 **collection_id** | **str**| The collection id. | 

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
**0** | \&quot;OK\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection_name**
> update_collection_name(name, collection_id)

Update collection name

Sets the name of the collection with the identifier `collection-id`.

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
api_instance = vidispine.CollectionApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | New name of the collection.
collection_id = 'collection_id_example' # str | The collection id.

try:
    # Update collection name
    api_instance.update_collection_name(name, collection_id)
except ApiException as e:
    print("Exception when calling CollectionApi->update_collection_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| New name of the collection. | 
 **collection_id** | **str**| The collection id. | 

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

