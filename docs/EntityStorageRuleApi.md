# vidispine.EntityStorageRuleApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_entity_default_storage_rule**](EntityStorageRuleApi.md#delete_entity_default_storage_rule) | **DELETE** /{type}/{entity-id}/storage-rule | Delete a default rule
[**delete_entity_shape_tag_storage_rule**](EntityStorageRuleApi.md#delete_entity_shape_tag_storage_rule) | **DELETE** /{type}/{entity-id}/storage-rule/{tag-name} | Delete a storage rule
[**get_entity_shape_tag_storage_rule**](EntityStorageRuleApi.md#get_entity_shape_tag_storage_rule) | **GET** /{type}/{entity-id}/storage-rule/{tag-name} | Retrieve a a storage rule
[**get_entity_storage_rules**](EntityStorageRuleApi.md#get_entity_storage_rules) | **GET** /{type}/{entity-id}/storage-rule | List all storage rules for an entity
[**update_entity_default_storage_rule**](EntityStorageRuleApi.md#update_entity_default_storage_rule) | **PUT** /{type}/{entity-id}/storage-rule | Set a default rule
[**update_entity_shape_tag_storage_rule**](EntityStorageRuleApi.md#update_entity_shape_tag_storage_rule) | **PUT** /{type}/{entity-id}/storage-rule/{tag-name} | Set a storage rule


# **delete_entity_default_storage_rule**
> delete_entity_default_storage_rule(type, entity_id)

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
api_instance = vidispine.EntityStorageRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.

try:
    # Delete a default rule
    api_instance.delete_entity_default_storage_rule(type, entity_id)
except ApiException as e:
    print("Exception when calling EntityStorageRuleApi->delete_entity_default_storage_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 

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

# **delete_entity_shape_tag_storage_rule**
> delete_entity_shape_tag_storage_rule(type, entity_id, tag_name)

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
api_instance = vidispine.EntityStorageRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Delete a storage rule
    api_instance.delete_entity_shape_tag_storage_rule(type, entity_id, tag_name)
except ApiException as e:
    print("Exception when calling EntityStorageRuleApi->delete_entity_shape_tag_storage_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
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

# **get_entity_shape_tag_storage_rule**
> StorageRuleType get_entity_shape_tag_storage_rule(type, entity_id, tag_name)

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
api_instance = vidispine.EntityStorageRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Retrieve a a storage rule
    api_response = api_instance.get_entity_shape_tag_storage_rule(type, entity_id, tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityStorageRuleApi->get_entity_shape_tag_storage_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
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

# **get_entity_storage_rules**
> StorageRulesType get_entity_storage_rules(type, entity_id)

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
api_instance = vidispine.EntityStorageRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.

try:
    # List all storage rules for an entity
    api_response = api_instance.get_entity_storage_rules(type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityStorageRuleApi->get_entity_storage_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 

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

# **update_entity_default_storage_rule**
> update_entity_default_storage_rule(type, entity_id, storage_rule_type)

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
api_instance = vidispine.EntityStorageRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
storage_rule_type = vidispine.StorageRuleType() # StorageRuleType | 

try:
    # Set a default rule
    api_instance.update_entity_default_storage_rule(type, entity_id, storage_rule_type)
except ApiException as e:
    print("Exception when calling EntityStorageRuleApi->update_entity_default_storage_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
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

# **update_entity_shape_tag_storage_rule**
> update_entity_shape_tag_storage_rule(type, entity_id, tag_name, storage_rule_type)

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
api_instance = vidispine.EntityStorageRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
tag_name = 'tag_name_example' # str | The tag name.
storage_rule_type = vidispine.StorageRuleType() # StorageRuleType | 

try:
    # Set a storage rule
    api_instance.update_entity_shape_tag_storage_rule(type, entity_id, tag_name, storage_rule_type)
except ApiException as e:
    print("Exception when calling EntityStorageRuleApi->update_entity_shape_tag_storage_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
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

