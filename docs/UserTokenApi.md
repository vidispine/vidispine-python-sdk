# vidispine.UserTokenApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth_token**](UserTokenApi.md#get_auth_token) | **GET** /token | Retrieve an authentication token
[**get_user_auth_token**](UserTokenApi.md#get_user_auth_token) | **GET** /user/{username}/token | Retrieve an authentication token for a specific user


# **get_auth_token**
> AuthenticationTokenType get_auth_token(auto_refresh=auto_refresh, seconds=seconds)

Retrieve an authentication token

Creates a authentication token for the calling user. This token can be used for calling the API without specifying username or password.  Useful when users authenticate using an alias and the actual username of the user is not known.

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
api_instance = vidispine.UserTokenApi(vidispine.ApiClient(configuration))
auto_refresh = False # bool | - `true` - The expiration clock is reset with every API call.  - `false` (default) - The token always expires after `seconds` seconds after the token was created. (optional) (default to False)
seconds = 56 # int | The duration of the token. (optional)

try:
    # Retrieve an authentication token
    api_response = api_instance.get_auth_token(auto_refresh=auto_refresh, seconds=seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTokenApi->get_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_refresh** | **bool**| - &#x60;true&#x60; - The expiration clock is reset with every API call.  - &#x60;false&#x60; (default) - The token always expires after &#x60;seconds&#x60; seconds after the token was created. | [optional] [default to False]
 **seconds** | **int**| The duration of the token. | [optional] 

### Return type

[**AuthenticationTokenType**](AuthenticationTokenType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The generated token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_auth_token**
> str get_user_auth_token(username, auto_refresh=auto_refresh, seconds=seconds)

Retrieve an authentication token for a specific user

Creates a authentication token for a user. This token can be used for calling the API without specifying username or password.  The username path parameter must match the calling user's credentials, unless the calling user has `_administrator` role.

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
api_instance = vidispine.UserTokenApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
auto_refresh = False # bool | - `true` - The expiration clock is reset with every API call.  - `false` (default) - The token always expires after `seconds` seconds after the token was created. (optional) (default to False)
seconds = 56 # int | The duration of the token. (optional)

try:
    # Retrieve an authentication token for a specific user
    api_response = api_instance.get_user_auth_token(username, auto_refresh=auto_refresh, seconds=seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTokenApi->get_user_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **auto_refresh** | **bool**| - &#x60;true&#x60; - The expiration clock is reset with every API call.  - &#x60;false&#x60; (default) - The token always expires after &#x60;seconds&#x60; seconds after the token was created. | [optional] [default to False]
 **seconds** | **int**| The duration of the token. | [optional] 

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
**0** | The generated token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

