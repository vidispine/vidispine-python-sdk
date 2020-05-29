# vidispine.ProjectionApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_projection**](ProjectionApi.md#delete_projection) | **DELETE** /projection/{projection-id} | Delete a projection
[**get_incoming_projection**](ProjectionApi.md#get_incoming_projection) | **GET** /projection/{projection-id}/incoming | Retrieve an incoming projection
[**get_outgoing_projection**](ProjectionApi.md#get_outgoing_projection) | **GET** /projection/{projection-id}/outgoing | Retrieve an outgoing projection
[**get_projections**](ProjectionApi.md#get_projections) | **GET** /projection | List all projections
[**update_or_create_incoming_projection**](ProjectionApi.md#update_or_create_incoming_projection) | **PUT** /projection/{projection-id}/incoming | Update or create an incoming projection
[**update_or_create_outgoing_projection**](ProjectionApi.md#update_or_create_outgoing_projection) | **PUT** /projection/{projection-id}/outgoing | Update or create an outgoing projection


# **delete_projection**
> delete_projection(projection_id)

Delete a projection

Removes the projection.

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
api_instance = vidispine.ProjectionApi(vidispine.ApiClient(configuration))
projection_id = 'projection_id_example' # str | The projection id.

try:
    # Delete a projection
    api_instance.delete_projection(projection_id)
except ApiException as e:
    print("Exception when calling ProjectionApi->delete_projection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projection_id** | **str**| The projection id. | 

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

# **get_incoming_projection**
> str get_incoming_projection(projection_id)

Retrieve an incoming projection

Returns the projection use to transform information *to* the Vidispine API, `PUT metadata`.

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
api_instance = vidispine.ProjectionApi(vidispine.ApiClient(configuration))
projection_id = 'projection_id_example' # str | The projection id.

try:
    # Retrieve an incoming projection
    api_response = api_instance.get_incoming_projection(projection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectionApi->get_incoming_projection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projection_id** | **str**| The projection id. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | XML, XSLT stylesheet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outgoing_projection**
> str get_outgoing_projection(projection_id)

Retrieve an outgoing projection

Returns the projection use to transform information *from* the Vidispine API, `GET metadata`.

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
api_instance = vidispine.ProjectionApi(vidispine.ApiClient(configuration))
projection_id = 'projection_id_example' # str | The projection id.

try:
    # Retrieve an outgoing projection
    api_response = api_instance.get_outgoing_projection(projection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectionApi->get_outgoing_projection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projection_id** | **str**| The projection id. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | XML, XSLT stylesheet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projections**
> URIListType get_projections(url=url)

List all projections

Returns a list of all defined projections.

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
api_instance = vidispine.ProjectionApi(vidispine.ApiClient(configuration))
url = False # bool | - `true` - Return list of URLs.  - `false` (default) - Return list of ids. (optional) (default to False)

try:
    # List all projections
    api_response = api_instance.get_projections(url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectionApi->get_projections: %s\n" % e)
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
**0** | CRLF-delimited list of ids or URLs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_incoming_projection**
> str update_or_create_incoming_projection(projection_id, body)

Update or create an incoming projection

Creates a new projection if not defined earlier, and sets the incoming projection to the specified stylesheet.  If a new projection is created, the outgoing transformation is set to be the identity transform.

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
api_instance = vidispine.ProjectionApi(vidispine.ApiClient(configuration))
projection_id = 'projection_id_example' # str | The projection id.
body = 'body_example' # str | XML, XSLT stylesheet

try:
    # Update or create an incoming projection
    api_response = api_instance.update_or_create_incoming_projection(projection_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectionApi->update_or_create_incoming_projection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projection_id** | **str**| The projection id. | 
 **body** | **str**| XML, XSLT stylesheet | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | XML, XSLT stylesheet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_outgoing_projection**
> str update_or_create_outgoing_projection(projection_id, body)

Update or create an outgoing projection

Creates a new projection if not defined earlier, and sets the outgoing projection to the specified stylesheet.  If a new projection is created, the incoming transformation is set to be the identity transform.

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
api_instance = vidispine.ProjectionApi(vidispine.ApiClient(configuration))
projection_id = 'projection_id_example' # str | The projection id.
body = 'body_example' # str | XML, XSLT stylesheet

try:
    # Update or create an outgoing projection
    api_response = api_instance.update_or_create_outgoing_projection(projection_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectionApi->update_or_create_outgoing_projection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projection_id** | **str**| The projection id. | 
 **body** | **str**| XML, XSLT stylesheet | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | XML, XSLT stylesheet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

