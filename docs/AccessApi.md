# vidispine.AccessApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_control**](AccessApi.md#create_access_control) | **POST** /{type}/{entity-id}/access | Create an access control entry
[**create_access_control_for_all_items**](AccessApi.md#create_access_control_for_all_items) | **POST** /item/access | Add access control entries to all items
[**create_access_controls**](AccessApi.md#create_access_controls) | **POST** /{type}/{entity-id}/access/bulk | Create multiple entry access control entries
[**delete_access_control**](AccessApi.md#delete_access_control) | **DELETE** /{type}/{entity-id}/access/{access-id} | Delete an access control entry
[**delete_access_controls**](AccessApi.md#delete_access_controls) | **DELETE** /{type}/{entity-id}/access/bulk | Delete multiple access control entries
[**delete_access_controls_from_all_items**](AccessApi.md#delete_access_controls_from_all_items) | **DELETE** /item/access | Delete all access control entries from all items
[**get_access_control**](AccessApi.md#get_access_control) | **GET** /{type}/{entity-id}/access/{access-id} | Retrieve an access control entry
[**get_access_controls**](AccessApi.md#get_access_controls) | **GET** /{type}/{entity-id}/access | Retrieve the access control list for an entity
[**get_access_graph**](AccessApi.md#get_access_graph) | **GET** /{type}/{entity-id}/access/graph | Retrieve the access graph
[**get_access_graph_dot**](AccessApi.md#get_access_graph_dot) | **GET** /{type}/{entity-id}/access/graph/dot | Retrieve the access graph as dot file
[**get_merged_access**](AccessApi.md#get_merged_access) | **GET** /{type}/{entity-id}/merged-access/ | List the applied access control entries for an entity
[**get_merged_access_for_group**](AccessApi.md#get_merged_access_for_group) | **GET** /{type}/{entity-id}/merged-access/group | List the applied access control entries that affects groups
[**update_owner**](AccessApi.md#update_owner) | **PUT** /{type}/{entity-id}/access/owner/{username} | Update the owner of an entity


# **create_access_control**
> AccessControlType create_access_control(type, entity_id, access_control_type, allow_duplicate=allow_duplicate)

Create an access control entry

Adds a new access control entry for the specified entity.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
access_control_type = vidispine.AccessControlType() # AccessControlType | 
allow_duplicate = True # bool | Set to `false` in order to avoid adding a duplicate access control. (optional) (default to True)

try:
    # Create an access control entry
    api_response = api_instance.create_access_control(type, entity_id, access_control_type, allow_duplicate=allow_duplicate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->create_access_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **access_control_type** | [**AccessControlType**](AccessControlType.md)|  | 
 **allow_duplicate** | **bool**| Set to &#x60;false&#x60; in order to avoid adding a duplicate access control. | [optional] [default to True]

### Return type

[**AccessControlType**](AccessControlType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The id of the created entry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_control_for_all_items**
> create_access_control_for_all_items(access_control_type)

Add access control entries to all items

Adds access control entries to all known items.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
access_control_type = vidispine.AccessControlType() # AccessControlType | 

try:
    # Add access control entries to all items
    api_instance.create_access_control_for_all_items(access_control_type)
except ApiException as e:
    print("Exception when calling AccessApi->create_access_control_for_all_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_control_type** | [**AccessControlType**](AccessControlType.md)|  | 

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

# **create_access_controls**
> AccessControlListType create_access_controls(type, entity_id, access_control_list_type)

Create multiple entry access control entries

Adds multiple new access control entries to the specified entity.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
access_control_list_type = vidispine.AccessControlListType() # AccessControlListType | 

try:
    # Create multiple entry access control entries
    api_response = api_instance.create_access_controls(type, entity_id, access_control_list_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->create_access_controls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **access_control_list_type** | [**AccessControlListType**](AccessControlListType.md)|  | 

### Return type

[**AccessControlListType**](AccessControlListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The ids of the created entries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_control**
> delete_access_control(type, entity_id, access_id)

Delete an access control entry

Removes the desired access control entry.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
access_id = 'access_id_example' # str | The access id.

try:
    # Delete an access control entry
    api_instance.delete_access_control(type, entity_id, access_id)
except ApiException as e:
    print("Exception when calling AccessApi->delete_access_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **access_id** | **str**| The access id. | 

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

# **delete_access_controls**
> delete_access_controls(type, entity_id, access_control_list_type)

Delete multiple access control entries

Deletes multiple access control entries by id.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
access_control_list_type = vidispine.AccessControlListType() # AccessControlListType | 

try:
    # Delete multiple access control entries
    api_instance.delete_access_controls(type, entity_id, access_control_list_type)
except ApiException as e:
    print("Exception when calling AccessApi->delete_access_controls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **access_control_list_type** | [**AccessControlListType**](AccessControlListType.md)|  | 

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

# **delete_access_controls_from_all_items**
> delete_access_controls_from_all_items()

Delete all access control entries from all items

Deletes all access control entries from all known items.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))

try:
    # Delete all access control entries from all items
    api_instance.delete_access_controls_from_all_items()
except ApiException as e:
    print("Exception when calling AccessApi->delete_access_controls_from_all_items: %s\n" % e)
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

# **get_access_control**
> AccessControlType get_access_control(type, entity_id, access_id)

Retrieve an access control entry

Retrieves the desired access control entry.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
access_id = 'access_id_example' # str | The access id.

try:
    # Retrieve an access control entry
    api_response = api_instance.get_access_control(type, entity_id, access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_access_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **access_id** | **str**| The access id. | 

### Return type

[**AccessControlType**](AccessControlType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The id of the entry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_controls**
> AccessControlListType get_access_controls(type, entity_id)

Retrieve the access control list for an entity

Retrieves the entire access control list for the specified entity.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.

try:
    # Retrieve the access control list for an entity
    api_response = api_instance.get_access_controls(type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_access_controls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 

### Return type

[**AccessControlListType**](AccessControlListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_graph**
> file get_access_graph(type, entity_id, users=users, type2=type2, groups=groups)

Retrieve the access graph

Shows the entity and any ancestor collections or libraries and the access controls on each. The access-entity can be item or collection (library is not implemented).

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
users = True # bool | If the user and group hierarchy should be shown as a subgraph for the relevant users/groups. (optional)
type2 = 'type_example' # str | - `ancestor` - Show the entity and ancestor entities in a hierarchy.  - `grant` - Show users and how permissions have been granted. (optional)
groups = True # bool | If groups should be shown as nodes in the grant graph. (optional)

try:
    # Retrieve the access graph
    api_response = api_instance.get_access_graph(type, entity_id, users=users, type2=type2, groups=groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_access_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **users** | **bool**| If the user and group hierarchy should be shown as a subgraph for the relevant users/groups. | [optional] 
 **type2** | **str**| - &#x60;ancestor&#x60; - Show the entity and ancestor entities in a hierarchy.  - &#x60;grant&#x60; - Show users and how permissions have been granted. | [optional] 
 **groups** | **bool**| If groups should be shown as nodes in the grant graph. | [optional] 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_graph_dot**
> str get_access_graph_dot(type, entity_id, users=users, type2=type2, groups=groups)

Retrieve the access graph as dot file

Shows the entity and any ancestor collections or libraries and the access controls on each. The access-entity can be item or collection (library is not implemented).

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
users = True # bool | If the user and group hierarchy should be shown as a subgraph for the relevant users/groups. (optional)
type2 = 'type_example' # str | - `ancestor` - Show the entity and ancestor entities in a hierarchy.  - `grant` - Show users and how permissions have been granted. (optional)
groups = True # bool | If groups should be shown as nodes in the grant graph. (optional)

try:
    # Retrieve the access graph as dot file
    api_response = api_instance.get_access_graph_dot(type, entity_id, users=users, type2=type2, groups=groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_access_graph_dot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **users** | **bool**| If the user and group hierarchy should be shown as a subgraph for the relevant users/groups. | [optional] 
 **type2** | **str**| - &#x60;ancestor&#x60; - Show the entity and ancestor entities in a hierarchy.  - &#x60;grant&#x60; - Show users and how permissions have been granted. | [optional] 
 **groups** | **bool**| If groups should be shown as nodes in the grant graph. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/vnd.graphviz, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merged_access**
> AccessControlMergedType get_merged_access(type, entity_id, type2=type2, permission=permission, username=username, extradata=extradata)

List the applied access control entries for an entity

Retrieves a list of all access control entries that affects each user for a given entity. This includes all access derived from the user's group memberships, and from the entity's inclusion in collections or libraries.  There are two modes of operation, either retrieving the access on the item for all users or querying for the access of a specific user. In the former case no parameters are specified and in the latter all parameters must be supplied.  The `access` element of the *AccessControlMergedDocument* includes the following fields:  The entries are listed grouped by user, in order of priority for each user.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
type2 = 'type_example' # str | The type of operation to check for. (optional)
permission = 'permission_example' # str | The lowest required permission level. (optional)
username = 'username_example' # str | The name of the user to check. (optional)
extradata = 'extradata_example' # str | Any possible extradata. (optional)

try:
    # List the applied access control entries for an entity
    api_response = api_instance.get_merged_access(type, entity_id, type2=type2, permission=permission, username=username, extradata=extradata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_merged_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **type2** | **str**| The type of operation to check for. | [optional] 
 **permission** | **str**| The lowest required permission level. | [optional] 
 **username** | **str**| The name of the user to check. | [optional] 
 **extradata** | **str**| Any possible extradata. | [optional] 

### Return type

[**AccessControlMergedType**](AccessControlMergedType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An &lt;em&gt;AccessControlMergedDocument&lt;/em&gt; containing all access control that affects the entity. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merged_access_for_group**
> AccessControlMergedGroupType get_merged_access_for_group(type, entity_id, full=full)

List the applied access control entries that affects groups

Lists groups that have access to an entity.  Even though a user belongs to a group that has access to an entity, the user may not have access due to other access control entries that take precedence.  Groups without users will not appear, unless the group belongs to an inheritance hierarchy that has users.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
full = False # bool | - `true` - Return all access controls that apply for a group.  Also include additional information about the access controls in the response.  - `false` (default) - Return a single access entry with the permission that applies for each group and type. (optional) (default to False)

try:
    # List the applied access control entries that affects groups
    api_response = api_instance.get_merged_access_for_group(type, entity_id, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_merged_access_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **full** | **bool**| - &#x60;true&#x60; - Return all access controls that apply for a group.  Also include additional information about the access controls in the response.  - &#x60;false&#x60; (default) - Return a single access entry with the permission that applies for each group and type. | [optional] [default to False]

### Return type

[**AccessControlMergedGroupType**](AccessControlMergedGroupType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An &lt;em&gt;AccessControlMergedGroupDocument&lt;/em&gt;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_owner**
> AccessControlType update_owner(type, entity_id, username)

Update the owner of an entity

Update the owner of the specified entity to the specified user.

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
api_instance = vidispine.AccessApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
username = 'username_example' # str | The username.

try:
    # Update the owner of an entity
    api_response = api_instance.update_owner(type, entity_id, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->update_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **username** | **str**| The username. | 

### Return type

[**AccessControlType**](AccessControlType.md)

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

