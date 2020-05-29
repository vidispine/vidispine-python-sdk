# vidispine.AnalyzeApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_analyze_job**](AnalyzeApi.md#create_item_analyze_job) | **POST** /item/{item-id}/analyze | Analyze an item
[**create_shape_analyze_job**](AnalyzeApi.md#create_shape_analyze_job) | **POST** /item/{item-id}/shape/{shape-id}/analyze | Analyze a specific shape


# **create_item_analyze_job**
> JobType create_item_analyze_job(item_id, analyze_job_type, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, tag=tag, notification=notification, priority=priority, resource_id=resource_id)

Analyze an item

Analyzes an item with the parameters specified in the job document. The result of the analyze will appear in the bulky metadata of the shape when doing a transcoder analysis, or in the metadata of the item when doing a cognitive service analysis.  New in version 5.0.

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
api_instance = vidispine.AnalyzeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
analyze_job_type = vidispine.AnalyzeJobType() # AnalyzeJobType | 
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
storage_id = 'storage_id_example' # str | The storage on which to store a temporary analysis data file when using a Vidinet transcoder to analyze a shape.  If no storage id has been specified Vidispine will (by default) automatically pick a supported storage.  The storage id will be ignored when using a non Vidinet transcoder. (optional)
tag = 'tag_example' # str | The shape tag to analyze.  If omitted the original shape tag will be used. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
resource_id = 'resource_id_example' # str | The transcoder or cognitive service resource to use to execute the analysis. (optional)

try:
    # Analyze an item
    api_response = api_instance.create_item_analyze_job(item_id, analyze_job_type, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, tag=tag, notification=notification, priority=priority, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyzeApi->create_item_analyze_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **analyze_job_type** | [**AnalyzeJobType**](AnalyzeJobType.md)|  | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **storage_id** | **str**| The storage on which to store a temporary analysis data file when using a Vidinet transcoder to analyze a shape.  If no storage id has been specified Vidispine will (by default) automatically pick a supported storage.  The storage id will be ignored when using a non Vidinet transcoder. | [optional] 
 **tag** | **str**| The shape tag to analyze.  If omitted the original shape tag will be used. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **resource_id** | **str**| The transcoder or cognitive service resource to use to execute the analysis. | [optional] 

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

# **create_shape_analyze_job**
> JobType create_shape_analyze_job(item_id, shape_id, analyze_job_type, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, notification=notification, priority=priority, resource_id=resource_id)

Analyze a specific shape

Analyzes the specified shape with the parameters specified in the job document. The result of the analyze will appear in the bulky metadata of the shape when doing a transcoder analysis, or in the metadata of the item when doing a cognitive service analysis.

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
api_instance = vidispine.AnalyzeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
analyze_job_type = vidispine.AnalyzeJobType() # AnalyzeJobType | 
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
storage_id = 'storage_id_example' # str | The storage on which to store a temporary analysis data file when using a Vidinet transcoder to analyze a shape.  If no storage id has been specified Vidispine will (by default) automatically pick a supported storage.  The storage id will be ignored when using a non Vidinet transcoder. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
resource_id = 'resource_id_example' # str | The transcoder or cognitive service resource to use to execute the analysis. (optional)

try:
    # Analyze a specific shape
    api_response = api_instance.create_shape_analyze_job(item_id, shape_id, analyze_job_type, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, notification=notification, priority=priority, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyzeApi->create_shape_analyze_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **analyze_job_type** | [**AnalyzeJobType**](AnalyzeJobType.md)|  | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **storage_id** | **str**| The storage on which to store a temporary analysis data file when using a Vidinet transcoder to analyze a shape.  If no storage id has been specified Vidispine will (by default) automatically pick a supported storage.  The storage id will be ignored when using a non Vidinet transcoder. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **resource_id** | **str**| The transcoder or cognitive service resource to use to execute the analysis. | [optional] 

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

