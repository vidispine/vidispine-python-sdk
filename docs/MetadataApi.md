# vidispine.MetadataApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_metadata_change_sets**](MetadataApi.md#compare_metadata_change_sets) | **GET** /{type}/{entity-id}/metadata/changes/{changeset-id}/compareTo/{from-changeset-id} | Compare two change sets
[**delete_metadata_change_set**](MetadataApi.md#delete_metadata_change_set) | **DELETE** /{type}/{entity-id}/metadata/changes/{changeset-id} | Delete a change set
[**get_metadata**](MetadataApi.md#get_metadata) | **GET** /{type}/{entity-id}/metadata | Retrieve metadata
[**get_metadata_change_set**](MetadataApi.md#get_metadata_change_set) | **GET** /{type}/{entity-id}/metadata/changes/{changeset-id} | Retrieve a change set
[**get_metadata_change_sets**](MetadataApi.md#get_metadata_change_sets) | **GET** /{type}/{entity-id}/metadata/changes | List all change sets
[**get_metadata_graph**](MetadataApi.md#get_metadata_graph) | **GET** /{type}/{entity-id}/metadata/graph | Retrieve the metadata graph
[**get_metadata_graph_dot**](MetadataApi.md#get_metadata_graph_dot) | **GET** /{type}/{entity-id}/metadata/graph/dot | Retrieve the metadata graph as dot file
[**get_subtitles_scc**](MetadataApi.md#get_subtitles_scc) | **GET** /item/{id}/metadata/export/scc | Export to SCC
[**get_subtitles_ttml**](MetadataApi.md#get_subtitles_ttml) | **GET** /item/{id}/metadata/export/ttml | Export to TTML
[**move_metadata**](MetadataApi.md#move_metadata) | **PUT** /{type}/{entity-id}/metadata/move | Move metadata
[**trim_metadata_change_set**](MetadataApi.md#trim_metadata_change_set) | **PUT** /{type}/{entity-id}/metadata/changes/{changeset-id}/trim | Trim a change set
[**trim_metadata_change_sets**](MetadataApi.md#trim_metadata_change_sets) | **PUT** /{type}/{entity-id}/metadata/changes/trim | Trim multiple change sets
[**update_metadata**](MetadataApi.md#update_metadata) | **PUT** /{type}/{entity-id}/metadata | Create a metadata change set
[**update_metadata_change_set**](MetadataApi.md#update_metadata_change_set) | **PUT** /{type}/{entity-id}/metadata/changes/{changeset-id} | Update a change set
[**update_metadata_change_sets**](MetadataApi.md#update_metadata_change_sets) | **PUT** /{type}/{entity-id}/metadata/changes | Update multiple change sets
[**update_metadata_entries**](MetadataApi.md#update_metadata_entries) | **PUT** /{type}/{entity-id}/metadata/entry | Modify multiple metadata entries
[**update_metadata_entry**](MetadataApi.md#update_metadata_entry) | **PUT** /{type}/{entity-id}/metadata/entry/{entry-uuid} | Modify a metadata entry


# **compare_metadata_change_sets**
> MetadataType compare_metadata_change_sets(from_changeset_id, type, entity_id, changeset_id, language=language, track=track, conflict=conflict, samplerate=samplerate, values_by_uuid=values_by_uuid, default_value=default_value, interval=interval, group=group, field=field, include=include)

Compare two change sets

Retrieves a metadata document containing the differences between the entity metadata as of revision `changeset-id` compared to the metadata as of revision `from-changeset-id`.  The `mode` attribute is used to indicate if a field, field group or value has been added or removed.  Note: This should be seen as a diff between the metadata as it was between the two revisions, meaning that for example fields or field groups that have been added and then removed in between will not be shown.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
from_changeset_id = 'from_changeset_id_example' # str | The id of the change set to compare against.  Use `previous` to compare with the preceding change set.
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
changeset_id = 'changeset_id_example' # str | The changeset id.
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
samplerate = 'samplerate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
values_by_uuid = True # bool | If `true` (default) then field values will be compared by uuid, if `false` then by the value itself. (optional)
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = 'include_example' # str | A list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)

try:
    # Compare two change sets
    api_response = api_instance.compare_metadata_change_sets(from_changeset_id, type, entity_id, changeset_id, language=language, track=track, conflict=conflict, samplerate=samplerate, values_by_uuid=values_by_uuid, default_value=default_value, interval=interval, group=group, field=field, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->compare_metadata_change_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_changeset_id** | **str**| The id of the change set to compare against.  Use &#x60;previous&#x60; to compare with the preceding change set. | 
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **changeset_id** | **str**| The changeset id. | 
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **track** | [**list[str]**](str.md)| Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is &#x60;A2&#x60;.  - *track-type* *t1* &#x60;-&#x60; *t2* - Return metadata for specified track interval, e. g.  &#x60;A2-4&#x60;.  - *track-type* &#x60;*&#x60; - Return metadata for all tracks of specified type, e. g.  &#x60;A*&#x60;.  - &#x60;generic&#x60; - Return all non-tracked metadata.  - &#x60;all&#x60; (default) - All metadata, with or without track specification, are returned. | [optional] [default to [&quot;all&quot;]]
 **conflict** | **str**| - &#x60;yes&#x60; (default) - Include all metadata conflicts, unresolved.  - &#x60;no&#x60; - Return conflicts resolved according to field rules. | [optional] [default to &#39;yes&#39;]
 **samplerate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **values_by_uuid** | **bool**| If &#x60;true&#x60; (default) then field values will be compared by uuid, if &#x60;false&#x60; then by the value itself. | [optional] 
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

# **delete_metadata_change_set**
> MetadataType delete_metadata_change_set(type, entity_id, changeset_id)

Delete a change set

Deletes an entire change set.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
changeset_id = 'changeset_id_example' # str | The changeset id.

try:
    # Delete a change set
    api_response = api_instance.delete_metadata_change_set(type, entity_id, changeset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->delete_metadata_change_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **changeset_id** | **str**| The changeset id. | 

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
**0** | A &lt;em&gt;MetadataDocument&lt;/em&gt; containing the metadata of the item. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> MetadataListType get_metadata(type, entity_id, language=language, include_constraint_value=include_constraint_value, track=track, to=to, conflict=conflict, _from=_from, include_transient_metadata=include_transient_metadata, starttc=starttc, projection=projection, terse=terse, samplerate=samplerate, revision=revision, default_value=default_value, interval=interval, group=group, field=field, include=include)

Retrieve metadata

Returns the metadata set for an entity. This means all metadata change sets, combined, and then filtered according to query parameters.  Conflicts are normally returned with all possible values. With conflict=no, a user interface may choose to receive only one value; i.e., automatic conflict resolution will be enforced. The conflict resolution is only applied to the returned XML document, not to metadata in database.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
language = ["all"] # list[str] | Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  `en_US`.  Wildcards may be used, e. g.  `*_CA` for both Canadian French and Canadian English.  - `none` - Return all metadata without language specification.  - `all` (default) - Return all metadata, with or without language specification. (optional) (default to ["all"])
include_constraint_value = ["all"] # list[str] | Comma-separated list of fields whose \"display value\" should be retrieved from the metadata dataset.   - `all` (default) - Return the \"display value\" of all fields.  - `none` - No \"display value\" will be returned.  The fields will only have `id` set.  - *comma-separated field names* - Return the \"display value\" of the specified fields. (optional) (default to ["all"])
track = ["all"] # list[str] | Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is `A2`.  - *track-type* *t1* `-` *t2* - Return metadata for specified track interval, e. g.  `A2-4`.  - *track-type* `*` - Return metadata for all tracks of specified type, e. g.  `A*`.  - `generic` - Return all non-tracked metadata.  - `all` (default) - All metadata, with or without track specification, are returned. (optional) (default to ["all"])
to = 'to_example' # str | (only supported in item metadata) A timestamp value.  Return metadata until the specific timestamp (non-inclusive) (optional)
conflict = 'yes' # str | - `yes` (default) - Include all metadata conflicts, unresolved.  - `no` - Return conflicts resolved according to field rules. (optional) (default to 'yes')
_from = '_from_example' # str | (only supported in item metadata) A timestamp value.  Return metadata starting from the specific timestamp (inclusive) (optional)
include_transient_metadata = True # bool | - `true` (default) - Include transient metadata.  - `false` - Do not include transient metadata in response. (optional) (default to True)
starttc = False # bool | - `true` - Interval is given relative to start timecode of item.  - `false` (default) - Interval is 0-based. (optional) (default to False)
projection = 'default' # str | (only supported in item metadata) Return metadata set according to projection. (optional) (default to 'default')
terse = 'terse_example' # str | (only supported in item metadata)  - `yes` - Return metadata in terse format - `no` (default) - Return metadata in verbose format (optional)
samplerate = 'samplerate_example' # str | Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. (optional)
revision = 'revision_example' # str | A *change-set-id*, retrieves metadata the way it looked at the given revision. (optional)
default_value = False # bool | - `true` - For unset fields, return default values.  - `false` (default) - Do not return default values. (optional) (default to False)
interval = ["all"] # list[str] | Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - `generic` - Return all non-timed metadata.  - `all` (default) - Return all metadata, same as `interval=generic,-INF-+INF` (optional) (default to ["all"])
group = ['group_example'] # list[str] | Comma-separated list.   - *group-name* - Return specified group.  - *group-name* `+` - Return specified group and subgroups.  - *group-name* `:` *new-name* - Return specified group, renamed to a new name in return value.  - `-` *group-name* - Exclude specified group.  - (default) - Return all groups. (optional)
field = ['field_example'] # list[str] | Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \":\" *new-name* - Return specified field, renamed to a new name in return value.  - \"-\" *field-name* - Exclude specified field.  - (default) - Return all fields. (optional)
include = ['include_example'] # list[str] | Comma-separated list of keys.   Includes additional field specific data.  Additionally, if set to `type` the type definition of the field will be retrieved. (optional)

try:
    # Retrieve metadata
    api_response = api_instance.get_metadata(type, entity_id, language=language, include_constraint_value=include_constraint_value, track=track, to=to, conflict=conflict, _from=_from, include_transient_metadata=include_transient_metadata, starttc=starttc, projection=projection, terse=terse, samplerate=samplerate, revision=revision, default_value=default_value, interval=interval, group=group, field=field, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **language** | [**list[str]**](str.md)| Comma-separated list.   - *language-tag* - Return metadata for specific language, e. g.  &#x60;en_US&#x60;.  Wildcards may be used, e. g.  &#x60;*_CA&#x60; for both Canadian French and Canadian English.  - &#x60;none&#x60; - Return all metadata without language specification.  - &#x60;all&#x60; (default) - Return all metadata, with or without language specification. | [optional] [default to [&quot;all&quot;]]
 **include_constraint_value** | [**list[str]**](str.md)| Comma-separated list of fields whose \&quot;display value\&quot; should be retrieved from the metadata dataset.   - &#x60;all&#x60; (default) - Return the \&quot;display value\&quot; of all fields.  - &#x60;none&#x60; - No \&quot;display value\&quot; will be returned.  The fields will only have &#x60;id&#x60; set.  - *comma-separated field names* - Return the \&quot;display value\&quot; of the specified fields. | [optional] [default to [&quot;all&quot;]]
 **track** | [**list[str]**](str.md)| Comma-separated list.   - *track-type* *track-number* - Return metadata for specified track.  Example of track is &#x60;A2&#x60;.  - *track-type* *t1* &#x60;-&#x60; *t2* - Return metadata for specified track interval, e. g.  &#x60;A2-4&#x60;.  - *track-type* &#x60;*&#x60; - Return metadata for all tracks of specified type, e. g.  &#x60;A*&#x60;.  - &#x60;generic&#x60; - Return all non-tracked metadata.  - &#x60;all&#x60; (default) - All metadata, with or without track specification, are returned. | [optional] [default to [&quot;all&quot;]]
 **to** | **str**| (only supported in item metadata) A timestamp value.  Return metadata until the specific timestamp (non-inclusive) | [optional] 
 **conflict** | **str**| - &#x60;yes&#x60; (default) - Include all metadata conflicts, unresolved.  - &#x60;no&#x60; - Return conflicts resolved according to field rules. | [optional] [default to &#39;yes&#39;]
 **_from** | **str**| (only supported in item metadata) A timestamp value.  Return metadata starting from the specific timestamp (inclusive) | [optional] 
 **include_transient_metadata** | **bool**| - &#x60;true&#x60; (default) - Include transient metadata.  - &#x60;false&#x60; - Do not include transient metadata in response. | [optional] [default to True]
 **starttc** | **bool**| - &#x60;true&#x60; - Interval is given relative to start timecode of item.  - &#x60;false&#x60; (default) - Interval is 0-based. | [optional] [default to False]
 **projection** | **str**| (only supported in item metadata) Return metadata set according to projection. | [optional] [default to &#39;default&#39;]
 **terse** | **str**| (only supported in item metadata)  - &#x60;yes&#x60; - Return metadata in terse format - &#x60;no&#x60; (default) - Return metadata in verbose format | [optional] 
 **samplerate** | **str**| Convert all outgoing time instants to specified rate.  *NB!* Time codes which cannot be expressed in an integer number of samples will be returned as a decimal number, with risk of losing precision. | [optional] 
 **revision** | **str**| A *change-set-id*, retrieves metadata the way it looked at the given revision. | [optional] 
 **default_value** | **bool**| - &#x60;true&#x60; - For unset fields, return default values.  - &#x60;false&#x60; (default) - Do not return default values. | [optional] [default to False]
 **interval** | [**list[str]**](str.md)| Comma-separated list  - *time-span* - Filter out metadata, return only metadata for specified time span.  - &#x60;generic&#x60; - Return all non-timed metadata.  - &#x60;all&#x60; (default) - Return all metadata, same as &#x60;interval&#x3D;generic,-INF-+INF&#x60; | [optional] [default to [&quot;all&quot;]]
 **group** | [**list[str]**](str.md)| Comma-separated list.   - *group-name* - Return specified group.  - *group-name* &#x60;+&#x60; - Return specified group and subgroups.  - *group-name* &#x60;:&#x60; *new-name* - Return specified group, renamed to a new name in return value.  - &#x60;-&#x60; *group-name* - Exclude specified group.  - (default) - Return all groups. | [optional] 
 **field** | [**list[str]**](str.md)| Comma-separated list.   - *field-name* - Return specified field.  - *field-name* \&quot;:\&quot; *new-name* - Return specified field, renamed to a new name in return value.  - \&quot;-\&quot; *field-name* - Exclude specified field.  - (default) - Return all fields. | [optional] 
 **include** | [**list[str]**](str.md)| Comma-separated list of keys.   Includes additional field specific data.  Additionally, if set to &#x60;type&#x60; the type definition of the field will be retrieved. | [optional] 

### Return type

[**MetadataListType**](MetadataListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;ul&gt;&lt;li&gt;&lt;em&gt;MetadataListDocument&lt;/em&gt; for items&lt;/li&gt;&lt;li&gt;&lt;em&gt;MetadataDocument&lt;/em&gt; for collections&lt;/li&gt;&lt;li&gt;or according to specified outgoing projection&lt;/li&gt;&lt;/ul&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_change_set**
> MetadataChangeSetType get_metadata_change_set(type, entity_id, changeset_id)

Retrieve a change set

Retrieves a specific change set.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
changeset_id = 'changeset_id_example' # str | The changeset id.

try:
    # Retrieve a change set
    api_response = api_instance.get_metadata_change_set(type, entity_id, changeset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_metadata_change_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **changeset_id** | **str**| The changeset id. | 

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
**0** | A &lt;em&gt;MetadataChangeSetDocument&lt;/em&gt; containing the metadata from the change. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_change_sets**
> MetadataChangeSetType get_metadata_change_sets(type, entity_id, change=change, first=first, number=number)

List all change sets

Retrieves change sets that have been applied to the metadata.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
change = 'change_example' # str | Retrieve a single change set. (optional)
first = 1 # int | Return change sets from that number in the list of sorted change sets. (optional) (default to 1)
number = 0 # int | Return at most that number of change sets. (optional) (default to 0)

try:
    # List all change sets
    api_response = api_instance.get_metadata_change_sets(type, entity_id, change=change, first=first, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_metadata_change_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **change** | **str**| Retrieve a single change set. | [optional] 
 **first** | **int**| Return change sets from that number in the list of sorted change sets. | [optional] [default to 1]
 **number** | **int**| Return at most that number of change sets. | [optional] [default to 0]

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

# **get_metadata_graph**
> file get_metadata_graph(type, entity_id, group_by=group_by)

Retrieve the metadata graph

Shows fields and values and their history as a graph.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
group_by = 'change' # str | - `change` (default) - Group fields and values by change set.  - `none` - Present fields and groups without any grouping. (optional) (default to 'change')

try:
    # Retrieve the metadata graph
    api_response = api_instance.get_metadata_graph(type, entity_id, group_by=group_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_metadata_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **group_by** | **str**| - &#x60;change&#x60; (default) - Group fields and values by change set.  - &#x60;none&#x60; - Present fields and groups without any grouping. | [optional] [default to &#39;change&#39;]

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_graph_dot**
> str get_metadata_graph_dot(type, entity_id, group_by=group_by)

Retrieve the metadata graph as dot file

Shows fields and values and their history in dot format, for further processing.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
group_by = 'change' # str | - `change` (default) - Group fields and values by change set.  - `none` - Present fields and groups without any grouping. (optional) (default to 'change')

try:
    # Retrieve the metadata graph as dot file
    api_response = api_instance.get_metadata_graph_dot(type, entity_id, group_by=group_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_metadata_graph_dot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **group_by** | **str**| - &#x60;change&#x60; (default) - Group fields and values by change set.  - &#x60;none&#x60; - Present fields and groups without any grouping. | [optional] [default to &#39;change&#39;]

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/vnd.graphviz, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subtitles_scc**
> str get_subtitles_scc(id, interval=interval)

Export to SCC

Returns the subtitles from the item metadata in SCC format.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
interval = ["all"] # list[str] | Comma-separated list of time spans of subtitle metadata to export. (optional) (default to ["all"])

try:
    # Export to SCC
    api_response = api_instance.get_subtitles_scc(id, interval=interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_subtitles_scc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **interval** | [**list[str]**](str.md)| Comma-separated list of time spans of subtitle metadata to export. | [optional] [default to [&quot;all&quot;]]

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
**0** | The SCC data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subtitles_ttml**
> str get_subtitles_ttml(id, interval=interval)

Export to TTML

Generates a TTML file containing the subtitle metadata from a specific item.  The output TTML file obeys EBU-TT standard (EBU Tech 3360)  An optional offset can be applied to the time span by adding \":\" and the offset.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
interval = ["all"] # list[str] | Comma-separated list of time spans of subtitle metadata to export. (optional) (default to ["all"])

try:
    # Export to TTML
    api_response = api_instance.get_subtitles_ttml(id, interval=interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_subtitles_ttml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **interval** | [**list[str]**](str.md)| Comma-separated list of time spans of subtitle metadata to export. | [optional] [default to [&quot;all&quot;]]

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
**0** | The TTML XML. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_metadata**
> MetadataType move_metadata(type, uuid, entity_id, end=end, start=start)

Move metadata

Moves the specified field or group from one timespan to another. There are some restrictions to this operation:

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
uuid = 'uuid_example' # str | The UUID of the element.
entity_id = 'entity_id_example' # str | The entity id.
end = 'end_example' # str | The new end time code (optional)
start = 'start_example' # str | The new start time code (optional)

try:
    # Move metadata
    api_response = api_instance.move_metadata(type, uuid, entity_id, end=end, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->move_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **uuid** | **str**| The UUID of the element. | 
 **entity_id** | **str**| The entity id. | 
 **end** | **str**| The new end time code | [optional] 
 **start** | **str**| The new start time code | [optional] 

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

# **trim_metadata_change_set**
> MetadataChangeSetType trim_metadata_change_set(type, entity_id, changeset_id)

Trim a change set

Removes fields and values from the change set(s) that did not result in an actual change of the metadata.  Note that if all fields of a change set are removed, then the change set will also be removed.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
changeset_id = 'changeset_id_example' # str | The changeset id.

try:
    # Trim a change set
    api_response = api_instance.trim_metadata_change_set(type, entity_id, changeset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->trim_metadata_change_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **changeset_id** | **str**| The changeset id. | 

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
**0** | A &lt;em&gt;MetadataChangeSetDocument&lt;/em&gt; containing a list of the modified change sets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trim_metadata_change_sets**
> MetadataChangeSetType trim_metadata_change_sets(type, entity_id)

Trim multiple change sets

Removes fields and values from the change set(s) that did not result in an actual change of the metadata.  Note that if all fields of a change set are removed, then the change set will also be removed.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.

try:
    # Trim multiple change sets
    api_response = api_instance.trim_metadata_change_sets(type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->trim_metadata_change_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 

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
**0** | A &lt;em&gt;MetadataChangeSetDocument&lt;/em&gt; containing a list of the modified change sets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata**
> MetadataListType update_metadata(type, entity_id, metadata_type, revision=revision, only_return_changes=only_return_changes, projection=projection, output_projection=output_projection, skip_forbidden=skip_forbidden)

Create a metadata change set

Sets the metadata for an entity, or, more specifically, creates a metadata change set for an entity.  The metadata change set binds to different intervals, tracks, and languages, which can be specified either in the URL or in the XML. Providing an empty timespan or an empty field will be interpreted as the removal of any existing element that matches. Fields specified by the system will not be removed by this action.  The revision can either be specified in the input XML/JSON or as a query parameter. If it is not set at all, it will attempt to override any existing values.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
metadata_type = vidispine.MetadataType() # MetadataType | <em>MetadataDocument</em> or according to specified projection
revision = 'revision_example' # str | The known revision.  If not specified, the change set will attempt to override existing change sets. (optional)
only_return_changes = False # bool | New in version 4. 16. 6.   - `true` - Only return the changed entries.  - `false` (default) - Return the whole global metadata after the update. (optional) (default to False)
projection = 'default' # str | (only supported in item metadata) Sets metadata set according to projection (optional) (default to 'default')
output_projection = 'default' # str | (only supported in item metadata) Returns metadata according to projection (optional) (default to 'default')
skip_forbidden = False # bool | Skip fields or groups that the user doesn't have write access to (optional) (default to False)

try:
    # Create a metadata change set
    api_response = api_instance.update_metadata(type, entity_id, metadata_type, revision=revision, only_return_changes=only_return_changes, projection=projection, output_projection=output_projection, skip_forbidden=skip_forbidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **metadata_type** | [**MetadataType**](MetadataType.md)| &lt;em&gt;MetadataDocument&lt;/em&gt; or according to specified projection | 
 **revision** | **str**| The known revision.  If not specified, the change set will attempt to override existing change sets. | [optional] 
 **only_return_changes** | **bool**| New in version 4. 16. 6.   - &#x60;true&#x60; - Only return the changed entries.  - &#x60;false&#x60; (default) - Return the whole global metadata after the update. | [optional] [default to False]
 **projection** | **str**| (only supported in item metadata) Sets metadata set according to projection | [optional] [default to &#39;default&#39;]
 **output_projection** | **str**| (only supported in item metadata) Returns metadata according to projection | [optional] [default to &#39;default&#39;]
 **skip_forbidden** | **bool**| Skip fields or groups that the user doesn&#39;t have write access to | [optional] [default to False]

### Return type

[**MetadataListType**](MetadataListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;ul&gt;&lt;li&gt;&lt;em&gt;MetadataListDocument&lt;/em&gt; for items&lt;/li&gt;&lt;li&gt;&lt;em&gt;MetadataDocument&lt;/em&gt; for collections&lt;/li&gt;&lt;li&gt;or according to specified outgoing projection&lt;/li&gt;&lt;/ul&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_change_set**
> MetadataType update_metadata_change_set(type, entity_id, changeset_id, metadata_type)

Update a change set

Replaces the contents of a change set with the specified id with the metadata given in the document.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
changeset_id = 'changeset_id_example' # str | The changeset id.
metadata_type = vidispine.MetadataType() # MetadataType | A <em>MetadataDocument</em> containing the new version of the change set.

try:
    # Update a change set
    api_response = api_instance.update_metadata_change_set(type, entity_id, changeset_id, metadata_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata_change_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **changeset_id** | **str**| The changeset id. | 
 **metadata_type** | [**MetadataType**](MetadataType.md)| A &lt;em&gt;MetadataDocument&lt;/em&gt; containing the new version of the change set. | 

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
**0** | A &lt;em&gt;MetadataDocument&lt;/em&gt; containing the metadata of the item. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_change_sets**
> MetadataChangeSetType update_metadata_change_sets(type, entity_id, metadata_change_set_type)

Update multiple change sets

Replaces the metadata in the specified change sets with the given data.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
metadata_change_set_type = vidispine.MetadataChangeSetType() # MetadataChangeSetType | A <em>MetadataChangeSetDocument</em> containing the change sets that should be modified.

try:
    # Update multiple change sets
    api_response = api_instance.update_metadata_change_sets(type, entity_id, metadata_change_set_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata_change_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **metadata_change_set_type** | [**MetadataChangeSetType**](MetadataChangeSetType.md)| A &lt;em&gt;MetadataChangeSetDocument&lt;/em&gt; containing the change sets that should be modified. | 

### Return type

[**MetadataChangeSetType**](MetadataChangeSetType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;MetadataChangeSetDocument&lt;/em&gt; containing a list of the modified change sets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_entries**
> MetadataType update_metadata_entries(type, entity_id, metadata_entry_list_type2)

Modify multiple metadata entries

Modifies multiple metadata fields/groups/values by UUID.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
metadata_entry_list_type2 = vidispine.MetadataEntryListType2() # MetadataEntryListType2 | 

try:
    # Modify multiple metadata entries
    api_response = api_instance.update_metadata_entries(type, entity_id, metadata_entry_list_type2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **metadata_entry_list_type2** | [**MetadataEntryListType2**](MetadataEntryListType2.md)|  | 

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

# **update_metadata_entry**
> MetadataType update_metadata_entry(type, entity_id, entry_uuid, metadata_entry_type)

Modify a metadata entry

Modifies a specific metadata field/group/value by UUID.

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
api_instance = vidispine.MetadataApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
entry_uuid = 'entry_uuid_example' # str | The entry uuid.
metadata_entry_type = vidispine.MetadataEntryType() # MetadataEntryType | 

try:
    # Modify a metadata entry
    api_response = api_instance.update_metadata_entry(type, entity_id, entry_uuid, metadata_entry_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **entry_uuid** | **str**| The entry uuid. | 
 **metadata_entry_type** | [**MetadataEntryType**](MetadataEntryType.md)|  | 

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

