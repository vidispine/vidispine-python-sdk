# vidispine.ResourceApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource**](ResourceApi.md#create_resource) | **POST** /resource/{type} | Create a resource
[**delete_resource**](ResourceApi.md#delete_resource) | **DELETE** /resource/{type}/{resource-id} | Delete a resource
[**get_resource**](ResourceApi.md#get_resource) | **GET** /resource/{type}/{resource-id} | Retrieve a resource
[**get_resource_status**](ResourceApi.md#get_resource_status) | **GET** /resource/{type}/{resource-id}/status | View resource status
[**get_resource_type**](ResourceApi.md#get_resource_type) | **GET** /resource/{type} | List all resources
[**get_resource_types**](ResourceApi.md#get_resource_types) | **GET** /resource | List all resource types
[**synchronize_ldap**](ResourceApi.md#synchronize_ldap) | **POST** /resource/{type}/{resource-id}/sync | Trigger LDAP synchronization
[**update_resource**](ResourceApi.md#update_resource) | **PUT** /resource/{type}/{resource-id} | Modify a resource


# **create_resource**
> ResourceType create_resource(type, resource_type)

Create a resource

Create a new resource.

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
api_instance = vidispine.ResourceApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
resource_type = vidispine.ResourceType() # ResourceType | 

try:
    # Create a resource
    api_response = api_instance.create_resource(type, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->create_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **resource_type** | [**ResourceType**](ResourceType.md)|  | 

### Return type

[**ResourceType**](ResourceType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Resource URL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource**
> delete_resource(type, resource_id)

Delete a resource

Deletes the resource. All connection from other resources to the resource will become invalid.

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
api_instance = vidispine.ResourceApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
resource_id = 'resource_id_example' # str | The resource id.

try:
    # Delete a resource
    api_instance.delete_resource(type, resource_id)
except ApiException as e:
    print("Exception when calling ResourceApi->delete_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **resource_id** | **str**| The resource id. | 

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

# **get_resource**
> ResourceType get_resource(type, resource_id)

Retrieve a resource

Retrieves information on a specific resource.

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
api_instance = vidispine.ResourceApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
resource_id = 'resource_id_example' # str | The resource id.

try:
    # Retrieve a resource
    api_response = api_instance.get_resource(type, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->get_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **resource_id** | **str**| The resource id. | 

### Return type

[**ResourceType**](ResourceType.md)

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

# **get_resource_status**
> str get_resource_status(type, resource_id)

View resource status

Retrieves the status of a specific resource.

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
api_instance = vidispine.ResourceApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
resource_id = 'resource_id_example' # str | The resource id.

try:
    # View resource status
    api_response = api_instance.get_resource_status(type, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->get_resource_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **resource_id** | **str**| The resource id. | 

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
**0** | Status string |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_type**
> ResourceListType get_resource_type(type)

List all resources

Retrieves the resources of the given type that have been configured.

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
api_instance = vidispine.ResourceApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.

try:
    # List all resources
    api_response = api_instance.get_resource_type(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->get_resource_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 

### Return type

[**ResourceListType**](ResourceListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of resource URLs  ( &lt;code&gt;/resource/&lt;/code&gt; { &lt;strong&gt;type&lt;/strong&gt; } &lt;code&gt;/&lt;/code&gt; { &lt;strong&gt;resource-id&lt;/strong&gt; }) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_types**
> ResourceTypeListType get_resource_types()

List all resource types

Retrieves the available resource types.

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
api_instance = vidispine.ResourceApi(vidispine.ApiClient(configuration))

try:
    # List all resource types
    api_response = api_instance.get_resource_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->get_resource_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceTypeListType**](ResourceTypeListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of resource type URLs  ( &lt;code&gt;/resource/&lt;/code&gt; { &lt;strong&gt;type&lt;/strong&gt; }) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_ldap**
> synchronize_ldap(type, resource_id)

Trigger LDAP synchronization

Triggers a synchronization of users and groups.  If users and groups are already synchronizing, than this will have no effect.

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
api_instance = vidispine.ResourceApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | Must be <pre>ldap</pre>.
resource_id = 'resource_id_example' # str | The resource id.

try:
    # Trigger LDAP synchronization
    api_instance.synchronize_ldap(type, resource_id)
except ApiException as e:
    print("Exception when calling ResourceApi->synchronize_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Must be &lt;pre&gt;ldap&lt;/pre&gt;. | 
 **resource_id** | **str**| The resource id. | 

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

# **update_resource**
> ResourceType update_resource(type, resource_id, resource_type)

Modify a resource

Updates an existing resource.

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
api_instance = vidispine.ResourceApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
resource_id = 'resource_id_example' # str | The resource id.
resource_type = vidispine.ResourceType() # ResourceType | 

try:
    # Modify a resource
    api_response = api_instance.update_resource(type, resource_id, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceApi->update_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **resource_id** | **str**| The resource id. | 
 **resource_type** | [**ResourceType**](ResourceType.md)|  | 

### Return type

[**ResourceType**](ResourceType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Resource URL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

