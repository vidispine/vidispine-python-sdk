# vidispine.ThumbnailResourceApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_thumbnail_export_job**](ThumbnailResourceApi.md#create_thumbnail_export_job) | **POST** /thumbnail/{service}/{item-id}/{time}/export | Export a thumbnail
[**delete_thumbnail**](ThumbnailResourceApi.md#delete_thumbnail) | **DELETE** /thumbnail/{service}/{item-id}/{time} | Delete a thumbnail
[**delete_thumbnails**](ThumbnailResourceApi.md#delete_thumbnails) | **DELETE** /thumbnail/{service}/{item-id} | Delete all thumbnails
[**get_thumbnail**](ThumbnailResourceApi.md#get_thumbnail) | **GET** /thumbnail/{service}/{item-id}/{time} | Retrieve the image representation
[**get_thumbnails**](ThumbnailResourceApi.md#get_thumbnails) | **GET** /thumbnail/{service}/{item-id} | List all thumbnails
[**update_or_create_thumbnail**](ThumbnailResourceApi.md#update_or_create_thumbnail) | **PUT** /thumbnail/{service}/{item-id}/{time} | Update or create a thumbnail


# **create_thumbnail_export_job**
> JobType create_thumbnail_export_job(uri, service, item_id, time, jobmetadata=jobmetadata, notification_data=notification_data, format=format, notification=notification, priority=priority)

Export a thumbnail

Starts a job that writes the thumbnail or poster to a specific destination.

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
api_instance = vidispine.ThumbnailResourceApi(vidispine.ApiClient(configuration))
uri = 'uri_example' # str | URI of export location of thumbnail or poster
service = 'service_example' # str | The service.
item_id = 'item_id_example' # str | The item id.
time = 'time_example' # str | The time.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
format = 'format_example' # str | Image format of destination.  E. g.  `tiff`. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Export a thumbnail
    api_response = api_instance.create_thumbnail_export_job(uri, service, item_id, time, jobmetadata=jobmetadata, notification_data=notification_data, format=format, notification=notification, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailResourceApi->create_thumbnail_export_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| URI of export location of thumbnail or poster | 
 **service** | **str**| The service. | 
 **item_id** | **str**| The item id. | 
 **time** | **str**| The time. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **format** | **str**| Image format of destination.  E. g.  &#x60;tiff&#x60;. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]

### Return type

[**JobType**](JobType.md)

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

# **delete_thumbnail**
> delete_thumbnail(service, item_id, time)

Delete a thumbnail

Remove this thumbnail.

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
api_instance = vidispine.ThumbnailResourceApi(vidispine.ApiClient(configuration))
service = 'service_example' # str | The service.
item_id = 'item_id_example' # str | The item id.
time = 'time_example' # str | The time.

try:
    # Delete a thumbnail
    api_instance.delete_thumbnail(service, item_id, time)
except ApiException as e:
    print("Exception when calling ThumbnailResourceApi->delete_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| The service. | 
 **item_id** | **str**| The item id. | 
 **time** | **str**| The time. | 

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

# **delete_thumbnails**
> delete_thumbnails(service, item_id)

Delete all thumbnails

Remove all thumbnails handled by this resource.

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
api_instance = vidispine.ThumbnailResourceApi(vidispine.ApiClient(configuration))
service = 'service_example' # str | The service.
item_id = 'item_id_example' # str | The item id.

try:
    # Delete all thumbnails
    api_instance.delete_thumbnails(service, item_id)
except ApiException as e:
    print("Exception when calling ThumbnailResourceApi->delete_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| The service. | 
 **item_id** | **str**| The item id. | 

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

# **get_thumbnail**
> file get_thumbnail(service, item_id, time, hash=hash)

Retrieve the image representation

Return the image representation of this thumbnail.

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
api_instance = vidispine.ThumbnailResourceApi(vidispine.ApiClient(configuration))
service = 'service_example' # str | The service.
item_id = 'item_id_example' # str | The item id.
time = 'time_example' # str | The time.
hash = 'hash_example' # str | The checksum of the image. (optional)

try:
    # Retrieve the image representation
    api_response = api_instance.get_thumbnail(service, item_id, time, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailResourceApi->get_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| The service. | 
 **item_id** | **str**| The item id. | 
 **time** | **str**| The time. | 
 **hash** | **str**| The checksum of the image. | [optional] 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/jpeg

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Image of the thumbnail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnails**
> URIListType get_thumbnails(service, item_id, noauth_url=noauth_url, url=url)

List all thumbnails

Returns thumbnail URIs on which further requests may be performed.

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
api_instance = vidispine.ThumbnailResourceApi(vidispine.ApiClient(configuration))
service = 'service_example' # str | The service.
item_id = 'item_id_example' # str | The item id.
noauth_url = True # bool | - `true` Return URIs that do not need authentication.  - `false` (default) Return normal URIs (optional)
url = False # bool | - `true` - Return list of URLs.  - `false` (default) - Return list of ids. (optional) (default to False)

try:
    # List all thumbnails
    api_response = api_instance.get_thumbnails(service, item_id, noauth_url=noauth_url, url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailResourceApi->get_thumbnails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| The service. | 
 **item_id** | **str**| The item id. | 
 **noauth_url** | **bool**| - &#x60;true&#x60; Return URIs that do not need authentication.  - &#x60;false&#x60; (default) Return normal URIs | [optional] 
 **url** | **bool**| - &#x60;true&#x60; - Return list of URLs.  - &#x60;false&#x60; (default) - Return list of ids. | [optional] [default to False]

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
**0** | &lt;em&gt;URIListDocument&lt;/em&gt; of thumbnail URIs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_thumbnail**
> str update_or_create_thumbnail(service, item_id, time, body)

Update or create a thumbnail

Create a new thumbnail at the specified time code. If a thumbnail with the specified time code already exists it is replaced.

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
api_instance = vidispine.ThumbnailResourceApi(vidispine.ApiClient(configuration))
service = 'service_example' # str | The service.
item_id = 'item_id_example' # str | The item id.
time = 'time_example' # str | The time.
body = '/path/to/file' # file | Image to insert

try:
    # Update or create a thumbnail
    api_response = api_instance.update_or_create_thumbnail(service, item_id, time, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThumbnailResourceApi->update_or_create_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| The service. | 
 **item_id** | **str**| The item id. | 
 **time** | **str**| The time. | 
 **body** | **file**| Image to insert | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: image/png, image/jpeg
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Informational status message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

