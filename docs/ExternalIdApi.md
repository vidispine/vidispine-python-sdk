# vidispine.ExternalIdApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_external_id**](ExternalIdApi.md#create_entity_external_id) | **PUT** /{type}/{entity-id}/external-id/{external-id} | Create a new external id
[**delete_entity_external_id**](ExternalIdApi.md#delete_entity_external_id) | **DELETE** /{type}/{entity-id}/external-id/{external-id} | Remove an external id
[**delete_entity_external_ids**](ExternalIdApi.md#delete_entity_external_ids) | **DELETE** /{type}/{entity-id}/external-id | Clear all external ids for an entity
[**get_entity_external_ids**](ExternalIdApi.md#get_entity_external_ids) | **GET** /{type}/{entity-id}/external-id | Retrieve all external ids for an entity


# **create_entity_external_id**
> create_entity_external_id(type, entity_id, external_id)

Create a new external id

Creates a new external id for the specified entity.

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
api_instance = vidispine.ExternalIdApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
external_id = 'external_id_example' # str | The external id.

try:
    # Create a new external id
    api_instance.create_entity_external_id(type, entity_id, external_id)
except ApiException as e:
    print("Exception when calling ExternalIdApi->create_entity_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **external_id** | **str**| The external id. | 

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

# **delete_entity_external_id**
> delete_entity_external_id(type, entity_id, external_id)

Remove an external id

Removes the external identifier from a specific entity.

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
api_instance = vidispine.ExternalIdApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
external_id = 'external_id_example' # str | The external id.

try:
    # Remove an external id
    api_instance.delete_entity_external_id(type, entity_id, external_id)
except ApiException as e:
    print("Exception when calling ExternalIdApi->delete_entity_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **external_id** | **str**| The external id. | 

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

# **delete_entity_external_ids**
> delete_entity_external_ids(type, entity_id)

Clear all external ids for an entity

Clears all external identifiers that are registered with an entity.

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
api_instance = vidispine.ExternalIdApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.

try:
    # Clear all external ids for an entity
    api_instance.delete_entity_external_ids(type, entity_id)
except ApiException as e:
    print("Exception when calling ExternalIdApi->delete_entity_external_ids: %s\n" % e)
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

# **get_entity_external_ids**
> ExternalIdentifierListType get_entity_external_ids(type, entity_id)

Retrieve all external ids for an entity

Retrieves all external ids that are assigned to a particular entity.

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
api_instance = vidispine.ExternalIdApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.

try:
    # Retrieve all external ids for an entity
    api_response = api_instance.get_entity_external_ids(type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalIdApi->get_entity_external_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 

### Return type

[**ExternalIdentifierListType**](ExternalIdentifierListType.md)

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

