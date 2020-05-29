# vidispine.ProjectVersionApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_version**](ProjectVersionApi.md#create_project_version) | **POST** /collection/{id}/version | Create a project version collection
[**delete_project_version_asset_document**](ProjectVersionApi.md#delete_project_version_asset_document) | **DELETE** /collection/{id}/definition/{format}/asset | Delete the asset definition
[**delete_project_version_binary**](ProjectVersionApi.md#delete_project_version_binary) | **DELETE** /collection/{id}/definition/{format} | Delete a project version definition
[**delete_project_version_extra_data**](ProjectVersionApi.md#delete_project_version_extra_data) | **DELETE** /collection/{id}/definition/{format}/extradata | Delete the extradata
[**export_project**](ProjectVersionApi.md#export_project) | **POST** /collection/{id}/version/export | Export a project or sequence
[**get_project_definitions**](ProjectVersionApi.md#get_project_definitions) | **GET** /collection/{id}/definition | List all project version definitions
[**get_project_in_format**](ProjectVersionApi.md#get_project_in_format) | **GET** /collection/{id}/version/export | Export a project or sequence
[**get_project_version_asset_document**](ProjectVersionApi.md#get_project_version_asset_document) | **GET** /collection/{id}/definition/{format}/asset | Retrieve the asset definition
[**get_project_version_binary**](ProjectVersionApi.md#get_project_version_binary) | **GET** /collection/{id}/definition/{format} | Retrieve a project version definition
[**get_project_version_extra_data**](ProjectVersionApi.md#get_project_version_extra_data) | **GET** /collection/{id}/definition/{format}/extradata | Retrieve the extradata
[**update_project_definition**](ProjectVersionApi.md#update_project_definition) | **PUT** /collection/{id}/definition/{format} | Update a project version definition
[**update_project_version_asset_document**](ProjectVersionApi.md#update_project_version_asset_document) | **PUT** /collection/{id}/definition/{format}/asset | Update the asset definition
[**update_project_version_extra_data**](ProjectVersionApi.md#update_project_version_extra_data) | **PUT** /collection/{id}/definition/{format}/extradata | Update the extradata


# **create_project_version**
> URIListType create_project_version(id, project_version_type)

Create a project version collection

Creates a new project version collection for a specific project.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
project_version_type = vidispine.ProjectVersionType() # ProjectVersionType | 

try:
    # Create a project version collection
    api_response = api_instance.create_project_version(id, project_version_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->create_project_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **project_version_type** | [**ProjectVersionType**](ProjectVersionType.md)|  | 

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

# **delete_project_version_asset_document**
> delete_project_version_asset_document(id, format)

Delete the asset definition

Deletes an asset document for a specific project version definition.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.

try:
    # Delete the asset definition
    api_instance.delete_project_version_asset_document(id, format)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->delete_project_version_asset_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 

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

# **delete_project_version_binary**
> delete_project_version_binary(id, format)

Delete a project version definition

Deletes a binary representation of the project version.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.

try:
    # Delete a project version definition
    api_instance.delete_project_version_binary(id, format)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->delete_project_version_binary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 

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

# **delete_project_version_extra_data**
> delete_project_version_extra_data(id, format)

Delete the extradata

Deletes the extradata for a specific project version definition.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.

try:
    # Delete the extradata
    api_instance.delete_project_version_extra_data(id, format)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->delete_project_version_extra_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 

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

# **export_project**
> str export_project(id, export_request_type, format=format, to_sequence=to_sequence, dry_run=dry_run, tag=tag, type=type, uri=uri, content=content)

Export a project or sequence

Exports the sequence or project to the requested output format and saves the result at the given location.  For POST /sequence/export the sequence must be specified in the request document.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
export_request_type = vidispine.ExportRequestType() # ExportRequestType | <em>ExportRequestDocument</em> with details on the export.
format = 'format_example' # str | Comma separated list of formats specifying which shapes to reference in the output.  If both tag and format is given, then both must match. (optional)
to_sequence = False # bool | Export as a sequence with an item, instead of as a standalone item (optional) (default to False)
dry_run = False # bool | When set to `true`, any export problems will be returned and no file will be written (optional) (default to False)
tag = 'tag_example' # str | Comma separated list of shape tags specifying which shapes to reference in the output. (optional)
type = 'type_example' # str | The output format. (optional)
uri = 'uri_example' # str | The destination URI. (optional)
content = ['content_example'] # list[str] | Comma-separated list of content to include in the output. (optional)

try:
    # Export a project or sequence
    api_response = api_instance.export_project(id, export_request_type, format=format, to_sequence=to_sequence, dry_run=dry_run, tag=tag, type=type, uri=uri, content=content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->export_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **export_request_type** | [**ExportRequestType**](ExportRequestType.md)| &lt;em&gt;ExportRequestDocument&lt;/em&gt; with details on the export. | 
 **format** | **str**| Comma separated list of formats specifying which shapes to reference in the output.  If both tag and format is given, then both must match. | [optional] 
 **to_sequence** | **bool**| Export as a sequence with an item, instead of as a standalone item | [optional] [default to False]
 **dry_run** | **bool**| When set to &#x60;true&#x60;, any export problems will be returned and no file will be written | [optional] [default to False]
 **tag** | **str**| Comma separated list of shape tags specifying which shapes to reference in the output. | [optional] 
 **type** | **str**| The output format. | [optional] 
 **uri** | **str**| The destination URI. | [optional] 
 **content** | [**list[str]**](str.md)| Comma-separated list of content to include in the output. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: multipart/mixed, application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The response document and the export data. The uri parameter will be ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_definitions**
> str get_project_definitions(id)

List all project version definitions

Returns the format of the definitions that have been stored for a specific project version.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # List all project version definitions
    api_response = api_instance.get_project_definitions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->get_project_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

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
**0** | A CLRF separated list of formats. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_in_format**
> str get_project_in_format(id, format=format, to_sequence=to_sequence, storage=storage, dry_run=dry_run, tag=tag, type=type, item=item, content=content)

Export a project or sequence

Exports the sequence or project to the requested output format and saves the result at the given location.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | Comma separated list of formats specifying which shapes to reference in the output.  If both tag and format is given, then both must match. (optional)
to_sequence = False # bool | Export as a sequence with an item, instead of as a standalone item (optional) (default to False)
storage = ['storage_example'] # list[str] | Comma-separated list of item paths in format `storageId=path`. (optional)
dry_run = False # bool | When set to `true`, any export problems will be returned and no file will be written (optional) (default to False)
tag = 'tag_example' # str | Comma separated list of shape tags specifying which shapes to reference in the output. (optional)
type = 'type_example' # str | The output format. (optional)
item = ['item_example'] # list[str] | Comma-separated list of item paths in format `itemId=path`. (optional)
content = ['content_example'] # list[str] | Comma-separated list of content to include in the output. (optional)

try:
    # Export a project or sequence
    api_response = api_instance.get_project_in_format(id, format=format, to_sequence=to_sequence, storage=storage, dry_run=dry_run, tag=tag, type=type, item=item, content=content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->get_project_in_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| Comma separated list of formats specifying which shapes to reference in the output.  If both tag and format is given, then both must match. | [optional] 
 **to_sequence** | **bool**| Export as a sequence with an item, instead of as a standalone item | [optional] [default to False]
 **storage** | [**list[str]**](str.md)| Comma-separated list of item paths in format &#x60;storageId&#x3D;path&#x60;. | [optional] 
 **dry_run** | **bool**| When set to &#x60;true&#x60;, any export problems will be returned and no file will be written | [optional] [default to False]
 **tag** | **str**| Comma separated list of shape tags specifying which shapes to reference in the output. | [optional] 
 **type** | **str**| The output format. | [optional] 
 **item** | [**list[str]**](str.md)| Comma-separated list of item paths in format &#x60;itemId&#x3D;path&#x60;. | [optional] 
 **content** | [**list[str]**](str.md)| Comma-separated list of content to include in the output. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The export data, in the media type of the format, if &lt;code&gt;dryRun&#x3D;false&lt;/code&gt;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_version_asset_document**
> EssenceMappingsType get_project_version_asset_document(id, format)

Retrieve the asset definition

Returns the asset document that has been stored for a specific project version definition.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.

try:
    # Retrieve the asset definition
    api_response = api_instance.get_project_version_asset_document(id, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->get_project_version_asset_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 

### Return type

[**EssenceMappingsType**](EssenceMappingsType.md)

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

# **get_project_version_binary**
> file get_project_version_binary(id, format)

Retrieve a project version definition

Retrieves a binary representation of the project version.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.

try:
    # Retrieve a project version definition
    api_response = api_instance.get_project_version_binary(id, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->get_project_version_binary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The stored version definition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_version_extra_data**
> file get_project_version_extra_data(id, format)

Retrieve the extradata

Returns the extradata that has been stored for a specific project version definition.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.

try:
    # Retrieve the extradata
    api_response = api_instance.get_project_version_extra_data(id, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->get_project_version_extra_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The binary extradata. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_definition**
> update_project_definition(id, format, body)

Update a project version definition

Updates a binary representation of the project version. The collection must be a project version collection.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.
body = '/path/to/file' # file | The binary version definition

try:
    # Update a project version definition
    api_instance.update_project_definition(id, format, body)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->update_project_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 
 **body** | **file**| The binary version definition | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_version_asset_document**
> update_project_version_asset_document(id, format, essence_mappings_type)

Update the asset definition

Stores an asset document for a specific project version definition. The document should identify the items and files referenced by the definition.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.
essence_mappings_type = vidispine.EssenceMappingsType() # EssenceMappingsType | 

try:
    # Update the asset definition
    api_instance.update_project_version_asset_document(id, format, essence_mappings_type)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->update_project_version_asset_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 
 **essence_mappings_type** | [**EssenceMappingsType**](EssenceMappingsType.md)|  | 

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

# **update_project_version_extra_data**
> update_project_version_extra_data(id, format, body)

Update the extradata

Stores extradata for a specific project version definition.

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
api_instance = vidispine.ProjectVersionApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.
body = '/path/to/file' # file | The binary extradata.

try:
    # Update the extradata
    api_instance.update_project_version_extra_data(id, format, body)
except ApiException as e:
    print("Exception when calling ProjectVersionApi->update_project_version_extra_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 
 **body** | **file**| The binary extradata. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

