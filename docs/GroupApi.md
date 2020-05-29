# vidispine.GroupApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_to_group**](GroupApi.md#add_group_to_group) | **PUT** /group/{group-name}/group/{child-groupname} | Add a group to another group
[**add_user_to_group**](GroupApi.md#add_user_to_group) | **PUT** /group/{group-name}/user/{username} | Add a user to a group
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /group/{group-name} | Delete a group
[**delete_group_from_group**](GroupApi.md#delete_group_from_group) | **DELETE** /group/{group-name}/group/{child-groupname} | Remove a group from another group
[**delete_group_metadata**](GroupApi.md#delete_group_metadata) | **DELETE** /group/{group-name}/metadata | Delete all key-value pairs
[**delete_group_metadata_key**](GroupApi.md#delete_group_metadata_key) | **DELETE** /group/{group-name}/metadata/{keypath} | Delete key-value pairs
[**delete_groups**](GroupApi.md#delete_groups) | **DELETE** /group | Delete multiple groups
[**delete_user_from_group**](GroupApi.md#delete_user_from_group) | **DELETE** /group/{group-name}/user/{username} | Remove a user from a group
[**get_group**](GroupApi.md#get_group) | **GET** /group/{group-name} | Retrieve a group/role
[**get_group_children**](GroupApi.md#get_group_children) | **GET** /group/{group-name}/children | List all child groups to a group
[**get_group_description**](GroupApi.md#get_group_description) | **GET** /group/{group-name}/description | Retrieve the group description
[**get_group_metadata**](GroupApi.md#get_group_metadata) | **GET** /group/{group-name}/metadata | Retrieve all metadata
[**get_group_metadata_key**](GroupApi.md#get_group_metadata_key) | **GET** /group/{group-name}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_group_parents**](GroupApi.md#get_group_parents) | **GET** /group/{group-name}/parents | List all parent groups to a group
[**get_group_role**](GroupApi.md#get_group_role) | **GET** /group/{group-name}/role | Retrieve role status
[**get_group_users**](GroupApi.md#get_group_users) | **GET** /group/{group-name}/users | List all users in a group
[**get_groups**](GroupApi.md#get_groups) | **GET** /group | List all groups/roles
[**search_groups**](GroupApi.md#search_groups) | **PUT** /group | Search for groups
[**update_group_description**](GroupApi.md#update_group_description) | **PUT** /group/{group-name}/description | Update the description of a group
[**update_group_metadata**](GroupApi.md#update_group_metadata) | **PUT** /group/{group-name}/metadata | Create multiple key-value pairs
[**update_group_metadata_key**](GroupApi.md#update_group_metadata_key) | **PUT** /group/{group-name}/metadata/{keypath} | Set the value for a specific key
[**update_or_create_group**](GroupApi.md#update_or_create_group) | **PUT** /group/{group-name} | Update or create a group


# **add_group_to_group**
> add_group_to_group(group_name, child_groupname)

Add a group to another group

Creates parent-child relation between the two specified groups.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
child_groupname = 'child_groupname_example' # str | The child groupname.

try:
    # Add a group to another group
    api_instance.add_group_to_group(group_name, child_groupname)
except ApiException as e:
    print("Exception when calling GroupApi->add_group_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **child_groupname** | **str**| The child groupname. | 

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

# **add_user_to_group**
> add_user_to_group(group_name, username)

Add a user to a group

Adds the specified user to the specified group.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
username = 'username_example' # str | The username.

try:
    # Add a user to a group
    api_instance.add_user_to_group(group_name, username)
except ApiException as e:
    print("Exception when calling GroupApi->add_user_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **username** | **str**| The username. | 

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

# **delete_group**
> delete_group(group_name)

Delete a group

Deletes the group with the specified name.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Delete a group
    api_instance.delete_group(group_name)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

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

# **delete_group_from_group**
> delete_group_from_group(group_name, child_groupname)

Remove a group from another group

Removes the parent-child relation between the two specified groups.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
child_groupname = 'child_groupname_example' # str | The child groupname.

try:
    # Remove a group from another group
    api_instance.delete_group_from_group(group_name, child_groupname)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **child_groupname** | **str**| The child groupname. | 

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

# **delete_group_metadata**
> delete_group_metadata(group_name)

Delete all key-value pairs

Clears all key-value pairs for the specified entity.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Delete all key-value pairs
    api_instance.delete_group_metadata(group_name)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

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

# **delete_group_metadata_key**
> delete_group_metadata_key(group_name, keypath)

Delete key-value pairs

Deletes the key-value pair with the specified key. If a key path is given, it may include wildcards for deleting multiple keys.  Key paths can also be specified as well as specific keys.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_group_metadata_key(group_name, keypath)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **keypath** | **str**| The keypath. | 

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

# **delete_groups**
> delete_groups(name)

Delete multiple groups

Deletes the groups with the specified names.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
name = ['name_example'] # list[str] | Comma-separated list of group names.

try:
    # Delete multiple groups
    api_instance.delete_groups(name)
except ApiException as e:
    print("Exception when calling GroupApi->delete_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**list[str]**](str.md)| Comma-separated list of group names. | 

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

# **delete_user_from_group**
> delete_user_from_group(group_name, username)

Remove a user from a group

Removes the specified user from the specified group.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
username = 'username_example' # str | The username.

try:
    # Remove a user from a group
    api_instance.delete_user_from_group(group_name, username)
except ApiException as e:
    print("Exception when calling GroupApi->delete_user_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **username** | **str**| The username. | 

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

# **get_group**
> GroupType get_group(group_name)

Retrieve a group/role

Returns information about the specified group.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Retrieve a group/role
    api_response = api_instance.get_group(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

### Return type

[**GroupType**](GroupType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The URI to the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_children**
> GroupListType get_group_children(group_name, traverse=traverse)

List all child groups to a group

Returns groups that belongs to the specified group.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
traverse = False # bool | - `true` - Return all descendants.  - `false` (default) - Return only direct children. (optional) (default to False)

try:
    # List all child groups to a group
    api_response = api_instance.get_group_children(group_name, traverse=traverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **traverse** | **bool**| - &#x60;true&#x60; - Return all descendants.  - &#x60;false&#x60; (default) - Return only direct children. | [optional] [default to False]

### Return type

[**GroupListType**](GroupListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CCRLF-delimeted list of URIs to the groups |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_description**
> str get_group_description(group_name)

Retrieve the group description

Returns the descriptive text about the specified group.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Retrieve the group description
    api_response = api_instance.get_group_description(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

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
**0** | Group description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metadata**
> SimpleMetadataType get_group_metadata(group_name)

Retrieve all metadata

Retrieves all key-value pairs associated with the specified entity.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Retrieve all metadata
    api_response = api_instance.get_group_metadata(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

### Return type

[**SimpleMetadataType**](SimpleMetadataType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;SimpleMetadataDocument&lt;/em&gt; containing all key-value pairs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metadata_key**
> str get_group_metadata_key(group_name, keypath)

Retrieve the metadata for a specific key

Retrieves the value of a specific key. If a key path is specified, exactly one key-value pair must match the key path, else an error is returned.  Key paths can also be specified as well as specific keys.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_group_metadata_key(group_name, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **keypath** | **str**| The keypath. | 

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
**0** | The raw string value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_parents**
> GroupListType get_group_parents(group_name, traverse=traverse)

List all parent groups to a group

Returns groups that the specified group belongs to.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
traverse = False # bool | - `true` - Return all ancestors.  - `false` (default) - Return only direct parents. (optional) (default to False)

try:
    # List all parent groups to a group
    api_response = api_instance.get_group_parents(group_name, traverse=traverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_parents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **traverse** | **bool**| - &#x60;true&#x60; - Return all ancestors.  - &#x60;false&#x60; (default) - Return only direct parents. | [optional] [default to False]

### Return type

[**GroupListType**](GroupListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimeted list of URIs to the groups |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_role**
> str get_group_role(group_name)

Retrieve role status

Returns the role status of the specified group.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Retrieve role status
    api_response = api_instance.get_group_role(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

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
**0** | 1 if group is a role, 0 if group is a regular group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_users**
> UserListType get_group_users(group_name, traverse=traverse)

List all users in a group

Returns all users belonging to the group/role, directly or indirectly.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
traverse = False # bool | - `true` - Return all users, including users in child groups.  - `false` (default) - Return only direct users. (optional) (default to False)

try:
    # List all users in a group
    api_response = api_instance.get_group_users(group_name, traverse=traverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **traverse** | **bool**| - &#x60;true&#x60; - Return all users, including users in child groups.  - &#x60;false&#x60; (default) - Return only direct users. | [optional] [default to False]

### Return type

[**UserListType**](UserListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimeted list of TabbedTuple of user name, user real name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> GroupListType get_groups(role=role, first=first, number=number)

List all groups/roles

Returns list of all groups.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
role = True # bool | - `true` - Return only roles.  - `false` - Return only regular groups.  Default is to return all.  New in version 4. 16. (optional)
first = 1 # int | Start returning groups from specified number. (optional) (default to 1)
number = 56 # int | Return at most specified number of groups.  Default is no limit. (optional)

try:
    # List all groups/roles
    api_response = api_instance.get_groups(role=role, first=first, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **bool**| - &#x60;true&#x60; - Return only roles.  - &#x60;false&#x60; - Return only regular groups.  Default is to return all.  New in version 4. 16. | [optional] 
 **first** | **int**| Start returning groups from specified number. | [optional] [default to 1]
 **number** | **int**| Return at most specified number of groups.  Default is no limit. | [optional] 

### Return type

[**GroupListType**](GroupListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of group URIs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groups**
> GroupListType search_groups(simple_search_type, role=role, number=number)

Search for groups

Simple search of fields `groupname`, `description` and metadata.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
simple_search_type = vidispine.SimpleSearchType() # SimpleSearchType | 
role = True # bool | - `true` - Return only roles.  - `false` - Return only regular groups.  Default is to return all. (optional)
number = 10 # int | Return at most specified number of groups. (optional) (default to 10)

try:
    # Search for groups
    api_response = api_instance.search_groups(simple_search_type, role=role, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->search_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simple_search_type** | [**SimpleSearchType**](SimpleSearchType.md)|  | 
 **role** | **bool**| - &#x60;true&#x60; - Return only roles.  - &#x60;false&#x60; - Return only regular groups.  Default is to return all. | [optional] 
 **number** | **int**| Return at most specified number of groups. | [optional] [default to 10]

### Return type

[**GroupListType**](GroupListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of group names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_description**
> update_group_description(group_name, body)

Update the description of a group

Changes the description of a group.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
body = 'body_example' # str | The new description.

try:
    # Update the description of a group
    api_instance.update_group_description(group_name, body)
except ApiException as e:
    print("Exception when calling GroupApi->update_group_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **body** | **str**| The new description. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metadata**
> update_group_metadata(group_name, simple_metadata_type)

Create multiple key-value pairs

Sets all the specified key-value pairs.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_group_metadata(group_name, simple_metadata_type)
except ApiException as e:
    print("Exception when calling GroupApi->update_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **simple_metadata_type** | [**SimpleMetadataType**](SimpleMetadataType.md)|  | 

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

# **update_group_metadata_key**
> update_group_metadata_key(group_name, keypath, body)

Set the value for a specific key

Sets the value for a specific key. The key path may not contain wildcards.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_group_metadata_key(group_name, keypath, body)
except ApiException as e:
    print("Exception when calling GroupApi->update_group_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **keypath** | **str**| The keypath. | 
 **body** | **str**| The raw string value. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_group**
> update_or_create_group(group_name, group_type, clear=clear)

Update or create a group

Creates or updates the group with the specified name. Also any specified parent and child associations, users, metadata and description will be added.

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
api_instance = vidispine.GroupApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
group_type = vidispine.GroupType() # GroupType | 
clear = False # bool | - `true` - Remove any existing groups and users not in the given document.  - `false` (default) - Existing groups and users not in the request document will be kept as is. (optional) (default to False)

try:
    # Update or create a group
    api_instance.update_or_create_group(group_name, group_type, clear=clear)
except ApiException as e:
    print("Exception when calling GroupApi->update_or_create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **group_type** | [**GroupType**](GroupType.md)|  | 
 **clear** | **bool**| - &#x60;true&#x60; - Remove any existing groups and users not in the given document.  - &#x60;false&#x60; (default) - Existing groups and users not in the request document will be kept as is. | [optional] [default to False]

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

