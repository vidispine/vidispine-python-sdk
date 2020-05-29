# vidispine.TaskDefinitionApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_job_type**](TaskDefinitionApi.md#create_custom_job_type) | **POST** /task-definition/jobtype/{type} | Create a new custom job type
[**create_task_definitions**](TaskDefinitionApi.md#create_task_definitions) | **POST** /task-definition | Define new task
[**delete_custom_job_type**](TaskDefinitionApi.md#delete_custom_job_type) | **DELETE** /task-definition/jobtype/{type} | Delete a custom job type
[**delete_job_step_task_definition**](TaskDefinitionApi.md#delete_job_step_task_definition) | **DELETE** /task-definition/jobtype/{type}/step/{step} | Delete a task
[**delete_job_step_task_definition_metadata**](TaskDefinitionApi.md#delete_job_step_task_definition_metadata) | **DELETE** /task-definition/jobtype/{type}/step/{step}/metadata | Delete all key-value pairs
[**delete_job_step_task_definition_metadata_key**](TaskDefinitionApi.md#delete_job_step_task_definition_metadata_key) | **DELETE** /task-definition/jobtype/{type}/step/{step}/metadata/{keypath} | Delete key-value pairs
[**delete_task_definition**](TaskDefinitionApi.md#delete_task_definition) | **DELETE** /task-definition/{task-id} | Delete a task
[**delete_task_definition_metadata**](TaskDefinitionApi.md#delete_task_definition_metadata) | **DELETE** /task-definition/{task-id}/metadata | Delete all key-value pairs
[**delete_task_definition_metadata_key**](TaskDefinitionApi.md#delete_task_definition_metadata_key) | **DELETE** /task-definition/{task-id}/metadata/{keypath} | Delete key-value pairs
[**get_job_step_task_definition**](TaskDefinitionApi.md#get_job_step_task_definition) | **GET** /task-definition/jobtype/{type}/step/{step} | Retrieve a task
[**get_job_step_task_definition_metadata**](TaskDefinitionApi.md#get_job_step_task_definition_metadata) | **GET** /task-definition/jobtype/{type}/step/{step}/metadata | Retrieve all metadata
[**get_job_step_task_definition_metadata_key**](TaskDefinitionApi.md#get_job_step_task_definition_metadata_key) | **GET** /task-definition/jobtype/{type}/step/{step}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_job_step_task_definition_script**](TaskDefinitionApi.md#get_job_step_task_definition_script) | **GET** /task-definition/jobtype/{type}/step/{step}/script | Retrieve the script for a task definition
[**get_job_type_task_definitions**](TaskDefinitionApi.md#get_job_type_task_definitions) | **GET** /task-definition/jobtype/{type} | Retrieve task definitions by type
[**get_task_definition**](TaskDefinitionApi.md#get_task_definition) | **GET** /task-definition/{task-id} | Retrieve a task
[**get_task_definition_job_graph**](TaskDefinitionApi.md#get_task_definition_job_graph) | **GET** /task-definition/jobtype/{type}/graph | Get job graph
[**get_task_definition_job_graph_dot**](TaskDefinitionApi.md#get_task_definition_job_graph_dot) | **GET** /task-definition/jobtype/{type}/graph/dot | Get job graph as DOT file
[**get_task_definition_metadata**](TaskDefinitionApi.md#get_task_definition_metadata) | **GET** /task-definition/{task-id}/metadata | Retrieve all metadata
[**get_task_definition_metadata_key**](TaskDefinitionApi.md#get_task_definition_metadata_key) | **GET** /task-definition/{task-id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_task_definition_script**](TaskDefinitionApi.md#get_task_definition_script) | **GET** /task-definition/{task-id}/script | Retrieve the script for a task definition
[**get_task_definitions**](TaskDefinitionApi.md#get_task_definitions) | **GET** /task-definition | Retrieve task definitions
[**update_job_step_task_definition**](TaskDefinitionApi.md#update_job_step_task_definition) | **PUT** /task-definition/jobtype/{type}/step/{step} | Update an existing task
[**update_job_step_task_definition_metadata**](TaskDefinitionApi.md#update_job_step_task_definition_metadata) | **PUT** /task-definition/jobtype/{type}/step/{step}/metadata | Create multiple key-value pairs
[**update_job_step_task_definition_metadata_key**](TaskDefinitionApi.md#update_job_step_task_definition_metadata_key) | **PUT** /task-definition/jobtype/{type}/step/{step}/metadata/{keypath} | Set the value for a specific key
[**update_job_step_task_definition_script**](TaskDefinitionApi.md#update_job_step_task_definition_script) | **PUT** /task-definition/jobtype/{type}/step/{step}/script | Set a script for a shape tag
[**update_task_definition**](TaskDefinitionApi.md#update_task_definition) | **PUT** /task-definition/{task-id} | Update an existing task
[**update_task_definition_metadata**](TaskDefinitionApi.md#update_task_definition_metadata) | **PUT** /task-definition/{task-id}/metadata | Create multiple key-value pairs
[**update_task_definition_metadata_key**](TaskDefinitionApi.md#update_task_definition_metadata_key) | **PUT** /task-definition/{task-id}/metadata/{keypath} | Set the value for a specific key
[**update_task_definition_script**](TaskDefinitionApi.md#update_task_definition_script) | **PUT** /task-definition/{task-id}/script | Set a script for a shape tag
[**validate_job_step_task_definition**](TaskDefinitionApi.md#validate_job_step_task_definition) | **GET** /task-definition/jobtype/{type}/step/{step}/validate | Validate a task
[**validate_task_definition**](TaskDefinitionApi.md#validate_task_definition) | **GET** /task-definition/{task-id}/validate | Validate a task


# **create_custom_job_type**
> TaskDefinitionListType create_custom_job_type(id, type)

Create a new custom job type

Creates a new job type with the specified name. The recommended format of the `type` path parameter is `{VENDOR_PREFIX}_{JOB_TYPE}`.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
id = 56 # int | An integer between 20000 and 30000, must be unique among job types.
type = 'type_example' # str | The type.

try:
    # Create a new custom job type
    api_response = api_instance.create_custom_job_type(id, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->create_custom_job_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| An integer between 20000 and 30000, must be unique among job types. | 
 **type** | **str**| The type. | 

### Return type

[**TaskDefinitionListType**](TaskDefinitionListType.md)

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

# **create_task_definitions**
> URIListType create_task_definitions(task_definition_list_type, url=url)

Define new task

Defines one or more new tasks.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_definition_list_type = vidispine.TaskDefinitionListType() # TaskDefinitionListType | 
url = False # bool | - `true` - Return list of URLs.  - `false` (default) - Return list of ids. (optional) (default to False)

try:
    # Define new task
    api_response = api_instance.create_task_definitions(task_definition_list_type, url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->create_task_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_definition_list_type** | [**TaskDefinitionListType**](TaskDefinitionListType.md)|  | 
 **url** | **bool**| - &#x60;true&#x60; - Return list of URLs.  - &#x60;false&#x60; (default) - Return list of ids. | [optional] [default to False]

### Return type

[**URIListType**](URIListType.md)

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

# **delete_custom_job_type**
> delete_custom_job_type(type)

Delete a custom job type

Deletes the job type with the specified name. This will only work for custom job types. System defined job types cannot be deleted.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.

try:
    # Delete a custom job type
    api_instance.delete_custom_job_type(type)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->delete_custom_job_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 

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

# **delete_job_step_task_definition**
> delete_job_step_task_definition(type, step)

Delete a task

Deletes the task.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.

try:
    # Delete a task
    api_instance.delete_job_step_task_definition(type, step)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->delete_job_step_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 

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

# **delete_job_step_task_definition_metadata**
> delete_job_step_task_definition_metadata(type, step)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.

try:
    # Delete all key-value pairs
    api_instance.delete_job_step_task_definition_metadata(type, step)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->delete_job_step_task_definition_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 

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

# **delete_job_step_task_definition_metadata_key**
> delete_job_step_task_definition_metadata_key(type, step, keypath)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_job_step_task_definition_metadata_key(type, step, keypath)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->delete_job_step_task_definition_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 
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

# **delete_task_definition**
> delete_task_definition(task_id)

Delete a task

Deletes the task.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.

try:
    # Delete a task
    api_instance.delete_task_definition(task_id)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->delete_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 

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

# **delete_task_definition_metadata**
> delete_task_definition_metadata(task_id)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.

try:
    # Delete all key-value pairs
    api_instance.delete_task_definition_metadata(task_id)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->delete_task_definition_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 

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

# **delete_task_definition_metadata_key**
> delete_task_definition_metadata_key(task_id, keypath)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_task_definition_metadata_key(task_id, keypath)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->delete_task_definition_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 
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

# **get_job_step_task_definition**
> TaskDefinitionType get_job_step_task_definition(type, step)

Retrieve a task

Retrieves the definition document for a task with a specific id.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.

try:
    # Retrieve a task
    api_response = api_instance.get_job_step_task_definition(type, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_job_step_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 

### Return type

[**TaskDefinitionType**](TaskDefinitionType.md)

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

# **get_job_step_task_definition_metadata**
> SimpleMetadataType get_job_step_task_definition_metadata(type, step)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.

try:
    # Retrieve all metadata
    api_response = api_instance.get_job_step_task_definition_metadata(type, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_job_step_task_definition_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 

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

# **get_job_step_task_definition_metadata_key**
> str get_job_step_task_definition_metadata_key(type, step, keypath)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_job_step_task_definition_metadata_key(type, step, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_job_step_task_definition_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 
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

# **get_job_step_task_definition_script**
> str get_job_step_task_definition_script(type, step)

Retrieve the script for a task definition

Retrieves the script of the task definition.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.

try:
    # Retrieve the script for a task definition
    api_response = api_instance.get_job_step_task_definition_script(type, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_job_step_task_definition_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A JavaScript |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_type_task_definitions**
> TaskDefinitionListType get_job_type_task_definitions(type)

Retrieve task definitions by type

Retrieves the tasks that have been defined for a specific job type.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.

try:
    # Retrieve task definitions by type
    api_response = api_instance.get_job_type_task_definitions(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_job_type_task_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 

### Return type

[**TaskDefinitionListType**](TaskDefinitionListType.md)

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

# **get_task_definition**
> TaskDefinitionType get_task_definition(task_id)

Retrieve a task

Retrieves the definition document for a task with a specific id.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.

try:
    # Retrieve a task
    api_response = api_instance.get_task_definition(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 

### Return type

[**TaskDefinitionType**](TaskDefinitionType.md)

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

# **get_task_definition_job_graph**
> file get_task_definition_job_graph(type)

Get job graph

Shows the dependencies of the tasks of a specified job type.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.

try:
    # Get job graph
    api_response = api_instance.get_task_definition_job_graph(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_task_definition_job_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_definition_job_graph_dot**
> str get_task_definition_job_graph_dot(type)

Get job graph as DOT file

Shows the dependencies of the tasks of a specified job type in DOT format, for further processing.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.

try:
    # Get job graph as DOT file
    api_response = api_instance.get_task_definition_job_graph_dot(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_task_definition_job_graph_dot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/vnd.graphviz, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_definition_metadata**
> SimpleMetadataType get_task_definition_metadata(task_id)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_task_definition_metadata(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_task_definition_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 

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

# **get_task_definition_metadata_key**
> str get_task_definition_metadata_key(task_id, keypath)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_task_definition_metadata_key(task_id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_task_definition_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 
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

# **get_task_definition_script**
> str get_task_definition_script(task_id)

Retrieve the script for a task definition

Retrieves the script of the task definition.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.

try:
    # Retrieve the script for a task definition
    api_response = api_instance.get_task_definition_script(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_task_definition_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A JavaScript |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_definitions**
> TaskDefinitionListType get_task_definitions(type=type)

Retrieve task definitions

Retrieves all tasks that have been defined in the system.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | Job type to retrieve task definitions for. (optional)

try:
    # Retrieve task definitions
    api_response = api_instance.get_task_definitions(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->get_task_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Job type to retrieve task definitions for. | [optional] 

### Return type

[**TaskDefinitionListType**](TaskDefinitionListType.md)

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

# **update_job_step_task_definition**
> TaskDefinitionType update_job_step_task_definition(type, step, task_definition_type)

Update an existing task

Updates the task.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.
task_definition_type = vidispine.TaskDefinitionType() # TaskDefinitionType | 

try:
    # Update an existing task
    api_response = api_instance.update_job_step_task_definition(type, step, task_definition_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->update_job_step_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 
 **task_definition_type** | [**TaskDefinitionType**](TaskDefinitionType.md)|  | 

### Return type

[**TaskDefinitionType**](TaskDefinitionType.md)

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

# **update_job_step_task_definition_metadata**
> update_job_step_task_definition_metadata(type, step, simple_metadata_type)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_job_step_task_definition_metadata(type, step, simple_metadata_type)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->update_job_step_task_definition_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 
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

# **update_job_step_task_definition_metadata_key**
> update_job_step_task_definition_metadata_key(type, step, keypath, body)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_job_step_task_definition_metadata_key(type, step, keypath, body)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->update_job_step_task_definition_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 
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

# **update_job_step_task_definition_script**
> update_job_step_task_definition_script(type, step, body)

Set a script for a shape tag

Sets a script for the task definition.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.
body = 'body_example' # str | A JavaScript

try:
    # Set a script for a shape tag
    api_instance.update_job_step_task_definition_script(type, step, body)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->update_job_step_task_definition_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 
 **body** | **str**| A JavaScript | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/javascript
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_definition**
> TaskDefinitionType update_task_definition(task_id, task_definition_type)

Update an existing task

Updates the task.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.
task_definition_type = vidispine.TaskDefinitionType() # TaskDefinitionType | 

try:
    # Update an existing task
    api_response = api_instance.update_task_definition(task_id, task_definition_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->update_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 
 **task_definition_type** | [**TaskDefinitionType**](TaskDefinitionType.md)|  | 

### Return type

[**TaskDefinitionType**](TaskDefinitionType.md)

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

# **update_task_definition_metadata**
> update_task_definition_metadata(task_id, simple_metadata_type)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_task_definition_metadata(task_id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->update_task_definition_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 
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

# **update_task_definition_metadata_key**
> update_task_definition_metadata_key(task_id, keypath, body)

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_task_definition_metadata_key(task_id, keypath, body)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->update_task_definition_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 
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

# **update_task_definition_script**
> update_task_definition_script(task_id, body)

Set a script for a shape tag

Sets a script for the task definition.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.
body = 'body_example' # str | A JavaScript

try:
    # Set a script for a shape tag
    api_instance.update_task_definition_script(task_id, body)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->update_task_definition_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 
 **body** | **str**| A JavaScript | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/javascript
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_job_step_task_definition**
> str validate_job_step_task_definition(type, step)

Validate a task

Verifies that the bean referred to in the task can be resolved and that it contains the specified method.  Does nothing if the task is a script task.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
step = 'step_example' # str | The step.

try:
    # Validate a task
    api_response = api_instance.validate_job_step_task_definition(type, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->validate_job_step_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **step** | **str**| The step. | 

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
**0** | Informational status text. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_task_definition**
> str validate_task_definition(task_id)

Validate a task

Verifies that the bean referred to in the task can be resolved and that it contains the specified method.  Does nothing if the task is a script task.

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
api_instance = vidispine.TaskDefinitionApi(vidispine.ApiClient(configuration))
task_id = 'task_id_example' # str | The task id.

try:
    # Validate a task
    api_response = api_instance.validate_task_definition(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDefinitionApi->validate_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The task id. | 

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
**0** | Informational status text. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

