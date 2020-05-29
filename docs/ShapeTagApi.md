# vidispine.ShapeTagApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_shape_tag**](ShapeTagApi.md#delete_shape_tag) | **DELETE** /shape-tag/{tag-name} | Delete a shape tag
[**delete_shape_tag_metadata**](ShapeTagApi.md#delete_shape_tag_metadata) | **DELETE** /shape-tag/{tag-name}/metadata | Delete all key-value pairs
[**delete_shape_tag_metadata_key**](ShapeTagApi.md#delete_shape_tag_metadata_key) | **DELETE** /shape-tag/{tag-name}/metadata/{keypath} | Delete key-value pairs
[**delete_shape_tag_script**](ShapeTagApi.md#delete_shape_tag_script) | **DELETE** /shape-tag/{tag-name}/script | Remove the script for a shape tag
[**get_all_shape_tags**](ShapeTagApi.md#get_all_shape_tags) | **GET** /shape-tag/ | List all shape tags
[**get_shape_tag**](ShapeTagApi.md#get_shape_tag) | **GET** /shape-tag/{tag-name} | Retrieve a shape tag
[**get_shape_tag_metadata**](ShapeTagApi.md#get_shape_tag_metadata) | **GET** /shape-tag/{tag-name}/metadata | Retrieve all metadata
[**get_shape_tag_metadata_key**](ShapeTagApi.md#get_shape_tag_metadata_key) | **GET** /shape-tag/{tag-name}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_shape_tag_script**](ShapeTagApi.md#get_shape_tag_script) | **GET** /shape-tag/{tag-name}/script | Retrieve the script for a shape tag
[**test_shape_tag_script**](ShapeTagApi.md#test_shape_tag_script) | **GET** /shape-tag/{tag-name}/item/{item-id}/shape/{shape-id} | Test a script
[**update_or_create_shape_tag**](ShapeTagApi.md#update_or_create_shape_tag) | **PUT** /shape-tag/{tag-name} | Update or create a shape tag
[**update_or_create_shape_tag_script**](ShapeTagApi.md#update_or_create_shape_tag_script) | **PUT** /shape-tag/{tag-name}/script | Update or create the script for a shape tag
[**update_shape_tag_metadata**](ShapeTagApi.md#update_shape_tag_metadata) | **PUT** /shape-tag/{tag-name}/metadata | Create multiple key-value pairs
[**update_shape_tag_metadata_key**](ShapeTagApi.md#update_shape_tag_metadata_key) | **PUT** /shape-tag/{tag-name}/metadata/{keypath} | Set the value for a specific key


# **delete_shape_tag**
> delete_shape_tag(tag_name)

Delete a shape tag

Deletes a shape tag with the given tag name.

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Delete a shape tag
    api_instance.delete_shape_tag(tag_name)
except ApiException as e:
    print("Exception when calling ShapeTagApi->delete_shape_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 

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

# **delete_shape_tag_metadata**
> delete_shape_tag_metadata(tag_name)

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Delete all key-value pairs
    api_instance.delete_shape_tag_metadata(tag_name)
except ApiException as e:
    print("Exception when calling ShapeTagApi->delete_shape_tag_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 

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

# **delete_shape_tag_metadata_key**
> delete_shape_tag_metadata_key(tag_name, keypath)

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_shape_tag_metadata_key(tag_name, keypath)
except ApiException as e:
    print("Exception when calling ShapeTagApi->delete_shape_tag_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 
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

# **delete_shape_tag_script**
> delete_shape_tag_script(tag_name)

Remove the script for a shape tag

Unsets the script for the shape tag.

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Remove the script for a shape tag
    api_instance.delete_shape_tag_script(tag_name)
except ApiException as e:
    print("Exception when calling ShapeTagApi->delete_shape_tag_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 

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

# **get_all_shape_tags**
> URIListType get_all_shape_tags(url=url)

List all shape tags

Retrieves all shape tags known by the system.

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
url = False # bool | - `true` - Return list of URLs.  - `false` (default) - Return list of ids. (optional) (default to False)

try:
    # List all shape tags
    api_response = api_instance.get_all_shape_tags(url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeTagApi->get_all_shape_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **bool**| - &#x60;true&#x60; - Return list of URLs.  - &#x60;false&#x60; (default) - Return list of ids. | [optional] [default to False]

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
**0** | A list of the tags. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shape_tag**
> TranscodePresetType get_shape_tag(tag_name)

Retrieve a shape tag

Retrieves the transcode preset of shape tag with the given tag name.

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Retrieve a shape tag
    api_response = api_instance.get_shape_tag(tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeTagApi->get_shape_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 

### Return type

[**TranscodePresetType**](TranscodePresetType.md)

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

# **get_shape_tag_metadata**
> SimpleMetadataType get_shape_tag_metadata(tag_name)

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Retrieve all metadata
    api_response = api_instance.get_shape_tag_metadata(tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeTagApi->get_shape_tag_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 

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

# **get_shape_tag_metadata_key**
> str get_shape_tag_metadata_key(tag_name, keypath)

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_shape_tag_metadata_key(tag_name, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeTagApi->get_shape_tag_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 
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

# **get_shape_tag_script**
> str get_shape_tag_script(tag_name)

Retrieve the script for a shape tag

Retrieves the script of the shape tag.

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Retrieve the script for a shape tag
    api_response = api_instance.get_shape_tag_script(tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeTagApi->get_shape_tag_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 

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

# **test_shape_tag_script**
> TranscodePresetType test_shape_tag_script(tag_name, item_id, shape_id, job=job)

Test a script

Tests the script of the shape tag with the specified shape as input and returns the resulting preset.

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
job = 'job_example' # str | The id of a job to retrieve job metadata from. (optional)

try:
    # Test a script
    api_response = api_instance.test_shape_tag_script(tag_name, item_id, shape_id, job=job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeTagApi->test_shape_tag_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **job** | **str**| The id of a job to retrieve job metadata from. | [optional] 

### Return type

[**TranscodePresetType**](TranscodePresetType.md)

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

# **update_or_create_shape_tag**
> update_or_create_shape_tag(tag_name, transcode_preset_type)

Update or create a shape tag

Creates a new shape tag with the given tag name. If the tag already exists, its transcode preset will be updated.

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.
transcode_preset_type = vidispine.TranscodePresetType() # TranscodePresetType | 

try:
    # Update or create a shape tag
    api_instance.update_or_create_shape_tag(tag_name, transcode_preset_type)
except ApiException as e:
    print("Exception when calling ShapeTagApi->update_or_create_shape_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 
 **transcode_preset_type** | [**TranscodePresetType**](TranscodePresetType.md)|  | 

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

# **update_or_create_shape_tag_script**
> update_or_create_shape_tag_script(tag_name, body)

Update or create the script for a shape tag

Sets a script for the shape tag.

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.
body = 'body_example' # str | A JavaScript

try:
    # Update or create the script for a shape tag
    api_instance.update_or_create_shape_tag_script(tag_name, body)
except ApiException as e:
    print("Exception when calling ShapeTagApi->update_or_create_shape_tag_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 
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

# **update_shape_tag_metadata**
> update_shape_tag_metadata(tag_name, simple_metadata_type)

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_shape_tag_metadata(tag_name, simple_metadata_type)
except ApiException as e:
    print("Exception when calling ShapeTagApi->update_shape_tag_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 
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

# **update_shape_tag_metadata_key**
> update_shape_tag_metadata_key(tag_name, keypath, body)

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
api_instance = vidispine.ShapeTagApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_shape_tag_metadata_key(tag_name, keypath, body)
except ApiException as e:
    print("Exception when calling ShapeTagApi->update_shape_tag_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 
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

