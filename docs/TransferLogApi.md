# vidispine.TransferLogApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transfer_log**](TransferLogApi.md#get_transfer_log) | **GET** /log/transfer-log | List all transfer log entries


# **get_transfer_log**
> TransferLogListType get_transfer_log(shape=shape, method=method, endtime=endtime, storage=storage, first=first, uri=uri, file=file, rows=rows, item=item, starttime=starttime, status=status, perform_count=perform_count, job=job)

List all transfer log entries

Retrieves log entries according to the specified filtering criteria. Note that the transfer log table does not have a lot of indices, so the extraction of data can be slow. Do not use this method other than for troubleshooting.

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
api_instance = vidispine.TransferLogApi(vidispine.ApiClient(configuration))
shape = 'shape_example' # str | Site id, only return transfers where source or destination shape matches.  Default is all rows.  Note that not all transfers contains information about shapes. (optional)
method = ['method_example'] # list[str] | Comma-separated list Only return transfers where method matches. (optional)
endtime = 'endtime_example' # str | ISO 8601 time, for upper limit of rows to return. (optional)
storage = 'storage_example' # str | Site id, only return transfers where source or destination storage matches.  Default is all rows.  Note that not all transfers contains information about storages. (optional)
first = 0 # int | Number of first row to return. (optional) (default to 0)
uri = 'uri_example' # str | URI, only return transfers where source or destination URI matches.  Default is all rows.  A star (`*`) in the URI represents a wildcard. (optional)
file = 'file_example' # str | Site id, only return transfers where source or destination file matches.  Default is all rows.  Note that not all transfers contains information about files. (optional)
rows = 100 # int | Number of rows to return.  Cannot be greater than 1000. (optional) (default to 100)
item = 'item_example' # str | Site id, only return transfers where source or destination item matches.  Default is all rows.  Note that not all transfers contains information about items. (optional)
starttime = 'starttime_example' # str | ISO 8601 time, for lower limit of rows to return. (optional)
status = ['status_example'] # list[str] | Comma-separated list.  Only return transfers where status matches. (optional)
perform_count = False # bool | - `true` - Return a total number of rows matching criteria (except first and count).  - `false` (default) - Do not return a total number of rows matching criteria. (optional) (default to False)
job = 'job_example' # str | Site id, only return transfers where job matches.  Default is all rows.  Note that not all transfers contains information about jobs. (optional)

try:
    # List all transfer log entries
    api_response = api_instance.get_transfer_log(shape=shape, method=method, endtime=endtime, storage=storage, first=first, uri=uri, file=file, rows=rows, item=item, starttime=starttime, status=status, perform_count=perform_count, job=job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferLogApi->get_transfer_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shape** | **str**| Site id, only return transfers where source or destination shape matches.  Default is all rows.  Note that not all transfers contains information about shapes. | [optional] 
 **method** | [**list[str]**](str.md)| Comma-separated list Only return transfers where method matches. | [optional] 
 **endtime** | **str**| ISO 8601 time, for upper limit of rows to return. | [optional] 
 **storage** | **str**| Site id, only return transfers where source or destination storage matches.  Default is all rows.  Note that not all transfers contains information about storages. | [optional] 
 **first** | **int**| Number of first row to return. | [optional] [default to 0]
 **uri** | **str**| URI, only return transfers where source or destination URI matches.  Default is all rows.  A star (&#x60;*&#x60;) in the URI represents a wildcard. | [optional] 
 **file** | **str**| Site id, only return transfers where source or destination file matches.  Default is all rows.  Note that not all transfers contains information about files. | [optional] 
 **rows** | **int**| Number of rows to return.  Cannot be greater than 1000. | [optional] [default to 100]
 **item** | **str**| Site id, only return transfers where source or destination item matches.  Default is all rows.  Note that not all transfers contains information about items. | [optional] 
 **starttime** | **str**| ISO 8601 time, for lower limit of rows to return. | [optional] 
 **status** | [**list[str]**](str.md)| Comma-separated list.  Only return transfers where status matches. | [optional] 
 **perform_count** | **bool**| - &#x60;true&#x60; - Return a total number of rows matching criteria (except first and count).  - &#x60;false&#x60; (default) - Do not return a total number of rows matching criteria. | [optional] [default to False]
 **job** | **str**| Site id, only return transfers where job matches.  Default is all rows.  Note that not all transfers contains information about jobs. | [optional] 

### Return type

[**TransferLogListType**](TransferLogListType.md)

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

