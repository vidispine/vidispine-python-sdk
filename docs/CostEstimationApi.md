# vidispine.CostEstimationApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cost_estimate**](CostEstimationApi.md#create_cost_estimate) | **POST** /cost/{path} | Request a cost estimate
[**get_cost_estimate**](CostEstimationApi.md#get_cost_estimate) | **GET** /cost/estimate/{id} | Retrieve the cost estimate results


# **create_cost_estimate**
> CostEstimateType create_cost_estimate(path)

Request a cost estimate

Requests a cost estimate for performing a specific operation.  The same query parameters and request body as used by the target request should be specified in the cost estimate request.  No additional roles or permissions are required to request a cost estimate. If a user has permission to for example transcode an item, then that user may also request a cost estimate for that operation.

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
api_instance = vidispine.CostEstimationApi(vidispine.ApiClient(configuration))
path = 'path_example' # str | The path.

try:
    # Request a cost estimate
    api_response = api_instance.create_cost_estimate(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostEstimationApi->create_cost_estimate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path. | 

### Return type

[**CostEstimateType**](CostEstimateType.md)

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

# **get_cost_estimate**
> CostEstimateType get_cost_estimate(id)

Retrieve the cost estimate results

Retrieves the cost estimate.

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
api_instance = vidispine.CostEstimationApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # Retrieve the cost estimate results
    api_response = api_instance.get_cost_estimate(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CostEstimationApi->get_cost_estimate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

### Return type

[**CostEstimateType**](CostEstimateType.md)

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

