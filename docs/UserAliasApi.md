# vidispine.UserAliasApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_alias**](UserAliasApi.md#create_user_alias) | **PUT** /user/{username}/alias/{name} | Create an alias
[**delete_user_alias**](UserAliasApi.md#delete_user_alias) | **DELETE** /user/{username}/alias/{name} | Delete an alias


# **create_user_alias**
> create_user_alias(username, name)

Create an alias

Adds a new user alias for the specified user.

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
api_instance = vidispine.UserAliasApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
name = 'name_example' # str | The name.

try:
    # Create an alias
    api_instance.create_user_alias(username, name)
except ApiException as e:
    print("Exception when calling UserAliasApi->create_user_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **name** | **str**| The name. | 

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

# **delete_user_alias**
> delete_user_alias(username, name)

Delete an alias

Removes the specific user alias.

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
api_instance = vidispine.UserAliasApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
name = 'name_example' # str | The name.

try:
    # Delete an alias
    api_instance.delete_user_alias(username, name)
except ApiException as e:
    print("Exception when calling UserAliasApi->delete_user_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **name** | **str**| The name. | 

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

