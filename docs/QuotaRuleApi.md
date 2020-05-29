# vidispine.QuotaRuleApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quota_rule**](QuotaRuleApi.md#create_quota_rule) | **POST** /quota/ | Create a quota rule
[**delete_quota_rule**](QuotaRuleApi.md#delete_quota_rule) | **DELETE** /quota/{rule-id} | Delete a quota rule
[**evaluate_quota_rule**](QuotaRuleApi.md#evaluate_quota_rule) | **PUT** /quota/{rule-id}/evaluate | Evaluate a quota rule
[**get_quota_rule**](QuotaRuleApi.md#get_quota_rule) | **GET** /quota/{rule-id} | Retrieve a quota rule
[**get_quota_rules**](QuotaRuleApi.md#get_quota_rules) | **GET** /quota/ | List all quota rules


# **create_quota_rule**
> QuotaRuleType create_quota_rule(quota_rule_type)

Create a quota rule

Creates a quota rule with the filters and resource limits as specified in the quota rule document.

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
api_instance = vidispine.QuotaRuleApi(vidispine.ApiClient(configuration))
quota_rule_type = vidispine.QuotaRuleType() # QuotaRuleType | 

try:
    # Create a quota rule
    api_response = api_instance.create_quota_rule(quota_rule_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaRuleApi->create_quota_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_rule_type** | [**QuotaRuleType**](QuotaRuleType.md)|  | 

### Return type

[**QuotaRuleType**](QuotaRuleType.md)

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

# **delete_quota_rule**
> delete_quota_rule(rule_id)

Delete a quota rule

Deletes the quota rule.

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
api_instance = vidispine.QuotaRuleApi(vidispine.ApiClient(configuration))
rule_id = 'rule_id_example' # str | The rule id.

try:
    # Delete a quota rule
    api_instance.delete_quota_rule(rule_id)
except ApiException as e:
    print("Exception when calling QuotaRuleApi->delete_quota_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The rule id. | 

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

# **evaluate_quota_rule**
> evaluate_quota_rule(rule_id)

Evaluate a quota rule

Immediately calculates the resource usage as defined by a quota rule.

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
api_instance = vidispine.QuotaRuleApi(vidispine.ApiClient(configuration))
rule_id = 'rule_id_example' # str | The rule id.

try:
    # Evaluate a quota rule
    api_instance.evaluate_quota_rule(rule_id)
except ApiException as e:
    print("Exception when calling QuotaRuleApi->evaluate_quota_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The rule id. | 

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

# **get_quota_rule**
> QuotaRuleType get_quota_rule(rule_id)

Retrieve a quota rule

Retrieves a specific quota rule.

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
api_instance = vidispine.QuotaRuleApi(vidispine.ApiClient(configuration))
rule_id = 'rule_id_example' # str | The rule id.

try:
    # Retrieve a quota rule
    api_response = api_instance.get_quota_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaRuleApi->get_quota_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The rule id. | 

### Return type

[**QuotaRuleType**](QuotaRuleType.md)

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

# **get_quota_rules**
> QuotaRuleListType get_quota_rules(content=content, exceeded=exceeded, filter=filter)

List all quota rules

Returns the quota rules that exist in the system.

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
api_instance = vidispine.QuotaRuleApi(vidispine.ApiClient(configuration))
content = ['content_example'] # list[str] | Comma-separated list of addition content to retrieve. (optional)
exceeded = False # bool | - `true` - Returns only rules where the usage of a resource exceeds the limit that has been specified for a rule.  - `false` (default) - Returns rules regardless of the current resource usage. (optional) (default to False)
filter = ['filter_example'] # list[str] | Comma-separated list of key-value pairs (in the format key=value) that can be used to filter the result set.  Valid key values are: `user`, `group`, `storage`, `storageGroup`, `collection`, `library` and `tag`. (optional)

try:
    # List all quota rules
    api_response = api_instance.get_quota_rules(content=content, exceeded=exceeded, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaRuleApi->get_quota_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | [**list[str]**](str.md)| Comma-separated list of addition content to retrieve. | [optional] 
 **exceeded** | **bool**| - &#x60;true&#x60; - Returns only rules where the usage of a resource exceeds the limit that has been specified for a rule.  - &#x60;false&#x60; (default) - Returns rules regardless of the current resource usage. | [optional] [default to False]
 **filter** | [**list[str]**](str.md)| Comma-separated list of key-value pairs (in the format key&#x3D;value) that can be used to filter the result set.  Valid key values are: &#x60;user&#x60;, &#x60;group&#x60;, &#x60;storage&#x60;, &#x60;storageGroup&#x60;, &#x60;collection&#x60;, &#x60;library&#x60; and &#x60;tag&#x60;. | [optional] 

### Return type

[**QuotaRuleListType**](QuotaRuleListType.md)

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

