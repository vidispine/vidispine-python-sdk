# vidispine.JobApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_job**](JobApi.md#abort_job) | **DELETE** /job/{job-id} | Abort a job
[**create_custom_job**](JobApi.md#create_custom_job) | **POST** /job | Start a job with custom type
[**create_duplicate_job**](JobApi.md#create_duplicate_job) | **POST** /job/{job-id}/re-run | Create a duplicate job
[**delete_jobs**](JobApi.md#delete_jobs) | **DELETE** /job | Delete one or several jobs
[**get_all_job_problems**](JobApi.md#get_all_job_problems) | **GET** /job/problem | List all job problems
[**get_job**](JobApi.md#get_job) | **GET** /job/{job-id} | Retrieve a job
[**get_job_problems**](JobApi.md#get_job_problems) | **GET** /job/{job-id}/problem | List all problems for a job
[**get_job_types**](JobApi.md#get_job_types) | **GET** /jobtype | List all job types
[**get_jobs**](JobApi.md#get_jobs) | **GET** /job | List all jobs
[**update_job**](JobApi.md#update_job) | **PUT** /job/{job-id} | Modify a job


# **abort_job**
> abort_job(job_id, reason=reason, cleanup=cleanup)

Abort a job

Does not delete the job, but aborts it.  To delete one or more jobs, use `DELETE /job`.  The job is marked for abortion, but the call may return before all tasks have been killed. Hence, the status return by this call is likely to be ABORT_PENDING rather than ABORTED. Caller should poll the status of the job or use job notifications to find out when job has been fully aborted.

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
api_instance = vidispine.JobApi(vidispine.ApiClient(configuration))
job_id = 'job_id_example' # str | The job id.
reason = 'reason_example' # str | Reason for cancellation. (optional)
cleanup = True # bool | - `true` (default) - Run cleanup steps before aborting.  - `false` - Skip the cleanup steps, unless the job is already running.  For READY jobs this means that the job will immediately be marked as ABORTED. (optional) (default to True)

try:
    # Abort a job
    api_instance.abort_job(job_id, reason=reason, cleanup=cleanup)
except ApiException as e:
    print("Exception when calling JobApi->abort_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id. | 
 **reason** | **str**| Reason for cancellation. | [optional] 
 **cleanup** | **bool**| - &#x60;true&#x60; (default) - Run cleanup steps before aborting.  - &#x60;false&#x60; - Skip the cleanup steps, unless the job is already running.  For READY jobs this means that the job will immediately be marked as ABORTED. | [optional] [default to True]

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

# **create_custom_job**
> JobType create_custom_job(type, simple_metadata_type, jobmetadata=jobmetadata, notification_data=notification_data, priority=priority, notification=notification)

Start a job with custom type

Starts a new job, of the type specified in the `type` parameter.  Changed in version 5.0.  Additional job metadata can also be added using an *optional* *SimpleMetadataDocument*. If any `jobmetadata` keys would collide between the query parameters and the *SimpleMetadataDocument*, the key and value from the *SimpleMetadataDocument* would have precedence over the query parameter.

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
api_instance = vidispine.JobApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The job type name.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)

try:
    # Start a job with custom type
    api_response = api_instance.create_custom_job(type, simple_metadata_type, jobmetadata=jobmetadata, notification_data=notification_data, priority=priority, notification=notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->create_custom_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The job type name. | 
 **simple_metadata_type** | [**SimpleMetadataType**](SimpleMetadataType.md)|  | 
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

# **create_duplicate_job**
> JobType create_duplicate_job(job_id, priority=priority)

Create a duplicate job

Retrieves an existing job, duplicates it and starts the duplicated version.

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
api_instance = vidispine.JobApi(vidispine.ApiClient(configuration))
job_id = 'job_id_example' # str | The job id.
priority = 'priority_example' # str | The priority of the new job.  If no priority is specified then the priority of the existing job will be used. (optional)

try:
    # Create a duplicate job
    api_response = api_instance.create_duplicate_job(job_id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->create_duplicate_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id. | 
 **priority** | **str**| The priority of the new job.  If no priority is specified then the priority of the existing job will be used. | [optional] 

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

# **delete_jobs**
> delete_jobs(id)

Delete one or several jobs

Deletes a job and every related database entry.

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
api_instance = vidispine.JobApi(vidispine.ApiClient(configuration))
id = ['id_example'] # list[str] | Comma-separated list of job ids.

try:
    # Delete one or several jobs
    api_instance.delete_jobs(id)
except ApiException as e:
    print("Exception when calling JobApi->delete_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| Comma-separated list of job ids. | 

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

# **get_all_job_problems**
> JobProblemListType get_all_job_problems()

List all job problems

Returns a list of unresolved problems, together with what jobs are waiting for them to be resolved.

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
api_instance = vidispine.JobApi(vidispine.ApiClient(configuration))

try:
    # List all job problems
    api_response = api_instance.get_all_job_problems()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_all_job_problems: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JobProblemListType**](JobProblemListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;JobProblemListDocument&lt;/em&gt;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> JobType get_job(job_id, field=field, metadata=metadata)

Retrieve a job

Return information about specified job.  When returning in format `text/plain`, only a string representation of the state is returned.

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
api_instance = vidispine.JobApi(vidispine.ApiClient(configuration))
job_id = 'job_id_example' # str | The job id.
field = ['field_example'] # list[str] | Comma-separated list of fields to include in the result metadata. (optional)
metadata = False # bool | - `true` - Include job metadata with all jobs.  - `false` (default) - Do not include job metadata with all jobs. (optional) (default to False)

try:
    # Retrieve a job
    api_response = api_instance.get_job(job_id, field=field, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id. | 
 **field** | [**list[str]**](str.md)| Comma-separated list of fields to include in the result metadata. | [optional] 
 **metadata** | **bool**| - &#x60;true&#x60; - Include job metadata with all jobs.  - &#x60;false&#x60; (default) - Do not include job metadata with all jobs. | [optional] [default to False]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | State of job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_problems**
> JobProblemListType get_job_problems(job_id)

List all problems for a job

Retrieves a list of problems that affects the specified job.

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
api_instance = vidispine.JobApi(vidispine.ApiClient(configuration))
job_id = 'job_id_example' # str | The job id.

try:
    # List all problems for a job
    api_response = api_instance.get_job_problems(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_problems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id. | 

### Return type

[**JobProblemListType**](JobProblemListType.md)

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

# **get_job_types**
> URIListType get_job_types()

List all job types

Get list of job types

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
api_instance = vidispine.JobApi(vidispine.ApiClient(configuration))

try:
    # List all job types
    api_response = api_instance.get_job_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**0** | list of job types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> JobListType get_jobs(jobmetadata=jobmetadata, field=field, starttime_to=starttime_to, user=user, first=first, type=type, starttime_from=starttime_from, step=step, idonly=idonly, number=number, state=state, sort=sort, metadata=metadata, finishtime_from=finishtime_from, finishtime_to=finishtime_to)

List all jobs

Return jobs matching the criteria given.

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
api_instance = vidispine.JobApi(vidispine.ApiClient(configuration))
jobmetadata = ['jobmetadata_example'] # list[str] | Multiple query parameters can be specified.  If no query parameters are specified, all jobs are returned.   - *key* `=` *value* - Filter out only the jobs that has job metadata according to the filter criteria.  Note that `=` is part of the query parameter, and has to be encoded (`%3d`). (optional)
field = ['field_example'] # list[str] | Comma-separated list of fields to include in the result metadata. (optional)
starttime_to = 'starttime_to_example' # str | ISO 8601 timestamp.  Return only jobs started before and at the given timestamp. (optional)
user = True # bool | - `true` (default) - Include only jobs created by current user - `false` - Include all jobs (optional) (default to True)
first = 1 # int | Return jobs from that number in the list of sorted jobs. (optional) (default to 1)
type = ["all"] # list[str] | Comma-separated list of job types. (optional) (default to ["all"])
starttime_from = 'starttime_from_example' # str | ISO 8601 timestamp.  Return only jobs started after and at the given timestamp. (optional)
step = False # bool | - `true` - Include step information in the job listing.  - `false` (default) - Do not include step information in the job listing. (optional) (default to False)
idonly = True # bool | - `true` - Only return a list of ids - `false` (default) - Return job information such as job status (optional)
number = 56 # int | Return at most that number of jobs.  Default returns the first 100 jobs. (optional)
state = ["all"] # list[str] | Comma-separated list of job states. (optional) (default to ["all"])
sort = 'sort_example' # str | List of form `field (asc|desc)[, . . . ]`.  Sort by specific fields.   - `jobId` - `type` - `state` - `user` - `startTime` - `priority` (optional)
metadata = False # bool | - `true` - Include job metadata with all jobs.  - `false` (default) - Do not include job metadata with all jobs. (optional) (default to False)
finishtime_from = 'finishtime_from_example' # str | ISO 8601 timestamp.  Return only jobs finished after and at the given timestamp. (optional)
finishtime_to = 'finishtime_to_example' # str | ISO 8601 timestamp.  Return only jobs finished before and at the given timestamp. (optional)

try:
    # List all jobs
    api_response = api_instance.get_jobs(jobmetadata=jobmetadata, field=field, starttime_to=starttime_to, user=user, first=first, type=type, starttime_from=starttime_from, step=step, idonly=idonly, number=number, state=state, sort=sort, metadata=metadata, finishtime_from=finishtime_from, finishtime_to=finishtime_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobmetadata** | [**list[str]**](str.md)| Multiple query parameters can be specified.  If no query parameters are specified, all jobs are returned.   - *key* &#x60;&#x3D;&#x60; *value* - Filter out only the jobs that has job metadata according to the filter criteria.  Note that &#x60;&#x3D;&#x60; is part of the query parameter, and has to be encoded (&#x60;%3d&#x60;). | [optional] 
 **field** | [**list[str]**](str.md)| Comma-separated list of fields to include in the result metadata. | [optional] 
 **starttime_to** | **str**| ISO 8601 timestamp.  Return only jobs started before and at the given timestamp. | [optional] 
 **user** | **bool**| - &#x60;true&#x60; (default) - Include only jobs created by current user - &#x60;false&#x60; - Include all jobs | [optional] [default to True]
 **first** | **int**| Return jobs from that number in the list of sorted jobs. | [optional] [default to 1]
 **type** | [**list[str]**](str.md)| Comma-separated list of job types. | [optional] [default to [&quot;all&quot;]]
 **starttime_from** | **str**| ISO 8601 timestamp.  Return only jobs started after and at the given timestamp. | [optional] 
 **step** | **bool**| - &#x60;true&#x60; - Include step information in the job listing.  - &#x60;false&#x60; (default) - Do not include step information in the job listing. | [optional] [default to False]
 **idonly** | **bool**| - &#x60;true&#x60; - Only return a list of ids - &#x60;false&#x60; (default) - Return job information such as job status | [optional] 
 **number** | **int**| Return at most that number of jobs.  Default returns the first 100 jobs. | [optional] 
 **state** | [**list[str]**](str.md)| Comma-separated list of job states. | [optional] [default to [&quot;all&quot;]]
 **sort** | **str**| List of form &#x60;field (asc|desc)[, . . . ]&#x60;.  Sort by specific fields.   - &#x60;jobId&#x60; - &#x60;type&#x60; - &#x60;state&#x60; - &#x60;user&#x60; - &#x60;startTime&#x60; - &#x60;priority&#x60; | [optional] 
 **metadata** | **bool**| - &#x60;true&#x60; - Include job metadata with all jobs.  - &#x60;false&#x60; (default) - Do not include job metadata with all jobs. | [optional] [default to False]
 **finishtime_from** | **str**| ISO 8601 timestamp.  Return only jobs finished after and at the given timestamp. | [optional] 
 **finishtime_to** | **str**| ISO 8601 timestamp.  Return only jobs finished before and at the given timestamp. | [optional] 

### Return type

[**JobListType**](JobListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of job ids. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job**
> update_job(job_id, priority=priority)

Modify a job

Updates the job by setting job priority

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
api_instance = vidispine.JobApi(vidispine.ApiClient(configuration))
job_id = 'job_id_example' # str | The job id.
priority = 'MEDIUM' # str | Change the job priority (optional) (default to 'MEDIUM')

try:
    # Modify a job
    api_instance.update_job(job_id, priority=priority)
except ApiException as e:
    print("Exception when calling JobApi->update_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id. | 
 **priority** | **str**| Change the job priority | [optional] [default to &#39;MEDIUM&#39;]

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

