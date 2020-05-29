# vidispine.MetadataFieldApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_metadata_field**](MetadataFieldApi.md#delete_metadata_field) | **DELETE** /metadata-field/{field-name} | Delete a metadata field
[**delete_metadata_field_metadata**](MetadataFieldApi.md#delete_metadata_field_metadata) | **DELETE** /metadata-field/{field-name}/metadata | Delete all key-value pairs
[**delete_metadata_field_metadata_key**](MetadataFieldApi.md#delete_metadata_field_metadata_key) | **DELETE** /metadata-field/{field-name}/metadata/{keypath} | Delete key-value pairs
[**get_metadata_field**](MetadataFieldApi.md#get_metadata_field) | **GET** /metadata-field/{field-name} | Retrieve a metadata field
[**get_metadata_field_allowed_values**](MetadataFieldApi.md#get_metadata_field_allowed_values) | **POST** /metadata-field/{field-name}/allowed-values | Retrieve the enumeration for field given some constraints
[**get_metadata_field_enumeration**](MetadataFieldApi.md#get_metadata_field_enumeration) | **GET** /metadata-field/{field-name}/values | Retrieve the enumeration for a field
[**get_metadata_field_merged_access**](MetadataFieldApi.md#get_metadata_field_merged_access) | **GET** /metadata-field/{field-name}/merged-access/ | Retrieve user access to field
[**get_metadata_field_metadata**](MetadataFieldApi.md#get_metadata_field_metadata) | **GET** /metadata-field/{field-name}/metadata | Retrieve all metadata
[**get_metadata_field_metadata_key**](MetadataFieldApi.md#get_metadata_field_metadata_key) | **GET** /metadata-field/{field-name}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_metadata_fields**](MetadataFieldApi.md#get_metadata_fields) | **GET** /metadata-field | List all metadata fields
[**get_metadata_fields_merged_access**](MetadataFieldApi.md#get_metadata_fields_merged_access) | **GET** /metadata-field/merged-access/ | Retrieve user access to all fields
[**get_metadata_fields_terse_schema**](MetadataFieldApi.md#get_metadata_fields_terse_schema) | **GET** /metadata-field/terse-schema | Retrieve terse metadata schema
[**update_metadata_field_enumeration**](MetadataFieldApi.md#update_metadata_field_enumeration) | **PUT** /metadata-field/{field-name}/values | Set the enumeration for a field
[**update_metadata_field_metadata**](MetadataFieldApi.md#update_metadata_field_metadata) | **PUT** /metadata-field/{field-name}/metadata | Create multiple key-value pairs
[**update_metadata_field_metadata_key**](MetadataFieldApi.md#update_metadata_field_metadata_key) | **PUT** /metadata-field/{field-name}/metadata/{keypath} | Set the value for a specific key
[**update_or_create_metadata_field**](MetadataFieldApi.md#update_or_create_metadata_field) | **PUT** /metadata-field/{field-name} | Update or create a metadata field


# **delete_metadata_field**
> delete_metadata_field(field_name)

Delete a metadata field

Removes the metadata field definition. Note that this action may invalidate existing metadata.

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.

try:
    # Delete a metadata field
    api_instance.delete_metadata_field(field_name)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->delete_metadata_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 

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

# **delete_metadata_field_metadata**
> delete_metadata_field_metadata(field_name)

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.

try:
    # Delete all key-value pairs
    api_instance.delete_metadata_field_metadata(field_name)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->delete_metadata_field_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 

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

# **delete_metadata_field_metadata_key**
> delete_metadata_field_metadata_key(field_name, keypath)

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_metadata_field_metadata_key(field_name, keypath)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->delete_metadata_field_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
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

# **get_metadata_field**
> MetadataFieldType get_metadata_field(field_name, data=data, include_values=include_values)

Retrieve a metadata field

Returns information about a specific metadata field definition.

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
data = ['data_example'] # list[str] | Comma-separated list of any additional data to include.  Wildcard characters.  e. g.   `*`, `myapp_*`,  `*_version` can be used.  (New in 4. 17. ) (optional)
include_values = False # bool | Return the value enumeration for this field. (optional) (default to False)

try:
    # Retrieve a metadata field
    api_response = api_instance.get_metadata_field(field_name, data=data, include_values=include_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->get_metadata_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
 **data** | [**list[str]**](str.md)| Comma-separated list of any additional data to include.  Wildcard characters.  e. g.   &#x60;*&#x60;, &#x60;myapp_*&#x60;,  &#x60;*_version&#x60; can be used.  (New in 4. 17. ) | [optional] 
 **include_values** | **bool**| Return the value enumeration for this field. | [optional] [default to False]

### Return type

[**MetadataFieldType**](MetadataFieldType.md)

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

# **get_metadata_field_allowed_values**
> ConstraintValueListType get_metadata_field_allowed_values(field_name, metadata_field_value_constraint_list_type)

Retrieve the enumeration for field given some constraints

Returns the allowed values for a field based on the defined metadata dataset on the field.

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
metadata_field_value_constraint_list_type = vidispine.MetadataFieldValueConstraintListType() # MetadataFieldValueConstraintListType | 

try:
    # Retrieve the enumeration for field given some constraints
    api_response = api_instance.get_metadata_field_allowed_values(field_name, metadata_field_value_constraint_list_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->get_metadata_field_allowed_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
 **metadata_field_value_constraint_list_type** | [**MetadataFieldValueConstraintListType**](MetadataFieldValueConstraintListType.md)|  | 

### Return type

[**ConstraintValueListType**](ConstraintValueListType.md)

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

# **get_metadata_field_enumeration**
> SimpleMetadataType get_metadata_field_enumeration(field_name, key_regex=key_regex, value_start=value_start, key_start=key_start, hits=hits, value_regex=value_regex, key_exact=key_exact, value_exact=value_exact)

Retrieve the enumeration for a field

Retrieves the value enumeration for a specific field.

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
key_regex = 'key_regex_example' # str | Return keys matching this regular expression. (optional)
value_start = 'value_start_example' # str | Return keys with a value starting with this prefix. (optional)
key_start = 'key_start_example' # str | Return keys starting with this prefix. (optional)
hits = 56 # int | The maximum number of keys to return.  Default is all. (optional)
value_regex = 'value_regex_example' # str | Return keys with a value matching this regular expression. (optional)
key_exact = 'key_exact_example' # str | Return the key with this name. (optional)
value_exact = 'value_exact_example' # str | Return keys with this value. (optional)

try:
    # Retrieve the enumeration for a field
    api_response = api_instance.get_metadata_field_enumeration(field_name, key_regex=key_regex, value_start=value_start, key_start=key_start, hits=hits, value_regex=value_regex, key_exact=key_exact, value_exact=value_exact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->get_metadata_field_enumeration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
 **key_regex** | **str**| Return keys matching this regular expression. | [optional] 
 **value_start** | **str**| Return keys with a value starting with this prefix. | [optional] 
 **key_start** | **str**| Return keys starting with this prefix. | [optional] 
 **hits** | **int**| The maximum number of keys to return.  Default is all. | [optional] 
 **value_regex** | **str**| Return keys with a value matching this regular expression. | [optional] 
 **key_exact** | **str**| Return the key with this name. | [optional] 
 **value_exact** | **str**| Return keys with this value. | [optional] 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_field_merged_access**
> AccessControlMergedType get_metadata_field_merged_access(field_name, username=username)

Retrieve user access to field

Retrieves the permission for a specific user to a field.

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
username = 'username_example' # str | The name of the user to check. (optional)

try:
    # Retrieve user access to field
    api_response = api_instance.get_metadata_field_merged_access(field_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->get_metadata_field_merged_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
 **username** | **str**| The name of the user to check. | [optional] 

### Return type

[**AccessControlMergedType**](AccessControlMergedType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An &lt;em&gt;AccessControlMergedDocument&lt;/em&gt; containing the field, user and permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_field_metadata**
> SimpleMetadataType get_metadata_field_metadata(field_name)

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.

try:
    # Retrieve all metadata
    api_response = api_instance.get_metadata_field_metadata(field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->get_metadata_field_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 

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

# **get_metadata_field_metadata_key**
> str get_metadata_field_metadata_key(field_name, keypath)

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_metadata_field_metadata_key(field_name, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->get_metadata_field_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
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

# **get_metadata_fields**
> MetadataFieldListType get_metadata_fields(data=data, include_values=include_values)

List all metadata fields

Returns a list of all defined fields.

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
data = ['data_example'] # list[str] | Comma-separated list of any additional data to include. (optional)
include_values = False # bool | Return the value enumeration for each field. (optional) (default to False)

try:
    # List all metadata fields
    api_response = api_instance.get_metadata_fields(data=data, include_values=include_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->get_metadata_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**list[str]**](str.md)| Comma-separated list of any additional data to include. | [optional] 
 **include_values** | **bool**| Return the value enumeration for each field. | [optional] [default to False]

### Return type

[**MetadataFieldListType**](MetadataFieldListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of ids or URLs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_fields_merged_access**
> AccessControlMergedType get_metadata_fields_merged_access(username=username)

Retrieve user access to all fields

Retrieves the permission for a specific user to all fields.

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
username = 'username_example' # str | The name of the user to check. (optional)

try:
    # Retrieve user access to all fields
    api_response = api_instance.get_metadata_fields_merged_access(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->get_metadata_fields_merged_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name of the user to check. | [optional] 

### Return type

[**AccessControlMergedType**](AccessControlMergedType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An &lt;em&gt;AccessControlMergedDocument&lt;/em&gt; containing the fields, user and permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_fields_terse_schema**
> str get_metadata_fields_terse_schema()

Retrieve terse metadata schema

Retrieves the schema that defines terse metadata. This schema is dynamically generated based on the fields present in the system.

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))

try:
    # Retrieve terse metadata schema
    api_response = api_instance.get_metadata_fields_terse_schema()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->get_metadata_fields_terse_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | An XML schema. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_field_enumeration**
> update_metadata_field_enumeration(field_name, simple_metadata_type)

Set the enumeration for a field

Sets the value enumeration for a specific field.

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Set the enumeration for a field
    api_instance.update_metadata_field_enumeration(field_name, simple_metadata_type)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->update_metadata_field_enumeration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
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

# **update_metadata_field_metadata**
> update_metadata_field_metadata(field_name, simple_metadata_type)

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_metadata_field_metadata(field_name, simple_metadata_type)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->update_metadata_field_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
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

# **update_metadata_field_metadata_key**
> update_metadata_field_metadata_key(field_name, keypath, body)

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_metadata_field_metadata_key(field_name, keypath, body)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->update_metadata_field_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
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

# **update_or_create_metadata_field**
> MetadataFieldType update_or_create_metadata_field(field_name, metadata_field_type)

Update or create a metadata field

Updates or creates a metadata field definition.

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
api_instance = vidispine.MetadataFieldApi(vidispine.ApiClient(configuration))
field_name = 'field_name_example' # str | The field name.
metadata_field_type = vidispine.MetadataFieldType() # MetadataFieldType | 

try:
    # Update or create a metadata field
    api_response = api_instance.update_or_create_metadata_field(field_name, metadata_field_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataFieldApi->update_or_create_metadata_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | 
 **metadata_field_type** | [**MetadataFieldType**](MetadataFieldType.md)|  | 

### Return type

[**MetadataFieldType**](MetadataFieldType.md)

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

