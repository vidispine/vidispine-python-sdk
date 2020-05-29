# vidispine.LibraryApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_to_library**](LibraryApi.md#add_item_to_library) | **PUT** /library/{library-id}/{item-id} | Add an item to a library
[**create_library**](LibraryApi.md#create_library) | **POST** /library | Create a library
[**create_library_export_job**](LibraryApi.md#create_library_export_job) | **POST** /library/{library-id}/export | Start an export job for a collection or a library
[**create_library_item_listing_job**](LibraryApi.md#create_library_item_listing_job) | **POST** /library/{library-id}/list | Creating an item list job
[**delete_item_from_library**](LibraryApi.md#delete_item_from_library) | **DELETE** /library/{library-id}/{item-id} | Remove an item from a library
[**delete_libraries**](LibraryApi.md#delete_libraries) | **DELETE** /library | Delete multiple libraries
[**delete_library**](LibraryApi.md#delete_library) | **DELETE** /library/{library-id} | Delete a library
[**delete_library_metadata**](LibraryApi.md#delete_library_metadata) | **DELETE** /library/{library-id}/metadata | Delete all key-value pairs
[**delete_library_metadata_key**](LibraryApi.md#delete_library_metadata_key) | **DELETE** /library/{library-id}/metadata/{keypath} | Delete key-value pairs
[**get_libraries**](LibraryApi.md#get_libraries) | **GET** /library | List all libraries
[**get_library**](LibraryApi.md#get_library) | **GET** /library/{library-id} | Retrieve library content
[**get_library_metadata**](LibraryApi.md#get_library_metadata) | **GET** /library/{library-id}/metadata | Retrieve all metadata
[**get_library_metadata_key**](LibraryApi.md#get_library_metadata_key) | **GET** /library/{library-id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_library_settings**](LibraryApi.md#get_library_settings) | **GET** /library/{library-id}/settings | Retrieve library settings
[**update_library_content**](LibraryApi.md#update_library_content) | **PUT** /library/{library-id} | Add multiple items to a library
[**update_library_item_metadata**](LibraryApi.md#update_library_item_metadata) | **PUT** /library/{library-id}/item-metadata | Modify metadata of the items in a specific library
[**update_library_metadata**](LibraryApi.md#update_library_metadata) | **PUT** /library/{library-id}/metadata | Create multiple key-value pairs
[**update_library_metadata_key**](LibraryApi.md#update_library_metadata_key) | **PUT** /library/{library-id}/metadata/{keypath} | Set the value for a specific key
[**update_library_settings**](LibraryApi.md#update_library_settings) | **PUT** /library/{library-id}/settings | Update library settings


# **add_item_to_library**
> add_item_to_library(library_id, item_id)

Add an item to a library

Adds the specified item to the library.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
item_id = 'item_id_example' # str | The item id.

try:
    # Add an item to a library
    api_instance.add_item_to_library(library_id, item_id)
except ApiException as e:
    print("Exception when calling LibraryApi->add_item_to_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
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

# **create_library**
> URIListType create_library(item_list_type, external_id=external_id)

Create a library

Creates a library and returns the id of the created library.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
item_list_type = vidispine.ItemListType() # ItemListType | <em>ItemListDocument</em> that contains the ids of any items that should be added to the library
external_id = 'external_id_example' # str | An external identifier to assign to the library. (optional)

try:
    # Create a library
    api_response = api_instance.create_library(item_list_type, external_id=external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->create_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_list_type** | [**ItemListType**](ItemListType.md)| &lt;em&gt;ItemListDocument&lt;/em&gt; that contains the ids of any items that should be added to the library | 
 **external_id** | **str**| An external identifier to assign to the library. | [optional] 

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

# **create_library_export_job**
> JobType create_library_export_job(library_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, tag=tag, all=all, projection=projection, use_original_component_filename=use_original_component_filename, notification=notification, priority=priority, version=version, uri=uri, metadata=metadata, template=template, location_name=location_name)

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
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
    api_response = api_instance.create_library_export_job(library_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, tag=tag, all=all, projection=projection, use_original_component_filename=use_original_component_filename, notification=notification, priority=priority, version=version, uri=uri, metadata=metadata, template=template, location_name=location_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->create_library_export_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
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

# **create_library_item_listing_job**
> JobType create_library_item_listing_job(destination_uri, library_id, item_list_type, jobmetadata=jobmetadata, p=p, output_format=output_format, data=data, notification=notification, notification_data=notification_data, field=field, priority=priority)

Creating an item list job

Starts a new job that goes through all the items in the specific library and outputs a file to the supplied URI.  The output format depends on the specified parameter, if set to XML an *ItemListDocument* will be produced. Furthermore if an XSLT is given the *ItemListDocument* will be transformed.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
destination_uri = 'destination_uri_example' # str | The URI to output the CSV file to.
library_id = 'library_id_example' # str | The library id.
item_list_type = vidispine.ItemListType() # ItemListType | An optional XSLT capable of transforming <em>ItemListDocument</em>.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
p = ['p_example'] # list[str] | Comma-separated list of paths specifying the content to include.  Overrides the field and data parameters.  Only supported for XML output. (optional)
output_format = 'output_format_example' # str | Specifies the output format. (optional)
data = 'data_example' # str | Specifies any additional data that should be included with the metadata fields. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
field = ['field_example'] # list[str] | Comma-separated list of metadata fields to include in the result. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Creating an item list job
    api_response = api_instance.create_library_item_listing_job(destination_uri, library_id, item_list_type, jobmetadata=jobmetadata, p=p, output_format=output_format, data=data, notification=notification, notification_data=notification_data, field=field, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->create_library_item_listing_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_uri** | **str**| The URI to output the CSV file to. | 
 **library_id** | **str**| The library id. | 
 **item_list_type** | [**ItemListType**](ItemListType.md)| An optional XSLT capable of transforming &lt;em&gt;ItemListDocument&lt;/em&gt;. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **p** | [**list[str]**](str.md)| Comma-separated list of paths specifying the content to include.  Overrides the field and data parameters.  Only supported for XML output. | [optional] 
 **output_format** | **str**| Specifies the output format. | [optional] 
 **data** | **str**| Specifies any additional data that should be included with the metadata fields. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **field** | [**list[str]**](str.md)| Comma-separated list of metadata fields to include in the result. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xslt
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;JobDocument&lt;/em&gt;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_from_library**
> delete_item_from_library(library_id, item_id)

Remove an item from a library

Removes the specified item from the library.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
item_id = 'item_id_example' # str | The item id.

try:
    # Remove an item from a library
    api_instance.delete_item_from_library(library_id, item_id)
except ApiException as e:
    print("Exception when calling LibraryApi->delete_item_from_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
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

# **delete_libraries**
> JobType delete_libraries(id, jobmetadata=jobmetadata, notification_data=notification_data, async=async, notification=notification, priority=priority)

Delete multiple libraries

Deletes the libraries with the specified ids.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
id = ['id_example'] # list[str] | Comma-separated list of library ids or external ids.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
async = False # bool | - `true` - Start a DELETE_LIBRARY job that removes the libraries.  - `false` (default) - Remove the libraries immediately. (optional) (default to False)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Delete multiple libraries
    api_response = api_instance.delete_libraries(id, jobmetadata=jobmetadata, notification_data=notification_data, async=async, notification=notification, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->delete_libraries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| Comma-separated list of library ids or external ids. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **async** | **bool**| - &#x60;true&#x60; - Start a DELETE_LIBRARY job that removes the libraries.  - &#x60;false&#x60; (default) - Remove the libraries immediately. | [optional] [default to False]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]

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
**0** | &lt;em&gt;JobDocument&lt;/em&gt; containing library delete job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library**
> JobType delete_library(library_id, jobmetadata=jobmetadata, notification_data=notification_data, async=async, priority=priority, notification=notification)

Delete a library

Deletes the library with the specified id.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
async = False # bool | - `true` - Start a DELETE_LIBRARY job that removes the library.  - `false` (default) - Remove the library immediately. (optional) (default to False)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)

try:
    # Delete a library
    api_response = api_instance.delete_library(library_id, jobmetadata=jobmetadata, notification_data=notification_data, async=async, priority=priority, notification=notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->delete_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **async** | **bool**| - &#x60;true&#x60; - Start a DELETE_LIBRARY job that removes the library.  - &#x60;false&#x60; (default) - Remove the library immediately. | [optional] [default to False]
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
**0** | &lt;em&gt;JobDocument&lt;/em&gt; containing library delete job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_metadata**
> delete_library_metadata(library_id)

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.

try:
    # Delete all key-value pairs
    api_instance.delete_library_metadata(library_id)
except ApiException as e:
    print("Exception when calling LibraryApi->delete_library_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 

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

# **delete_library_metadata_key**
> delete_library_metadata_key(library_id, keypath)

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_library_metadata_key(library_id, keypath)
except ApiException as e:
    print("Exception when calling LibraryApi->delete_library_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
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

# **get_libraries**
> URIListType get_libraries(auto_refresh=auto_refresh, frequency_from=frequency_from, first=first, frequency_to=frequency_to, number=number, update_mode=update_mode)

List all libraries

Retrieves a list of the ids of all known libraries.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
auto_refresh = True # bool | Only list libraries with the specified auto refresh status. (optional)
frequency_from = 56 # int | Only list libraries whose update frequency is greater than it. (optional)
first = 1 # int | From the resulting list of items, start return list from specified offset. (optional) (default to 1)
frequency_to = 56 # int | Only list libraries whose update frequency is less than it. (optional)
number = 100 # int | The number of entities to fetch. (optional) (default to 100)
update_mode = 'update_mode_example' # str | Only list libraries with the specified update mode. (optional)

try:
    # List all libraries
    api_response = api_instance.get_libraries(auto_refresh=auto_refresh, frequency_from=frequency_from, first=first, frequency_to=frequency_to, number=number, update_mode=update_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_libraries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_refresh** | **bool**| Only list libraries with the specified auto refresh status. | [optional] 
 **frequency_from** | **int**| Only list libraries whose update frequency is greater than it. | [optional] 
 **first** | **int**| From the resulting list of items, start return list from specified offset. | [optional] [default to 1]
 **frequency_to** | **int**| Only list libraries whose update frequency is less than it. | [optional] 
 **number** | **int**| The number of entities to fetch. | [optional] [default to 100]
 **update_mode** | **str**| Only list libraries with the specified update mode. | [optional] 

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

# **get_library**
> ItemListType get_library(library_id, language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, number=number, interval=interval, group=group, merged_permission=merged_permission, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, uri_type=uri_type, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, p=p, base_uri=base_uri, merged_extradata=merged_extradata, storage=storage, revision=revision, scheme=scheme, version=version, include_values=include_values, sample_rate=sample_rate, count=count, noauth_url=noauth_url)

Retrieve library content

Returns the items together with any requested data.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
first = 1 # int | From the resulting list of items, start return list from specified offset. (optional) (default to 1)
closed_files = True # bool | A URI parameter:  - `true` (default) - Return only URIs that point to closed files.  - `false` - Return all URIs. (optional) (default to True)
terse = 'no' # str | - `yes` - Return metadata in terse format.  - `no` (default) - Return metadata in verbose format. (optional) (default to 'no')
method_metadata = 'method_metadata_example' # str | Metadata used with storage method. (optional)
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
p = ['p_example'] # list[str] | Comma-separated list of paths specifying the content to include.  Overrides the content and filter parameters. (optional)
base_uri = 'base_uri_example' # str | Which base URI to use for the thumbnail URLs. (optional)
merged_extradata = 'merged_extradata_example' # str | Any possible extra data. (optional)
storage = ['storage_example'] # list[str] | List of storage ids.  Return only files from specific storages.  Can be specified multiple times. (optional)
revision = 'revision_example' # str | Specifying which metadata revision to display.  Only used if requesting a single item or collection. (optional)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
version = 'version_example' # str | Specifying which essence version to return for shapes.  If special value `all`, display all versions.  If special value `latest` (default), display latest version of shapes. (optional)
include_values = True # bool | Return the value enumeration for each metadata field. (optional)
sample_rate = 'sample_rate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
count = True # bool | - `true` (default) - Return hits in result.  - `false` - Do not return hits in result, in order to produce results faster. (optional) (default to True)
noauth_url = True # bool | - `true` Return URIs that do not need authentication.  - `false` (default) Return normal URIs (optional)

try:
    # Retrieve library content
    api_response = api_instance.get_library(library_id, language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, number=number, interval=interval, group=group, merged_permission=merged_permission, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, uri_type=uri_type, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, p=p, base_uri=base_uri, merged_extradata=merged_extradata, storage=storage, revision=revision, scheme=scheme, version=version, include_values=include_values, sample_rate=sample_rate, count=count, noauth_url=noauth_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **first** | **int**| From the resulting list of items, start return list from specified offset. | [optional] [default to 1]
 **closed_files** | **bool**| A URI parameter:  - &#x60;true&#x60; (default) - Return only URIs that point to closed files.  - &#x60;false&#x60; - Return all URIs. | [optional] [default to True]
 **terse** | **str**| - &#x60;yes&#x60; - Return metadata in terse format.  - &#x60;no&#x60; (default) - Return metadata in verbose format. | [optional] [default to &#39;no&#39;]
 **method_metadata** | **str**| Metadata used with storage method. | [optional] 
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
 **p** | [**list[str]**](str.md)| Comma-separated list of paths specifying the content to include.  Overrides the content and filter parameters. | [optional] 
 **base_uri** | **str**| Which base URI to use for the thumbnail URLs. | [optional] 
 **merged_extradata** | **str**| Any possible extra data. | [optional] 
 **storage** | [**list[str]**](str.md)| List of storage ids.  Return only files from specific storages.  Can be specified multiple times. | [optional] 
 **revision** | **str**| Specifying which metadata revision to display.  Only used if requesting a single item or collection. | [optional] 
 **scheme** | **str**| URI scheme to return. | [optional] 
 **version** | **str**| Specifying which essence version to return for shapes.  If special value &#x60;all&#x60;, display all versions.  If special value &#x60;latest&#x60; (default), display latest version of shapes. | [optional] 
 **include_values** | **bool**| Return the value enumeration for each metadata field. | [optional] 
 **sample_rate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **count** | **bool**| - &#x60;true&#x60; (default) - Return hits in result.  - &#x60;false&#x60; - Do not return hits in result, in order to produce results faster. | [optional] [default to True]
 **noauth_url** | **bool**| - &#x60;true&#x60; Return URIs that do not need authentication.  - &#x60;false&#x60; (default) Return normal URIs | [optional] 

### Return type

[**ItemListType**](ItemListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;ItemListDocument&lt;/em&gt; containing the items together with the requested data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_metadata**
> SimpleMetadataType get_library_metadata(library_id)

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_library_metadata(library_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_library_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 

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

# **get_library_metadata_key**
> str get_library_metadata_key(library_id, keypath)

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_library_metadata_key(library_id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_library_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
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

# **get_library_settings**
> LibrarySettingsType get_library_settings(library_id)

Retrieve library settings

Retrieves the settings and status of a library.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.

try:
    # Retrieve library settings
    api_response = api_instance.get_library_settings(library_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_library_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 

### Return type

[**LibrarySettingsType**](LibrarySettingsType.md)

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

# **update_library_content**
> update_library_content(library_id, item_list_type)

Add multiple items to a library

Adds all the items specified in the document to the library.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
item_list_type = vidispine.ItemListType() # ItemListType | <em>ItemListDocument</em> that contains the item ids.

try:
    # Add multiple items to a library
    api_instance.update_library_content(library_id, item_list_type)
except ApiException as e:
    print("Exception when calling LibraryApi->update_library_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
 **item_list_type** | [**ItemListType**](ItemListType.md)| &lt;em&gt;ItemListDocument&lt;/em&gt; that contains the item ids. | 

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

# **update_library_item_metadata**
> JobType update_library_item_metadata(library_id, metadata_type, jobmetadata=jobmetadata, notification_data=notification_data, priority=priority, notification=notification)

Modify metadata of the items in a specific library

Modify metadata of the items in a specific library

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
metadata_type = vidispine.MetadataType() # MetadataType | <em>MetadataDocument</em> the metadata to apply to the items.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)

try:
    # Modify metadata of the items in a specific library
    api_response = api_instance.update_library_item_metadata(library_id, metadata_type, jobmetadata=jobmetadata, notification_data=notification_data, priority=priority, notification=notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->update_library_item_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
 **metadata_type** | [**MetadataType**](MetadataType.md)| &lt;em&gt;MetadataDocument&lt;/em&gt; the metadata to apply to the items. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_metadata**
> update_library_metadata(library_id, simple_metadata_type)

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_library_metadata(library_id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling LibraryApi->update_library_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
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

# **update_library_metadata_key**
> update_library_metadata_key(library_id, keypath, body)

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_library_metadata_key(library_id, keypath, body)
except ApiException as e:
    print("Exception when calling LibraryApi->update_library_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
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

# **update_library_settings**
> update_library_settings(library_id, library_settings_type)

Update library settings

Update the settings of a library.

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
api_instance = vidispine.LibraryApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
library_settings_type = vidispine.LibrarySettingsType() # LibrarySettingsType | 

try:
    # Update library settings
    api_instance.update_library_settings(library_id, library_settings_type)
except ApiException as e:
    print("Exception when calling LibraryApi->update_library_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
 **library_settings_type** | [**LibrarySettingsType**](LibrarySettingsType.md)|  | 

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

