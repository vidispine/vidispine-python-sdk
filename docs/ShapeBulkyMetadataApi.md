# vidispine.ShapeBulkyMetadataApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_shape_bulky_metadata**](ShapeBulkyMetadataApi.md#add_item_shape_bulky_metadata) | **PUT** /item/{item-id}/shape/{shape-id}/metadata/bulky/ | Insert values in bulk
[**delete_item_shape_bulky_metadata_key**](ShapeBulkyMetadataApi.md#delete_item_shape_bulky_metadata_key) | **DELETE** /item/{item-id}/shape/{shape-id}/metadata/bulky/{key} | Remove values
[**delete_item_shape_bulky_metadata_keys**](ShapeBulkyMetadataApi.md#delete_item_shape_bulky_metadata_keys) | **DELETE** /item/{item-id}/shape/{shape-id}/metadata/bulky/ | Delete all keys used in the bulky metadata
[**get_item_shape_bulky_metadata_key**](ShapeBulkyMetadataApi.md#get_item_shape_bulky_metadata_key) | **GET** /item/{item-id}/shape/{shape-id}/metadata/bulky/{key} | Read values
[**get_item_shape_bulky_metadata_keys**](ShapeBulkyMetadataApi.md#get_item_shape_bulky_metadata_keys) | **GET** /item/{item-id}/shape/{shape-id}/metadata/bulky/ | Retrieve all keys used in the bulky metadata
[**update_item_shape_bulky_metadata_key**](ShapeBulkyMetadataApi.md#update_item_shape_bulky_metadata_key) | **PUT** /item/{item-id}/shape/{shape-id}/metadata/bulky/{key} | Insert values


# **add_item_shape_bulky_metadata**
> add_item_shape_bulky_metadata(item_id, shape_id, bulky_metadata_type)

Insert values in bulk

Inserts all key-value pairs from a given document.

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
api_instance = vidispine.ShapeBulkyMetadataApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
bulky_metadata_type = vidispine.BulkyMetadataType() # BulkyMetadataType | 

try:
    # Insert values in bulk
    api_instance.add_item_shape_bulky_metadata(item_id, shape_id, bulky_metadata_type)
except ApiException as e:
    print("Exception when calling ShapeBulkyMetadataApi->add_item_shape_bulky_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **bulky_metadata_type** | [**BulkyMetadataType**](BulkyMetadataType.md)|  | 

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

# **delete_item_shape_bulky_metadata_key**
> delete_item_shape_bulky_metadata_key(item_id, shape_id, key, end=end, start=start)

Remove values

Removes all the values for a certain key over the specified interval.

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
api_instance = vidispine.ShapeBulkyMetadataApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
key = 'key_example' # str | The key.
end = 'end_example' # str | A time code that defines the end of the interval. (optional)
start = 'start_example' # str | A time code that defines the start of the interval. (optional)

try:
    # Remove values
    api_instance.delete_item_shape_bulky_metadata_key(item_id, shape_id, key, end=end, start=start)
except ApiException as e:
    print("Exception when calling ShapeBulkyMetadataApi->delete_item_shape_bulky_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **key** | **str**| The key. | 
 **end** | **str**| A time code that defines the end of the interval. | [optional] 
 **start** | **str**| A time code that defines the start of the interval. | [optional] 

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

# **delete_item_shape_bulky_metadata_keys**
> delete_item_shape_bulky_metadata_keys(item_id, shape_id)

Delete all keys used in the bulky metadata

Removes all the keys in the bulky metadata.

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
api_instance = vidispine.ShapeBulkyMetadataApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # Delete all keys used in the bulky metadata
    api_instance.delete_item_shape_bulky_metadata_keys(item_id, shape_id)
except ApiException as e:
    print("Exception when calling ShapeBulkyMetadataApi->delete_item_shape_bulky_metadata_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 

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

# **get_item_shape_bulky_metadata_key**
> BulkyMetadataType get_item_shape_bulky_metadata_key(item_id, shape_id, key, end=end, start=start)

Read values

Retrieves all values of a certain key over a specified interval. All values for that key can be retrieved by specifying start as \"-INF\" and end as \"+INF\".

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
api_instance = vidispine.ShapeBulkyMetadataApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
key = 'key_example' # str | The key.
end = 'end_example' # str | A time code that defines the end of the interval. (optional)
start = 'start_example' # str | A time code that defines the start of the interval. (optional)

try:
    # Read values
    api_response = api_instance.get_item_shape_bulky_metadata_key(item_id, shape_id, key, end=end, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeBulkyMetadataApi->get_item_shape_bulky_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **key** | **str**| The key. | 
 **end** | **str**| A time code that defines the end of the interval. | [optional] 
 **start** | **str**| A time code that defines the start of the interval. | [optional] 

### Return type

[**BulkyMetadataType**](BulkyMetadataType.md)

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

# **get_item_shape_bulky_metadata_keys**
> URIListType get_item_shape_bulky_metadata_keys(item_id, shape_id)

Retrieve all keys used in the bulky metadata

Retrieves a list of all keys in the bulky metadata.

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
api_instance = vidispine.ShapeBulkyMetadataApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # Retrieve all keys used in the bulky metadata
    api_response = api_instance.get_item_shape_bulky_metadata_keys(item_id, shape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeBulkyMetadataApi->get_item_shape_bulky_metadata_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 

### Return type

[**URIListType**](URIListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of keys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_shape_bulky_metadata_key**
> update_item_shape_bulky_metadata_key(item_id, shape_id, key, body, item_track=item_track, end=end, channel=channel, stream=stream, start=start)

Insert values

Inserts a value at the specified interval for the given key. If the key already has a value at that specific interval then that value will be overwritten.

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
api_instance = vidispine.ShapeBulkyMetadataApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
key = 'key_example' # str | The key.
body = 'body_example' # str | The value to set.
item_track = 'item_track_example' # str | The track in the item. (optional)
end = 'end_example' # str | A time code that defines the end of the interval. (optional)
channel = 56 # int | The audio channel index. (optional)
stream = 56 # int | The stream index. (optional)
start = 'start_example' # str | A time code that defines the start of the interval. (optional)

try:
    # Insert values
    api_instance.update_item_shape_bulky_metadata_key(item_id, shape_id, key, body, item_track=item_track, end=end, channel=channel, stream=stream, start=start)
except ApiException as e:
    print("Exception when calling ShapeBulkyMetadataApi->update_item_shape_bulky_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **key** | **str**| The key. | 
 **body** | **str**| The value to set. | 
 **item_track** | **str**| The track in the item. | [optional] 
 **end** | **str**| A time code that defines the end of the interval. | [optional] 
 **channel** | **int**| The audio channel index. | [optional] 
 **stream** | **int**| The stream index. | [optional] 
 **start** | **str**| A time code that defines the start of the interval. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

