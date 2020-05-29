# vidispine.AutocompleteApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](AutocompleteApi.md#autocomplete) | **PUT** /search/autocomplete | Autocomplete text


# **autocomplete**
> AutocompleteResponseType autocomplete(autocomplete_request_type)

Autocomplete text

Requests suggestion matching text in all or a specific metadata field.

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
api_instance = vidispine.AutocompleteApi(vidispine.ApiClient(configuration))
autocomplete_request_type = vidispine.AutocompleteRequestType() # AutocompleteRequestType | 

try:
    # Autocomplete text
    api_response = api_instance.autocomplete(autocomplete_request_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutocompleteApi->autocomplete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autocomplete_request_type** | [**AutocompleteRequestType**](AutocompleteRequestType.md)|  | 

### Return type

[**AutocompleteResponseType**](AutocompleteResponseType.md)

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

