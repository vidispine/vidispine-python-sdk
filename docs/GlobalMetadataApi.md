# vidispine.GlobalMetadataApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_metadata_entry**](GlobalMetadataApi.md#delete_metadata_entry) | **DELETE** /metadata/{uuid} | Remove metadata by UUID
[**get_global_metadata**](GlobalMetadataApi.md#get_global_metadata) | **GET** /metadata | Retrieve the global metadata
[**get_metadata_entry**](GlobalMetadataApi.md#get_metadata_entry) | **GET** /metadata/{uuid} | Retrieve metadata by UUID
[**update_global_metadata**](GlobalMetadataApi.md#update_global_metadata) | **PUT** /metadata | Update the global metadata


# **delete_metadata_entry**
> delete_metadata_entry(uuid)

Remove metadata by UUID

Removes the metadata with the specified UUID.

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
api_instance = vidispine.GlobalMetadataApi(vidispine.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid.

try:
    # Remove metadata by UUID
    api_instance.delete_metadata_entry(uuid)
except ApiException as e:
    print("Exception when calling GlobalMetadataApi->delete_metadata_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid. | 

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

# **get_global_metadata**
> MetadataType get_global_metadata(language=language, include_constraint_value=include_constraint_value, track=track, conflict=conflict, samplerate=samplerate, default_value=default_value, interval=interval, group=group, field=field, include=include)

Retrieve the global metadata

Retrieves the global metadata.

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
api_instance = vidispine.GlobalMetadataApi(vidispine.ApiClient(configuration))
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
include_constraint_value = ["all"] # list[str] | Comma-separated list of fields whose \"display value\" should be retrieved from the metadata dataset.   - `all` (default) - Return the \"display value\" of all fields.  - `none` - No \"display value\" will be returned.  The fields will only have `id` set.  - *comma-separated field names* - Return the \"display value\" of the specified fields. (optional) (default to ["all"])
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
samplerate = 'samplerate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = 'include_example' # str | A list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)

try:
    # Retrieve the global metadata
    api_response = api_instance.get_global_metadata(language=language, include_constraint_value=include_constraint_value, track=track, conflict=conflict, samplerate=samplerate, default_value=default_value, interval=interval, group=group, field=field, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalMetadataApi->get_global_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **include_constraint_value** | [**list[str]**](str.md)| Comma-separated list of fields whose \&quot;display value\&quot; should be retrieved from the metadata dataset.   - &#x60;all&#x60; (default) - Return the \&quot;display value\&quot; of all fields.  - &#x60;none&#x60; - No \&quot;display value\&quot; will be returned.  The fields will only have &#x60;id&#x60; set.  - *comma-separated field names* - Return the \&quot;display value\&quot; of the specified fields. | [optional] [default to [&quot;all&quot;]]
 **track** | [**list[str]**](str.md)| Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is &#x60;A2&#x60;.  - *track-type* *t1* &#x60;-&#x60; *t2* - Return metadata for specified track interval, e. g.  &#x60;A2-4&#x60;.  - *track-type* &#x60;*&#x60; - Return metadata for all tracks of specified type, e. g.  &#x60;A*&#x60;.  - &#x60;generic&#x60; - Return all non-tracked metadata.  - &#x60;all&#x60; (default) - All metadata, with or without track specification, are returned. | [optional] [default to [&quot;all&quot;]]
 **conflict** | **str**| - &#x60;yes&#x60; (default) - Include all metadata conflicts, unresolved.  - &#x60;no&#x60; - Return conflicts resolved according to field rules. | [optional] [default to &#39;yes&#39;]
 **samplerate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **default_value** | **bool**| - &#x60;true&#x60; - For unset fields, return default values.  - &#x60;false&#x60; (default) - Do not return default values. | [optional] [default to False]
 **interval** | [**list[str]**](str.md)| Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - &#x60;generic&#x60; - Return all non-timed metadata.  - &#x60;all&#x60; (default) - Return all metadata, same as &#x60;interval&#x3D;generic,-INF-+INF&#x60; | [optional] [default to [&quot;all&quot;]]
 **group** | [**list[str]**](str.md)| Comma-separated list.   - *group-name* - Return specified group.  - *group-name* &#x60;+&#x60; - Return specified group and subgroups.  - *group-name* &#x60;:&#x60; *new-name* - Return specified group, renamed to a new name in return value.  - &#x60;-&#x60; *group-name* - Exclude specified group.  - (default) - Return all groups. | [optional] 
 **field** | [**list[str]**](str.md)| Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \&quot;:\&quot; *new-name* - Return specified field, renamed to a new name in return value.  - \&quot;-\&quot; *field-name* - Exclude specified field.  - (default) - Return all fields. | [optional] 
 **include** | **str**| A list of keys.   Includes additional field specific data.  Additionally, if set to &#x60;type&#x60; the type definition of the field will be retrieved. | [optional] 

### Return type

[**MetadataType**](MetadataType.md)

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

# **get_metadata_entry**
> MetadataEntryType get_metadata_entry(uuid)

Retrieve metadata by UUID

Retrieves the metadata entry that matches the UUID.

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
api_instance = vidispine.GlobalMetadataApi(vidispine.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid.

try:
    # Retrieve metadata by UUID
    api_response = api_instance.get_metadata_entry(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalMetadataApi->get_metadata_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid. | 

### Return type

[**MetadataEntryType**](MetadataEntryType.md)

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

# **update_global_metadata**
> MetadataType update_global_metadata(metadata_type, revision=revision, only_return_changes=only_return_changes, skip_forbidden=skip_forbidden)

Update the global metadata

Modifies the global metadata. This resource shares the same query parameters as the item metadata resource.

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
api_instance = vidispine.GlobalMetadataApi(vidispine.ApiClient(configuration))
metadata_type = vidispine.MetadataType() # MetadataType | 
revision = 'revision_example' # str | The known revision.  If not specified, the change set will attempt to override existing change sets. (optional)
only_return_changes = False # bool | New in version 4. 16. 6.   - `true` - Only return the changed entries.  - `false` (default) - Return the whole global metadata after the update. (optional) (default to False)
skip_forbidden = False # bool | Skip fields or groups that the user doesn't have write access to (optional) (default to False)

try:
    # Update the global metadata
    api_response = api_instance.update_global_metadata(metadata_type, revision=revision, only_return_changes=only_return_changes, skip_forbidden=skip_forbidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalMetadataApi->update_global_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_type** | [**MetadataType**](MetadataType.md)|  | 
 **revision** | **str**| The known revision.  If not specified, the change set will attempt to override existing change sets. | [optional] 
 **only_return_changes** | **bool**| New in version 4. 16. 6.   - &#x60;true&#x60; - Only return the changed entries.  - &#x60;false&#x60; (default) - Return the whole global metadata after the update. | [optional] [default to False]
 **skip_forbidden** | **bool**| Skip fields or groups that the user doesn&#39;t have write access to | [optional] [default to False]

### Return type

[**MetadataType**](MetadataType.md)

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

