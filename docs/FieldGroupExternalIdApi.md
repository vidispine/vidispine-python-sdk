# vidispine.FieldGroupExternalIdApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata_field_group_external_id**](FieldGroupExternalIdApi.md#create_metadata_field_group_external_id) | **PUT** /metadata-field/field-group/{field-group-name}/external-id/{external-id} | Create a new external id
[**delete_metadata_field_group_external_id**](FieldGroupExternalIdApi.md#delete_metadata_field_group_external_id) | **DELETE** /metadata-field/field-group/{field-group-name}/external-id/{external-id} | Remove an external id
[**delete_metadata_field_group_external_ids**](FieldGroupExternalIdApi.md#delete_metadata_field_group_external_ids) | **DELETE** /metadata-field/field-group/{field-group-name}/external-id | Clear all external ids for an entity
[**get_metadata_field_group_external_ids**](FieldGroupExternalIdApi.md#get_metadata_field_group_external_ids) | **GET** /metadata-field/field-group/{field-group-name}/external-id | Retrieve all external ids for an entity


# **create_metadata_field_group_external_id**
> create_metadata_field_group_external_id(field_group_name, external_id)

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
api_instance = vidispine.FieldGroupExternalIdApi(vidispine.ApiClient(configuration))
field_group_name = 'field_group_name_example' # str | The field group name.
external_id = 'external_id_example' # str | The external id.

try:
    # Create a new external id
    api_instance.create_metadata_field_group_external_id(field_group_name, external_id)
except ApiException as e:
    print("Exception when calling FieldGroupExternalIdApi->create_metadata_field_group_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_group_name** | **str**| The field group name. | 
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

# **delete_metadata_field_group_external_id**
> delete_metadata_field_group_external_id(field_group_name, external_id)

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
api_instance = vidispine.FieldGroupExternalIdApi(vidispine.ApiClient(configuration))
field_group_name = 'field_group_name_example' # str | The field group name.
external_id = 'external_id_example' # str | The external id.

try:
    # Remove an external id
    api_instance.delete_metadata_field_group_external_id(field_group_name, external_id)
except ApiException as e:
    print("Exception when calling FieldGroupExternalIdApi->delete_metadata_field_group_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_group_name** | **str**| The field group name. | 
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

# **delete_metadata_field_group_external_ids**
> delete_metadata_field_group_external_ids(field_group_name)

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
api_instance = vidispine.FieldGroupExternalIdApi(vidispine.ApiClient(configuration))
field_group_name = 'field_group_name_example' # str | The field group name.

try:
    # Clear all external ids for an entity
    api_instance.delete_metadata_field_group_external_ids(field_group_name)
except ApiException as e:
    print("Exception when calling FieldGroupExternalIdApi->delete_metadata_field_group_external_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_group_name** | **str**| The field group name. | 

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

# **get_metadata_field_group_external_ids**
> ExternalIdentifierListType get_metadata_field_group_external_ids(field_group_name)

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
api_instance = vidispine.FieldGroupExternalIdApi(vidispine.ApiClient(configuration))
field_group_name = 'field_group_name_example' # str | The field group name.

try:
    # Retrieve all external ids for an entity
    api_response = api_instance.get_metadata_field_group_external_ids(field_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldGroupExternalIdApi->get_metadata_field_group_external_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_group_name** | **str**| The field group name. | 

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

