# vidispine.SequenceApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_sequence_render_job**](SequenceApi.md#create_item_sequence_render_job) | **POST** /item/{id}/sequence/render | Render a sequence
[**create_sequence_render_job**](SequenceApi.md#create_sequence_render_job) | **POST** /sequence/render | Render a standalone sequence
[**delete_item_sequence**](SequenceApi.md#delete_item_sequence) | **DELETE** /item/{id}/sequence/{format} | Delete a sequence
[**export_item_sequence**](SequenceApi.md#export_item_sequence) | **POST** /item/{id}/sequence/export | Export a project or sequence
[**export_sequence**](SequenceApi.md#export_sequence) | **POST** /sequence/export | Export a project or sequence
[**get_item_sequence**](SequenceApi.md#get_item_sequence) | **GET** /item/{id}/sequence/{format} | Retrieve a sequence
[**get_item_sequence_in_format**](SequenceApi.md#get_item_sequence_in_format) | **GET** /item/{id}/sequence/export | Export a project or sequence
[**get_item_sequences**](SequenceApi.md#get_item_sequences) | **GET** /item/{id}/sequence | List all sequences
[**update_item_metadata_from_sequence**](SequenceApi.md#update_item_metadata_from_sequence) | **POST** /item/{id}/sequence/conform-metadata | Conform metadata
[**update_or_create_item_sequence**](SequenceApi.md#update_or_create_item_sequence) | **PUT** /item/{id}/sequence/{format} | Update or create a sequence


# **create_item_sequence_render_job**
> JobType create_item_sequence_render_job(id, source_tag=source_tag, jobmetadata=jobmetadata, notification_data=notification_data, tag=tag, notification=notification, subtitle_language=subtitle_language, destination_item=destination_item, resource_id=resource_id, priority=priority, original=original)

Render a sequence

Creates a new job that renders the sequence for the given item. The item will contain a new shape with the rendered result once the job is finished.

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
api_instance = vidispine.SequenceApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
source_tag = ['source_tag_example'] # list[str] | The shape tag specifying the shapes to use as input. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
tag = ['tag_example'] # list[str] | The shape tag specifying the format of the rendered sequence. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
subtitle_language = 'subtitle_language_example' # str | The language code specifying the subtitle language to use. (optional)
destination_item = 'destination_item_example' # str | An item id, to which the new new shape will be associated. (optional)
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode.  New in version 4. 16. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)

try:
    # Render a sequence
    api_response = api_instance.create_item_sequence_render_job(id, source_tag=source_tag, jobmetadata=jobmetadata, notification_data=notification_data, tag=tag, notification=notification, subtitle_language=subtitle_language, destination_item=destination_item, resource_id=resource_id, priority=priority, original=original)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->create_item_sequence_render_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **source_tag** | [**list[str]**](str.md)| The shape tag specifying the shapes to use as input. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **tag** | [**list[str]**](str.md)| The shape tag specifying the format of the rendered sequence. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **subtitle_language** | **str**| The language code specifying the subtitle language to use. | [optional] 
 **destination_item** | **str**| An item id, to which the new new shape will be associated. | [optional] 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode.  New in version 4. 16. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 

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

# **create_sequence_render_job**
> JobType create_sequence_render_job(sequence_render_request_type, source_tag=source_tag, jobmetadata=jobmetadata, notification_data=notification_data, tag=tag, notification=notification, destination_item=destination_item, resource_id=resource_id, priority=priority, original=original)

Render a standalone sequence

Creates a new job that renders the given sequence. A new item will be created containing a shape with the rendered result once the job is finished.

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
api_instance = vidispine.SequenceApi(vidispine.ApiClient(configuration))
sequence_render_request_type = vidispine.SequenceRenderRequestType() # SequenceRenderRequestType | 
source_tag = ['source_tag_example'] # list[str] | The shape tag specifying the shapes to use as input. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
tag = ['tag_example'] # list[str] | The shape tag specifying the format of the rendered sequence. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
destination_item = 'destination_item_example' # str | An item id, to which the new new shape will be associated. (optional)
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode.  New in version 4. 16. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)

try:
    # Render a standalone sequence
    api_response = api_instance.create_sequence_render_job(sequence_render_request_type, source_tag=source_tag, jobmetadata=jobmetadata, notification_data=notification_data, tag=tag, notification=notification, destination_item=destination_item, resource_id=resource_id, priority=priority, original=original)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->create_sequence_render_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_render_request_type** | [**SequenceRenderRequestType**](SequenceRenderRequestType.md)|  | 
 **source_tag** | [**list[str]**](str.md)| The shape tag specifying the shapes to use as input. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **tag** | [**list[str]**](str.md)| The shape tag specifying the format of the rendered sequence. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **destination_item** | **str**| An item id, to which the new new shape will be associated. | [optional] 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode.  New in version 4. 16. | [optional] 
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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_sequence**
> delete_item_sequence(id, format)

Delete a sequence

Removes a specific sequence from an item.

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
api_instance = vidispine.SequenceApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.

try:
    # Delete a sequence
    api_instance.delete_item_sequence(id, format)
except ApiException as e:
    print("Exception when calling SequenceApi->delete_item_sequence: %s\n" % e)
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

# **export_item_sequence**
> str export_item_sequence(id, export_request_type, format=format, to_sequence=to_sequence, dry_run=dry_run, tag=tag, type=type, uri=uri, content=content)

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
api_instance = vidispine.SequenceApi(vidispine.ApiClient(configuration))
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
    api_response = api_instance.export_item_sequence(id, export_request_type, format=format, to_sequence=to_sequence, dry_run=dry_run, tag=tag, type=type, uri=uri, content=content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->export_item_sequence: %s\n" % e)
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

# **export_sequence**
> str export_sequence(export_request_type, format=format, to_sequence=to_sequence, dry_run=dry_run, tag=tag, type=type, uri=uri, content=content)

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
api_instance = vidispine.SequenceApi(vidispine.ApiClient(configuration))
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
    api_response = api_instance.export_sequence(export_request_type, format=format, to_sequence=to_sequence, dry_run=dry_run, tag=tag, type=type, uri=uri, content=content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->export_sequence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_item_sequence**
> str get_item_sequence(id, format)

Retrieve a sequence

Retrieves the definition of the sequence in the given format.

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
api_instance = vidispine.SequenceApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.

try:
    # Retrieve a sequence
    api_response = api_instance.get_item_sequence(id, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->get_item_sequence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Media type based on the format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_sequence_in_format**
> str get_item_sequence_in_format(id, format=format, to_sequence=to_sequence, storage=storage, dry_run=dry_run, tag=tag, type=type, item=item, content=content)

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
api_instance = vidispine.SequenceApi(vidispine.ApiClient(configuration))
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
    api_response = api_instance.get_item_sequence_in_format(id, format=format, to_sequence=to_sequence, storage=storage, dry_run=dry_run, tag=tag, type=type, item=item, content=content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->get_item_sequence_in_format: %s\n" % e)
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

# **get_item_sequences**
> SequenceListType get_item_sequences(id)

List all sequences

Retrieves the sequences that have been stored for a specific item.

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
api_instance = vidispine.SequenceApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # List all sequences
    api_response = api_instance.get_item_sequences(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->get_item_sequences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

### Return type

[**SequenceListType**](SequenceListType.md)

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

# **update_item_metadata_from_sequence**
> update_item_metadata_from_sequence(id)

Conform metadata

Updates the item metadata with the metadata from the items listed in the sequence. The metadata will be selected based on the intervals.

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
api_instance = vidispine.SequenceApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # Conform metadata
    api_instance.update_item_metadata_from_sequence(id)
except ApiException as e:
    print("Exception when calling SequenceApi->update_item_metadata_from_sequence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

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

# **update_or_create_item_sequence**
> ItemType update_or_create_item_sequence(id, format, body, pause_frame=pause_frame)

Update or create a sequence

Creates or updates the sequence in the given format.

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
api_instance = vidispine.SequenceApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
format = 'format_example' # str | The format.
body = '/path/to/file' # file | The sequence definition
pause_frame = 56 # int | When a rendering job is started, this parameter determines which frame the job will pause at.  The job will resume when the sequence is updated. (optional)

try:
    # Update or create a sequence
    api_response = api_instance.update_or_create_item_sequence(id, format, body, pause_frame=pause_frame)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->update_or_create_item_sequence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **format** | **str**| The format. | 
 **body** | **file**| The sequence definition | 
 **pause_frame** | **int**| When a rendering job is started, this parameter determines which frame the job will pause at.  The job will resume when the sequence is updated. | [optional] 

### Return type

[**ItemType**](ItemType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;ItemDocument&lt;/em&gt; with the id of the sequence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

