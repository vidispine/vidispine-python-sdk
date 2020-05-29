# vidispine.AutoProjectionApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_projection_rule**](AutoProjectionApi.md#create_auto_projection_rule) | **PUT** /auto-projection/{name} | Create an automatic projection rule
[**delete_auto_projection_rule**](AutoProjectionApi.md#delete_auto_projection_rule) | **DELETE** /auto-projection/{name} | Delete an automatic projection rule
[**disable_auto_projection_rule**](AutoProjectionApi.md#disable_auto_projection_rule) | **PUT** /auto-projection/{name}/disable | Disable an automatic projection rule
[**enable_auto_projection_rule**](AutoProjectionApi.md#enable_auto_projection_rule) | **PUT** /auto-projection/{name}/enable | Enable an automatic projection rule
[**get_auto_projection_rule**](AutoProjectionApi.md#get_auto_projection_rule) | **GET** /auto-projection/{name} | Retrieve an automatic projection rule
[**get_auto_projection_rules**](AutoProjectionApi.md#get_auto_projection_rules) | **GET** /auto-projection | List all automatic projection rules
[**get_disabled_auto_projection_rules**](AutoProjectionApi.md#get_disabled_auto_projection_rules) | **GET** /auto-projection/disable | List all disabled automatic projection rules
[**get_enabled_auto_projection_rules**](AutoProjectionApi.md#get_enabled_auto_projection_rules) | **GET** /auto-projection/enable | List all enabled automatic projection rules


# **create_auto_projection_rule**
> create_auto_projection_rule(name, auto_projection_rule_type)

Create an automatic projection rule

Creates a new projection rule based on the information in the *AutoProjectionRuleDocument*.

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
api_instance = vidispine.AutoProjectionApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.
auto_projection_rule_type = vidispine.AutoProjectionRuleType() # AutoProjectionRuleType | 

try:
    # Create an automatic projection rule
    api_instance.create_auto_projection_rule(name, auto_projection_rule_type)
except ApiException as e:
    print("Exception when calling AutoProjectionApi->create_auto_projection_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name. | 
 **auto_projection_rule_type** | [**AutoProjectionRuleType**](AutoProjectionRuleType.md)|  | 

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

# **delete_auto_projection_rule**
> delete_auto_projection_rule(name)

Delete an automatic projection rule

Deletes the automatic projection rule.

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
api_instance = vidispine.AutoProjectionApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.

try:
    # Delete an automatic projection rule
    api_instance.delete_auto_projection_rule(name)
except ApiException as e:
    print("Exception when calling AutoProjectionApi->delete_auto_projection_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **disable_auto_projection_rule**
> disable_auto_projection_rule(name)

Disable an automatic projection rule

Disables the automatic projection rule.

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
api_instance = vidispine.AutoProjectionApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.

try:
    # Disable an automatic projection rule
    api_instance.disable_auto_projection_rule(name)
except ApiException as e:
    print("Exception when calling AutoProjectionApi->disable_auto_projection_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **enable_auto_projection_rule**
> enable_auto_projection_rule(name)

Enable an automatic projection rule

Enables the automatic projection rule.

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
api_instance = vidispine.AutoProjectionApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.

try:
    # Enable an automatic projection rule
    api_instance.enable_auto_projection_rule(name)
except ApiException as e:
    print("Exception when calling AutoProjectionApi->enable_auto_projection_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_auto_projection_rule**
> AutoProjectionRuleType get_auto_projection_rule(name)

Retrieve an automatic projection rule

Retrieves a specific projection rule.

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
api_instance = vidispine.AutoProjectionApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.

try:
    # Retrieve an automatic projection rule
    api_response = api_instance.get_auto_projection_rule(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoProjectionApi->get_auto_projection_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name. | 

### Return type

[**AutoProjectionRuleType**](AutoProjectionRuleType.md)

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

# **get_auto_projection_rules**
> URIListType get_auto_projection_rules()

List all automatic projection rules

Retrieves all automatic projection rules.

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
api_instance = vidispine.AutoProjectionApi(vidispine.ApiClient(configuration))

try:
    # List all automatic projection rules
    api_response = api_instance.get_auto_projection_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoProjectionApi->get_auto_projection_rules: %s\n" % e)
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
**0** | CRLF-delimited list of names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disabled_auto_projection_rules**
> URIListType get_disabled_auto_projection_rules()

List all disabled automatic projection rules

Retrieves all disabled automatic projection rules.

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
api_instance = vidispine.AutoProjectionApi(vidispine.ApiClient(configuration))

try:
    # List all disabled automatic projection rules
    api_response = api_instance.get_disabled_auto_projection_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoProjectionApi->get_disabled_auto_projection_rules: %s\n" % e)
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
**0** | CRLF-delimited list of names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enabled_auto_projection_rules**
> URIListType get_enabled_auto_projection_rules()

List all enabled automatic projection rules

Retrieves all enabled automatic projection rules.

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
api_instance = vidispine.AutoProjectionApi(vidispine.ApiClient(configuration))

try:
    # List all enabled automatic projection rules
    api_response = api_instance.get_enabled_auto_projection_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoProjectionApi->get_enabled_auto_projection_rules: %s\n" % e)
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
**0** | CRLF-delimited list of names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

