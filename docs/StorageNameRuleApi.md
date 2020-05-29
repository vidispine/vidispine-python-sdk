# vidispine.StorageNameRuleApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shape_storage_name_rule**](StorageNameRuleApi.md#create_shape_storage_name_rule) | **PUT** /item/{item-id}/shape/{shape-id}/filename/{storage-id} | Create a new storage name rule
[**delete_shape_storage_name_rule**](StorageNameRuleApi.md#delete_shape_storage_name_rule) | **DELETE** /item/{item-id}/shape/{shape-id}/filename/{storage-id} | Delete a storage name rule
[**get_shape_storage_name_rules**](StorageNameRuleApi.md#get_shape_storage_name_rules) | **GET** /item/{item-id}/shape/{shape-id}/filename | List all storage name rules applied on a shape


# **create_shape_storage_name_rule**
> create_shape_storage_name_rule(filename, item_id, shape_id, storage_id)

Create a new storage name rule

Creates a new storage name rule that attempts enforce the filename on a certain storage. This operation does not rename the file, it merely creates a rule for it. The file will then be renamed at a later time, if the file is located on that storage.

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
api_instance = vidispine.StorageNameRuleApi(vidispine.ApiClient(configuration))
filename = 'filename_example' # str | The desired filename of the file.
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Create a new storage name rule
    api_instance.create_shape_storage_name_rule(filename, item_id, shape_id, storage_id)
except ApiException as e:
    print("Exception when calling StorageNameRuleApi->create_shape_storage_name_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| The desired filename of the file. | 
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **storage_id** | **str**| The storage id. | 

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

# **delete_shape_storage_name_rule**
> delete_shape_storage_name_rule(filename, item_id, shape_id, storage_id)

Delete a storage name rule

Deletes a storage name rule that matches the (item id, shape id, storage id, filename) quadruple. Note that this does not change any existing filenames a file might have.

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
api_instance = vidispine.StorageNameRuleApi(vidispine.ApiClient(configuration))
filename = 'filename_example' # str | The filename of the rule.
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Delete a storage name rule
    api_instance.delete_shape_storage_name_rule(filename, item_id, shape_id, storage_id)
except ApiException as e:
    print("Exception when calling StorageNameRuleApi->delete_shape_storage_name_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| The filename of the rule. | 
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **storage_id** | **str**| The storage id. | 

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

# **get_shape_storage_name_rules**
> URIListType get_shape_storage_name_rules(item_id, shape_id)

List all storage name rules applied on a shape

Retrieves a list of URIs to all storage name rules that are contained within a shape.

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
api_instance = vidispine.StorageNameRuleApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # List all storage name rules applied on a shape
    api_response = api_instance.get_shape_storage_name_rules(item_id, shape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageNameRuleApi->get_shape_storage_name_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 

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
**0** | CRLF-delimited list of URIs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

