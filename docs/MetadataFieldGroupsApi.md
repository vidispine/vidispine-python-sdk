# vidispine.MetadataFieldGroupsApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_field_group_to_field_group**](MetadataFieldGroupsApi.md#add_metadata_field_group_to_field_group) | **PUT** /metadata-field/field-group/{parent-group-name}/group/{child-group-name} | Add a group to a group
[**delete_metadata_field_group**](MetadataFieldGroupsApi.md#delete_metadata_field_group) | **DELETE** /metadata-field/field-group/{group-name} | Delete a field group
[**delete_metadata_field_group_field**](MetadataFieldGroupsApi.md#delete_metadata_field_group_field) | **DELETE** /metadata-field/field-group/{group-name}/{field-name} | Remove a field from a group
[**delete_metadata_field_group_from_field_group**](MetadataFieldGroupsApi.md#delete_metadata_field_group_from_field_group) | **DELETE** /metadata-field/field-group/{parent-group-name}/group/{child-group-name} | Remove a group from a group
[**delete_metadata_field_group_metadata**](MetadataFieldGroupsApi.md#delete_metadata_field_group_metadata) | **DELETE** /metadata-field/field-group/{group-name}/metadata | Delete all key-value pairs
[**delete_metadata_field_group_metadata_key**](MetadataFieldGroupsApi.md#delete_metadata_field_group_metadata_key) | **DELETE** /metadata-field/field-group/{group-name}/metadata/{keypath} | Delete key-value pairs
[**get_metadata_field_group**](MetadataFieldGroupsApi.md#get_metadata_field_group) | **GET** /metadata-field/field-group/{group-name} | List all fields of a group
[**get_metadata_field_group_merged_access**](MetadataFieldGroupsApi.md#get_metadata_field_group_merged_access) | **GET** /metadata-field/field-group/{group-name}/merged-access/ | Retrieve user access to field group
[**get_metadata_field_group_metadata**](MetadataFieldGroupsApi.md#get_metadata_field_group_metadata) | **GET** /metadata-field/field-group/{group-name}/metadata | Retrieve all metadata
[**get_metadata_field_group_metadata_key**](MetadataFieldGroupsApi.md#get_metadata_field_group_metadata_key) | **GET** /metadata-field/field-group/{group-name}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_metadata_field_groups**](MetadataFieldGroupsApi.md#get_metadata_field_groups) | **GET** /metadata-field/field-group | List all field groups
[**get_metadata_field_groups_merged_access**](MetadataFieldGroupsApi.md#get_metadata_field_groups_merged_access) | **GET** /metadata-field/field-group/merged-access/ | Retrieve user access to all field groups
[**search_metadata_field_groups**](MetadataFieldGroupsApi.md#search_metadata_field_groups) | **PUT** /metadata-field/field-group | Search for groups used in metadata
[**update_metadata_field_group**](MetadataFieldGroupsApi.md#update_metadata_field_group) | **PUT** /metadata-field/field-group/{group-name}/{field-name} | Add a field to a group
[**update_metadata_field_group_metadata**](MetadataFieldGroupsApi.md#update_metadata_field_group_metadata) | **PUT** /metadata-field/field-group/{group-name}/metadata | Create multiple key-value pairs
[**update_metadata_field_group_metadata_key**](MetadataFieldGroupsApi.md#update_metadata_field_group_metadata_key) | **PUT** /metadata-field/field-group/{group-name}/metadata/{keypath} | Set the value for a specific key
[**update_or_create_metadata_field_group**](MetadataFieldGroupsApi.md#update_or_create_metadata_field_group) | **PUT** /metadata-field/field-group/{group-name} | Update or create a field group


# **add_metadata_field_group_to_field_group**
> add_metadata_field_group_to_field_group(parent_group_name, child_group_name)

Add a group to a group

Adds the group with the specified name to the group. If the group is already contained within the group this operation does nothing.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
parent_group_name = 'parent_group_name_example' # str | The parent group name.
child_group_name = 'child_group_name_example' # str | The child group name.

try:
    # Add a group to a group
    api_instance.add_metadata_field_group_to_field_group(parent_group_name, child_group_name)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->add_metadata_field_group_to_field_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_group_name** | **str**| The parent group name. | 
 **child_group_name** | **str**| The child group name. | 

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

# **delete_metadata_field_group**
> delete_metadata_field_group(group_name)

Delete a field group

Deletes the group with the given name.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Delete a field group
    api_instance.delete_metadata_field_group(group_name)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->delete_metadata_field_group: %s\n" % e)
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

# **delete_metadata_field_group_field**
> delete_metadata_field_group_field(group_name, field_name)

Remove a field from a group

Removes the field with the specified name from the group.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
field_name = 'field_name_example' # str | The field name.

try:
    # Remove a field from a group
    api_instance.delete_metadata_field_group_field(group_name, field_name)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->delete_metadata_field_group_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **field_name** | **str**| The field name. | 

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

# **delete_metadata_field_group_from_field_group**
> delete_metadata_field_group_from_field_group(parent_group_name, child_group_name)

Remove a group from a group

Removes the group with the specified name from the group.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
parent_group_name = 'parent_group_name_example' # str | The parent group name.
child_group_name = 'child_group_name_example' # str | The child group name.

try:
    # Remove a group from a group
    api_instance.delete_metadata_field_group_from_field_group(parent_group_name, child_group_name)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->delete_metadata_field_group_from_field_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_group_name** | **str**| The parent group name. | 
 **child_group_name** | **str**| The child group name. | 

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

# **delete_metadata_field_group_metadata**
> delete_metadata_field_group_metadata(group_name)

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Delete all key-value pairs
    api_instance.delete_metadata_field_group_metadata(group_name)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->delete_metadata_field_group_metadata: %s\n" % e)
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

# **delete_metadata_field_group_metadata_key**
> delete_metadata_field_group_metadata_key(group_name, keypath)

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_metadata_field_group_metadata_key(group_name, keypath)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->delete_metadata_field_group_metadata_key: %s\n" % e)
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

# **get_metadata_field_group**
> MetadataFieldGroupType get_metadata_field_group(group_name, data=data, traverse=traverse, include_values=include_values)

List all fields of a group

Retrieves the specified field group.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
data = ['data_example'] # list[str] | Comma-separated list of any additional data to include.   - accepts wildcard characters.  e. g.   `*`, `myapp_*`,  `*_version`.  (New in 4. 17. ) (optional)
traverse = False # bool | - `true` - Traverse any sub-groups in order to retrieve the entire hierarchy.  - `false` (default) - Only retrieves the names of the members. (optional) (default to False)
include_values = False # bool | Return the value enumeration for each field (optional) (default to False)

try:
    # List all fields of a group
    api_response = api_instance.get_metadata_field_group(group_name, data=data, traverse=traverse, include_values=include_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->get_metadata_field_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **data** | [**list[str]**](str.md)| Comma-separated list of any additional data to include.   - accepts wildcard characters.  e. g.   &#x60;*&#x60;, &#x60;myapp_*&#x60;,  &#x60;*_version&#x60;.  (New in 4. 17. ) | [optional] 
 **traverse** | **bool**| - &#x60;true&#x60; - Traverse any sub-groups in order to retrieve the entire hierarchy.  - &#x60;false&#x60; (default) - Only retrieves the names of the members. | [optional] [default to False]
 **include_values** | **bool**| Return the value enumeration for each field | [optional] [default to False]

### Return type

[**MetadataFieldGroupType**](MetadataFieldGroupType.md)

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

# **get_metadata_field_group_merged_access**
> AccessControlMergedType get_metadata_field_group_merged_access(group_name, username=username)

Retrieve user access to field group

Retrieves the permission for a specific user to a field group and the field groups and fields part of that group.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
username = 'username_example' # str | The name of the user to check. (optional)

try:
    # Retrieve user access to field group
    api_response = api_instance.get_metadata_field_group_merged_access(group_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->get_metadata_field_group_merged_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **username** | **str**| The name of the user to check. | [optional] 

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
**0** | An &lt;em&gt;AccessControlMergedDocument&lt;/em&gt; containing the group, its children, user and permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_field_group_metadata**
> SimpleMetadataType get_metadata_field_group_metadata(group_name)

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Retrieve all metadata
    api_response = api_instance.get_metadata_field_group_metadata(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->get_metadata_field_group_metadata: %s\n" % e)
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

# **get_metadata_field_group_metadata_key**
> str get_metadata_field_group_metadata_key(group_name, keypath)

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_metadata_field_group_metadata_key(group_name, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->get_metadata_field_group_metadata_key: %s\n" % e)
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

# **get_metadata_field_groups**
> MetadataFieldGroupListType get_metadata_field_groups(data=data, content=content, traverse=traverse)

List all field groups

Retrieves all metadata field groups known by the system.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
data = ['data_example'] # list[str] | Comma-separated list of any additional data to include.   - accepts wildcard characters.  e. g.   `*`, `myapp_*`,  `*_version`.  (New in 4. 17. ) (optional)
content = False # bool | - `true` - Return the groups and their members.  - `false` (default) - Return the group names only. (optional) (default to False)
traverse = False # bool | - `true` - Traverse any sub-groups in order to retrieve the entire hierarchy.  - `false` (default) - Only retrieves the names of the members. (optional) (default to False)

try:
    # List all field groups
    api_response = api_instance.get_metadata_field_groups(data=data, content=content, traverse=traverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->get_metadata_field_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**list[str]**](str.md)| Comma-separated list of any additional data to include.   - accepts wildcard characters.  e. g.   &#x60;*&#x60;, &#x60;myapp_*&#x60;,  &#x60;*_version&#x60;.  (New in 4. 17. ) | [optional] 
 **content** | **bool**| - &#x60;true&#x60; - Return the groups and their members.  - &#x60;false&#x60; (default) - Return the group names only. | [optional] [default to False]
 **traverse** | **bool**| - &#x60;true&#x60; - Traverse any sub-groups in order to retrieve the entire hierarchy.  - &#x60;false&#x60; (default) - Only retrieves the names of the members. | [optional] [default to False]

### Return type

[**MetadataFieldGroupListType**](MetadataFieldGroupListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of field group names. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_field_groups_merged_access**
> AccessControlMergedType get_metadata_field_groups_merged_access(username=username)

Retrieve user access to all field groups

Retrieves the permission for a specific user to all field groups and the field groups and fields part of those groups.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The name of the user to check. (optional)

try:
    # Retrieve user access to all field groups
    api_response = api_instance.get_metadata_field_groups_merged_access(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->get_metadata_field_groups_merged_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name of the user to check. | [optional] 

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
**0** | An &lt;em&gt;AccessControlMergedDocument&lt;/em&gt; containing the group, its children, user and permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_metadata_field_groups**
> MetadataFieldResultType search_metadata_field_groups(item_search_type, source=source, first=first, data=data, number=number, include_source=include_source, traverse=traverse, include_value=include_value, include_definition=include_definition, group=group)

Search for groups used in metadata

Much like searching for items, specific fields can be used when searching. The result is a list of used metadata groups that matches the query. Optionally the definition of the group and the value of the group can be retrieved.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
item_search_type = vidispine.ItemSearchType() # ItemSearchType | 
source = 'source_example' # str | - `item` - Only search for groups in item metadata.  - `collection` - Only search for groups in collection metadata.  - `global` - Only search for groups in the global metadata.  - `document` - Only search for groups in the document metadata. (optional)
first = 1 # int | From the resulting list of items, start return list from specified offset. (optional) (default to 1)
data = ['data_example'] # list[str] | Comma-separated list of any additional data to include.   - accepts wildcard characters.  e. g.   `*`, `myapp_*`,  `*_version`.  (New in 4. 17. ) (optional)
number = 100 # int | The number of entities to fetch. (optional) (default to 100)
include_source = False # bool | - `true` - Information about which entity that contains the matching metadata group is included in the result.  - `false` (default) - Entity information is not included. (optional) (default to False)
traverse = False # bool | - `true` - Traverse any sub-groups in order to retrieve the entire hierarchy.  - `false` (default) - Only retrieves the names of the members. (optional) (default to False)
include_value = False # bool | - `true` - The value is included in the result.  I. e. , how the group is specified in the metadata.  - `false` (default) - The value is not included. (optional) (default to False)
include_definition = False # bool | - `true` - The definition of the group is included in the result.  - `false` (default) - The definition is not included. (optional) (default to False)
group = ['group_example'] # list[str] | Comma-separated list of group names to restrict search in. (optional)

try:
    # Search for groups used in metadata
    api_response = api_instance.search_metadata_field_groups(item_search_type, source=source, first=first, data=data, number=number, include_source=include_source, traverse=traverse, include_value=include_value, include_definition=include_definition, group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->search_metadata_field_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_search_type** | [**ItemSearchType**](ItemSearchType.md)|  | 
 **source** | **str**| - &#x60;item&#x60; - Only search for groups in item metadata.  - &#x60;collection&#x60; - Only search for groups in collection metadata.  - &#x60;global&#x60; - Only search for groups in the global metadata.  - &#x60;document&#x60; - Only search for groups in the document metadata. | [optional] 
 **first** | **int**| From the resulting list of items, start return list from specified offset. | [optional] [default to 1]
 **data** | [**list[str]**](str.md)| Comma-separated list of any additional data to include.   - accepts wildcard characters.  e. g.   &#x60;*&#x60;, &#x60;myapp_*&#x60;,  &#x60;*_version&#x60;.  (New in 4. 17. ) | [optional] 
 **number** | **int**| The number of entities to fetch. | [optional] [default to 100]
 **include_source** | **bool**| - &#x60;true&#x60; - Information about which entity that contains the matching metadata group is included in the result.  - &#x60;false&#x60; (default) - Entity information is not included. | [optional] [default to False]
 **traverse** | **bool**| - &#x60;true&#x60; - Traverse any sub-groups in order to retrieve the entire hierarchy.  - &#x60;false&#x60; (default) - Only retrieves the names of the members. | [optional] [default to False]
 **include_value** | **bool**| - &#x60;true&#x60; - The value is included in the result.  I. e. , how the group is specified in the metadata.  - &#x60;false&#x60; (default) - The value is not included. | [optional] [default to False]
 **include_definition** | **bool**| - &#x60;true&#x60; - The definition of the group is included in the result.  - &#x60;false&#x60; (default) - The definition is not included. | [optional] [default to False]
 **group** | [**list[str]**](str.md)| Comma-separated list of group names to restrict search in. | [optional] 

### Return type

[**MetadataFieldResultType**](MetadataFieldResultType.md)

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

# **update_metadata_field_group**
> update_metadata_field_group(group_name, field_name)

Add a field to a group

Adds the field with the specified name to the group. If the field is already contained within the group this operation does nothing.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
field_name = 'field_name_example' # str | The field name.

try:
    # Add a field to a group
    api_instance.update_metadata_field_group(group_name, field_name)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->update_metadata_field_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **field_name** | **str**| The field name. | 

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

# **update_metadata_field_group_metadata**
> update_metadata_field_group_metadata(group_name, simple_metadata_type)

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_metadata_field_group_metadata(group_name, simple_metadata_type)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->update_metadata_field_group_metadata: %s\n" % e)
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

# **update_metadata_field_group_metadata_key**
> update_metadata_field_group_metadata_key(group_name, keypath, body)

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_metadata_field_group_metadata_key(group_name, keypath, body)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->update_metadata_field_group_metadata_key: %s\n" % e)
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

# **update_or_create_metadata_field_group**
> update_or_create_metadata_field_group(group_name, metadata_field_group_type, clear=clear)

Update or create a field group

Creates a new group with the given name, if it does not already exists, and adds any specified fields and access control entries to it. If the fields does not exist, they will be created. Furthermore any additional data for the fields will be set as well.

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
api_instance = vidispine.MetadataFieldGroupsApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
metadata_field_group_type = vidispine.MetadataFieldGroupType() # MetadataFieldGroupType | 
clear = False # bool | - `true` - If the group already exists, clear all content from it before updating.  - `false` (default) - If the group already exists, append child groups/fields from the input document. (optional) (default to False)

try:
    # Update or create a field group
    api_instance.update_or_create_metadata_field_group(group_name, metadata_field_group_type, clear=clear)
except ApiException as e:
    print("Exception when calling MetadataFieldGroupsApi->update_or_create_metadata_field_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **metadata_field_group_type** | [**MetadataFieldGroupType**](MetadataFieldGroupType.md)|  | 
 **clear** | **bool**| - &#x60;true&#x60; - If the group already exists, clear all content from it before updating.  - &#x60;false&#x60; (default) - If the group already exists, append child groups/fields from the input document. | [optional] [default to False]

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

