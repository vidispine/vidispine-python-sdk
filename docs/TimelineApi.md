# vidispine.TimelineApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_timeline_conform_job**](TimelineApi.md#create_item_timeline_conform_job) | **POST** /item/{id}/timeline/{timeline-format}/conform | Start a conform job for an existing item
[**delete_item_timeline**](TimelineApi.md#delete_item_timeline) | **DELETE** /item/{id}/timeline/{timeline-format} | Delete a timeline
[**delete_item_timelines**](TimelineApi.md#delete_item_timelines) | **DELETE** /item/{id}/timeline | Delete all timelines
[**get_item_timeline**](TimelineApi.md#get_item_timeline) | **GET** /item/{id}/timeline/{timeline-format} | Retrieve a timeline
[**get_item_timelines**](TimelineApi.md#get_item_timelines) | **GET** /item/{id}/timeline | List all timelines
[**update_or_create_item_timeline**](TimelineApi.md#update_or_create_item_timeline) | **PUT** /item/{id}/timeline/{timeline-format} | Update or create a timeline


# **create_item_timeline_conform_job**
> JobType create_item_timeline_conform_job(id, timeline_format, jobmetadata=jobmetadata, notification_data=notification_data, conform_metadata=conform_metadata, thumbnail_service=thumbnail_service, tag=tag, source_tag=source_tag, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, destination_item=destination_item, create_posters=create_posters, override_fast_start=override_fast_start, original=original, priority=priority, resource_id=resource_id)

Start a conform job for an existing item

Starts a new `CONFORM` job that creates one or more shapes that contains media according to the conform timeline.  The timeline must be a *ConformDocument*, else the request will be rejected.

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
api_instance = vidispine.TimelineApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
timeline_format = 'timeline_format_example' # str | The timeline format.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
conform_metadata = True # bool | - `true` (default) - Copy metadata from the source items, according to the timeline, to the resulting item.  - `false` - Do not copy metadata from the source items. (optional) (default to True)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
tag = ['tag_example'] # list[str] | Comma-separated list of shape tags, that specify the desired output. (optional)
source_tag = ['source_tag_example'] # list[str] | Comma-separated list of shape tags, that specify the shapes that should be used as inputs. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
create_thumbnails = False # bool | - `true` - Creates thumbnails according to default transcoder rules.  - `false` (default) - No thumbnails will be created. (optional) (default to False)
destination_item = 'destination_item_example' # str | An item id, to which the new new shape will be associated. (optional)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)

try:
    # Start a conform job for an existing item
    api_response = api_instance.create_item_timeline_conform_job(id, timeline_format, jobmetadata=jobmetadata, notification_data=notification_data, conform_metadata=conform_metadata, thumbnail_service=thumbnail_service, tag=tag, source_tag=source_tag, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, destination_item=destination_item, create_posters=create_posters, override_fast_start=override_fast_start, original=original, priority=priority, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimelineApi->create_item_timeline_conform_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **timeline_format** | **str**| The timeline format. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **conform_metadata** | **bool**| - &#x60;true&#x60; (default) - Copy metadata from the source items, according to the timeline, to the resulting item.  - &#x60;false&#x60; - Do not copy metadata from the source items. | [optional] [default to True]
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **tag** | [**list[str]**](str.md)| Comma-separated list of shape tags, that specify the desired output. | [optional] 
 **source_tag** | [**list[str]**](str.md)| Comma-separated list of shape tags, that specify the shapes that should be used as inputs. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; - Creates thumbnails according to default transcoder rules.  - &#x60;false&#x60; (default) - No thumbnails will be created. | [optional] [default to False]
 **destination_item** | **str**| An item id, to which the new new shape will be associated. | [optional] 
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
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

# **delete_item_timeline**
> delete_item_timeline(id, timeline_format)

Delete a timeline

Removes specific timeline representation.

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
api_instance = vidispine.TimelineApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
timeline_format = 'timeline_format_example' # str | The timeline format.

try:
    # Delete a timeline
    api_instance.delete_item_timeline(id, timeline_format)
except ApiException as e:
    print("Exception when calling TimelineApi->delete_item_timeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **timeline_format** | **str**| The timeline format. | 

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

# **delete_item_timelines**
> delete_item_timelines(id)

Delete all timelines

Removes all timeline representations.

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
api_instance = vidispine.TimelineApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # Delete all timelines
    api_instance.delete_item_timelines(id)
except ApiException as e:
    print("Exception when calling TimelineApi->delete_item_timelines: %s\n" % e)
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

# **get_item_timeline**
> str get_item_timeline(id, timeline_format)

Retrieve a timeline

Returns timeline.

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
api_instance = vidispine.TimelineApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
timeline_format = 'timeline_format_example' # str | The timeline format.

try:
    # Retrieve a timeline
    api_response = api_instance.get_item_timeline(id, timeline_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimelineApi->get_item_timeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **timeline_format** | **str**| The timeline format. | 

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
**0** | Timeline representation. The actual MIME type depends on timeline format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_timelines**
> str get_item_timelines(id)

List all timelines

Returns a list of timeline stored and all timeline formats that can be derived. The precision number returned is an estimation of how close the converted timeline format will match the original. The lowest number, 0, means the original timeline format, 1 means derived timeline without any loss of information compared to the original format. The highest number, 100, means straight cuts only.

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
api_instance = vidispine.TimelineApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # List all timelines
    api_response = api_instance.get_item_timelines(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimelineApi->get_item_timelines: %s\n" % e)
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
**0** | CRLF-delimited list of TabbedTuple of timeline format and precision. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_item_timeline**
> update_or_create_item_timeline(id, timeline_format, body)

Update or create a timeline

updates or creates a timeline representation for an item.

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
api_instance = vidispine.TimelineApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
timeline_format = 'timeline_format_example' # str | The timeline format.
body = 'body_example' # str | Timeline representation. The actual MIME type depends on timeline format.

try:
    # Update or create a timeline
    api_instance.update_or_create_item_timeline(id, timeline_format, body)
except ApiException as e:
    print("Exception when calling TimelineApi->update_or_create_item_timeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **timeline_format** | **str**| The timeline format. | 
 **body** | **str**| Timeline representation. The actual MIME type depends on timeline format. | 

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

