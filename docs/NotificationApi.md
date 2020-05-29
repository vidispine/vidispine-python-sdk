# vidispine.NotificationApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_notification**](NotificationApi.md#create_entity_notification) | **POST** /{type}/{entity-id}/notification | Create a notification that is applied to a particular entity
[**create_entity_notification_external_id**](NotificationApi.md#create_entity_notification_external_id) | **PUT** /{type}/{entity-id}/notification/{notification-id}/external-id/{external-id} | Create a new external id
[**create_notification**](NotificationApi.md#create_notification) | **POST** /{type}/notification/ | Create a notification that is applied to the entire resource
[**create_notification_external_id**](NotificationApi.md#create_notification_external_id) | **PUT** /{type}/notification/{notification-id}/external-id/{external-id} | Create a new external id
[**create_placeholder_notification**](NotificationApi.md#create_placeholder_notification) | **POST** /notification/ | Create a notification that is applied to the entire resource
[**delete_entity_notification**](NotificationApi.md#delete_entity_notification) | **DELETE** /{type}/{entity-id}/notification/{notification-id} | Delete a notification
[**delete_entity_notification_external_id**](NotificationApi.md#delete_entity_notification_external_id) | **DELETE** /{type}/{entity-id}/notification/{notification-id}/external-id/{external-id} | Remove an external id
[**delete_entity_notification_external_ids**](NotificationApi.md#delete_entity_notification_external_ids) | **DELETE** /{type}/{entity-id}/notification/{notification-id}/external-id | Clear all external ids for an entity
[**delete_entity_notifications**](NotificationApi.md#delete_entity_notifications) | **DELETE** /{type}/{entity-id}/notification | Delete all notifications that is applied to a particular entity
[**delete_notification**](NotificationApi.md#delete_notification) | **DELETE** /{type}/notification/{notification-id} | Delete a notification
[**delete_notification_external_id**](NotificationApi.md#delete_notification_external_id) | **DELETE** /{type}/notification/{notification-id}/external-id/{external-id} | Remove an external id
[**delete_notification_external_ids**](NotificationApi.md#delete_notification_external_ids) | **DELETE** /{type}/notification/{notification-id}/external-id | Clear all external ids for an entity
[**delete_notifications**](NotificationApi.md#delete_notifications) | **DELETE** /{type}/notification/ | Delete all notifications that exists within an entire resource
[**delete_placeholder_notification**](NotificationApi.md#delete_placeholder_notification) | **DELETE** /notification/{notification-id} | Delete a notification
[**delete_placeholder_notifications**](NotificationApi.md#delete_placeholder_notifications) | **DELETE** /notification/ | Delete all notifications that exists within an entire resource
[**get_entity_notification**](NotificationApi.md#get_entity_notification) | **GET** /{type}/{entity-id}/notification/{notification-id} | Retrieve a notification
[**get_entity_notification_external_ids**](NotificationApi.md#get_entity_notification_external_ids) | **GET** /{type}/{entity-id}/notification/{notification-id}/external-id | Retrieve all external ids for an entity
[**get_entity_notifications**](NotificationApi.md#get_entity_notifications) | **GET** /{type}/{entity-id}/notification | List all notifications that exists for a particular entity
[**get_notification**](NotificationApi.md#get_notification) | **GET** /{type}/notification/{notification-id} | Retrieve a notification
[**get_notification_external_ids**](NotificationApi.md#get_notification_external_ids) | **GET** /{type}/notification/{notification-id}/external-id | Retrieve all external ids for an entity
[**get_notifications**](NotificationApi.md#get_notifications) | **GET** /{type}/notification/ | List all notifications that exists within an entire resource
[**get_placeholder_notification**](NotificationApi.md#get_placeholder_notification) | **GET** /notification/{notification-id} | Retrieve a notification
[**get_placeholder_notifications**](NotificationApi.md#get_placeholder_notifications) | **GET** /notification/ | List all notifications that exists within an entire resource
[**update_entity_notification**](NotificationApi.md#update_entity_notification) | **PUT** /{type}/{entity-id}/notification/{notification-id} | Change a particular notification on a specific entity
[**update_notification**](NotificationApi.md#update_notification) | **PUT** /{type}/notification/{notification-id} | Change a particular notification on a whole entity
[**update_placeholder_notification**](NotificationApi.md#update_placeholder_notification) | **PUT** /notification/{notification-id} | Change a particular notification on a whole entity


# **create_entity_notification**
> URIListType create_entity_notification(type, entity_id, notification_type)

Create a notification that is applied to a particular entity

Adds a notification to the given entity.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
notification_type = vidispine.NotificationType() # NotificationType | 

try:
    # Create a notification that is applied to a particular entity
    api_response = api_instance.create_entity_notification(type, entity_id, notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->create_entity_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **notification_type** | [**NotificationType**](NotificationType.md)|  | 

### Return type

[**URIListType**](URIListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The id of the notification. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity_notification_external_id**
> create_entity_notification_external_id(type, entity_id, notification_id, external_id)

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
notification_id = 'notification_id_example' # str | The notification id.
external_id = 'external_id_example' # str | The external id.

try:
    # Create a new external id
    api_instance.create_entity_notification_external_id(type, entity_id, notification_id, external_id)
except ApiException as e:
    print("Exception when calling NotificationApi->create_entity_notification_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **notification_id** | **str**| The notification id. | 
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

# **create_notification**
> URIListType create_notification(type, notification_type)

Create a notification that is applied to the entire resource

Adds a notification that is applied to an entire resource

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
notification_type = vidispine.NotificationType() # NotificationType | 

try:
    # Create a notification that is applied to the entire resource
    api_response = api_instance.create_notification(type, notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->create_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **notification_type** | [**NotificationType**](NotificationType.md)|  | 

### Return type

[**URIListType**](URIListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The id of the notification. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_notification_external_id**
> create_notification_external_id(type, notification_id, external_id)

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
notification_id = 'notification_id_example' # str | The notification id.
external_id = 'external_id_example' # str | The external id.

try:
    # Create a new external id
    api_instance.create_notification_external_id(type, notification_id, external_id)
except ApiException as e:
    print("Exception when calling NotificationApi->create_notification_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **notification_id** | **str**| The notification id. | 
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

# **create_placeholder_notification**
> URIListType create_placeholder_notification(notification_type)

Create a notification that is applied to the entire resource

Adds a notification that is applied to an entire resource

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
notification_type = vidispine.NotificationType() # NotificationType | 

try:
    # Create a notification that is applied to the entire resource
    api_response = api_instance.create_placeholder_notification(notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->create_placeholder_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_type** | [**NotificationType**](NotificationType.md)|  | 

### Return type

[**URIListType**](URIListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The id of the notification. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_notification**
> delete_entity_notification(type, entity_id, notification_id)

Delete a notification

Removes a particular notification with the given id.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
notification_id = 'notification_id_example' # str | The notification id.

try:
    # Delete a notification
    api_instance.delete_entity_notification(type, entity_id, notification_id)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_entity_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **notification_id** | **str**| The notification id. | 

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

# **delete_entity_notification_external_id**
> delete_entity_notification_external_id(type, entity_id, notification_id, external_id)

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
notification_id = 'notification_id_example' # str | The notification id.
external_id = 'external_id_example' # str | The external id.

try:
    # Remove an external id
    api_instance.delete_entity_notification_external_id(type, entity_id, notification_id, external_id)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_entity_notification_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **notification_id** | **str**| The notification id. | 
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

# **delete_entity_notification_external_ids**
> delete_entity_notification_external_ids(type, entity_id, notification_id)

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
notification_id = 'notification_id_example' # str | The notification id.

try:
    # Clear all external ids for an entity
    api_instance.delete_entity_notification_external_ids(type, entity_id, notification_id)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_entity_notification_external_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **notification_id** | **str**| The notification id. | 

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

# **delete_entity_notifications**
> delete_entity_notifications(type, entity_id)

Delete all notifications that is applied to a particular entity

Removes all notifications that exists within the specified entity.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.

try:
    # Delete all notifications that is applied to a particular entity
    api_instance.delete_entity_notifications(type, entity_id)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_entity_notifications: %s\n" % e)
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

# **delete_notification**
> delete_notification(type, notification_id)

Delete a notification

Removes a particular notification with the given id.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
notification_id = 'notification_id_example' # str | The notification id.

try:
    # Delete a notification
    api_instance.delete_notification(type, notification_id)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **notification_id** | **str**| The notification id. | 

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

# **delete_notification_external_id**
> delete_notification_external_id(type, notification_id, external_id)

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
notification_id = 'notification_id_example' # str | The notification id.
external_id = 'external_id_example' # str | The external id.

try:
    # Remove an external id
    api_instance.delete_notification_external_id(type, notification_id, external_id)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_notification_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **notification_id** | **str**| The notification id. | 
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

# **delete_notification_external_ids**
> delete_notification_external_ids(type, notification_id)

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
notification_id = 'notification_id_example' # str | The notification id.

try:
    # Clear all external ids for an entity
    api_instance.delete_notification_external_ids(type, notification_id)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_notification_external_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **notification_id** | **str**| The notification id. | 

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

# **delete_notifications**
> delete_notifications(type)

Delete all notifications that exists within an entire resource

Removes all notifications that exists within the specified resource.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.

try:
    # Delete all notifications that exists within an entire resource
    api_instance.delete_notifications(type)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 

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

# **delete_placeholder_notification**
> delete_placeholder_notification(notification_id)

Delete a notification

Removes a particular notification with the given id.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
notification_id = 'notification_id_example' # str | The notification id.

try:
    # Delete a notification
    api_instance.delete_placeholder_notification(notification_id)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_placeholder_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| The notification id. | 

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

# **delete_placeholder_notifications**
> delete_placeholder_notifications()

Delete all notifications that exists within an entire resource

Removes all notifications that exists within the specified resource.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))

try:
    # Delete all notifications that exists within an entire resource
    api_instance.delete_placeholder_notifications()
except ApiException as e:
    print("Exception when calling NotificationApi->delete_placeholder_notifications: %s\n" % e)
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

# **get_entity_notification**
> NotificationType get_entity_notification(type, entity_id, notification_id)

Retrieve a notification

Retrieves a particular notification with the given id.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
notification_id = 'notification_id_example' # str | The notification id.

try:
    # Retrieve a notification
    api_response = api_instance.get_entity_notification(type, entity_id, notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_entity_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **notification_id** | **str**| The notification id. | 

### Return type

[**NotificationType**](NotificationType.md)

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

# **get_entity_notification_external_ids**
> ExternalIdentifierListType get_entity_notification_external_ids(type, entity_id, notification_id)

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
notification_id = 'notification_id_example' # str | The notification id.

try:
    # Retrieve all external ids for an entity
    api_response = api_instance.get_entity_notification_external_ids(type, entity_id, notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_entity_notification_external_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **notification_id** | **str**| The notification id. | 

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

# **get_entity_notifications**
> URIListType get_entity_notifications(type, entity_id)

List all notifications that exists for a particular entity

Lists URIs to all notifications that exists for a given entity.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.

try:
    # List all notifications that exists for a particular entity
    api_response = api_instance.get_entity_notifications(type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_entity_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 

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
**0** | A CRLF-delimited list of URIs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification**
> NotificationType get_notification(type, notification_id)

Retrieve a notification

Retrieves a particular notification with the given id.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
notification_id = 'notification_id_example' # str | The notification id.

try:
    # Retrieve a notification
    api_response = api_instance.get_notification(type, notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **notification_id** | **str**| The notification id. | 

### Return type

[**NotificationType**](NotificationType.md)

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

# **get_notification_external_ids**
> ExternalIdentifierListType get_notification_external_ids(type, notification_id)

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
notification_id = 'notification_id_example' # str | The notification id.

try:
    # Retrieve all external ids for an entity
    api_response = api_instance.get_notification_external_ids(type, notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_notification_external_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **notification_id** | **str**| The notification id. | 

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

# **get_notifications**
> URIListType get_notifications(type)

List all notifications that exists within an entire resource

Lists URIs to all notifications that exists within the given resource.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.

try:
    # List all notifications that exists within an entire resource
    api_response = api_instance.get_notifications(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 

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
**0** | A CRLF-delimited list of URIs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_placeholder_notification**
> NotificationType get_placeholder_notification(notification_id)

Retrieve a notification

Retrieves a particular notification with the given id.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
notification_id = 'notification_id_example' # str | The notification id.

try:
    # Retrieve a notification
    api_response = api_instance.get_placeholder_notification(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_placeholder_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| The notification id. | 

### Return type

[**NotificationType**](NotificationType.md)

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

# **get_placeholder_notifications**
> URIListType get_placeholder_notifications()

List all notifications that exists within an entire resource

Lists URIs to all notifications that exists within the given resource.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))

try:
    # List all notifications that exists within an entire resource
    api_response = api_instance.get_placeholder_notifications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->get_placeholder_notifications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**0** | A CRLF-delimited list of URIs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_notification**
> NotificationType update_entity_notification(type, entity_id, notification_id, notification_type)

Change a particular notification on a specific entity

Change the action and/or trigger of the notification that exists within the given resource.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
notification_id = 'notification_id_example' # str | The notification id.
notification_type = vidispine.NotificationType() # NotificationType | 

try:
    # Change a particular notification on a specific entity
    api_response = api_instance.update_entity_notification(type, entity_id, notification_id, notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->update_entity_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **notification_id** | **str**| The notification id. | 
 **notification_type** | [**NotificationType**](NotificationType.md)|  | 

### Return type

[**NotificationType**](NotificationType.md)

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

# **update_notification**
> NotificationType update_notification(type, notification_id, notification_type)

Change a particular notification on a whole entity

Change the action and/or trigger of the notification that exists within the given resource.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type.
notification_id = 'notification_id_example' # str | The notification id.
notification_type = vidispine.NotificationType() # NotificationType | 

try:
    # Change a particular notification on a whole entity
    api_response = api_instance.update_notification(type, notification_id, notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->update_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type. | 
 **notification_id** | **str**| The notification id. | 
 **notification_type** | [**NotificationType**](NotificationType.md)|  | 

### Return type

[**NotificationType**](NotificationType.md)

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

# **update_placeholder_notification**
> NotificationType update_placeholder_notification(notification_id, notification_type)

Change a particular notification on a whole entity

Change the action and/or trigger of the notification that exists within the given resource.

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
api_instance = vidispine.NotificationApi(vidispine.ApiClient(configuration))
notification_id = 'notification_id_example' # str | The notification id.
notification_type = vidispine.NotificationType() # NotificationType | 

try:
    # Change a particular notification on a whole entity
    api_response = api_instance.update_placeholder_notification(notification_id, notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->update_placeholder_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| The notification id. | 
 **notification_type** | [**NotificationType**](NotificationType.md)|  | 

### Return type

[**NotificationType**](NotificationType.md)

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

