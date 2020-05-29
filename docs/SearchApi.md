# vidispine.SearchApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**optimize_search_index**](SearchApi.md#optimize_search_index) | **POST** /search/optimize | Optimize the search index
[**search**](SearchApi.md#search) | **PUT** /search | Search items and collections
[**search_files**](SearchApi.md#search_files) | **PUT** /search/file | Search files
[**search_shapes**](SearchApi.md#search_shapes) | **PUT** /search/shape | Search shapes


# **optimize_search_index**
> optimize_search_index(blocking=blocking, timeout=timeout)

Optimize the search index

Submits an optimize request to Solr.  This request can be made to block until the optimize request has completed using the `blocking` parameter.

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
api_instance = vidispine.SearchApi(vidispine.ApiClient(configuration))
blocking = False # bool | - `true` - The request will block until the Solr optimize request has finished.  - `false` (default) - Optimize will be scheduled and the request will return immediately. (optional) (default to False)
timeout = 0 # int | Block for maximum number of specified milliseconds. (optional) (default to 0)

try:
    # Optimize the search index
    api_instance.optimize_search_index(blocking=blocking, timeout=timeout)
except ApiException as e:
    print("Exception when calling SearchApi->optimize_search_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocking** | **bool**| - &#x60;true&#x60; - The request will block until the Solr optimize request has finished.  - &#x60;false&#x60; (default) - Optimize will be scheduled and the request will return immediately. | [optional] [default to False]
 **timeout** | **int**| Block for maximum number of specified milliseconds. | [optional] [default to 0]

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

# **search**
> SearchResultType search(item_search_type, language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, number=number, interval=interval, group=group, include_values=include_values, storage_group=storage_group, track=track, conflict=conflict, content=content, merged_extradata=merged_extradata, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, p=p, base_uri=base_uri, uri_type=uri_type, storage=storage, revision=revision, scheme=scheme, version=version, merged_permission=merged_permission, sample_rate=sample_rate, count=count, save=save, noauth_url=noauth_url)

Search items and collections

Searches items and collections with a shared search query.

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
api_instance = vidispine.SearchApi(vidispine.ApiClient(configuration))
item_search_type = vidispine.ItemSearchType() # ItemSearchType | 
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
first = 1 # int | From the resulting list of items, start return list from specified offset. (optional) (default to 1)
closed_files = True # bool | A URI parameter:  - `true` (default) - Return only URIs that point to closed files.  - `false` - Return all URIs. (optional) (default to True)
terse = 'no' # str | - `yes` - Return metadata in terse format.  - `no` (default) - Return metadata in verbose format. (optional) (default to 'no')
method_metadata = 'method_metadata_example' # str | Metadata used with storage method. (optional)
number = 100 # int | The number of entities to fetch. (optional) (default to 100)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
include_values = True # bool | Return the value enumeration for each metadata field. (optional)
storage_group = 'storage_group_example' # str | Storage group id.  Return only files from storages specified in the storage group. (optional)
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
content = ['content_example'] # list[str] | Comma-separated list of the types of content to retrieve. (optional)
merged_extradata = 'merged_extradata_example' # str | Any possible extra data. (optional)
include_transient_metadata = True # bool | - `true` (default) - Include transient metadata.  - `false` - Do not include transient metadata in response. (optional) (default to True)
merged_type = 'merged_type_example' # str | The type of operation to check for. (optional)
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
tag = 'tag_example' # str | A URI parameter: Comma-separated list of shape tags to return. (optional)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = 'include_example' # str | A list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)
method_type = 'method_type_example' # str | Access method.   - `AUTO` - Gives an APInoauth URI to the media.  Access to file is tunneled through Vidispine.  - `AZURE_SAS` - If the storage schema is azure:// you can get direct access to the media.  The resulting URI will not tunnel through Vidispine but rather point directly to the media location at the azure storage. (optional)
p = ['p_example'] # list[str] | Comma-separated list of paths specifying the content to include.  Overrides the content and filter parameters. (optional)
base_uri = 'base_uri_example' # str | Which base URI to use for the thumbnail URLs. (optional)
uri_type = ['uri_type_example'] # list[str] | Comma-separated list of format types (container format) to return. (optional)
storage = ['storage_example'] # list[str] | List of storage ids.  Return only files from specific storages.  Can be specified multiple times. (optional)
revision = 'revision_example' # str | Specifying which metadata revision to display.  Only used if requesting a single item or collection. (optional)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
version = 'version_example' # str | Specifying which essence version to return for shapes.  If special value `all`, display all versions.  If special value `latest` (default), display latest version of shapes. (optional)
merged_permission = 'merged_permission_example' # str | The lowest required permission level. (optional)
sample_rate = 'sample_rate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
count = True # bool | - `true` (default) - Return hits in result.  - `false` - Do not return hits in result, in order to produce results faster. (optional) (default to True)
save = True # bool | - `true` - Returns a `303 See Other`, with a `Location` header containing an URI to fetch the search result - `false` (default) - Returns a regular search result (optional)
noauth_url = True # bool | - `true` Return URIs that do not need authentication.  - `false` (default) Return normal URIs (optional)

try:
    # Search items and collections
    api_response = api_instance.search(item_search_type, language=language, storage_type=storage_type, first=first, closed_files=closed_files, terse=terse, method_metadata=method_metadata, number=number, interval=interval, group=group, include_values=include_values, storage_group=storage_group, track=track, conflict=conflict, content=content, merged_extradata=merged_extradata, include_transient_metadata=include_transient_metadata, merged_type=merged_type, default_value=default_value, tag=tag, field=field, include=include, method_type=method_type, p=p, base_uri=base_uri, uri_type=uri_type, storage=storage, revision=revision, scheme=scheme, version=version, merged_permission=merged_permission, sample_rate=sample_rate, count=count, save=save, noauth_url=noauth_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_search_type** | [**ItemSearchType**](ItemSearchType.md)|  | 
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **first** | **int**| From the resulting list of items, start return list from specified offset. | [optional] [default to 1]
 **closed_files** | **bool**| A URI parameter:  - &#x60;true&#x60; (default) - Return only URIs that point to closed files.  - &#x60;false&#x60; - Return all URIs. | [optional] [default to True]
 **terse** | **str**| - &#x60;yes&#x60; - Return metadata in terse format.  - &#x60;no&#x60; (default) - Return metadata in verbose format. | [optional] [default to &#39;no&#39;]
 **method_metadata** | **str**| Metadata used with storage method. | [optional] 
 **number** | **int**| The number of entities to fetch. | [optional] [default to 100]
 **interval** | [**list[str]**](str.md)| Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - &#x60;generic&#x60; - Return all non-timed metadata.  - &#x60;all&#x60; (default) - Return all metadata, same as &#x60;interval&#x3D;generic,-INF-+INF&#x60; | [optional] [default to [&quot;all&quot;]]
 **group** | [**list[str]**](str.md)| Comma-separated list.   - *group-name* - Return specified group.  - *group-name* &#x60;+&#x60; - Return specified group and subgroups.  - *group-name* &#x60;:&#x60; *new-name* - Return specified group, renamed to a new name in return value.  - &#x60;-&#x60; *group-name* - Exclude specified group.  - (default) - Return all groups. | [optional] 
 **include_values** | **bool**| Return the value enumeration for each metadata field. | [optional] 
 **storage_group** | **str**| Storage group id.  Return only files from storages specified in the storage group. | [optional] 
 **track** | [**list[str]**](str.md)| Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is &#x60;A2&#x60;.  - *track-type* *t1* &#x60;-&#x60; *t2* - Return metadata for specified track interval, e. g.  &#x60;A2-4&#x60;.  - *track-type* &#x60;*&#x60; - Return metadata for all tracks of specified type, e. g.  &#x60;A*&#x60;.  - &#x60;generic&#x60; - Return all non-tracked metadata.  - &#x60;all&#x60; (default) - All metadata, with or without track specification, are returned. | [optional] [default to [&quot;all&quot;]]
 **conflict** | **str**| - &#x60;yes&#x60; (default) - Include all metadata conflicts, unresolved.  - &#x60;no&#x60; - Return conflicts resolved according to field rules. | [optional] [default to &#39;yes&#39;]
 **content** | [**list[str]**](str.md)| Comma-separated list of the types of content to retrieve. | [optional] 
 **merged_extradata** | **str**| Any possible extra data. | [optional] 
 **include_transient_metadata** | **bool**| - &#x60;true&#x60; (default) - Include transient metadata.  - &#x60;false&#x60; - Do not include transient metadata in response. | [optional] [default to True]
 **merged_type** | **str**| The type of operation to check for. | [optional] 
 **default_value** | **bool**| - &#x60;true&#x60; - For unset fields, return default values.  - &#x60;false&#x60; (default) - Do not return default values. | [optional] [default to False]
 **tag** | **str**| A URI parameter: Comma-separated list of shape tags to return. | [optional] 
 **field** | [**list[str]**](str.md)| Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \&quot;:\&quot; *new-name* - Return specified field, renamed to a new name in return value.  - \&quot;-\&quot; *field-name* - Exclude specified field.  - (default) - Return all fields. | [optional] 
 **include** | **str**| A list of keys.   Includes additional field specific data.  Additionally, if set to &#x60;type&#x60; the type definition of the field will be retrieved. | [optional] 
 **method_type** | **str**| Access method.   - &#x60;AUTO&#x60; - Gives an APInoauth URI to the media.  Access to file is tunneled through Vidispine.  - &#x60;AZURE_SAS&#x60; - If the storage schema is azure:// you can get direct access to the media.  The resulting URI will not tunnel through Vidispine but rather point directly to the media location at the azure storage. | [optional] 
 **p** | [**list[str]**](str.md)| Comma-separated list of paths specifying the content to include.  Overrides the content and filter parameters. | [optional] 
 **base_uri** | **str**| Which base URI to use for the thumbnail URLs. | [optional] 
 **uri_type** | [**list[str]**](str.md)| Comma-separated list of format types (container format) to return. | [optional] 
 **storage** | [**list[str]**](str.md)| List of storage ids.  Return only files from specific storages.  Can be specified multiple times. | [optional] 
 **revision** | **str**| Specifying which metadata revision to display.  Only used if requesting a single item or collection. | [optional] 
 **scheme** | **str**| URI scheme to return. | [optional] 
 **version** | **str**| Specifying which essence version to return for shapes.  If special value &#x60;all&#x60;, display all versions.  If special value &#x60;latest&#x60; (default), display latest version of shapes. | [optional] 
 **merged_permission** | **str**| The lowest required permission level. | [optional] 
 **sample_rate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **count** | **bool**| - &#x60;true&#x60; (default) - Return hits in result.  - &#x60;false&#x60; - Do not return hits in result, in order to produce results faster. | [optional] [default to True]
 **save** | **bool**| - &#x60;true&#x60; - Returns a &#x60;303 See Other&#x60;, with a &#x60;Location&#x60; header containing an URI to fetch the search result - &#x60;false&#x60; (default) - Returns a regular search result | [optional] 
 **noauth_url** | **bool**| - &#x60;true&#x60; Return URIs that do not need authentication.  - &#x60;false&#x60; (default) Return normal URIs | [optional] 

### Return type

[**SearchResultType**](SearchResultType.md)

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

# **search_files**
> FileListType search_files(file_search_type, storage_type=storage_type, first=first, method_metadata=method_metadata, save=save, count=count, number=number, scheme=scheme, method_type=method_type)

Search files

Searches files. Using GET is identical as performing a search with an empty search document.

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
api_instance = vidispine.SearchApi(vidispine.ApiClient(configuration))
file_search_type = vidispine.FileSearchType() # FileSearchType | 
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
first = 1 # int | From the resulting list of items, start return list from specified offset. (optional) (default to 1)
method_metadata = ['method_metadata_example'] # list[str] | metadata used with storage method. (optional)
save = True # bool | - `true` - Returns a `303 See Other`, with a `Location` header containing an URI to fetch the search result - `false` (default) - Returns a regular search result (optional)
count = True # bool | - `true` (default) - Return hits in result.  - `false` - Do not return hits in result, in order to produce results faster. (optional) (default to True)
number = 100 # int | The number of entities to fetch. (optional) (default to 100)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
method_type = 'method_type_example' # str | Return URIs from storage methods with a particular type.  By default, return URLs with empty `methodType`. (optional)

try:
    # Search files
    api_response = api_instance.search_files(file_search_type, storage_type=storage_type, first=first, method_metadata=method_metadata, save=save, count=count, number=number, scheme=scheme, method_type=method_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_search_type** | [**FileSearchType**](FileSearchType.md)|  | 
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **first** | **int**| From the resulting list of items, start return list from specified offset. | [optional] [default to 1]
 **method_metadata** | [**list[str]**](str.md)| metadata used with storage method. | [optional] 
 **save** | **bool**| - &#x60;true&#x60; - Returns a &#x60;303 See Other&#x60;, with a &#x60;Location&#x60; header containing an URI to fetch the search result - &#x60;false&#x60; (default) - Returns a regular search result | [optional] 
 **count** | **bool**| - &#x60;true&#x60; (default) - Return hits in result.  - &#x60;false&#x60; - Do not return hits in result, in order to produce results faster. | [optional] [default to True]
 **number** | **int**| The number of entities to fetch. | [optional] [default to 100]
 **scheme** | **str**| URI scheme to return. | [optional] 
 **method_type** | **str**| Return URIs from storage methods with a particular type.  By default, return URLs with empty &#x60;methodType&#x60;. | [optional] 

### Return type

[**FileListType**](FileListType.md)

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

# **search_shapes**
> ShapeListType search_shapes(shape_search_type, storage_type=storage_type, first=first, content=content, number=number, scheme=scheme, count=count, save=save, method_metadata=method_metadata, method_type=method_type)

Search shapes

Searches shapes. Using GET is identical as performing a search with an empty search document.

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
api_instance = vidispine.SearchApi(vidispine.ApiClient(configuration))
shape_search_type = vidispine.ShapeSearchType() # ShapeSearchType | 
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
first = 1 # int | From the resulting list of items, start return list from specified offset. (optional) (default to 1)
content = ['content_example'] # list[str] | Comma-separated list of the types of content to retrieve. (optional)
number = 100 # int | The number of entities to fetch. (optional) (default to 100)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
count = True # bool | - `true` (default) - Return hits in result.  - `false` - Do not return hits in result, in order to produce results faster. (optional) (default to True)
save = True # bool | - `true` - Returns a `303 See Other`, with a `Location` header containing an URI to fetch the search result - `false` (default) - Returns a regular search result (optional)
method_metadata = ['method_metadata_example'] # list[str] | metadata used with storage method. (optional)
method_type = 'method_type_example' # str | Return URIs from storage methods with a particular type.  By default, return URLs with empty `methodType`. (optional)

try:
    # Search shapes
    api_response = api_instance.search_shapes(shape_search_type, storage_type=storage_type, first=first, content=content, number=number, scheme=scheme, count=count, save=save, method_metadata=method_metadata, method_type=method_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_shapes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shape_search_type** | [**ShapeSearchType**](ShapeSearchType.md)|  | 
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **first** | **int**| From the resulting list of items, start return list from specified offset. | [optional] [default to 1]
 **content** | [**list[str]**](str.md)| Comma-separated list of the types of content to retrieve. | [optional] 
 **number** | **int**| The number of entities to fetch. | [optional] [default to 100]
 **scheme** | **str**| URI scheme to return. | [optional] 
 **count** | **bool**| - &#x60;true&#x60; (default) - Return hits in result.  - &#x60;false&#x60; - Do not return hits in result, in order to produce results faster. | [optional] [default to True]
 **save** | **bool**| - &#x60;true&#x60; - Returns a &#x60;303 See Other&#x60;, with a &#x60;Location&#x60; header containing an URI to fetch the search result - &#x60;false&#x60; (default) - Returns a regular search result | [optional] 
 **method_metadata** | [**list[str]**](str.md)| metadata used with storage method. | [optional] 
 **method_type** | **str**| Return URIs from storage methods with a particular type.  By default, return URLs with empty &#x60;methodType&#x60;. | [optional] 

### Return type

[**ShapeListType**](ShapeListType.md)

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

