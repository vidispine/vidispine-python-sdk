# vidispine.ExternalIdNamespaceApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_external_id**](ExternalIdNamespaceApi.md#delete_external_id) | **DELETE** /external-id/id/{external-id} | Remove an external id
[**delete_external_id_namespace**](ExternalIdNamespaceApi.md#delete_external_id_namespace) | **DELETE** /external-id/{namespace-id} | Delete a namespace and all external ids in that namespace
[**get_external_id_namespace**](ExternalIdNamespaceApi.md#get_external_id_namespace) | **GET** /external-id/{namespace-id} | Retrieve a specific namespace
[**get_external_id_namespaces**](ExternalIdNamespaceApi.md#get_external_id_namespaces) | **GET** /external-id | Retrieve all known namespaces
[**update_or_create_external_id_namespace**](ExternalIdNamespaceApi.md#update_or_create_external_id_namespace) | **PUT** /external-id/{namespace-id} | Update or create a namespace


# **delete_external_id**
> delete_external_id(external_id)

Remove an external id

Removes the external identifier from all entities.

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
api_instance = vidispine.ExternalIdNamespaceApi(vidispine.ApiClient(configuration))
external_id = 'external_id_example' # str | The external id.

try:
    # Remove an external id
    api_instance.delete_external_id(external_id)
except ApiException as e:
    print("Exception when calling ExternalIdNamespaceApi->delete_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_external_id_namespace**
> delete_external_id_namespace(namespace_id)

Delete a namespace and all external ids in that namespace

Deletes the specified namespace together with all *external ids that exist in that namespace*.

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
api_instance = vidispine.ExternalIdNamespaceApi(vidispine.ApiClient(configuration))
namespace_id = 'namespace_id_example' # str | The namespace id.

try:
    # Delete a namespace and all external ids in that namespace
    api_instance.delete_external_id_namespace(namespace_id)
except ApiException as e:
    print("Exception when calling ExternalIdNamespaceApi->delete_external_id_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**| The namespace id. | 

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

# **get_external_id_namespace**
> ExternalIdentifierNamespaceType get_external_id_namespace(namespace_id)

Retrieve a specific namespace

Retrieves the namespace with the specified name.

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
api_instance = vidispine.ExternalIdNamespaceApi(vidispine.ApiClient(configuration))
namespace_id = 'namespace_id_example' # str | The namespace id.

try:
    # Retrieve a specific namespace
    api_response = api_instance.get_external_id_namespace(namespace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalIdNamespaceApi->get_external_id_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**| The namespace id. | 

### Return type

[**ExternalIdentifierNamespaceType**](ExternalIdentifierNamespaceType.md)

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

# **get_external_id_namespaces**
> ExternalIdentifierNamespaceListType get_external_id_namespaces()

Retrieve all known namespaces

Retrieves all known external id namespaces.

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
api_instance = vidispine.ExternalIdNamespaceApi(vidispine.ApiClient(configuration))

try:
    # Retrieve all known namespaces
    api_response = api_instance.get_external_id_namespaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalIdNamespaceApi->get_external_id_namespaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExternalIdentifierNamespaceListType**](ExternalIdentifierNamespaceListType.md)

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

# **update_or_create_external_id_namespace**
> update_or_create_external_id_namespace(namespace_id, external_identifier_namespace_type)

Update or create a namespace

Creates or modifies a namespace with the specified name.

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
api_instance = vidispine.ExternalIdNamespaceApi(vidispine.ApiClient(configuration))
namespace_id = 'namespace_id_example' # str | The namespace id.
external_identifier_namespace_type = vidispine.ExternalIdentifierNamespaceType() # ExternalIdentifierNamespaceType | 

try:
    # Update or create a namespace
    api_instance.update_or_create_external_id_namespace(namespace_id, external_identifier_namespace_type)
except ApiException as e:
    print("Exception when calling ExternalIdNamespaceApi->update_or_create_external_id_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**| The namespace id. | 
 **external_identifier_namespace_type** | [**ExternalIdentifierNamespaceType**](ExternalIdentifierNamespaceType.md)|  | 

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

