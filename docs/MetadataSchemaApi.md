# vidispine.MetadataSchemaApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_metadata_group_schema**](MetadataSchemaApi.md#delete_metadata_group_schema) | **DELETE** /metadata-schema/{group-name} | Remove a group from the schema
[**delete_metadata_schema**](MetadataSchemaApi.md#delete_metadata_schema) | **DELETE** /metadata-schema | Delete the schema
[**get_metadata_group_schema**](MetadataSchemaApi.md#get_metadata_group_schema) | **GET** /metadata-schema/{group-name} | Retrieve a group from the schema
[**get_metadata_schema**](MetadataSchemaApi.md#get_metadata_schema) | **GET** /metadata-schema | Retrieve the schema
[**update_metadata_group_schema**](MetadataSchemaApi.md#update_metadata_group_schema) | **PUT** /metadata-schema/{group-name} | Update a group in the schema
[**update_metadata_schema**](MetadataSchemaApi.md#update_metadata_schema) | **PUT** /metadata-schema | Update the schema


# **delete_metadata_group_schema**
> delete_metadata_group_schema(group_name)

Remove a group from the schema

Removes the group from the schema.

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
api_instance = vidispine.MetadataSchemaApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Remove a group from the schema
    api_instance.delete_metadata_group_schema(group_name)
except ApiException as e:
    print("Exception when calling MetadataSchemaApi->delete_metadata_group_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

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

# **delete_metadata_schema**
> delete_metadata_schema()

Delete the schema

Clears the schema, causing no validation to be made.

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
api_instance = vidispine.MetadataSchemaApi(vidispine.ApiClient(configuration))

try:
    # Delete the schema
    api_instance.delete_metadata_schema()
except ApiException as e:
    print("Exception when calling MetadataSchemaApi->delete_metadata_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **get_metadata_group_schema**
> MetadataSchemaGroupType get_metadata_group_schema(group_name)

Retrieve a group from the schema

Retrieves the schema for a particular group.

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
api_instance = vidispine.MetadataSchemaApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.

try:
    # Retrieve a group from the schema
    api_response = api_instance.get_metadata_group_schema(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataSchemaApi->get_metadata_group_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 

### Return type

[**MetadataSchemaGroupType**](MetadataSchemaGroupType.md)

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

# **get_metadata_schema**
> MetadataSchemaType get_metadata_schema()

Retrieve the schema

Retrieves the full metadata schema.

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
api_instance = vidispine.MetadataSchemaApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the schema
    api_response = api_instance.get_metadata_schema()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataSchemaApi->get_metadata_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataSchemaType**](MetadataSchemaType.md)

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

# **update_metadata_group_schema**
> update_metadata_group_schema(group_name, metadata_schema_group_type)

Update a group in the schema

Updates the specified group in the schema

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
api_instance = vidispine.MetadataSchemaApi(vidispine.ApiClient(configuration))
group_name = 'group_name_example' # str | The group name.
metadata_schema_group_type = vidispine.MetadataSchemaGroupType() # MetadataSchemaGroupType | 

try:
    # Update a group in the schema
    api_instance.update_metadata_group_schema(group_name, metadata_schema_group_type)
except ApiException as e:
    print("Exception when calling MetadataSchemaApi->update_metadata_group_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| The group name. | 
 **metadata_schema_group_type** | [**MetadataSchemaGroupType**](MetadataSchemaGroupType.md)|  | 

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

# **update_metadata_schema**
> update_metadata_schema(metadata_schema_type)

Update the schema

Updates the schema with the given document.

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
api_instance = vidispine.MetadataSchemaApi(vidispine.ApiClient(configuration))
metadata_schema_type = vidispine.MetadataSchemaType() # MetadataSchemaType | 

try:
    # Update the schema
    api_instance.update_metadata_schema(metadata_schema_type)
except ApiException as e:
    print("Exception when calling MetadataSchemaApi->update_metadata_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_schema_type** | [**MetadataSchemaType**](MetadataSchemaType.md)|  | 

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

