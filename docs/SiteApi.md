# vidispine.SiteApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_site_metadata**](SiteApi.md#delete_site_metadata) | **DELETE** /site/{id}/metadata | Delete all key-value pairs
[**delete_site_metadata_key**](SiteApi.md#delete_site_metadata_key) | **DELETE** /site/{id}/metadata/{keypath} | Delete key-value pairs
[**get_site**](SiteApi.md#get_site) | **GET** /site/{site-id} | Retrieve a site
[**get_site_metadata**](SiteApi.md#get_site_metadata) | **GET** /site/{id}/metadata | Retrieve all metadata
[**get_site_metadata_key**](SiteApi.md#get_site_metadata_key) | **GET** /site/{id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_sites**](SiteApi.md#get_sites) | **GET** /site | List all sites
[**update_or_create_site**](SiteApi.md#update_or_create_site) | **PUT** /site/{site-id} | Update or create a site
[**update_site_metadata**](SiteApi.md#update_site_metadata) | **PUT** /site/{id}/metadata | Create multiple key-value pairs
[**update_site_metadata_key**](SiteApi.md#update_site_metadata_key) | **PUT** /site/{id}/metadata/{keypath} | Set the value for a specific key


# **delete_site_metadata**
> delete_site_metadata(id)

Delete all key-value pairs

Clears all key-value pairs for the specified entity.

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
api_instance = vidispine.SiteApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # Delete all key-value pairs
    api_instance.delete_site_metadata(id)
except ApiException as e:
    print("Exception when calling SiteApi->delete_site_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

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

# **delete_site_metadata_key**
> delete_site_metadata_key(id, keypath)

Delete key-value pairs

Deletes the key-value pair with the specified key. If a key path is given, it may include wildcards for deleting multiple keys.  Key paths can also be specified as well as specific keys.

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
api_instance = vidispine.SiteApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_site_metadata_key(id, keypath)
except ApiException as e:
    print("Exception when calling SiteApi->delete_site_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **keypath** | **str**| The keypath. | 

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

# **get_site**
> SiteDefinitionType get_site(site_id)

Retrieve a site

Retrieves the definition for a specific site.

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
api_instance = vidispine.SiteApi(vidispine.ApiClient(configuration))
site_id = 'site_id_example' # str | The site id.

try:
    # Retrieve a site
    api_response = api_instance.get_site(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site id. | 

### Return type

[**SiteDefinitionType**](SiteDefinitionType.md)

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

# **get_site_metadata**
> SimpleMetadataType get_site_metadata(id)

Retrieve all metadata

Retrieves all key-value pairs associated with the specified entity.

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
api_instance = vidispine.SiteApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_site_metadata(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

### Return type

[**SimpleMetadataType**](SimpleMetadataType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;SimpleMetadataDocument&lt;/em&gt; containing all key-value pairs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_metadata_key**
> str get_site_metadata_key(id, keypath)

Retrieve the metadata for a specific key

Retrieves the value of a specific key. If a key path is specified, exactly one key-value pair must match the key path, else an error is returned.  Key paths can also be specified as well as specific keys.

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
api_instance = vidispine.SiteApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_site_metadata_key(id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **keypath** | **str**| The keypath. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The raw string value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sites**
> URIListType get_sites(type=type)

List all sites

Retrieves the ids of the sites that have been configured.

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
api_instance = vidispine.SiteApi(vidispine.ApiClient(configuration))
type = 'all' # str | - `all` (default) - Return the ids of all added sites.  - `current` - Return the id of the current site. (optional) (default to 'all')

try:
    # List all sites
    api_response = api_instance.get_sites(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| - &#x60;all&#x60; (default) - Return the ids of all added sites.  - &#x60;current&#x60; - Return the id of the current site. | [optional] [default to &#39;all&#39;]

### Return type

[**URIListType**](URIListType.md)

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

# **update_or_create_site**
> SiteDefinitionType update_or_create_site(site_id, site_definition_type)

Update or create a site

Adds a new site using the given site definition.  The only supported value for `syncPolicy` is currently `ONDEMAND`.

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
api_instance = vidispine.SiteApi(vidispine.ApiClient(configuration))
site_id = 'site_id_example' # str | The site id.
site_definition_type = vidispine.SiteDefinitionType() # SiteDefinitionType | 

try:
    # Update or create a site
    api_response = api_instance.update_or_create_site(site_id, site_definition_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->update_or_create_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The site id. | 
 **site_definition_type** | [**SiteDefinitionType**](SiteDefinitionType.md)|  | 

### Return type

[**SiteDefinitionType**](SiteDefinitionType.md)

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

# **update_site_metadata**
> update_site_metadata(id, simple_metadata_type)

Create multiple key-value pairs

Sets all the specified key-value pairs.

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
api_instance = vidispine.SiteApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_site_metadata(id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling SiteApi->update_site_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **simple_metadata_type** | [**SimpleMetadataType**](SimpleMetadataType.md)|  | 

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

# **update_site_metadata_key**
> update_site_metadata_key(id, keypath, body)

Set the value for a specific key

Sets the value for a specific key. The key path may not contain wildcards.

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
api_instance = vidispine.SiteApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_site_metadata_key(id, keypath, body)
except ApiException as e:
    print("Exception when calling SiteApi->update_site_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **keypath** | **str**| The keypath. | 
 **body** | **str**| The raw string value. | 

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

