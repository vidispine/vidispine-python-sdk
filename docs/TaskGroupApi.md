# vidispine.TaskGroupApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_task_group_transcoder**](TaskGroupApi.md#add_task_group_transcoder) | **PUT** /task-group/{group-name}/transcoder/{transcoder-id} | Add a transcoder to a task group
[**delete_task_group**](TaskGroupApi.md#delete_task_group) | **DELETE** /task-group/{group-name} | Delete a task group
[**delete_task_group_metadata**](TaskGroupApi.md#delete_task_group_metadata) | **DELETE** /task-group/{group-name}/metadata | Delete all key-value pairs
[**delete_task_group_metadata_key**](TaskGroupApi.md#delete_task_group_metadata_key) | **DELETE** /task-group/{group-name}/metadata/{keypath} | Delete key-value pairs
[**delete_task_groups**](TaskGroupApi.md#delete_task_groups) | **DELETE** /task-group | Delete all task groups
[**get_task_group**](TaskGroupApi.md#get_task_group) | **GET** /task-group/{group-name} | Retrieve a task group
[**get_task_group_metadata**](TaskGroupApi.md#get_task_group_metadata) | **GET** /task-group/{group-name}/metadata | Retrieve all metadata
[**get_task_group_metadata_key**](TaskGroupApi.md#get_task_group_metadata_key) | **GET** /task-group/{group-name}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_task_groups**](TaskGroupApi.md#get_task_groups) | **GET** /task-group | List all task groups
[**remove_task_group_transcoder**](TaskGroupApi.md#remove_task_group_transcoder) | **DELETE** /task-group/{group-name}/transcoder/{transcoder-id} | Remove a transcoder from a task group
[**update_or_create_task_group**](TaskGroupApi.md#update_or_create_task_group) | **PUT** /task-group/{group-name} | Update or create a task group
[**update_task_group_metadata**](TaskGroupApi.md#update_task_group_metadata) | **PUT** /task-group/{group-name}/metadata | Create multiple key-value pairs
[**update_task_group_metadata_key**](TaskGroupApi.md#update_task_group_metadata_key) | **PUT** /task-group/{group-name}/metadata/{keypath} | Set the value for a specific key


# **add_task_group_transcoder**
> add_task_group_transcoder(group_name, transcoder_id)

Add a transcoder to a task group

Adds the transcoder to the specified task group.

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
transcoder_id = 'transcoder_id_example' # str | The transcoder id.

try:
    # Add a transcoder to a task group
    api_instance.add_task_group_transcoder(group_name, transcoder_id)
except ApiException as e:
    print("Exception when calling TaskGroupApi->add_task_group_transcoder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **transcoder_id** | **str**| The transcoder id. | 

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

# **delete_task_group**
> delete_task_group(group_name)

Delete a task group

Deletes the task group.  Note that this only deletes the task group. It will not remove any transcoders or other resources that are in the group.

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Delete a task group
    api_instance.delete_task_group(group_name)
except ApiException as e:
    print("Exception when calling TaskGroupApi->delete_task_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

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

# **delete_task_group_metadata**
> delete_task_group_metadata(group_name)

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Delete all key-value pairs
    api_instance.delete_task_group_metadata(group_name)
except ApiException as e:
    print("Exception when calling TaskGroupApi->delete_task_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

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

# **delete_task_group_metadata_key**
> delete_task_group_metadata_key(group_name, keypath)

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_task_group_metadata_key(group_name, keypath)
except ApiException as e:
    print("Exception when calling TaskGroupApi->delete_task_group_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
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

# **delete_task_groups**
> delete_task_groups()

Delete all task groups

Deletes all task groups.  Note that this only deletes the task groups. It will not remove any transcoders or other resources that are in the groups.

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))

try:
    # Delete all task groups
    api_instance.delete_task_groups()
except ApiException as e:
    print("Exception when calling TaskGroupApi->delete_task_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **get_task_group**
> TaskGroupType get_task_group(group_name)

Retrieve a task group

Retrieves the task group document for a task group with a specific name.

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Retrieve a task group
    api_response = api_instance.get_task_group(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskGroupApi->get_task_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

### Return type

[**TaskGroupType**](TaskGroupType.md)

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

# **get_task_group_metadata**
> SimpleMetadataType get_task_group_metadata(group_name)

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Retrieve all metadata
    api_response = api_instance.get_task_group_metadata(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskGroupApi->get_task_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

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

# **get_task_group_metadata_key**
> str get_task_group_metadata_key(group_name, keypath)

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_task_group_metadata_key(group_name, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskGroupApi->get_task_group_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
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

# **get_task_groups**
> TaskGroupListType get_task_groups()

List all task groups

Retrieves all task groups that have been defined in the system.

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))

try:
    # List all task groups
    api_response = api_instance.get_task_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskGroupApi->get_task_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaskGroupListType**](TaskGroupListType.md)

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

# **remove_task_group_transcoder**
> remove_task_group_transcoder(group_name, transcoder_id)

Remove a transcoder from a task group

Removes a transcoder from the specified task group.

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
transcoder_id = 'transcoder_id_example' # str | The transcoder id.

try:
    # Remove a transcoder from a task group
    api_instance.remove_task_group_transcoder(group_name, transcoder_id)
except ApiException as e:
    print("Exception when calling TaskGroupApi->remove_task_group_transcoder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **transcoder_id** | **str**| The transcoder id. | 

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

# **update_or_create_task_group**
> TaskGroupType update_or_create_task_group(group_name, task_group_type)

Update or create a task group

Updates or creates the task group with the given name.

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
task_group_type = vidispine.TaskGroupType() # TaskGroupType | 

try:
    # Update or create a task group
    api_response = api_instance.update_or_create_task_group(group_name, task_group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskGroupApi->update_or_create_task_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **task_group_type** | [**TaskGroupType**](TaskGroupType.md)|  | 

### Return type

[**TaskGroupType**](TaskGroupType.md)

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

# **update_task_group_metadata**
> update_task_group_metadata(group_name, simple_metadata_type)

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_task_group_metadata(group_name, simple_metadata_type)
except ApiException as e:
    print("Exception when calling TaskGroupApi->update_task_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
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

# **update_task_group_metadata_key**
> update_task_group_metadata_key(group_name, keypath, body)

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
api_instance = vidispine.TaskGroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_task_group_metadata_key(group_name, keypath, body)
except ApiException as e:
    print("Exception when calling TaskGroupApi->update_task_group_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
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

