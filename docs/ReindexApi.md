# vidispine.ReindexApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reindex_status**](ReindexApi.md#get_reindex_status) | **GET** /reindex/{index} | Retrieve reindex status
[**reindex**](ReindexApi.md#reindex) | **PUT** /reindex/{index} | Request a reindex


# **get_reindex_status**
> ReindexRequestType get_reindex_status(index)

Retrieve reindex status

Gets information about a reindex process, i.e., progress and whether it is finished.

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
api_instance = vidispine.ReindexApi(vidispine.ApiClient(configuration))
index = 'index_example' # str | The index.

try:
    # Retrieve reindex status
    api_response = api_instance.get_reindex_status(index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReindexApi->get_reindex_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| The index. | 

### Return type

[**ReindexRequestType**](ReindexRequestType.md)

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

# **reindex**
> ReindexRequestType reindex(index, status=status, priority=priority)

Request a reindex

Starts a reindex. If a reindex of the same type is already in progress, it is restarted.  The types than can be reindexed are: item, collection, ACL, file, thumbnail and document.

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
api_instance = vidispine.ReindexApi(vidispine.ApiClient(configuration))
index = 'index_example' # str | The index to rebuild.
status = 'IN_QUEUE' # str | If current status is `FINISHED` or `ABORTED` then `PAUSED`, `ABORTED` and `IN_PROGRESS` are no-ops.   - `IN_QUEUE` (default) - To start or restart reindex.  - `PAUSED` - To pause reindex.  - `ABORTED` - To cancel reindex.  - `IN_PROGRESS`/`IN PROGRESS` - To resume a paused reindex. (optional) (default to 'IN_QUEUE')
priority = 500 # int | The priority of this reindex request compare to other request.  Requests with a larger/higher priority will be processed first. (optional) (default to 500)

try:
    # Request a reindex
    api_response = api_instance.reindex(index, status=status, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReindexApi->reindex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| The index to rebuild. | 
 **status** | **str**| If current status is &#x60;FINISHED&#x60; or &#x60;ABORTED&#x60; then &#x60;PAUSED&#x60;, &#x60;ABORTED&#x60; and &#x60;IN_PROGRESS&#x60; are no-ops.   - &#x60;IN_QUEUE&#x60; (default) - To start or restart reindex.  - &#x60;PAUSED&#x60; - To pause reindex.  - &#x60;ABORTED&#x60; - To cancel reindex.  - &#x60;IN_PROGRESS&#x60;/&#x60;IN PROGRESS&#x60; - To resume a paused reindex. | [optional] [default to &#39;IN_QUEUE&#39;]
 **priority** | **int**| The priority of this reindex request compare to other request.  Requests with a larger/higher priority will be processed first. | [optional] [default to 500]

### Return type

[**ReindexRequestType**](ReindexRequestType.md)

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

