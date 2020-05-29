# vidispine.FieldAccessApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata_field_access_control**](FieldAccessApi.md#create_metadata_field_access_control) | **POST** /metadata-field/{field-name}/access | Create an access control entry
[**delete_metadata_field_access_control**](FieldAccessApi.md#delete_metadata_field_access_control) | **DELETE** /metadata-field/{field-name}/access/{access-id} | Delete an access control entry
[**get_metadata_field_access_controls**](FieldAccessApi.md#get_metadata_field_access_controls) | **GET** /metadata-field/{field-name}/access | Retrieve an access control list


# **create_metadata_field_access_control**
> MetadataFieldAccessControlType create_metadata_field_access_control(field_name, metadata_field_access_control_type)

Create an access control entry

Creates an entry in the access control list and returns the created entry together with its id.

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
api_instance = vidispine.FieldAccessApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
metadata_field_access_control_type = vidispine.MetadataFieldAccessControlType() # MetadataFieldAccessControlType | 

try:
    # Create an access control entry
    api_response = api_instance.create_metadata_field_access_control(field_name, metadata_field_access_control_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldAccessApi->create_metadata_field_access_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
 **metadata_field_access_control_type** | [**MetadataFieldAccessControlType**](MetadataFieldAccessControlType.md)|  | 

### Return type

[**MetadataFieldAccessControlType**](MetadataFieldAccessControlType.md)

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

# **delete_metadata_field_access_control**
> delete_metadata_field_access_control(field_name, access_id)

Delete an access control entry

Removes the access control entry with the specified id.

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
api_instance = vidispine.FieldAccessApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
access_id = 'access_id_example' # str | The access id.

try:
    # Delete an access control entry
    api_instance.delete_metadata_field_access_control(field_name, access_id)
except ApiException as e:
    print("Exception when calling FieldAccessApi->delete_metadata_field_access_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
 **access_id** | **str**| The access id. | 

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

# **get_metadata_field_access_controls**
> MetadataFieldAccessControlListType get_metadata_field_access_controls(field_name)

Retrieve an access control list

Returns the access control list that is applied to the specified field or group.

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
api_instance = vidispine.FieldAccessApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.

try:
    # Retrieve an access control list
    api_response = api_instance.get_metadata_field_access_controls(field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldAccessApi->get_metadata_field_access_controls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 

### Return type

[**MetadataFieldAccessControlListType**](MetadataFieldAccessControlListType.md)

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

