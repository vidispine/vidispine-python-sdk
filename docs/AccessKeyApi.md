# vidispine.AccessKeyApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_access_key**](AccessKeyApi.md#create_user_access_key) | **POST** /user/{username}/key | Create an access key
[**delete_user_access_key**](AccessKeyApi.md#delete_user_access_key) | **DELETE** /user/{username}/key/{key-id} | Delete an access key
[**get_user_access_key**](AccessKeyApi.md#get_user_access_key) | **GET** /user/{username}/key/{key-id} | Retrieve an access key
[**get_user_access_keys**](AccessKeyApi.md#get_user_access_keys) | **GET** /user/{username}/key | List all access keys for a user
[**update_user_access_key**](AccessKeyApi.md#update_user_access_key) | **PUT** /user/{username}/key/{key-id} | Update an access key


# **create_user_access_key**
> AccessKeyType create_user_access_key(username, name=name)

Create an access key

Generates a new access key and secret for the specified user. The only time the access key secret will be available is in the response of this request.

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
api_instance = vidispine.AccessKeyApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
name = 'name_example' # str | A friendly name/description of the key. (optional)

try:
    # Create an access key
    api_response = api_instance.create_user_access_key(username, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessKeyApi->create_user_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **name** | **str**| A friendly name/description of the key. | [optional] 

### Return type

[**AccessKeyType**](AccessKeyType.md)

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

# **delete_user_access_key**
> delete_user_access_key(username, key_id)

Delete an access key

Removes the specific access key.

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
api_instance = vidispine.AccessKeyApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
key_id = 'key_id_example' # str | The key id.

try:
    # Delete an access key
    api_instance.delete_user_access_key(username, key_id)
except ApiException as e:
    print("Exception when calling AccessKeyApi->delete_user_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **key_id** | **str**| The key id. | 

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

# **get_user_access_key**
> AccessKeyType get_user_access_key(username, key_id)

Retrieve an access key

Retrieves a specific access key.

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
api_instance = vidispine.AccessKeyApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
key_id = 'key_id_example' # str | The key id.

try:
    # Retrieve an access key
    api_response = api_instance.get_user_access_key(username, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessKeyApi->get_user_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **key_id** | **str**| The key id. | 

### Return type

[**AccessKeyType**](AccessKeyType.md)

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

# **get_user_access_keys**
> AccessKeyListType get_user_access_keys(username)

List all access keys for a user

Retrieves the access keys for the specified user.

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
api_instance = vidispine.AccessKeyApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.

try:
    # List all access keys for a user
    api_response = api_instance.get_user_access_keys(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessKeyApi->get_user_access_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 

### Return type

[**AccessKeyListType**](AccessKeyListType.md)

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

# **update_user_access_key**
> AccessKeyType update_user_access_key(username, key_id, access_key_type)

Update an access key

Updates the name and/or status of a specific access key.

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
api_instance = vidispine.AccessKeyApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The username.
key_id = 'key_id_example' # str | The key id.
access_key_type = vidispine.AccessKeyType() # AccessKeyType | 

try:
    # Update an access key
    api_response = api_instance.update_user_access_key(username, key_id, access_key_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessKeyApi->update_user_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username. | 
 **key_id** | **str**| The key id. | 
 **access_key_type** | [**AccessKeyType**](AccessKeyType.md)|  | 

### Return type

[**AccessKeyType**](AccessKeyType.md)

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

