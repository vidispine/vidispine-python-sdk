# vidispine.ItemApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_export_job**](ItemApi.md#create_item_export_job) | **POST** /item/{item-id}/export | Start an export job for a single item
[**create_item_imf_export_job**](ItemApi.md#create_item_imf_export_job) | **POST** /item/{item-id}/export/imp | Start an export job for a single item as an IMF package
[**create_item_list_job**](ItemApi.md#create_item_list_job) | **POST** /item/list | Create an item list job
[**create_item_thumbnail_job**](ItemApi.md#create_item_thumbnail_job) | **POST** /item/{item-id}/thumbnail | Create a thumbnail job
[**create_item_transcode_job**](ItemApi.md#create_item_transcode_job) | **POST** /item/{item-id}/transcode | Transcode an item
[**delete_item**](ItemApi.md#delete_item) | **DELETE** /item/{item-id} | Delete an item
[**delete_items**](ItemApi.md#delete_items) | **DELETE** /item | Delete multiple items
[**get_collections_containing_item**](ItemApi.md#get_collections_containing_item) | **GET** /item/{item-id}/collections | List collections that contain an item
[**get_item**](ItemApi.md#get_item) | **GET** /item/{item-id} | Retrieve an item
[**get_item_poster_resources**](ItemApi.md#get_item_poster_resources) | **GET** /item/{item-id}/posterresource | List thumbnail resources for an item
[**get_item_search_history**](ItemApi.md#get_item_search_history) | **GET** /item/history | Retrieve search history
[**get_item_thumbnail_resources**](ItemApi.md#get_item_thumbnail_resources) | **GET** /item/{item-id}/thumbnailresource | List thumbnail resources for an item
[**get_item_ur_is**](ItemApi.md#get_item_ur_is) | **GET** /item/{item-id}/uri | Get item URI
[**get_items**](ItemApi.md#get_items) | **GET** /item | List all items
[**get_libraries_containing_item**](ItemApi.md#get_libraries_containing_item) | **GET** /item/{item-id}/library | List libraries that contain an item
[**reindex_item**](ItemApi.md#reindex_item) | **PUT** /item/{item-id}/re-index | Re-index item
[**search_items**](ItemApi.md#search_items) | **PUT** /item | Search items
[**update_or_create_item_poster_resource**](ItemApi.md#update_or_create_item_poster_resource) | **PUT** /item/{item-id}/posterresource | Update or create a thumbnail resource for an item
[**update_or_create_item_thumbnail_resource**](ItemApi.md#update_or_create_item_thumbnail_resource) | **PUT** /item/{item-id}/thumbnailresource | Update or create a thumbnail resource for an item


# **create_item_export_job**
> JobType create_item_export_job(item_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, tag=tag, projection=projection, notification=notification, use_original_component_filename=use_original_component_filename, start=start, end=end, priority=priority, version=version, uri=uri, metadata=metadata, template=template, location_name=location_name, allow_missing=allow_missing)

Start an export job for a single item

Creates a new export job that will copy a file to a remote location.  A shape tag can be specified to decide which shape that will be exported.  If the URI ends with a \"/\" the URI is assumed to describe a folder and the file will retain its existing filename. Otherwise it is assumed that the URI describes a file and that filename will be used.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
track = ["*"] # list[str] | Comma-separated list of item track ids.  Can include wildcards, e. g.  `A*`.  Can also contain component ids. (optional) (default to ["*"])
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
use_original_filename = False # bool | If set to `true`, the file(s) will be exported with their original filename if available. (optional) (default to False)
tag = 'tag_example' # str | Finds a shape with the specified tag and uses that for export.  If not specified, the system will attempt to use the original shape. (optional)
projection = 'projection_example' # str | Defines the projection to use when exporting the metadata. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
use_original_component_filename = True # bool | If set to `true`, the file(s) will be exported with their original component filename if available. (optional)
start = 'start_example' # str | Defines a start time code for the media. (optional)
end = 'end_example' # str | Defines an end time code for the media. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
version = 'latest' # str | - *essence-version-id* - Return shapes for a specified version.  - `all` - Return shapes for all versions.  - `latest` (default) - Return shapes for the latest version.  - `latest-per-shapetag` - Return shapes with the highest essence version number per shape tag. (optional) (default to 'latest')
uri = 'uri_example' # str | A URI to the destination of the file. (optional)
metadata = False # bool | - `true` - Metadata will also be exported to side-car XML file.  - `false` (default) - No metadata is exported. (optional) (default to False)
template = 'template_example' # str | export template to use. (optional)
location_name = 'location_name_example' # str | The name of an export location. (optional)
allow_missing = True # bool | - `true` (default) - Job will be started and the missing files will be ignored.  - `false` - Job will fail if there are missing files and the files could not be generated by transcoding.  A shape tag should be specified. (optional) (default to True)

try:
    # Start an export job for a single item
    api_response = api_instance.create_item_export_job(item_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, tag=tag, projection=projection, notification=notification, use_original_component_filename=use_original_component_filename, start=start, end=end, priority=priority, version=version, uri=uri, metadata=metadata, template=template, location_name=location_name, allow_missing=allow_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->create_item_export_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **track** | [**list[str]**](str.md)| Comma-separated list of item track ids.  Can include wildcards, e. g.  &#x60;A*&#x60;.  Can also contain component ids. | [optional] [default to [&quot;*&quot;]]
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **use_original_filename** | **bool**| If set to &#x60;true&#x60;, the file(s) will be exported with their original filename if available. | [optional] [default to False]
 **tag** | **str**| Finds a shape with the specified tag and uses that for export.  If not specified, the system will attempt to use the original shape. | [optional] 
 **projection** | **str**| Defines the projection to use when exporting the metadata. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **use_original_component_filename** | **bool**| If set to &#x60;true&#x60;, the file(s) will be exported with their original component filename if available. | [optional] 
 **start** | **str**| Defines a start time code for the media. | [optional] 
 **end** | **str**| Defines an end time code for the media. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **version** | **str**| - *essence-version-id* - Return shapes for a specified version.  - &#x60;all&#x60; - Return shapes for all versions.  - &#x60;latest&#x60; (default) - Return shapes for the latest version.  - &#x60;latest-per-shapetag&#x60; - Return shapes with the highest essence version number per shape tag. | [optional] [default to &#39;latest&#39;]
 **uri** | **str**| A URI to the destination of the file. | [optional] 
 **metadata** | **bool**| - &#x60;true&#x60; - Metadata will also be exported to side-car XML file.  - &#x60;false&#x60; (default) - No metadata is exported. | [optional] [default to False]
 **template** | **str**| export template to use. | [optional] 
 **location_name** | **str**| The name of an export location. | [optional] 
 **allow_missing** | **bool**| - &#x60;true&#x60; (default) - Job will be started and the missing files will be ignored.  - &#x60;false&#x60; - Job will fail if there are missing files and the files could not be generated by transcoding.  A shape tag should be specified. | [optional] [default to True]

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

# **create_item_imf_export_job**
> JobType create_item_imf_export_job(item_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, tag=tag, uri=uri, notification=notification, cpl_track=cpl_track, start=start, projection=projection, end=end, use_original_component_filename=use_original_component_filename, version=version, allow_missing=allow_missing, metadata=metadata, template=template, priority=priority, location_name=location_name)

Start an export job for a single item as an IMF package

Creates a new export job that will create an IMF package as a remote location. URI must end with an \"/\" to denote a folder.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
track = ["*"] # list[str] | Comma-separated list of item track ids to include as physical files.  Can include wildcards, e. g.  `A*`.  Can also contain component ids.  Since 4. 17. 8, can also be on the format `{shape}:track`, where shape is identified by shape id or shape tag.  Since Vidispine 5. 0, can also be of syntax: `shape:` {shape-id}:{track}, `cpl:` {CPL UUID}:{track}, `tag:` {shape-tag}:{track}, or `component:` {component-id}.  (The `component:` syntax means the same as with no prefix. ) (optional) (default to ["*"])
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
use_original_filename = False # bool | If set to `true`, the file(s) will be exported with their original filename if available. (optional) (default to False)
tag = 'tag_example' # str | Finds a shape with the specified tag and uses that for export.  If not specified, the system will attempt to use the original shape. (optional)
uri = 'uri_example' # str | A URI to the destination of the file. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
cpl_track = ['cpl_track_example'] # list[str] | Comma-separated list of item track ids to include in the CPL.  Can include wildcards, e. g.  `A*`.  Can also contain component ids.  Since 4. 17. 8, can also be on the format `{shape}:track`, where shape is identified by shape id or shape tag.  Default is the same as the track parameter. (optional)
start = 'start_example' # str | Defines a start time_code for the media. (optional)
projection = 'projection_example' # str | Defines the projection to use when exporting the metadata. (optional)
end = 'end_example' # str | Defines an end time_code for the media. (optional)
use_original_component_filename = True # bool | If set to `true`, the file(s) will be exported with their original component filename if available. (optional)
version = 'latest' # str | - *essence-version-id* - Return shapes for a specified version.  - `all` - Return shapes for all versions.  - `latest` (default) - Return shapes for the latest version.  - `latest-per-shapetag` - Return shapes with the highest essence version number per shape tag. (optional) (default to 'latest')
allow_missing = True # bool | - `true` (default) - Job will be started and the missing files will be ignored.  - `false` - Job will fail if there are missing files and the files could not be generated by transcoding.  A shape tag should be specified. (optional) (default to True)
metadata = False # bool | - `true` - Metadata will also be exported to side-car XML file.  - `false` (default) - No metadata is exported. (optional) (default to False)
template = 'template_example' # str | Export template to use (see export-templates). (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
location_name = 'location_name_example' # str | The name of an export location. (optional)

try:
    # Start an export job for a single item as an IMF package
    api_response = api_instance.create_item_imf_export_job(item_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, tag=tag, uri=uri, notification=notification, cpl_track=cpl_track, start=start, projection=projection, end=end, use_original_component_filename=use_original_component_filename, version=version, allow_missing=allow_missing, metadata=metadata, template=template, priority=priority, location_name=location_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->create_item_imf_export_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **track** | [**list[str]**](str.md)| Comma-separated list of item track ids to include as physical files.  Can include wildcards, e. g.  &#x60;A*&#x60;.  Can also contain component ids.  Since 4. 17. 8, can also be on the format &#x60;{shape}:track&#x60;, where shape is identified by shape id or shape tag.  Since Vidispine 5. 0, can also be of syntax: &#x60;shape:&#x60; {shape-id}:{track}, &#x60;cpl:&#x60; {CPL UUID}:{track}, &#x60;tag:&#x60; {shape-tag}:{track}, or &#x60;component:&#x60; {component-id}.  (The &#x60;component:&#x60; syntax means the same as with no prefix. ) | [optional] [default to [&quot;*&quot;]]
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **use_original_filename** | **bool**| If set to &#x60;true&#x60;, the file(s) will be exported with their original filename if available. | [optional] [default to False]
 **tag** | **str**| Finds a shape with the specified tag and uses that for export.  If not specified, the system will attempt to use the original shape. | [optional] 
 **uri** | **str**| A URI to the destination of the file. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **cpl_track** | [**list[str]**](str.md)| Comma-separated list of item track ids to include in the CPL.  Can include wildcards, e. g.  &#x60;A*&#x60;.  Can also contain component ids.  Since 4. 17. 8, can also be on the format &#x60;{shape}:track&#x60;, where shape is identified by shape id or shape tag.  Default is the same as the track parameter. | [optional] 
 **start** | **str**| Defines a start time_code for the media. | [optional] 
 **projection** | **str**| Defines the projection to use when exporting the metadata. | [optional] 
 **end** | **str**| Defines an end time_code for the media. | [optional] 
 **use_original_component_filename** | **bool**| If set to &#x60;true&#x60;, the file(s) will be exported with their original component filename if available. | [optional] 
 **version** | **str**| - *essence-version-id* - Return shapes for a specified version.  - &#x60;all&#x60; - Return shapes for all versions.  - &#x60;latest&#x60; (default) - Return shapes for the latest version.  - &#x60;latest-per-shapetag&#x60; - Return shapes with the highest essence version number per shape tag. | [optional] [default to &#39;latest&#39;]
 **allow_missing** | **bool**| - &#x60;true&#x60; (default) - Job will be started and the missing files will be ignored.  - &#x60;false&#x60; - Job will fail if there are missing files and the files could not be generated by transcoding.  A shape tag should be specified. | [optional] [default to True]
 **metadata** | **bool**| - &#x60;true&#x60; - Metadata will also be exported to side-car XML file.  - &#x60;false&#x60; (default) - No metadata is exported. | [optional] [default to False]
 **template** | **str**| Export template to use (see export-templates). | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
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

# **create_item_list_job**
> JobType create_item_list_job(destination_uri, item_list_type, jobmetadata=jobmetadata, p=p, output_format=output_format, data=data, notification=notification, groupname=groupname, username=username, notification_data=notification_data, field=field, priority=priority)

Create an item list job

Starts a new job that goes through all the items available to the user/group and outputs a file to the supplied URI.  If no user and no group is supplied, all items will be retrieved. The output format depends on the specified parameter, if set to XML an *ItemListDocument* will be produced. Furthermore if an XSLT is given the *ItemListDocument* will be transformed.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
destination_uri = 'destination_uri_example' # str | The URI to output the CSV file to.
item_list_type = vidispine.ItemListType() # ItemListType | An optional XSLT capable of transforming <em>ItemListDocument</em>.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
p = ['p_example'] # list[str] | Comma-separated list of paths specifying the content to include.  Overrides the field and data parameters.  Only supported for XML output. (optional)
output_format = 'output_format_example' # str | Specifies the output format. (optional)
data = 'data_example' # str | Specifies any additional data that should be included with the metadata fields. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
groupname = 'groupname_example' # str | Filter items according to the access of the specified group. (optional)
username = 'username_example' # str | Filter items according to the access of the specified user. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
field = ['field_example'] # list[str] | Comma-separated list of metadata fields to include in the result. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Create an item list job
    api_response = api_instance.create_item_list_job(destination_uri, item_list_type, jobmetadata=jobmetadata, p=p, output_format=output_format, data=data, notification=notification, groupname=groupname, username=username, notification_data=notification_data, field=field, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->create_item_list_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_uri** | **str**| The URI to output the CSV file to. | 
 **item_list_type** | [**ItemListType**](ItemListType.md)| An optional XSLT capable of transforming &lt;em&gt;ItemListDocument&lt;/em&gt;. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **p** | [**list[str]**](str.md)| Comma-separated list of paths specifying the content to include.  Overrides the field and data parameters.  Only supported for XML output. | [optional] 
 **output_format** | **str**| Specifies the output format. | [optional] 
 **data** | **str**| Specifies any additional data that should be included with the metadata fields. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **groupname** | **str**| Filter items according to the access of the specified group. | [optional] 
 **username** | **str**| Filter items according to the access of the specified user. | [optional] 
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

# **create_item_thumbnail_job**
> JobType create_item_thumbnail_job(item_id, thumbnail_width=thumbnail_width, jobmetadata=jobmetadata, notification_data=notification_data, version=version, thumbnail_service=thumbnail_service, tag=tag, source_tag=source_tag, poster_format=poster_format, notification=notification, poster_width=poster_width, priority=priority, create_thumbnails=create_thumbnails, thumbnail_height=thumbnail_height, create_posters=create_posters, poster_height=poster_height, thumbnail_period=thumbnail_period, resource_id=resource_id)

Create a thumbnail job

Creates a new thumbnail job with the specified parameters. Note that a job cannot both create thumbnails at specified intervals and posters. Creating thumbnails according to transcoder rules and creating posters is however allowed.  Changed in version 5.0: For multi-layer PSD/PSB files, only a thumbnail of all layers flattened will be generated by default.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
thumbnail_width = 56 # int | The width of the thumbnails.  If `thumbnailWidth` is specified, `thumbnailHeight` must also be specified. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
version = 56 # int | A version number.  For creating thumbnails for older versions of the item essence.  Default is latest version. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
tag = 'tag_example' # str | Include additional video settings from this transcode preset.  Resolution settings in the tag are overridden by query parameters `thumbnailHeight` and `thumbnailWidth`. (optional)
source_tag = 'source_tag_example' # str | Comma-separated shape tags.  The fist valid shape will be chosen as the source of the job.  If non of the tags are valid, the original shape will be used. (optional)
poster_format = 'jpeg' # str | - `jpeg` (default) - Creates posters in JPEG format.  - `png` - Creates posters in PNG format. (optional) (default to 'jpeg')
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
poster_width = 56 # int | The width of the posters. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
create_thumbnails = False # bool | - `true` - Creates thumbnails according to default transcoder rules.  - *t1*, . . .  - Thumbnails will be created on the specified, comma-separated, time codes.  - `false` (default) - No thumbnails will be created. (optional) (default to False)
thumbnail_height = 56 # int | The height of the thumbnails.  If `thumbnailHeight` is specified, `thumbnailWidth` must also be specified. (optional)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
poster_height = 56 # int | The height of the posters. (optional)
thumbnail_period = 'thumbnail_period_example' # str | Timecode string specifying the interval of the thumbnails.  It should be a decimal integer when working with multi-page images/PDFs, meaning every N page(s). (optional)
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)

try:
    # Create a thumbnail job
    api_response = api_instance.create_item_thumbnail_job(item_id, thumbnail_width=thumbnail_width, jobmetadata=jobmetadata, notification_data=notification_data, version=version, thumbnail_service=thumbnail_service, tag=tag, source_tag=source_tag, poster_format=poster_format, notification=notification, poster_width=poster_width, priority=priority, create_thumbnails=create_thumbnails, thumbnail_height=thumbnail_height, create_posters=create_posters, poster_height=poster_height, thumbnail_period=thumbnail_period, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->create_item_thumbnail_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **thumbnail_width** | **int**| The width of the thumbnails.  If &#x60;thumbnailWidth&#x60; is specified, &#x60;thumbnailHeight&#x60; must also be specified. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **version** | **int**| A version number.  For creating thumbnails for older versions of the item essence.  Default is latest version. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **tag** | **str**| Include additional video settings from this transcode preset.  Resolution settings in the tag are overridden by query parameters &#x60;thumbnailHeight&#x60; and &#x60;thumbnailWidth&#x60;. | [optional] 
 **source_tag** | **str**| Comma-separated shape tags.  The fist valid shape will be chosen as the source of the job.  If non of the tags are valid, the original shape will be used. | [optional] 
 **poster_format** | **str**| - &#x60;jpeg&#x60; (default) - Creates posters in JPEG format.  - &#x60;png&#x60; - Creates posters in PNG format. | [optional] [default to &#39;jpeg&#39;]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **poster_width** | **int**| The width of the posters. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **create_thumbnails** | **bool**| - &#x60;true&#x60; - Creates thumbnails according to default transcoder rules.  - *t1*, . . .  - Thumbnails will be created on the specified, comma-separated, time codes.  - &#x60;false&#x60; (default) - No thumbnails will be created. | [optional] [default to False]
 **thumbnail_height** | **int**| The height of the thumbnails.  If &#x60;thumbnailHeight&#x60; is specified, &#x60;thumbnailWidth&#x60; must also be specified. | [optional] 
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **poster_height** | **int**| The height of the posters. | [optional] 
 **thumbnail_period** | **str**| Timecode string specifying the interval of the thumbnails.  It should be a decimal integer when working with multi-page images/PDFs, meaning every N page(s). | [optional] 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 

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

# **create_item_transcode_job**
> JobType create_item_transcode_job(item_id, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, tag=tag, storage_id=storage_id, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, destination_item=destination_item, create_posters=create_posters, override_fast_start=override_fast_start, resource_id=resource_id, priority=priority, original=original)

Transcode an item

Starts a new job that transcode an item to a number of shapes according to the given shape tags.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
tag = ['tag_example'] # list[str] | Comma-separated list of shape tags, that specify the desired output. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored.  New in version 4. 16. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
create_thumbnails = False # bool | - `true` - Creates thumbnails according to default transcoder rules.  - `false` (default) - No thumbnails will be created. (optional) (default to False)
destination_item = 'destination_item_example' # str | An item id, to which the new new shape will be associated. (optional)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)

try:
    # Transcode an item
    api_response = api_instance.create_item_transcode_job(item_id, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, tag=tag, storage_id=storage_id, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, destination_item=destination_item, create_posters=create_posters, override_fast_start=override_fast_start, resource_id=resource_id, priority=priority, original=original)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->create_item_transcode_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **tag** | [**list[str]**](str.md)| Comma-separated list of shape tags, that specify the desired output. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored.  New in version 4. 16. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; - Creates thumbnails according to default transcoder rules.  - &#x60;false&#x60; (default) - No thumbnails will be created. | [optional] [default to False]
 **destination_item** | **str**| An item id, to which the new new shape will be associated. | [optional] 
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 
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

# **delete_item**
> delete_item(item_id, keep_shape_tag_storage=keep_shape_tag_storage, keep_shape_tag_media=keep_shape_tag_media)

Delete an item

Marks the item as being deleted, meaning it will not be returned in search results. The actual removement from the database is done approximately once every minute. Also, all files associated with the item is marked as `TO_BE_DELETED`, meaning they will be deleted by the storage supervisor, but not sooner than all jobs involving the actual file has finished.  By specifying `keepShapeTagMedia` and/or `keepShapeTagStorage`, the files associated with the item is not deleted, but simply unassociated with the item.  If only `keepShapeTagMedia` is given, all files belonging to shapes of the item with any of the given shape tags are preserved.  If only `keepShapeTagStorage` is given, all files belonging to the item residing on the given storages are preserved. If both `keepShapeTagMedia` and `keepShapeTagStorage` is given, all files which *both* belongs to the specified shapes and storages are preserved.  If any of `keepShapeTagMedia` or `keepShapeTagStorage` contains a value `*`, then no files will be removed.  Changed in version 5.0: New _item_write role required.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
keep_shape_tag_storage = ['keep_shape_tag_storage_example'] # list[str] | Comma-separated list of storage ids whose files will not be deleted. (optional)
keep_shape_tag_media = ['keep_shape_tag_media_example'] # list[str] | Comma-separated list of shape tags whose files will not be deleted. (optional)

try:
    # Delete an item
    api_instance.delete_item(item_id, keep_shape_tag_storage=keep_shape_tag_storage, keep_shape_tag_media=keep_shape_tag_media)
except ApiException as e:
    print("Exception when calling ItemApi->delete_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **keep_shape_tag_storage** | [**list[str]**](str.md)| Comma-separated list of storage ids whose files will not be deleted. | [optional] 
 **keep_shape_tag_media** | [**list[str]**](str.md)| Comma-separated list of shape tags whose files will not be deleted. | [optional] 

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

# **delete_items**
> delete_items(keep_shape_tag_storage=keep_shape_tag_storage, keep_shape_tag_media=keep_shape_tag_media, id=id)

Delete multiple items

Marks multiple items as being deleted, meaning they will not be returned in search results.  Changed in version 5.0: New _item_write role required.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
keep_shape_tag_storage = ['keep_shape_tag_storage_example'] # list[str] | Comma-separated list of storage ids whose files will not be deleted. (optional)
keep_shape_tag_media = ['keep_shape_tag_media_example'] # list[str] | Comma-separated list of shape tags whose files will not be deleted. (optional)
id = ['id_example'] # list[str] | Comma-separated list of item ids or external ids.  Must not be empty. (optional)

try:
    # Delete multiple items
    api_instance.delete_items(keep_shape_tag_storage=keep_shape_tag_storage, keep_shape_tag_media=keep_shape_tag_media, id=id)
except ApiException as e:
    print("Exception when calling ItemApi->delete_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keep_shape_tag_storage** | [**list[str]**](str.md)| Comma-separated list of storage ids whose files will not be deleted. | [optional] 
 **keep_shape_tag_media** | [**list[str]**](str.md)| Comma-separated list of shape tags whose files will not be deleted. | [optional] 
 **id** | [**list[str]**](str.md)| Comma-separated list of item ids or external ids.  Must not be empty. | [optional] 

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

# **get_collections_containing_item**
> URIListType get_collections_containing_item(item_id)

List collections that contain an item

Retrieves the ids of all collections that includes the item, and that the calling user has read access to.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.

try:
    # List collections that contain an item
    api_response = api_instance.get_collections_containing_item(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_collections_containing_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 

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

# **get_item**
> ItemType get_item(item_id, language=language, storage_type=storage_type, tag=tag, closed_files=closed_files, terse=terse, method_metadata=method_metadata, interval=interval, group=group, include_values=include_values, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, merged_extradata=merged_extradata, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, field=field, include=include, method_type=method_type, p=p, base_uri=base_uri, uri_type=uri_type, storage=storage, revision=revision, scheme=scheme, version=version, merged_permission=merged_permission, sample_rate=sample_rate, noauth_url=noauth_url)

Retrieve an item

Returns information about a single item.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
tag = 'tag_example' # str | A URI parameter: Comma-separated list of shape tags to return. (optional)
closed_files = True # bool | A URI parameter:  - `true` (default) - Return only URIs that point to closed files.  - `false` - Return all URIs. (optional) (default to True)
terse = 'no' # str | - `yes` - Return metadata in terse format.  - `no` (default) - Return metadata in verbose format. (optional) (default to 'no')
method_metadata = 'method_metadata_example' # str | Metadata used with storage method. (optional)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
include_values = True # bool | Return the value enumeration for each metadata field. (optional)
storage_group = 'storage_group_example' # str | Storage group id.  Return only files from storages specified in the storage group. (optional)
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
starttc = False # bool | - `true` - Interval is given relative to start timecode of item.  - `false` (default) - Interval is 0-based. (optional) (default to False)
content = ['content_example'] # list[str] | Comma-separated list of the types of content to retrieve. (optional)
merged_extradata = 'merged_extradata_example' # str | Any possible extra data. (optional)
include_transient_metadata = True # bool | - `true` (default) - Include transient metadata.  - `false` - Do not include transient metadata in response. (optional) (default to True)
merged_type = 'merged_type_example' # str | The type of operation to check for. (optional)
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = 'include_example' # str | A list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)
method_type = 'method_type_example' # str | Access method.   - `AUTO` - Gives an APInoauth URI to the media.  Access to file is tunneled through Vidispine.  - `AZURE_SAS` - If the storage schema is azure:// you can get direct access to the media.  The resulting URI will not tunnel through Vidispine but rather point directly to the media location at the azure storage. (optional)
p = ['p_example'] # list[str] | Comma-separated list of paths specifying the content to include.  Overrides the content and filter parameters. (optional)
base_uri = 'base_uri_example' # str | Which base URI to use for the thumbnail URLs. (optional)
uri_type = ['uri_type_example'] # list[str] | Comma-separated list of format types (container format) to return. (optional)
storage = ['storage_example'] # list[str] | List of storage ids.  Return only files from specific storages.  Can be specified multiple times. (optional)
revision = 'revision_example' # str | Specifying which metadata revision to display.  Only used if requesting a single item or collection. (optional)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
version = 'version_example' # str | Specifying which essence version to return for shapes.  If special value `all`, display all versions.  If special value `latest` (default), display latest version of shapes. (optional)
merged_permission = 'merged_permission_example' # str | The lowest required permission level. (optional)
sample_rate = 'sample_rate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
noauth_url = True # bool | - `true` Return URIs that do not need authentication.  - `false` (default) Return normal URIs (optional)

try:
    # Retrieve an item
    api_response = api_instance.get_item(item_id, language=language, storage_type=storage_type, tag=tag, closed_files=closed_files, terse=terse, method_metadata=method_metadata, interval=interval, group=group, include_values=include_values, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, merged_extradata=merged_extradata, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, field=field, include=include, method_type=method_type, p=p, base_uri=base_uri, uri_type=uri_type, storage=storage, revision=revision, scheme=scheme, version=version, merged_permission=merged_permission, sample_rate=sample_rate, noauth_url=noauth_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **tag** | **str**| A URI parameter: Comma-separated list of shape tags to return. | [optional] 
 **closed_files** | **bool**| A URI parameter:  - &#x60;true&#x60; (default) - Return only URIs that point to closed files.  - &#x60;false&#x60; - Return all URIs. | [optional] [default to True]
 **terse** | **str**| - &#x60;yes&#x60; - Return metadata in terse format.  - &#x60;no&#x60; (default) - Return metadata in verbose format. | [optional] [default to &#39;no&#39;]
 **method_metadata** | **str**| Metadata used with storage method. | [optional] 
 **interval** | [**list[str]**](str.md)| Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - &#x60;generic&#x60; - Return all non-timed metadata.  - &#x60;all&#x60; (default) - Return all metadata, same as &#x60;interval&#x3D;generic,-INF-+INF&#x60; | [optional] [default to [&quot;all&quot;]]
 **group** | [**list[str]**](str.md)| Comma-separated list.   - *group-name* - Return specified group.  - *group-name* &#x60;+&#x60; - Return specified group and subgroups.  - *group-name* &#x60;:&#x60; *new-name* - Return specified group, renamed to a new name in return value.  - &#x60;-&#x60; *group-name* - Exclude specified group.  - (default) - Return all groups. | [optional] 
 **include_values** | **bool**| Return the value enumeration for each metadata field. | [optional] 
 **storage_group** | **str**| Storage group id.  Return only files from storages specified in the storage group. | [optional] 
 **track** | [**list[str]**](str.md)| Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is &#x60;A2&#x60;.  - *track-type* *t1* &#x60;-&#x60; *t2* - Return metadata for specified track interval, e. g.  &#x60;A2-4&#x60;.  - *track-type* &#x60;*&#x60; - Return metadata for all tracks of specified type, e. g.  &#x60;A*&#x60;.  - &#x60;generic&#x60; - Return all non-tracked metadata.  - &#x60;all&#x60; (default) - All metadata, with or without track specification, are returned. | [optional] [default to [&quot;all&quot;]]
 **conflict** | **str**| - &#x60;yes&#x60; (default) - Include all metadata conflicts, unresolved.  - &#x60;no&#x60; - Return conflicts resolved according to field rules. | [optional] [default to &#39;yes&#39;]
 **starttc** | **bool**| - &#x60;true&#x60; - Interval is given relative to start timecode of item.  - &#x60;false&#x60; (default) - Interval is 0-based. | [optional] [default to False]
 **content** | [**list[str]**](str.md)| Comma-separated list of the types of content to retrieve. | [optional] 
 **merged_extradata** | **str**| Any possible extra data. | [optional] 
 **include_transient_metadata** | **bool**| - &#x60;true&#x60; (default) - Include transient metadata.  - &#x60;false&#x60; - Do not include transient metadata in response. | [optional] [default to True]
 **merged_type** | **str**| The type of operation to check for. | [optional] 
 **default_value** | **bool**| - &#x60;true&#x60; - For unset fields, return default values.  - &#x60;false&#x60; (default) - Do not return default values. | [optional] [default to False]
 **field** | [**list[str]**](str.md)| Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \&quot;:\&quot; *new-name* - Return specified field, renamed to a new name in return value.  - \&quot;-\&quot; *field-name* - Exclude specified field.  - (default) - Return all fields. | [optional] 
 **include** | **str**| A list of keys.   Includes additional field specific data.  Additionally, if set to &#x60;type&#x60; the type definition of the field will be retrieved. | [optional] 
 **method_type** | **str**| Access method.   - &#x60;AUTO&#x60; - Gives an APInoauth URI to the media.  Access to file is tunneled through Vidispine.  - &#x60;AZURE_SAS&#x60; - If the storage schema is azure:// you can get direct access to the media.  The resulting URI will not tunnel through Vidispine but rather point directly to the media location at the azure storage. | [optional] 
 **p** | [**list[str]**](str.md)| Comma-separated list of paths specifying the content to include.  Overrides the content and filter parameters. | [optional] 
 **base_uri** | **str**| Which base URI to use for the thumbnail URLs. | [optional] 
 **uri_type** | [**list[str]**](str.md)| Comma-separated list of format types (container format) to return. | [optional] 
 **storage** | [**list[str]**](str.md)| List of storage ids.  Return only files from specific storages.  Can be specified multiple times. | [optional] 
 **revision** | **str**| Specifying which metadata revision to display.  Only used if requesting a single item or collection. | [optional] 
 **scheme** | **str**| URI scheme to return. | [optional] 
 **version** | **str**| Specifying which essence version to return for shapes.  If special value &#x60;all&#x60;, display all versions.  If special value &#x60;latest&#x60; (default), display latest version of shapes. | [optional] 
 **merged_permission** | **str**| The lowest required permission level. | [optional] 
 **sample_rate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **noauth_url** | **bool**| - &#x60;true&#x60; Return URIs that do not need authentication.  - &#x60;false&#x60; (default) Return normal URIs | [optional] 

### Return type

[**ItemType**](ItemType.md)

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

# **get_item_poster_resources**
> URIListType get_item_poster_resources(item_id, version=version)

List thumbnail resources for an item

Return one or more poster resource URIs which can be used to manage the posters for a specific item.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
version = 56 # int | Return posters from this essence version.  By default posters for the latest version will be returned. (optional)

try:
    # List thumbnail resources for an item
    api_response = api_instance.get_item_poster_resources(item_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_item_poster_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **version** | **int**| Return posters from this essence version.  By default posters for the latest version will be returned. | [optional] 

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
**0** | &lt;em&gt;URIListDocument&lt;/em&gt; of thumbnail resource URIs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_search_history**
> SearchHistoryListType get_item_search_history(max_results=max_results, username=username, start=start)

Retrieve search history

Retrieves a list of searches made by a particular user, including \"item search\" and \"Item and collection search\". The results are ordered according to timestamp, with the latest searches being first. Duplicate queries will not be retrieved.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
max_results = 10 # int | The maximum number of searches that will be retrieved.  The value must be between `1` and `50`. (optional) (default to 10)
username = 'username_example' # str | The name of the user that has performed the searched.  If not specified, the user performing the request will be selected. (optional)
start = 'start_example' # str | An ISO 8601 date.  If set, only searches made after this date will be retrieved. (optional)

try:
    # Retrieve search history
    api_response = api_instance.get_item_search_history(max_results=max_results, username=username, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_item_search_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_results** | **int**| The maximum number of searches that will be retrieved.  The value must be between &#x60;1&#x60; and &#x60;50&#x60;. | [optional] [default to 10]
 **username** | **str**| The name of the user that has performed the searched.  If not specified, the user performing the request will be selected. | [optional] 
 **start** | **str**| An ISO 8601 date.  If set, only searches made after this date will be retrieved. | [optional] 

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
**0** | &lt;em&gt;SearchHistoryDocument&lt;/em&gt;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_thumbnail_resources**
> URIListType get_item_thumbnail_resources(item_id, version=version)

List thumbnail resources for an item

Return one or more poster resource URIs which can be used to manage the thumbnails for a specific item.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
version = 56 # int | Return thumbnails from this essence version.  By default thumbnails for the latest version will be returned. (optional)

try:
    # List thumbnail resources for an item
    api_response = api_instance.get_item_thumbnail_resources(item_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_item_thumbnail_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **version** | **int**| Return thumbnails from this essence version.  By default thumbnails for the latest version will be returned. | [optional] 

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
**0** | &lt;em&gt;URIListDocument&lt;/em&gt; of thumbnail resource URIs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_ur_is**
> URIListType get_item_ur_is(item_id, storage_type=storage_type, tag=tag, type=type, closed_files=closed_files, method_metadata=method_metadata, scheme=scheme, method_type=method_type)

Get item URI

Retrieves the URI to any container contained in the item that matches the specified type or the files contained in a shape that matches the given tags.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
tag = ['tag_example'] # list[str] | Comma-separated list of shape tags to return. (optional)
type = ['type_example'] # list[str] | Comma-separated list of format types (container format) to return. (optional)
closed_files = True # bool | - `true` (default) - Return only URIs that point to closed files.  - `false` - Return all URIs. (optional) (default to True)
method_metadata = 'method_metadata_example' # str | Metadata used with storage method. (optional)
scheme = 'scheme_example' # str | URI scheme to return, e. g.  `ftp`. (optional)
method_type = 'method_type_example' # str | Access method.   - `AUTO` - Gives an APInoauth URI to the media.  Access to file is tunneled through Vidispine.  - `AZURE_SAS` - If the storage schema is azure:// you can get direct access to the media.  The resulting URI will not tunnel through Vidispine but rather point directly to the media location at the azure storage. (optional)

try:
    # Get item URI
    api_response = api_instance.get_item_ur_is(item_id, storage_type=storage_type, tag=tag, type=type, closed_files=closed_files, method_metadata=method_metadata, scheme=scheme, method_type=method_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_item_ur_is: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **tag** | [**list[str]**](str.md)| Comma-separated list of shape tags to return. | [optional] 
 **type** | [**list[str]**](str.md)| Comma-separated list of format types (container format) to return. | [optional] 
 **closed_files** | **bool**| - &#x60;true&#x60; (default) - Return only URIs that point to closed files.  - &#x60;false&#x60; - Return all URIs. | [optional] [default to True]
 **method_metadata** | **str**| Metadata used with storage method. | [optional] 
 **scheme** | **str**| URI scheme to return, e. g.  &#x60;ftp&#x60;. | [optional] 
 **method_type** | **str**| Access method.   - &#x60;AUTO&#x60; - Gives an APInoauth URI to the media.  Access to file is tunneled through Vidispine.  - &#x60;AZURE_SAS&#x60; - If the storage schema is azure:// you can get direct access to the media.  The resulting URI will not tunnel through Vidispine but rather point directly to the media location at the azure storage. | [optional] 

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

# **get_items**
> ItemListType get_items(language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, update_frequency=update_frequency, number=number, interval=interval, group=group, merged_permission=merged_permission, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, uri_type=uri_type, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, q=q, p=p, library=library, base_uri=base_uri, merged_extradata=merged_extradata, result=result, storage=storage, revision=revision, url=url, scheme=scheme, auto_refresh=auto_refresh, version=version, cursor=cursor, include_values=include_values, sample_rate=sample_rate, library_id=library_id, count=count, save=save, noauth_url=noauth_url, update_mode=update_mode)

List all items

Returns a list of all items. This request is the same as performing an empty search.  Note that searching can also be performed by using the HTTP method PUT using the same syntax, except for the parameter `q` is omitted and the *ItemSearchDocument* is sent in the body of the request.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
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
    # List all items
    api_response = api_instance.get_items(language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, update_frequency=update_frequency, number=number, interval=interval, group=group, merged_permission=merged_permission, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, uri_type=uri_type, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, q=q, p=p, library=library, base_uri=base_uri, merged_extradata=merged_extradata, result=result, storage=storage, revision=revision, url=url, scheme=scheme, auto_refresh=auto_refresh, version=version, cursor=cursor, include_values=include_values, sample_rate=sample_rate, library_id=library_id, count=count, save=save, noauth_url=noauth_url, update_mode=update_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**0** | CRLF-delimited list of ids or URLs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_libraries_containing_item**
> URIListType get_libraries_containing_item(item_id)

List libraries that contain an item

Retrieves the ids of all libraries that includes the item, and that the calling user has read access to.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.

try:
    # List libraries that contain an item
    api_response = api_instance.get_libraries_containing_item(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_libraries_containing_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 

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

# **reindex_item**
> str reindex_item(item_id)

Re-index item

Queues a single item for re-index.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.

try:
    # Re-index item
    api_response = api_instance.reindex_item(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->reindex_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_items**
> ItemListType search_items(item_search_type, language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, update_frequency=update_frequency, number=number, interval=interval, group=group, merged_permission=merged_permission, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, uri_type=uri_type, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, q=q, p=p, library=library, base_uri=base_uri, merged_extradata=merged_extradata, result=result, storage=storage, revision=revision, url=url, scheme=scheme, auto_refresh=auto_refresh, version=version, cursor=cursor, include_values=include_values, sample_rate=sample_rate, library_id=library_id, count=count, save=save, noauth_url=noauth_url, update_mode=update_mode)

Search items

Performs an item search. If the `result` query parameter is set to `library` a new library is created, which can be used to further refine the search, using the `library` parameter.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
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
    # Search items
    api_response = api_instance.search_items(item_search_type, language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, update_frequency=update_frequency, number=number, interval=interval, group=group, merged_permission=merged_permission, storage_group=storage_group, track=track, conflict=conflict, starttc=starttc, content=content, uri_type=uri_type, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, q=q, p=p, library=library, base_uri=base_uri, merged_extradata=merged_extradata, result=result, storage=storage, revision=revision, url=url, scheme=scheme, auto_refresh=auto_refresh, version=version, cursor=cursor, include_values=include_values, sample_rate=sample_rate, library_id=library_id, count=count, save=save, noauth_url=noauth_url, update_mode=update_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->search_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **update_or_create_item_poster_resource**
> URIListType update_or_create_item_poster_resource(item_id)

Update or create a thumbnail resource for an item

If no poster resources are defined for an item, create a resource and return it.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.

try:
    # Update or create a thumbnail resource for an item
    api_response = api_instance.update_or_create_item_poster_resource(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->update_or_create_item_poster_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 

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
**0** | &lt;em&gt;URIListDocument&lt;/em&gt; of thumbnail resource URIs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_item_thumbnail_resource**
> URIListType update_or_create_item_thumbnail_resource(item_id)

Update or create a thumbnail resource for an item

If no thumbnail resources are defined for an item, create a resource and return it.

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
api_instance = vidispine.ItemApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.

try:
    # Update or create a thumbnail resource for an item
    api_response = api_instance.update_or_create_item_thumbnail_resource(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->update_or_create_item_thumbnail_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 

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
**0** | &lt;em&gt;URIListDocument&lt;/em&gt; of thumbnail resource URIs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

