# vidispine.ImportSettingsApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_import_setting**](ImportSettingsApi.md#create_import_setting) | **POST** /import/settings | Create an import profile
[**delete_import_setting**](ImportSettingsApi.md#delete_import_setting) | **DELETE** /import/settings/{settings-id} | Delete an import profile
[**get_import_setting**](ImportSettingsApi.md#get_import_setting) | **GET** /import/settings/{settings-id} | Retrieve an import profile
[**get_import_settings**](ImportSettingsApi.md#get_import_settings) | **GET** /import/settings | List all import profiles
[**update_import_setting**](ImportSettingsApi.md#update_import_setting) | **PUT** /import/settings/{settings-id} | Update an import profile


# **create_import_setting**
> ImportSettingsType create_import_setting(import_settings_type)

Create an import profile

Creates a new settings profile with the given settings.

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
api_instance = vidispine.ImportSettingsApi(vidispine.ApiClient(configuration))
import_settings_type = vidispine.ImportSettingsType() # ImportSettingsType | An <em>ImportSettingsDocument</em> containing the settings profile.

try:
    # Create an import profile
    api_response = api_instance.create_import_setting(import_settings_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportSettingsApi->create_import_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_settings_type** | [**ImportSettingsType**](ImportSettingsType.md)| An &lt;em&gt;ImportSettingsDocument&lt;/em&gt; containing the settings profile. | 

### Return type

[**ImportSettingsType**](ImportSettingsType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An &lt;em&gt;ImportSettingsDocument&lt;/em&gt; containing the the settings profile together with its id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_import_setting**
> delete_import_setting(settings_id)

Delete an import profile

Deletes the profile with specified id.

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
api_instance = vidispine.ImportSettingsApi(vidispine.ApiClient(configuration))
settings_id = 'settings_id_example' # str | The settings id.

try:
    # Delete an import profile
    api_instance.delete_import_setting(settings_id)
except ApiException as e:
    print("Exception when calling ImportSettingsApi->delete_import_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_id** | **str**| The settings id. | 

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

# **get_import_setting**
> ImportSettingsType get_import_setting(settings_id)

Retrieve an import profile

Retrieves the settings specified by a certain profile.

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
api_instance = vidispine.ImportSettingsApi(vidispine.ApiClient(configuration))
settings_id = 'settings_id_example' # str | The settings id.

try:
    # Retrieve an import profile
    api_response = api_instance.get_import_setting(settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportSettingsApi->get_import_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_id** | **str**| The settings id. | 

### Return type

[**ImportSettingsType**](ImportSettingsType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An &lt;em&gt;ImportSettingsDocument&lt;/em&gt; containing the settings of the profile. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_settings**
> URIListType get_import_settings()

List all import profiles

Retrieves a list of all profiles.

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
api_instance = vidispine.ImportSettingsApi(vidispine.ApiClient(configuration))

try:
    # List all import profiles
    api_response = api_instance.get_import_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportSettingsApi->get_import_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**0** | CRLF-delimited list of ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_import_setting**
> update_import_setting(settings_id, import_settings_type)

Update an import profile

Changes the settings of the specified profile.

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
api_instance = vidispine.ImportSettingsApi(vidispine.ApiClient(configuration))
settings_id = 'settings_id_example' # str | The settings id.
import_settings_type = vidispine.ImportSettingsType() # ImportSettingsType | An <em>ImportSettingsDocument</em> with the new settings.

try:
    # Update an import profile
    api_instance.update_import_setting(settings_id, import_settings_type)
except ApiException as e:
    print("Exception when calling ImportSettingsApi->update_import_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_id** | **str**| The settings id. | 
 **import_settings_type** | [**ImportSettingsType**](ImportSettingsType.md)| An &lt;em&gt;ImportSettingsDocument&lt;/em&gt; with the new settings. | 

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

