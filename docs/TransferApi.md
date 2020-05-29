# vidispine.TransferApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transfer**](TransferApi.md#get_transfer) | **GET** /transfer/{transfer-id} | Retrieve a transfer
[**get_transfers**](TransferApi.md#get_transfers) | **GET** /transfer | List all transfers
[**update_transfer_priority**](TransferApi.md#update_transfer_priority) | **PUT** /transfer/{transfer-id} | Update the priority of a transfer


# **get_transfer**
> TransferType get_transfer(transfer_id)

Retrieve a transfer

Retrieves a specific transfer.

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
api_instance = vidispine.TransferApi(vidispine.ApiClient(configuration))
transfer_id = 'transfer_id_example' # str | The transfer id.

try:
    # Retrieve a transfer
    api_response = api_instance.get_transfer(transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferApi->get_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **str**| The transfer id. | 

### Return type

[**TransferType**](TransferType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;TransferDocument&lt;/em&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfers**
> TransferListType get_transfers(state=state, first=first, number=number)

List all transfers

Returns all transfers that are in a particular state.

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
api_instance = vidispine.TransferApi(vidispine.ApiClient(configuration))
state = 'TRANSFERRING' # str | Transfer state of the transfers to retrieve. (optional) (default to 'TRANSFERRING')
first = 1 # int | The number of the first transfer to return. (optional) (default to 1)
number = 56 # int | The number of transfers to return.  Default is all transfers. (optional)

try:
    # List all transfers
    api_response = api_instance.get_transfers(state=state, first=first, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferApi->get_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Transfer state of the transfers to retrieve. | [optional] [default to &#39;TRANSFERRING&#39;]
 **first** | **int**| The number of the first transfer to return. | [optional] [default to 1]
 **number** | **int**| The number of transfers to return.  Default is all transfers. | [optional] 

### Return type

[**TransferListType**](TransferListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of transfer ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transfer_priority**
> update_transfer_priority(transfer_priority, transfer_id)

Update the priority of a transfer

Sets a new priority for a specific transfer.

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
api_instance = vidispine.TransferApi(vidispine.ApiClient(configuration))
transfer_priority = 56 # int | The desired priority.
transfer_id = 'transfer_id_example' # str | The transfer id.

try:
    # Update the priority of a transfer
    api_instance.update_transfer_priority(transfer_priority, transfer_id)
except ApiException as e:
    print("Exception when calling TransferApi->update_transfer_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_priority** | **int**| The desired priority. | 
 **transfer_id** | **str**| The transfer id. | 

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

