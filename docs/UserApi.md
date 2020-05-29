# vidispine.UserApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_groups**](UserApi.md#add_user_to_groups) | **PUT** /user/{username}/groups | Add a user to multiple groups
[**create_user**](UserApi.md#create_user) | **POST** /user | Create a user
[**delete_user_metadata**](UserApi.md#delete_user_metadata) | **DELETE** /user/{username}/metadata | Delete all key-value pairs
[**delete_user_metadata_key**](UserApi.md#delete_user_metadata_key) | **DELETE** /user/{username}/metadata/{keypath} | Delete key-value pairs
[**disable_user**](UserApi.md#disable_user) | **DELETE** /user/{username} | Disable a user
[**enable_user**](UserApi.md#enable_user) | **PUT** /user/{username}/enable | Re-enable a user
[**get_user**](UserApi.md#get_user) | **GET** /user/{username} | Retrieve a user
[**get_user_graph**](UserApi.md#get_user_graph) | **GET** /user/graph | Retrieve the user graph
[**get_user_graph_dot**](UserApi.md#get_user_graph_dot) | **GET** /user/graph/dot | Retrieve the user graph as dot file
[**get_user_groups**](UserApi.md#get_user_groups) | **GET** /user/{username}/groups | List all groups for a user
[**get_user_groups_and_roles**](UserApi.md#get_user_groups_and_roles) | **GET** /user/{username}/allgroups | List all roles and groups for a user
[**get_user_metadata**](UserApi.md#get_user_metadata) | **GET** /user/{username}/metadata | Retrieve all metadata
[**get_user_metadata_key**](UserApi.md#get_user_metadata_key) | **GET** /user/{username}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_user_password_salt**](UserApi.md#get_user_password_salt) | **GET** /user/{username}/password/salt | Retrieve the salt of a user
[**get_user_real_name**](UserApi.md#get_user_real_name) | **GET** /user/{username}/realname | Retrieve the real name of a user
[**get_user_roles**](UserApi.md#get_user_roles) | **GET** /user/{username}/roles | List all roles for a user
[**get_users**](UserApi.md#get_users) | **GET** /user | List all users
[**get_who_am_i**](UserApi.md#get_who_am_i) | **GET** /whoami | Return the current user
[**search_users**](UserApi.md#search_users) | **PUT** /user | Search users
[**update_user**](UserApi.md#update_user) | **PUT** /user/{username} | Update a user
[**update_user_metadata**](UserApi.md#update_user_metadata) | **PUT** /user/{username}/metadata | Create multiple key-value pairs
[**update_user_metadata_key**](UserApi.md#update_user_metadata_key) | **PUT** /user/{username}/metadata/{keypath} | Set the value for a specific key
[**update_user_password**](UserApi.md#update_user_password) | **PUT** /user/{username}/password | Update the password of a user
[**update_user_password_salt**](UserApi.md#update_user_password_salt) | **POST** /user/{username}/password/salt | Generate a salt for a user
[**update_user_real_name**](UserApi.md#update_user_real_name) | **PUT** /user/{username}/realname | Update the real name of a user
[**validate_user_password**](UserApi.md#validate_user_password) | **PUT** /user/{username}/validate | Validate the password of a user


# **add_user_to_groups**
> add_user_to_groups(username, group_list_type, move=move)

Add a user to multiple groups

Adds a to multiple to groups. If the move parameter is set to `true`, it will cause the user to be moved to the specified groups.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
group_list_type = vidispine.GroupListType() # GroupListType | 
move = True # bool | - `true` - Remove all previous group-to-user relations - `false` (default) - Keep the current group-to-user relations, and add the specified list (optional)

try:
    # Add a user to multiple groups
    api_instance.add_user_to_groups(username, group_list_type, move=move)
except ApiException as e:
    print("Exception when calling UserApi->add_user_to_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **group_list_type** | [**GroupListType**](GroupListType.md)|  | 
 **move** | **bool**| - &#x60;true&#x60; - Remove all previous group-to-user relations - &#x60;false&#x60; (default) - Keep the current group-to-user relations, and add the specified list | [optional] 

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

# **create_user**
> create_user(user_type, password_type=password_type)

Create a user

Creates a new user based on the information in the *UserDocument*.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
user_type = vidispine.UserType() # UserType | 
password_type = 'md5' # str | - `raw` - Password is in plaintext.  - `md5` (default) - Password is already hashed. (optional) (default to 'md5')

try:
    # Create a user
    api_instance.create_user(user_type, password_type=password_type)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_type** | [**UserType**](UserType.md)|  | 
 **password_type** | **str**| - &#x60;raw&#x60; - Password is in plaintext.  - &#x60;md5&#x60; (default) - Password is already hashed. | [optional] [default to &#39;md5&#39;]

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

# **delete_user_metadata**
> delete_user_metadata(username)

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.

try:
    # Delete all key-value pairs
    api_instance.delete_user_metadata(username)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_user_metadata_key**
> delete_user_metadata_key(username, keypath)

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_user_metadata_key(username, keypath)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
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

# **disable_user**
> JobType disable_user(username, jobmetadata=jobmetadata, notification_data=notification_data, preserve_access=preserve_access, notification=notification, hard=hard, priority=priority)

Disable a user

Disables a user with the given username, rendering that user unable to login.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
preserve_access = False # bool | If set to true, the access granted by the user will still apply.  Only applicable for `hard=false`.  New in version 4. 17. (optional) (default to False)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
hard = False # bool | If set to `true`, the user will be removed completely, including all access controls granted by the user.  Else the user will be disabled. (optional) (default to False)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Disable a user
    api_response = api_instance.disable_user(username, jobmetadata=jobmetadata, notification_data=notification_data, preserve_access=preserve_access, notification=notification, hard=hard, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->disable_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **preserve_access** | **bool**| If set to true, the access granted by the user will still apply.  Only applicable for &#x60;hard&#x3D;false&#x60;.  New in version 4. 17. | [optional] [default to False]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **hard** | **bool**| If set to &#x60;true&#x60;, the user will be removed completely, including all access controls granted by the user.  Else the user will be disabled. | [optional] [default to False]
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | XML/JSON, schema &lt;em&gt;JobDocument&lt;/em&gt; if &lt;code&gt;hard&#x3D;true&lt;/code&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_user**
> enable_user(username)

Re-enable a user

Re-enables a user with the given username, that has previously been disabled.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.

try:
    # Re-enable a user
    api_instance.enable_user(username)
except ApiException as e:
    print("Exception when calling UserApi->enable_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_user**
> UserType get_user(username)

Retrieve a user

Returns a specific user.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.

try:
    # Retrieve a user
    api_response = api_instance.get_user(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 

### Return type

[**UserType**](UserType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | XML/JSON, schema &lt;em&gt;UserDocument&lt;/em&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_graph**
> file get_user_graph(groups=groups, users=users)

Retrieve the user graph

Shows the relationships of users and groups.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
groups = ['groups_example'] # list[str] | Comma-separated list of groups to include.  Default is all groups. (optional)
users = ['users_example'] # list[str] | Comma-separated list of users to include.  Default is all users. (optional)

try:
    # Retrieve the user graph
    api_response = api_instance.get_user_graph(groups=groups, users=users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups** | [**list[str]**](str.md)| Comma-separated list of groups to include.  Default is all groups. | [optional] 
 **users** | [**list[str]**](str.md)| Comma-separated list of users to include.  Default is all users. | [optional] 

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

# **get_user_graph_dot**
> str get_user_graph_dot(groups=groups, users=users)

Retrieve the user graph as dot file

Shows the relationships of users and groups in dot format, for further processing.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
groups = ['groups_example'] # list[str] | Comma-separated list of groups to include.  Default is all groups. (optional)
users = ['users_example'] # list[str] | Comma-separated list of users to include.  Default is all users. (optional)

try:
    # Retrieve the user graph as dot file
    api_response = api_instance.get_user_graph_dot(groups=groups, users=users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_graph_dot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups** | [**list[str]**](str.md)| Comma-separated list of groups to include.  Default is all groups. | [optional] 
 **users** | [**list[str]**](str.md)| Comma-separated list of users to include.  Default is all users. | [optional] 

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

# **get_user_groups**
> GroupListType get_user_groups(username, allgroups=allgroups, traverse=traverse)

List all groups for a user

Retrieves a list of all the groups a user belongs to.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
allgroups = False # bool | - `true` - List all groups the user belongs to, including parent groups.  - `false` (default) - Just list the groups that the user is directly assigned to. (optional) (default to False)
traverse = False # bool | - `true` - When used in combination with `allgroups=true`, the groups' hierarchies are shown.  - `false` (default) - List the groups without hierarchical ordering. (optional) (default to False)

try:
    # List all groups for a user
    api_response = api_instance.get_user_groups(username, allgroups=allgroups, traverse=traverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **allgroups** | **bool**| - &#x60;true&#x60; - List all groups the user belongs to, including parent groups.  - &#x60;false&#x60; (default) - Just list the groups that the user is directly assigned to. | [optional] [default to False]
 **traverse** | **bool**| - &#x60;true&#x60; - When used in combination with &#x60;allgroups&#x3D;true&#x60;, the groups&#39; hierarchies are shown.  - &#x60;false&#x60; (default) - List the groups without hierarchical ordering. | [optional] [default to False]

### Return type

[**GroupListType**](GroupListType.md)

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

# **get_user_groups_and_roles**
> GroupListType get_user_groups_and_roles(username)

List all roles and groups for a user

Retrieves a list of all the groups a user belongs to, as well as all roles the user is in.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.

try:
    # List all roles and groups for a user
    api_response = api_instance.get_user_groups_and_roles(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_groups_and_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 

### Return type

[**GroupListType**](GroupListType.md)

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

# **get_user_metadata**
> SimpleMetadataType get_user_metadata(username)

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.

try:
    # Retrieve all metadata
    api_response = api_instance.get_user_metadata(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 

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

# **get_user_metadata_key**
> str get_user_metadata_key(username, keypath)

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_user_metadata_key(username, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
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

# **get_user_password_salt**
> file get_user_password_salt(username)

Retrieve the salt of a user

Retrieves the salt of the specified user.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.

try:
    # Retrieve the salt of a user
    api_response = api_instance.get_user_password_salt(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_password_salt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The salt of the user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_real_name**
> str get_user_real_name(username)

Retrieve the real name of a user

Returns the real name of a user.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.

try:
    # Retrieve the real name of a user
    api_response = api_instance.get_user_real_name(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_real_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 

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
**0** | The real name of the user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> GroupListType get_user_roles(username)

List all roles for a user

Returns a list of all the roles a user has.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.

try:
    # List all roles for a user
    api_response = api_instance.get_user_roles(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 

### Return type

[**GroupListType**](GroupListType.md)

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

# **get_users**
> UserListType get_users(first=first, name=name, number=number)

List all users

Retrieves a list of all known users.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
first = 1 # int | Start returning users from specified number. (optional) (default to 1)
name = ['name_example'] # list[str] | List of user names to return information about.  Default is all users. (optional)
number = 56 # int | Return at most specified number of users.  Default is no limit. (optional)

try:
    # List all users
    api_response = api_instance.get_users(first=first, name=name, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first** | **int**| Start returning users from specified number. | [optional] [default to 1]
 **name** | [**list[str]**](str.md)| List of user names to return information about.  Default is all users. | [optional] 
 **number** | **int**| Return at most specified number of users.  Default is no limit. | [optional] 

### Return type

[**UserListType**](UserListType.md)

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

# **get_who_am_i**
> str get_who_am_i()

Return the current user

Validates the currently used credentials and returns the calling users username.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))

try:
    # Return the current user
    api_response = api_instance.get_who_am_i()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_who_am_i: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**0** | $USERNAME |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> UserListType search_users(simple_search_type, first=first, number=number)

Search users

Simple search of fields `username`, `realname` and metadata.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
simple_search_type = vidispine.SimpleSearchType() # SimpleSearchType | 
first = 1 # int | Start returning users from specified number. (optional) (default to 1)
number = 10 # int | Return at most specified number of users. (optional) (default to 10)

try:
    # Search users
    api_response = api_instance.search_users(simple_search_type, first=first, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simple_search_type** | [**SimpleSearchType**](SimpleSearchType.md)|  | 
 **first** | **int**| Start returning users from specified number. | [optional] [default to 1]
 **number** | **int**| Return at most specified number of users. | [optional] [default to 10]

### Return type

[**UserListType**](UserListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of TabbedTuple: &lt;code&gt;username&lt;/code&gt;, &lt;code&gt;realname&lt;/code&gt;, &lt;code&gt;groups*&lt;/code&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserType update_user(username, user_type, password_type=password_type)

Update a user

Updates a user based on the information in the *UserDocument*.  The username of a user can be changed by providing a different username in the given user document.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
user_type = vidispine.UserType() # UserType | 
password_type = 'md5' # str | - `raw` - Password is in plaintext.  - `md5` (default) - Password is already hashed. (optional) (default to 'md5')

try:
    # Update a user
    api_response = api_instance.update_user(username, user_type, password_type=password_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **user_type** | [**UserType**](UserType.md)|  | 
 **password_type** | **str**| - &#x60;raw&#x60; - Password is in plaintext.  - &#x60;md5&#x60; (default) - Password is already hashed. | [optional] [default to &#39;md5&#39;]

### Return type

[**UserType**](UserType.md)

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

# **update_user_metadata**
> update_user_metadata(username, simple_metadata_type)

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_user_metadata(username, simple_metadata_type)
except ApiException as e:
    print("Exception when calling UserApi->update_user_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
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

# **update_user_metadata_key**
> update_user_metadata_key(username, keypath, body)

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_user_metadata_key(username, keypath, body)
except ApiException as e:
    print("Exception when calling UserApi->update_user_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
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

# **update_user_password**
> update_user_password(username, body, type=type)

Update the password of a user

Changes the password for a user. Hashed passwords are assumed to be represented as hexadecimal strings.  Any hashed passwords need to be salted using the salt of the user.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
body = 'body_example' # str | The new password.
type = 'md5' # str | - `raw` - Password is in plaintext.  - `md5` (default) - Password is already hashed. (optional) (default to 'md5')

try:
    # Update the password of a user
    api_instance.update_user_password(username, body, type=type)
except ApiException as e:
    print("Exception when calling UserApi->update_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **body** | **str**| The new password. | 
 **type** | **str**| - &#x60;raw&#x60; - Password is in plaintext.  - &#x60;md5&#x60; (default) - Password is already hashed. | [optional] [default to &#39;md5&#39;]

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

# **update_user_password_salt**
> file update_user_password_salt(username)

Generate a salt for a user

Generates a new salt for the user, overwriting any existing salt.  Note that this will invalidate any set password for the user and requires a new password to be set for the user to be able to login. This method is typically not relevant if passwords are updated using plaintext.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.

try:
    # Generate a salt for a user
    api_response = api_instance.update_user_password_salt(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user_password_salt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The salt of the user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_real_name**
> update_user_real_name(username, body)

Update the real name of a user

Changes the real name of a user.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
body = 'body_example' # str | The new name.

try:
    # Update the real name of a user
    api_instance.update_user_real_name(username, body)
except ApiException as e:
    print("Exception when calling UserApi->update_user_real_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **body** | **str**| The new name. | 

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

# **validate_user_password**
> str validate_user_password(username, body, type=type)

Validate the password of a user

Validates the given password against the password of the user. Hashed passwords are assumed to be represented as hexadecimal strings. Another option to validate the user credentials is to call whoami.  Any hashed passwords need to be salted using the salt of the user.

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
api_instance = vidispine.UserApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
body = 'body_example' # str | The password of the user.
type = 'md5' # str | - `raw` - Password is in plaintext.  - `md5` (default) - Password is hashed. (optional) (default to 'md5')

try:
    # Validate the password of a user
    api_response = api_instance.validate_user_password(username, body, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->validate_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **body** | **str**| The password of the user. | 
 **type** | **str**| - &#x60;raw&#x60; - Password is in plaintext.  - &#x60;md5&#x60; (default) - Password is hashed. | [optional] [default to &#39;md5&#39;]

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | \&quot;OK &amp;lt;$PASSWORD&amp;gt;\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

