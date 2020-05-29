# vidispine.EidrApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**synchronize_eidr_item**](EidrApi.md#synchronize_eidr_item) | **PUT** /item/{item-id}/eidr/sync | Synchronize EIDR metadata
[**synchronize_eidr_library**](EidrApi.md#synchronize_eidr_library) | **PUT** /library/{library-id}/eidr/sync | Synchronize EIDR metadata


# **synchronize_eidr_item**
> MetadataListType synchronize_eidr_item(item_id, force_sync=force_sync, eidr_resource=eidr_resource)

Synchronize EIDR metadata

Synchronizes `item(s)` metadata that are out of date. An item is considered out of date if the EIDR record has changed or if the included projections have changed.  Returns a list of synchronized items with the metadata that was written to the item.

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
api_instance = vidispine.EidrApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
force_sync = True # bool | - `true` - force metadata write to item.  - `false` - (default) (optional)
eidr_resource = 'eidr_resource_example' # str | If set, the resource identified by this id will be used instead of first found EIDR resource. (optional)

try:
    # Synchronize EIDR metadata
    api_response = api_instance.synchronize_eidr_item(item_id, force_sync=force_sync, eidr_resource=eidr_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EidrApi->synchronize_eidr_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **force_sync** | **bool**| - &#x60;true&#x60; - force metadata write to item.  - &#x60;false&#x60; - (default) | [optional] 
 **eidr_resource** | **str**| If set, the resource identified by this id will be used instead of first found EIDR resource. | [optional] 

### Return type

[**MetadataListType**](MetadataListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;ul&gt;&lt;li&gt;&lt;em&gt;MetadataListDocument&lt;/em&gt;&lt;/li&gt;&lt;/ul&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_eidr_library**
> MetadataListType synchronize_eidr_library(library_id, force_sync=force_sync, eidr_resource=eidr_resource)

Synchronize EIDR metadata

Synchronizes `item(s)` metadata that are out of date. An item is considered out of date if the EIDR record has changed or if the included projections have changed.  Returns a list of synchronized items with the metadata that was written to the item.

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
api_instance = vidispine.EidrApi(vidispine.ApiClient(configuration))
library_id = 'library_id_example' # str | The library id.
force_sync = True # bool | - `true` - force metadata write to item.  - `false` - (default) (optional)
eidr_resource = 'eidr_resource_example' # str | If set, the resource identified by this id will be used instead of first found EIDR resource. (optional)

try:
    # Synchronize EIDR metadata
    api_response = api_instance.synchronize_eidr_library(library_id, force_sync=force_sync, eidr_resource=eidr_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EidrApi->synchronize_eidr_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**| The library id. | 
 **force_sync** | **bool**| - &#x60;true&#x60; - force metadata write to item.  - &#x60;false&#x60; - (default) | [optional] 
 **eidr_resource** | **str**| If set, the resource identified by this id will be used instead of first found EIDR resource. | [optional] 

### Return type

[**MetadataListType**](MetadataListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;ul&gt;&lt;li&gt;&lt;em&gt;MetadataListDocument&lt;/em&gt;&lt;/li&gt;&lt;/ul&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

