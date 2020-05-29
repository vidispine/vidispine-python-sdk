# vidispine.StorageRuleApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_shape_tag_default_storage_rule**](StorageRuleApi.md#delete_shape_tag_default_storage_rule) | **DELETE** /shape-tag/storage-rule | Delete a default rule
[**delete_shape_tag_storage_rule**](StorageRuleApi.md#delete_shape_tag_storage_rule) | **DELETE** /shape-tag/storage-rule/{tag-name} | Delete a storage rule
[**get_shape_tag_storage_rule**](StorageRuleApi.md#get_shape_tag_storage_rule) | **GET** /shape-tag/storage-rule/{tag-name} | Retrieve a a storage rule
[**get_shape_tag_storage_rules**](StorageRuleApi.md#get_shape_tag_storage_rules) | **GET** /shape-tag/storage-rule | List all storage rules for an entity
[**get_storage_rules**](StorageRuleApi.md#get_storage_rules) | **GET** /storage-rule/ | List all storage rules
[**update_shape_tag_default_storage_rule**](StorageRuleApi.md#update_shape_tag_default_storage_rule) | **PUT** /shape-tag/storage-rule | Set a default rule
[**update_shape_tag_storage_rule**](StorageRuleApi.md#update_shape_tag_storage_rule) | **PUT** /shape-tag/storage-rule/{tag-name} | Set a storage rule


# **delete_shape_tag_default_storage_rule**
> delete_shape_tag_default_storage_rule()

Delete a default rule

Deletes the default rule.

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
api_instance = vidispine.StorageRuleApi(vidispine.ApiClient(configuration))

try:
    # Delete a default rule
    api_instance.delete_shape_tag_default_storage_rule()
except ApiException as e:
    print("Exception when calling StorageRuleApi->delete_shape_tag_default_storage_rule: %s\n" % e)
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

# **delete_shape_tag_storage_rule**
> delete_shape_tag_storage_rule(tag_name)

Delete a storage rule

Deletes a specific rule.

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
api_instance = vidispine.StorageRuleApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Delete a storage rule
    api_instance.delete_shape_tag_storage_rule(tag_name)
except ApiException as e:
    print("Exception when calling StorageRuleApi->delete_shape_tag_storage_rule: %s\n" % e)
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

# **get_shape_tag_storage_rule**
> StorageRuleType get_shape_tag_storage_rule(tag_name)

Retrieve a a storage rule

Returns the rule that is applied to a certain shape tag.

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
api_instance = vidispine.StorageRuleApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Retrieve a a storage rule
    api_response = api_instance.get_shape_tag_storage_rule(tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageRuleApi->get_shape_tag_storage_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 

### Return type

[**StorageRuleType**](StorageRuleType.md)

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

# **get_shape_tag_storage_rules**
> StorageRulesType get_shape_tag_storage_rules()

List all storage rules for an entity

Retrieves all storage rules that are applied on a certain entity in a certain resource.

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
api_instance = vidispine.StorageRuleApi(vidispine.ApiClient(configuration))

try:
    # List all storage rules for an entity
    api_response = api_instance.get_shape_tag_storage_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageRuleApi->get_shape_tag_storage_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StorageRulesType**](StorageRulesType.md)

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

# **get_storage_rules**
> StorageRulesType get_storage_rules(tag=tag, type=type)

List all storage rules

Retrieves all storage-rules that matches the given parameters.

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
api_instance = vidispine.StorageRuleApi(vidispine.ApiClient(configuration))
tag = ['tag_example'] # list[str] | Comma-separated list of tags to retrieve, if not specified rules of all tag types will be retrieved. (optional)
type = ['type_example'] # list[str] | Comma-separated list of types to retrieve, if not specified all types will be retrieved. (optional)

try:
    # List all storage rules
    api_response = api_instance.get_storage_rules(tag=tag, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageRuleApi->get_storage_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**list[str]**](str.md)| Comma-separated list of tags to retrieve, if not specified rules of all tag types will be retrieved. | [optional] 
 **type** | [**list[str]**](str.md)| Comma-separated list of types to retrieve, if not specified all types will be retrieved. | [optional] 

### Return type

[**StorageRulesType**](StorageRulesType.md)

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

# **update_shape_tag_default_storage_rule**
> update_shape_tag_default_storage_rule(storage_rule_type)

Set a default rule

Sets the default rule.

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
api_instance = vidispine.StorageRuleApi(vidispine.ApiClient(configuration))
storage_rule_type = vidispine.StorageRuleType() # StorageRuleType | 

try:
    # Set a default rule
    api_instance.update_shape_tag_default_storage_rule(storage_rule_type)
except ApiException as e:
    print("Exception when calling StorageRuleApi->update_shape_tag_default_storage_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_rule_type** | [**StorageRuleType**](StorageRuleType.md)|  | 

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

# **update_shape_tag_storage_rule**
> update_shape_tag_storage_rule(tag_name, storage_rule_type)

Set a storage rule

Updates a storage rule applied to a certain shape tag.

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
api_instance = vidispine.StorageRuleApi(vidispine.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The tag name.
storage_rule_type = vidispine.StorageRuleType() # StorageRuleType | 

try:
    # Set a storage rule
    api_instance.update_shape_tag_storage_rule(tag_name, storage_rule_type)
except ApiException as e:
    print("Exception when calling StorageRuleApi->update_shape_tag_storage_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The tag name. | 
 **storage_rule_type** | [**StorageRuleType**](StorageRuleType.md)|  | 

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

