# vidispine.ConformApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_conform_job**](ConformApi.md#create_conform_job) | **POST** /conform | Start a conform job


# **create_conform_job**
> JobType create_conform_job(conform_request_type, jobmetadata=jobmetadata, notification_data=notification_data, conform_metadata=conform_metadata, thumbnail_service=thumbnail_service, tag=tag, source_tag=source_tag, notification=notification, create_thumbnails=create_thumbnails, destination_item=destination_item, create_posters=create_posters, original=original, priority=priority, resource_id=resource_id)

Start a conform job

Starts a new `CONFORM` job that creates a new item and one or more shapes that contains media according to the conform timeline.

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
api_instance = vidispine.ConformApi(vidispine.ApiClient(configuration))
conform_request_type = vidispine.ConformRequestType() # ConformRequestType | 
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
conform_metadata = True # bool | - `true` (default) - Copy metadata from the source items, according to the timeline, to the resulting item.  - `false` - Do not copy metadata from the source items. (optional) (default to True)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
tag = ['tag_example'] # list[str] | Comma-separated list of shape tags, that specify the desired output. (optional)
source_tag = ['source_tag_example'] # list[str] | Comma-separated list of shape tags, that specify the shapes that should be used as inputs. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
create_thumbnails = False # bool | - `true` - Creates thumbnails according to default transcoder rules.  - `false` (default) - No thumbnails will be created. (optional) (default to False)
destination_item = 'destination_item_example' # str | An item id, to which the new new shape will be associated. (optional)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)

try:
    # Start a conform job
    api_response = api_instance.create_conform_job(conform_request_type, jobmetadata=jobmetadata, notification_data=notification_data, conform_metadata=conform_metadata, thumbnail_service=thumbnail_service, tag=tag, source_tag=source_tag, notification=notification, create_thumbnails=create_thumbnails, destination_item=destination_item, create_posters=create_posters, original=original, priority=priority, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConformApi->create_conform_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conform_request_type** | [**ConformRequestType**](ConformRequestType.md)|  | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **conform_metadata** | **bool**| - &#x60;true&#x60; (default) - Copy metadata from the source items, according to the timeline, to the resulting item.  - &#x60;false&#x60; - Do not copy metadata from the source items. | [optional] [default to True]
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **tag** | [**list[str]**](str.md)| Comma-separated list of shape tags, that specify the desired output. | [optional] 
 **source_tag** | [**list[str]**](str.md)| Comma-separated list of shape tags, that specify the shapes that should be used as inputs. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; - Creates thumbnails according to default transcoder rules.  - &#x60;false&#x60; (default) - No thumbnails will be created. | [optional] [default to False]
 **destination_item** | **str**| An item id, to which the new new shape will be associated. | [optional] 
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 

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

