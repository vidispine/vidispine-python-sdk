# vidispine.LoudnessApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_interval_loudness**](LoudnessApi.md#get_item_interval_loudness) | **PUT** /item/{item-id}/loudness | Get loudness values for interval
[**get_item_loudness**](LoudnessApi.md#get_item_loudness) | **GET** /item/{item-id}/loudness | Get loudness values


# **get_item_interval_loudness**
> LoudnessType get_item_interval_loudness(item_id, loudness_type)

Get loudness values for interval

Extracts loudness information from bulky metadata. Start and end range can be specified, as well as custom mixing.

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
api_instance = vidispine.LoudnessApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
loudness_type = vidispine.LoudnessType() # LoudnessType | 

try:
    # Get loudness values for interval
    api_response = api_instance.get_item_interval_loudness(item_id, loudness_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoudnessApi->get_item_interval_loudness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **loudness_type** | [**LoudnessType**](LoudnessType.md)|  | 

### Return type

[**LoudnessType**](LoudnessType.md)

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

# **get_item_loudness**
> LoudnessType get_item_loudness(item_id)

Get loudness values

Extracts loudness information from bulky metadata.

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
api_instance = vidispine.LoudnessApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.

try:
    # Get loudness values
    api_response = api_instance.get_item_loudness(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoudnessApi->get_item_loudness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 

### Return type

[**LoudnessType**](LoudnessType.md)

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

