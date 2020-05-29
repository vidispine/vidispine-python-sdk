# vidispine.AutoImportApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_auto_import_rule**](AutoImportApi.md#create_or_update_auto_import_rule) | **PUT** /storage/{storage-id}/auto-import/ | Set an auto-import rule
[**delete_auto_import_rule**](AutoImportApi.md#delete_auto_import_rule) | **DELETE** /storage/{storage-id}/auto-import/ | Delete an auto-import rule
[**disable_auto_import_rule**](AutoImportApi.md#disable_auto_import_rule) | **PUT** /storage/{storage-id}/auto-import/disable | Disable an auto-import rule
[**enable_auto_import_rule**](AutoImportApi.md#enable_auto_import_rule) | **PUT** /storage/{storage-id}/auto-import/enable | Enable an auto-import rule
[**get_auto_import_rule**](AutoImportApi.md#get_auto_import_rule) | **GET** /storage/{storage-id}/auto-import/ | Retrieve an auto-import rule
[**get_auto_import_rules**](AutoImportApi.md#get_auto_import_rules) | **GET** /storage/auto-import/ | Retrieve all auto-import rules


# **create_or_update_auto_import_rule**
> create_or_update_auto_import_rule(storage_id, auto_import_rule_type)

Set an auto-import rule

Sets the auto-import rule for the specified storage.

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
api_instance = vidispine.AutoImportApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
auto_import_rule_type = vidispine.AutoImportRuleType() # AutoImportRuleType | 

try:
    # Set an auto-import rule
    api_instance.create_or_update_auto_import_rule(storage_id, auto_import_rule_type)
except ApiException as e:
    print("Exception when calling AutoImportApi->create_or_update_auto_import_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **auto_import_rule_type** | [**AutoImportRuleType**](AutoImportRuleType.md)|  | 

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

# **delete_auto_import_rule**
> delete_auto_import_rule(storage_id)

Delete an auto-import rule

Removes any auto-import rule that might exist on the storage.

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
api_instance = vidispine.AutoImportApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Delete an auto-import rule
    api_instance.delete_auto_import_rule(storage_id)
except ApiException as e:
    print("Exception when calling AutoImportApi->delete_auto_import_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 

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

# **disable_auto_import_rule**
> disable_auto_import_rule(storage_id)

Disable an auto-import rule

Stops auto-import jobs from being created for new files on this storage.

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
api_instance = vidispine.AutoImportApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Disable an auto-import rule
    api_instance.disable_auto_import_rule(storage_id)
except ApiException as e:
    print("Exception when calling AutoImportApi->disable_auto_import_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 

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

# **enable_auto_import_rule**
> enable_auto_import_rule(storage_id)

Enable an auto-import rule

Resumes creation of auto-import jobs for files on this storage.

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
api_instance = vidispine.AutoImportApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Enable an auto-import rule
    api_instance.enable_auto_import_rule(storage_id)
except ApiException as e:
    print("Exception when calling AutoImportApi->enable_auto_import_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 

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

# **get_auto_import_rule**
> AutoImportRuleType get_auto_import_rule(storage_id)

Retrieve an auto-import rule

Returns the auto-import rule for a storage if there is one.

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
api_instance = vidispine.AutoImportApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.

try:
    # Retrieve an auto-import rule
    api_response = api_instance.get_auto_import_rule(storage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoImportApi->get_auto_import_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 

### Return type

[**AutoImportRuleType**](AutoImportRuleType.md)

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

# **get_auto_import_rules**
> AutoImportRuleListType get_auto_import_rules()

Retrieve all auto-import rules

Returns all known auto-import rules.

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
api_instance = vidispine.AutoImportApi(vidispine.ApiClient(configuration))

try:
    # Retrieve all auto-import rules
    api_response = api_instance.get_auto_import_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoImportApi->get_auto_import_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AutoImportRuleListType**](AutoImportRuleListType.md)

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

