# vidispine.AuditLogApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_full_logs**](AuditLogApi.md#get_full_logs) | **GET** /log/export | Retrieve the entire audit log
[**get_logs**](AuditLogApi.md#get_logs) | **GET** /log | List all audit log entries


# **get_full_logs**
> AuditLogType get_full_logs(method=method, endtime=endtime, first=first, wildcard=wildcard, rows=rows, starttime=starttime, username=username, sort=sort, path=path)

Retrieve the entire audit log

Is very similar to the method above, but instead of delivering the entire document at once it is streamed. Therefore there is no restriction on the maximum number of rows that can be retrieved.

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
api_instance = vidispine.AuditLogApi(vidispine.ApiClient(configuration))
method = 'method_example' # str | Only return rows with the specified method, e. g.  `GET`.  Default is all rows. (optional)
endtime = 'endtime_example' # str | ISO 8601 time, for upper limit of rows to return. (optional)
first = 0 # int | Number of first row to return. (optional) (default to 0)
wildcard = True # bool | - `true` (default) - Treat end of path to have a `*` wildcard.  - `false` - Do truncation at end of path. (optional) (default to True)
rows = 100 # int | Number of rows to return. (optional) (default to 100)
starttime = 'starttime_example' # str | ISO 8601 time, for lower limit of rows to return. (optional)
username = 'username_example' # str | Only return rows that the specified user invoked.  Default is all rows. (optional)
sort = 'desc' # str | - `asc` - Order by timestamp ascending.  - `desc` (default) - Order by timestamp descending. (optional) (default to 'desc')
path = '/' # str | Matches path in log lines. (optional) (default to '/')

try:
    # Retrieve the entire audit log
    api_response = api_instance.get_full_logs(method=method, endtime=endtime, first=first, wildcard=wildcard, rows=rows, starttime=starttime, username=username, sort=sort, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogApi->get_full_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| Only return rows with the specified method, e. g.  &#x60;GET&#x60;.  Default is all rows. | [optional] 
 **endtime** | **str**| ISO 8601 time, for upper limit of rows to return. | [optional] 
 **first** | **int**| Number of first row to return. | [optional] [default to 0]
 **wildcard** | **bool**| - &#x60;true&#x60; (default) - Treat end of path to have a &#x60;*&#x60; wildcard.  - &#x60;false&#x60; - Do truncation at end of path. | [optional] [default to True]
 **rows** | **int**| Number of rows to return. | [optional] [default to 100]
 **starttime** | **str**| ISO 8601 time, for lower limit of rows to return. | [optional] 
 **username** | **str**| Only return rows that the specified user invoked.  Default is all rows. | [optional] 
 **sort** | **str**| - &#x60;asc&#x60; - Order by timestamp ascending.  - &#x60;desc&#x60; (default) - Order by timestamp descending. | [optional] [default to &#39;desc&#39;]
 **path** | **str**| Matches path in log lines. | [optional] [default to &#39;/&#39;]

### Return type

[**AuditLogType**](AuditLogType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> AuditLogType get_logs(method=method, endtime=endtime, first=first, wildcard=wildcard, rows=rows, starttime=starttime, perform_count=perform_count, username=username, sort=sort, path=path)

List all audit log entries

Retrieves log entries according to the specified filtering criteria. The path can be seen as having an implicit wildcard in the end, unless it is disabled with the `wildcard` parameter. For example `/item/VX-123` will match `/item/VX-123/shape` but not `/item/VX-124`.

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
api_instance = vidispine.AuditLogApi(vidispine.ApiClient(configuration))
method = 'method_example' # str | Only return rows with the specified method, e. g.  `GET`.  Default is all rows. (optional)
endtime = 'endtime_example' # str | ISO 8601 time, for upper limit of rows to return. (optional)
first = 0 # int | Number of first row to return. (optional) (default to 0)
wildcard = True # bool | - `true` (default) - Treat end of path to have a `*` wildcard.  - `false` - Do truncation at end of path. (optional) (default to True)
rows = 100 # int | Number of rows to return.  Cannot be greater than 1000. (optional) (default to 100)
starttime = 'starttime_example' # str | ISO 8601 time, for lower limit of rows to return. (optional)
perform_count = False # bool | - `true` - Return a total number of rows matching criteria (except first and count).  - `false` (default) - Do not return a total number of rows matching criteria. (optional) (default to False)
username = 'username_example' # str | Only return rows that the specified user invoked.  Default is all rows. (optional)
sort = 'desc' # str | - `asc` - Order by timestamp ascending.  - `desc` (default) - Order by timestamp descending. (optional) (default to 'desc')
path = '/' # str | Matches path in log lines. (optional) (default to '/')

try:
    # List all audit log entries
    api_response = api_instance.get_logs(method=method, endtime=endtime, first=first, wildcard=wildcard, rows=rows, starttime=starttime, perform_count=perform_count, username=username, sort=sort, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogApi->get_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| Only return rows with the specified method, e. g.  &#x60;GET&#x60;.  Default is all rows. | [optional] 
 **endtime** | **str**| ISO 8601 time, for upper limit of rows to return. | [optional] 
 **first** | **int**| Number of first row to return. | [optional] [default to 0]
 **wildcard** | **bool**| - &#x60;true&#x60; (default) - Treat end of path to have a &#x60;*&#x60; wildcard.  - &#x60;false&#x60; - Do truncation at end of path. | [optional] [default to True]
 **rows** | **int**| Number of rows to return.  Cannot be greater than 1000. | [optional] [default to 100]
 **starttime** | **str**| ISO 8601 time, for lower limit of rows to return. | [optional] 
 **perform_count** | **bool**| - &#x60;true&#x60; - Return a total number of rows matching criteria (except first and count).  - &#x60;false&#x60; (default) - Do not return a total number of rows matching criteria. | [optional] [default to False]
 **username** | **str**| Only return rows that the specified user invoked.  Default is all rows. | [optional] 
 **sort** | **str**| - &#x60;asc&#x60; - Order by timestamp ascending.  - &#x60;desc&#x60; (default) - Order by timestamp descending. | [optional] [default to &#39;desc&#39;]
 **path** | **str**| Matches path in log lines. | [optional] [default to &#39;/&#39;]

### Return type

[**AuditLogType**](AuditLogType.md)

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

