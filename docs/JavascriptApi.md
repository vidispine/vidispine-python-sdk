# vidispine.JavascriptApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_java_script_session**](JavascriptApi.md#delete_java_script_session) | **DELETE** /javascript/session/{id} | Stop a JavaScript session
[**execute_java_script**](JavascriptApi.md#execute_java_script) | **POST** /javascript/test | Execute JavaScript
[**get_java_script_session**](JavascriptApi.md#get_java_script_session) | **GET** /javascript/session/{id} | Retrieve a JavaScript session
[**get_java_script_sessions**](JavascriptApi.md#get_java_script_sessions) | **GET** /javascript/session | List all JavaScript sessions


# **delete_java_script_session**
> delete_java_script_session(id, stop=stop)

Stop a JavaScript session

Stops an active debugging session.

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
api_instance = vidispine.JavascriptApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
stop = False # bool | - `true` - Kill the running script.  - `false` (default) - Stop the debugging session, and leave the script running. (optional) (default to False)

try:
    # Stop a JavaScript session
    api_instance.delete_java_script_session(id, stop=stop)
except ApiException as e:
    print("Exception when calling JavascriptApi->delete_java_script_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **stop** | **bool**| - &#x60;true&#x60; - Kill the running script.  - &#x60;false&#x60; (default) - Stop the debugging session, and leave the script running. | [optional] [default to False]

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

# **execute_java_script**
> str execute_java_script(body)

Execute JavaScript

Executes the given JavaScript code.

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
api_instance = vidispine.JavascriptApi(vidispine.ApiClient(configuration))
body = 'body_example' # str | The JavaScript code

try:
    # Execute JavaScript
    api_response = api_instance.execute_java_script(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JavascriptApi->execute_java_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| The JavaScript code | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/javascript, text/javascript, text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The object returned by the code, in JSON format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_java_script_session**
> str get_java_script_session(id)

Retrieve a JavaScript session

Retrieves stack trace of a specific JavaScript session.

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
api_instance = vidispine.JavascriptApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # Retrieve a JavaScript session
    api_response = api_instance.get_java_script_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JavascriptApi->get_java_script_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

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
**0** | The stack trace of the session |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_java_script_sessions**
> str get_java_script_sessions()

List all JavaScript sessions

Retrieves the the current JavaScript sessions, their current status, and which port they listen to.

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
api_instance = vidispine.JavascriptApi(vidispine.ApiClient(configuration))

try:
    # List all JavaScript sessions
    api_response = api_instance.get_java_script_sessions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JavascriptApi->get_java_script_sessions: %s\n" % e)
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
**0** | A textual list of the current JavaScript sessions in Vidispine, their current status, and which port they listen to |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

