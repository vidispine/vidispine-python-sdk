# vidispine.SelftestApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_self_test**](SelftestApi.md#execute_self_test) | **GET** /selftest/{test-name} | Execute a self test
[**execute_self_tests**](SelftestApi.md#execute_self_tests) | **GET** /selftest | Execute all self tests


# **execute_self_test**
> SelfTestType execute_self_test(test_name)

Execute a self test

Executes the test with the specified name.

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
api_instance = vidispine.SelftestApi(vidispine.ApiClient(configuration))
test_name = 'test_name_example' # str | The test name.

try:
    # Execute a self test
    api_response = api_instance.execute_self_test(test_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelftestApi->execute_self_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_name** | **str**| The test name. | 

### Return type

[**SelfTestType**](SelfTestType.md)

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

# **execute_self_tests**
> SelfTestType execute_self_tests(exclude=exclude)

Execute all self tests

Executes all the self tests.

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
api_instance = vidispine.SelftestApi(vidispine.ApiClient(configuration))
exclude = ['exclude_example'] # list[str] | Comma-separated list of test names to exclude. (optional)

try:
    # Execute all self tests
    api_response = api_instance.execute_self_tests(exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelftestApi->execute_self_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude** | [**list[str]**](str.md)| Comma-separated list of test names to exclude. | [optional] 

### Return type

[**SelfTestType**](SelfTestType.md)

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

