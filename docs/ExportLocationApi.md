# vidispine.ExportLocationApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_export_location**](ExportLocationApi.md#delete_export_location) | **DELETE** /export-location/{location-name} | Delete an export location
[**get_export_location**](ExportLocationApi.md#get_export_location) | **GET** /export-location/{location-name} | Retrieve an export location
[**get_export_location_script**](ExportLocationApi.md#get_export_location_script) | **GET** /export-location/{location-name}/script | Retrieve the export location script
[**get_export_locations**](ExportLocationApi.md#get_export_locations) | **GET** /export-location | List all export locations
[**update_export_location_script**](ExportLocationApi.md#update_export_location_script) | **PUT** /export-location/{location-name}/script | Update the export location script
[**update_or_create_export_location**](ExportLocationApi.md#update_or_create_export_location) | **PUT** /export-location/{location-name} | Update or create an export location


# **delete_export_location**
> delete_export_location(location_name)

Delete an export location

Delete the export location with the specified name.

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
api_instance = vidispine.ExportLocationApi(vidispine.ApiClient(configuration))
location_name = 'location_name_example' # str | The location name.

try:
    # Delete an export location
    api_instance.delete_export_location(location_name)
except ApiException as e:
    print("Exception when calling ExportLocationApi->delete_export_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name. | 

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

# **get_export_location**
> ExportLocationType get_export_location(location_name)

Retrieve an export location

Return information about the export location with the specified name.

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
api_instance = vidispine.ExportLocationApi(vidispine.ApiClient(configuration))
location_name = 'location_name_example' # str | The location name.

try:
    # Retrieve an export location
    api_response = api_instance.get_export_location(location_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportLocationApi->get_export_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name. | 

### Return type

[**ExportLocationType**](ExportLocationType.md)

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

# **get_export_location_script**
> str get_export_location_script(location_name)

Retrieve the export location script

Retrieves the script on an export location.

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
api_instance = vidispine.ExportLocationApi(vidispine.ApiClient(configuration))
location_name = 'location_name_example' # str | The location name.

try:
    # Retrieve the export location script
    api_response = api_instance.get_export_location_script(location_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportLocationApi->get_export_location_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name. | 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export_locations**
> ExportLocationListType get_export_locations()

List all export locations

List all defined export locations.

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
api_instance = vidispine.ExportLocationApi(vidispine.ApiClient(configuration))

try:
    # List all export locations
    api_response = api_instance.get_export_locations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportLocationApi->get_export_locations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExportLocationListType**](ExportLocationListType.md)

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

# **update_export_location_script**
> str update_export_location_script(location_name, body)

Update the export location script

Updates the script of an existing export location.

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
api_instance = vidispine.ExportLocationApi(vidispine.ApiClient(configuration))
location_name = 'location_name_example' # str | The location name.
body = 'body_example' # str | 

try:
    # Update the export location script
    api_response = api_instance.update_export_location_script(location_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportLocationApi->update_export_location_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name. | 
 **body** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The script that was set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_export_location**
> ExportLocationType update_or_create_export_location(location_name, export_location_type)

Update or create an export location

Create a new export location, or if there already is one with that name, update it.

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
api_instance = vidispine.ExportLocationApi(vidispine.ApiClient(configuration))
location_name = 'location_name_example' # str | The location name.
export_location_type = vidispine.ExportLocationType() # ExportLocationType | 

try:
    # Update or create an export location
    api_response = api_instance.update_or_create_export_location(location_name, export_location_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportLocationApi->update_or_create_export_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**| The location name. | 
 **export_location_type** | [**ExportLocationType**](ExportLocationType.md)|  | 

### Return type

[**ExportLocationType**](ExportLocationType.md)

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

