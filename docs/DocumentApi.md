# vidispine.DocumentApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document**](DocumentApi.md#delete_document) | **DELETE** /document/{name} | Delete a document
[**get_document**](DocumentApi.md#get_document) | **GET** /document/{name} | Retrieve a document
[**get_document_change_sets**](DocumentApi.md#get_document_change_sets) | **GET** /document/{name}/changes | View change sets
[**get_documents**](DocumentApi.md#get_documents) | **GET** /document | List all documents
[**search_documents**](DocumentApi.md#search_documents) | **PUT** /document | Search for documents
[**update_or_create_document**](DocumentApi.md#update_or_create_document) | **PUT** /document/{name} | Update or creates a document


# **delete_document**
> delete_document(name)

Delete a document

Removes the metadata document with the specified name.

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
api_instance = vidispine.DocumentApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.

try:
    # Delete a document
    api_instance.delete_document(name)
except ApiException as e:
    print("Exception when calling DocumentApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name. | 

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

# **get_document**
> MetadataType get_document(name, language=language, track=track, conflict=conflict, samplerate=samplerate, default_value=default_value, interval=interval, group=group, field=field, include=include)

Retrieve a document

Retrieves the document with the specified name. This resource shares the same query parameters as the item metadata resource.

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
api_instance = vidispine.DocumentApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
samplerate = 'samplerate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = 'include_example' # str | A list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)

try:
    # Retrieve a document
    api_response = api_instance.get_document(name, language=language, track=track, conflict=conflict, samplerate=samplerate, default_value=default_value, interval=interval, group=group, field=field, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name. | 
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
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

# **get_document_change_sets**
> MetadataChangeSetType get_document_change_sets(name, change=change, first=first, number=number)

View change sets

Retrieves all change sets that have been applied to the document.

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
api_instance = vidispine.DocumentApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.
change = 'change_example' # str | Retrieve a single change set. (optional)
first = 1 # int | Return change sets from that number in the list of sorted change sets. (optional) (default to 1)
number = 56 # int | Return at most that number of change sets.  Default is all change sets. (optional)

try:
    # View change sets
    api_response = api_instance.get_document_change_sets(name, change=change, first=first, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_document_change_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name. | 
 **change** | **str**| Retrieve a single change set. | [optional] 
 **first** | **int**| Return change sets from that number in the list of sorted change sets. | [optional] [default to 1]
 **number** | **int**| Return at most that number of change sets.  Default is all change sets. | [optional] 

### Return type

[**MetadataChangeSetType**](MetadataChangeSetType.md)

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

# **get_documents**
> DocumentListType get_documents(first=first, number=number)

List all documents

Retrieves the list of metadata documents.

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
api_instance = vidispine.DocumentApi(vidispine.ApiClient(configuration))
first = 1 # int | Return documents from that number in the document list. (optional) (default to 1)
number = 100 # int | Return at most that number of documents. (optional) (default to 100)

try:
    # List all documents
    api_response = api_instance.get_documents(first=first, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first** | **int**| Return documents from that number in the document list. | [optional] [default to 1]
 **number** | **int**| Return at most that number of documents. | [optional] [default to 100]

### Return type

[**DocumentListType**](DocumentListType.md)

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

# **search_documents**
> SearchResultType search_documents(item_search_type, first=first, count=count, number=number)

Search for documents

Searches for documents matching a provided *ItemSearchDocument*.  Note that document indexing is disabled by default. Make sure to enable document indexing using `indexDocumentMetadata` and trigger a reindex so that any existing documents are added to the index.  New in version 5.0.

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
api_instance = vidispine.DocumentApi(vidispine.ApiClient(configuration))
item_search_type = vidispine.ItemSearchType() # ItemSearchType | 
first = 1 # int | Start returning results from this index. (optional) (default to 1)
count = True # bool | - `true` (default) - Return hits in result.  - `false` - Do not return hits in result, in order to produce results faster. (optional) (default to True)
number = 100 # int | Return at most this number of documents. (optional) (default to 100)

try:
    # Search for documents
    api_response = api_instance.search_documents(item_search_type, first=first, count=count, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->search_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_search_type** | [**ItemSearchType**](ItemSearchType.md)|  | 
 **first** | **int**| Start returning results from this index. | [optional] [default to 1]
 **count** | **bool**| - &#x60;true&#x60; (default) - Return hits in result.  - &#x60;false&#x60; - Do not return hits in result, in order to produce results faster. | [optional] [default to True]
 **number** | **int**| Return at most this number of documents. | [optional] [default to 100]

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

# **update_or_create_document**
> MetadataType update_or_create_document(name, metadata_type, revision=revision, skip_forbidden=skip_forbidden)

Update or creates a document

Creates a new or modifies the existing document with the specified name.

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
api_instance = vidispine.DocumentApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.
metadata_type = vidispine.MetadataType() # MetadataType | 
revision = 'revision_example' # str | The known revision.  If not specified, the change set will attempt to override existing change sets. (optional)
skip_forbidden = False # bool | Skip fields or groups that the user doesn't have write access to. (optional) (default to False)

try:
    # Update or creates a document
    api_response = api_instance.update_or_create_document(name, metadata_type, revision=revision, skip_forbidden=skip_forbidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentApi->update_or_create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name. | 
 **metadata_type** | [**MetadataType**](MetadataType.md)|  | 
 **revision** | **str**| The known revision.  If not specified, the change set will attempt to override existing change sets. | [optional] 
 **skip_forbidden** | **bool**| Skip fields or groups that the user doesn&#39;t have write access to. | [optional] [default to False]

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

