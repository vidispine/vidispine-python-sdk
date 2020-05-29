# vidispine.VidispineLogsApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vidispine_log_job**](VidispineLogsApi.md#create_vidispine_log_job) | **POST** /vidispine-logs/job | Start a log report job
[**create_vidispine_log_job_upload**](VidispineLogsApi.md#create_vidispine_log_job_upload) | **POST** /vidispine-logs/job/{job-id}/upload | Start an upload
[**delete_vidispine_log_job**](VidispineLogsApi.md#delete_vidispine_log_job) | **DELETE** /vidispine-logs/job/{job-id} | Delete a log report job
[**delete_vidispine_log_job_upload**](VidispineLogsApi.md#delete_vidispine_log_job_upload) | **DELETE** /vidispine-logs/job/{job-id}/upload | Abort an upload
[**get_vidispine_log_job**](VidispineLogsApi.md#get_vidispine_log_job) | **GET** /vidispine-logs/job/{job-id} | Retrieve a log report job
[**get_vidispine_log_job_file_info**](VidispineLogsApi.md#get_vidispine_log_job_file_info) | **GET** /vidispine-logs/job/{job-id}/uri | Retrieve files in job
[**get_vidispine_log_jobs**](VidispineLogsApi.md#get_vidispine_log_jobs) | **GET** /vidispine-logs/job | List all log report jobs
[**get_vidispine_logs**](VidispineLogsApi.md#get_vidispine_logs) | **GET** /vidispine-logs | Retrieve log files


# **create_vidispine_log_job**
> JobType create_vidispine_log_job(endtime, starttime, storage=storage, comment=comment, item=item, user=user, job=job, selftest=selftest)

Start a log report job

Starts a log report job that collects service log files into a zip file.

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
api_instance = vidispine.VidispineLogsApi(vidispine.ApiClient(configuration))
endtime = 'endtime_example' # str | ISO 8601 end time of time span.
starttime = 'starttime_example' # str | ISO 8601 start time of time span.
storage = ['storage_example'] # list[str] | Comma-separated list of storage ids to retrieve information about. (optional)
comment = 'comment_example' # str | Detailed description of what the problem is, to be written in zip file. (optional)
item = ['item_example'] # list[str] | Comma-separated list of item ids to retrieve information about. (optional)
user = ['user_example'] # list[str] | Comma-separated list of user names to retrieve information about. (optional)
job = ['job_example'] # list[str] | Comma-separated list of job ids to retrieve information about. (optional)
selftest = False # bool | If `true`, includes the result of a self-test. (optional) (default to False)

try:
    # Start a log report job
    api_response = api_instance.create_vidispine_log_job(endtime, starttime, storage=storage, comment=comment, item=item, user=user, job=job, selftest=selftest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VidispineLogsApi->create_vidispine_log_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endtime** | **str**| ISO 8601 end time of time span. | 
 **starttime** | **str**| ISO 8601 start time of time span. | 
 **storage** | [**list[str]**](str.md)| Comma-separated list of storage ids to retrieve information about. | [optional] 
 **comment** | **str**| Detailed description of what the problem is, to be written in zip file. | [optional] 
 **item** | [**list[str]**](str.md)| Comma-separated list of item ids to retrieve information about. | [optional] 
 **user** | [**list[str]**](str.md)| Comma-separated list of user names to retrieve information about. | [optional] 
 **job** | [**list[str]**](str.md)| Comma-separated list of job ids to retrieve information about. | [optional] 
 **selftest** | **bool**| If &#x60;true&#x60;, includes the result of a self-test. | [optional] [default to False]

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
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vidispine_log_job_upload**
> create_vidispine_log_job_upload(job_id, uri_list_type)

Start an upload

Starts upload.

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
api_instance = vidispine.VidispineLogsApi(vidispine.ApiClient(configuration))
job_id = 'job_id_example' # str | The job id.
uri_list_type = vidispine.URIListType() # URIListType | A <em>URIListDocument</em> with URIs from the list of files in the log.

try:
    # Start an upload
    api_instance.create_vidispine_log_job_upload(job_id, uri_list_type)
except ApiException as e:
    print("Exception when calling VidispineLogsApi->create_vidispine_log_job_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id. | 
 **uri_list_type** | [**URIListType**](URIListType.md)| A &lt;em&gt;URIListDocument&lt;/em&gt; with URIs from the list of files in the log. | 

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

# **delete_vidispine_log_job**
> delete_vidispine_log_job(job_id)

Delete a log report job

Deletes a job and the report created.

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
api_instance = vidispine.VidispineLogsApi(vidispine.ApiClient(configuration))
job_id = 'job_id_example' # str | The job id.

try:
    # Delete a log report job
    api_instance.delete_vidispine_log_job(job_id)
except ApiException as e:
    print("Exception when calling VidispineLogsApi->delete_vidispine_log_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id. | 

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

# **delete_vidispine_log_job_upload**
> delete_vidispine_log_job_upload(job_id)

Abort an upload

Aborts upload process.

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
api_instance = vidispine.VidispineLogsApi(vidispine.ApiClient(configuration))
job_id = 'job_id_example' # str | The job id.

try:
    # Abort an upload
    api_instance.delete_vidispine_log_job_upload(job_id)
except ApiException as e:
    print("Exception when calling VidispineLogsApi->delete_vidispine_log_job_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id. | 

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

# **get_vidispine_log_job**
> JobType get_vidispine_log_job(job_id)

Retrieve a log report job

Return information about specified job.

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
api_instance = vidispine.VidispineLogsApi(vidispine.ApiClient(configuration))
job_id = 'job_id_example' # str | The job id.

try:
    # Retrieve a log report job
    api_response = api_instance.get_vidispine_log_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VidispineLogsApi->get_vidispine_log_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id. | 

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

# **get_vidispine_log_job_file_info**
> str get_vidispine_log_job_file_info(job_id)

Retrieve files in job

Return file information about specified job.

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
api_instance = vidispine.VidispineLogsApi(vidispine.ApiClient(configuration))
job_id = 'job_id_example' # str | The job id.

try:
    # Retrieve files in job
    api_response = api_instance.get_vidispine_log_job_file_info(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VidispineLogsApi->get_vidispine_log_job_file_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An array of objects with keys name, &lt;code&gt;displayUri&lt;/code&gt;, &lt;code&gt;uri&lt;/code&gt;, and &lt;code&gt;size&lt;/code&gt;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vidispine_log_jobs**
> JobListType get_vidispine_log_jobs()

List all log report jobs

Return information about all jobs that have not expired.

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
api_instance = vidispine.VidispineLogsApi(vidispine.ApiClient(configuration))

try:
    # List all log report jobs
    api_response = api_instance.get_vidispine_log_jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VidispineLogsApi->get_vidispine_log_jobs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JobListType**](JobListType.md)

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

# **get_vidispine_logs**
> str get_vidispine_logs(endtime, starttime, storage=storage, comment=comment, item=item, user=user, job=job, selftest=selftest)

Retrieve log files

Retrieves a zip file with the various service log files.

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
api_instance = vidispine.VidispineLogsApi(vidispine.ApiClient(configuration))
endtime = 'endtime_example' # str | ISO 8601 end time of time span.
starttime = 'starttime_example' # str | ISO 8601 start time of time span.
storage = ['storage_example'] # list[str] | Comma-separated list of storage ids to retrieve information about. (optional)
comment = 'comment_example' # str | Detailed description of what the problem is, to be written in zip file. (optional)
item = ['item_example'] # list[str] | Comma-separated list of item ids to retrieve information about. (optional)
user = ['user_example'] # list[str] | Comma-separated list of user names to retrieve information about. (optional)
job = ['job_example'] # list[str] | Comma-separated list of job ids to retrieve information about. (optional)
selftest = False # bool | If `true`, includes the result of a self-test. (optional) (default to False)

try:
    # Retrieve log files
    api_response = api_instance.get_vidispine_logs(endtime, starttime, storage=storage, comment=comment, item=item, user=user, job=job, selftest=selftest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VidispineLogsApi->get_vidispine_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endtime** | **str**| ISO 8601 end time of time span. | 
 **starttime** | **str**| ISO 8601 start time of time span. | 
 **storage** | [**list[str]**](str.md)| Comma-separated list of storage ids to retrieve information about. | [optional] 
 **comment** | **str**| Detailed description of what the problem is, to be written in zip file. | [optional] 
 **item** | [**list[str]**](str.md)| Comma-separated list of item ids to retrieve information about. | [optional] 
 **user** | [**list[str]**](str.md)| Comma-separated list of user names to retrieve information about. | [optional] 
 **job** | [**list[str]**](str.md)| Comma-separated list of job ids to retrieve information about. | [optional] 
 **selftest** | **bool**| If &#x60;true&#x60;, includes the result of a self-test. | [optional] [default to False]

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, multipart/mixed, multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A multi-part response, with parts: &lt;ul&gt;&lt;li&gt;&lt;code&gt;zip&lt;/code&gt; Containing the zip file.&lt;/li&gt;&lt;li&gt;&lt;code&gt;message-text&lt;/code&gt; Containing CRLF-separated list of warnings.&lt;/li&gt;&lt;li&gt;&lt;code&gt;message-json&lt;/code&gt; Containing JSON array list of warnings.&lt;/li&gt;&lt;/ul&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

