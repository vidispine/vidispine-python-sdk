# vidispine.RelationApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_relation**](RelationApi.md#create_item_relation) | **POST** /item/{id1}/relation/{id2} | Create an item relation
[**create_item_relations**](RelationApi.md#create_item_relations) | **POST** /relation | Create multiple item relations
[**delete_item_relation**](RelationApi.md#delete_item_relation) | **DELETE** /relation/{relation-id} | Delete an item relation
[**delete_item_relations**](RelationApi.md#delete_item_relations) | **DELETE** /item/{id}/relation | Delete all item relations
[**delete_item_to_item_relation**](RelationApi.md#delete_item_to_item_relation) | **DELETE** /item/{id1}/relation/{id2} | Delete all relations between two items
[**get_item_relation**](RelationApi.md#get_item_relation) | **GET** /relation/{relation-id} | Retrieve an item relation
[**get_item_relations**](RelationApi.md#get_item_relations) | **GET** /item/{id}/relation | List all item relations
[**update_item_relation**](RelationApi.md#update_item_relation) | **PUT** /relation/{relation-id} | Update an item relation


# **create_item_relation**
> ItemRelationType create_item_relation(direction, id1, id2, allow_duplicate=allow_duplicate)

Create an item relation

Generates a new relation between the two items with the given ids, `id1` and `id2`, with the given parameters.  In addition, extra query parameters of the form `key=value` can be added, to set metadata of the item-to-item relation.

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
api_instance = vidispine.RelationApi(vidispine.ApiClient(configuration))
direction = 'direction_example' # str | - `U` - Set the direction of the relation as undirectional.  - `S` - Set the direction as `id1` being the source and `id2` being the target.  - `T` - Set the direction as `id2` being the source and `id1` being the target.
id1 = 'id1_example' # str | The id1.
id2 = 'id2_example' # str | The id2.
allow_duplicate = True # bool | - `true` (default) - Allow duplicate relations.  - `false` - Avoid adding duplicate relations. (optional) (default to True)

try:
    # Create an item relation
    api_response = api_instance.create_item_relation(direction, id1, id2, allow_duplicate=allow_duplicate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationApi->create_item_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**| - &#x60;U&#x60; - Set the direction of the relation as undirectional.  - &#x60;S&#x60; - Set the direction as &#x60;id1&#x60; being the source and &#x60;id2&#x60; being the target.  - &#x60;T&#x60; - Set the direction as &#x60;id2&#x60; being the source and &#x60;id1&#x60; being the target. | 
 **id1** | **str**| The id1. | 
 **id2** | **str**| The id2. | 
 **allow_duplicate** | **bool**| - &#x60;true&#x60; (default) - Allow duplicate relations.  - &#x60;false&#x60; - Avoid adding duplicate relations. | [optional] [default to True]

### Return type

[**ItemRelationType**](ItemRelationType.md)

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

# **create_item_relations**
> ItemRelationListType create_item_relations(item_relation_list_type, allow_duplicate=allow_duplicate)

Create multiple item relations

Generates multiple relations at once. Each relation has a `source` and a `target`, and the direction can take the value `U`, if not set it generates a directional relation from `source` to `target`.  For example:

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
api_instance = vidispine.RelationApi(vidispine.ApiClient(configuration))
item_relation_list_type = vidispine.ItemRelationListType() # ItemRelationListType | 
allow_duplicate = True # bool | - `true` (default) - Allow duplicate relations.  - `false` - Avoid adding duplicate relations. (optional) (default to True)

try:
    # Create multiple item relations
    api_response = api_instance.create_item_relations(item_relation_list_type, allow_duplicate=allow_duplicate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationApi->create_item_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_relation_list_type** | [**ItemRelationListType**](ItemRelationListType.md)|  | 
 **allow_duplicate** | **bool**| - &#x60;true&#x60; (default) - Allow duplicate relations.  - &#x60;false&#x60; - Avoid adding duplicate relations. | [optional] [default to True]

### Return type

[**ItemRelationListType**](ItemRelationListType.md)

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

# **delete_item_relation**
> delete_item_relation(relation_id)

Delete an item relation

Deletes the relation with the id `relation-id`.

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
api_instance = vidispine.RelationApi(vidispine.ApiClient(configuration))
relation_id = 'relation_id_example' # str | The relation id.

try:
    # Delete an item relation
    api_instance.delete_item_relation(relation_id)
except ApiException as e:
    print("Exception when calling RelationApi->delete_item_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | **str**| The relation id. | 

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

# **delete_item_relations**
> delete_item_relations(id, direction=direction)

Delete all item relations

Deletes the relations with the specified direction or all relations.

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
api_instance = vidispine.RelationApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
direction = 'direction_example' # str | - `A` - This is the default value.  Deletes all relations `id1` is involved in.  - `U` - Deletes only the relations with the direction as undirectional.  - `S` - Deletes only the relations where `id1` is the source and `id2` is the target.  - `T` - Deletes only the relations where `id2` is the source and `id1` is the target. (optional)

try:
    # Delete all item relations
    api_instance.delete_item_relations(id, direction=direction)
except ApiException as e:
    print("Exception when calling RelationApi->delete_item_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **direction** | **str**| - &#x60;A&#x60; - This is the default value.  Deletes all relations &#x60;id1&#x60; is involved in.  - &#x60;U&#x60; - Deletes only the relations with the direction as undirectional.  - &#x60;S&#x60; - Deletes only the relations where &#x60;id1&#x60; is the source and &#x60;id2&#x60; is the target.  - &#x60;T&#x60; - Deletes only the relations where &#x60;id2&#x60; is the source and &#x60;id1&#x60; is the target. | [optional] 

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

# **delete_item_to_item_relation**
> delete_item_to_item_relation(id1, id2, direction=direction)

Delete all relations between two items

Deletes the relations with the specified direction or all relations between `id1` and `id2`.

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
api_instance = vidispine.RelationApi(vidispine.ApiClient(configuration))
id1 = 'id1_example' # str | The id1.
id2 = 'id2_example' # str | The id2.
direction = 'direction_example' # str | - `A` - This is the default value.  Deletes all relations between `id1` and `id2`.  - `U` - Deletes only the relations with the direction as undirectional.  - `S` - Deletes only the relations where `id1` is the source and `id2` is the target.  - `T` - Deletes only the relations where `id2` is the source and `id1` is the target. (optional)

try:
    # Delete all relations between two items
    api_instance.delete_item_to_item_relation(id1, id2, direction=direction)
except ApiException as e:
    print("Exception when calling RelationApi->delete_item_to_item_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id1** | **str**| The id1. | 
 **id2** | **str**| The id2. | 
 **direction** | **str**| - &#x60;A&#x60; - This is the default value.  Deletes all relations between &#x60;id1&#x60; and &#x60;id2&#x60;.  - &#x60;U&#x60; - Deletes only the relations with the direction as undirectional.  - &#x60;S&#x60; - Deletes only the relations where &#x60;id1&#x60; is the source and &#x60;id2&#x60; is the target.  - &#x60;T&#x60; - Deletes only the relations where &#x60;id2&#x60; is the source and &#x60;id1&#x60; is the target. | [optional] 

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

# **get_item_relation**
> ItemRelationType get_item_relation(relation_id)

Retrieve an item relation

Retrieves the relation with the id `relation-id`.

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
api_instance = vidispine.RelationApi(vidispine.ApiClient(configuration))
relation_id = 'relation_id_example' # str | The relation id.

try:
    # Retrieve an item relation
    api_response = api_instance.get_item_relation(relation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationApi->get_item_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | **str**| The relation id. | 

### Return type

[**ItemRelationType**](ItemRelationType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;ItemRelationDocument&lt;/em&gt;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_relations**
> ItemRelationListType get_item_relations(id, direction=direction)

List all item relations

Returns a list of relations that matches the search criteria. Item id can be an identifier, that is libraries can be used.  In addition, extra query parameters of the form `key=value` can be added, to only return relations that matches the key-value pair(s).

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
api_instance = vidispine.RelationApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
direction = 'A' # str | - `U` - Only return undirectional relations where `id` is part of.  - `S` - Only return directional relations where `id` is the source item.  - `T` - Only return directional relations where `id` is the target item.  - `D` - Only return directional relations where `id` is the source or target item.  - `A` (default) - Return all relations that `id` is a part of. (optional) (default to 'A')

try:
    # List all item relations
    api_response = api_instance.get_item_relations(id, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationApi->get_item_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **direction** | **str**| - &#x60;U&#x60; - Only return undirectional relations where &#x60;id&#x60; is part of.  - &#x60;S&#x60; - Only return directional relations where &#x60;id&#x60; is the source item.  - &#x60;T&#x60; - Only return directional relations where &#x60;id&#x60; is the target item.  - &#x60;D&#x60; - Only return directional relations where &#x60;id&#x60; is the source or target item.  - &#x60;A&#x60; (default) - Return all relations that &#x60;id&#x60; is a part of. | [optional] [default to &#39;A&#39;]

### Return type

[**ItemRelationListType**](ItemRelationListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF -delimited list of TabbedTuple of relation id, relation URI, direction type (&lt;code&gt;U&lt;/code&gt;, &lt;code&gt;D&lt;/code&gt;), relation type, and source id, target id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_relation**
> ItemRelationType update_item_relation(relation_id, direction=direction)

Update an item relation

Updates the relation metadata for a relation with the id `relation-id`.  Query parameters of the form `key=value` are used to modify the metadata of the relation.

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
api_instance = vidispine.RelationApi(vidispine.ApiClient(configuration))
relation_id = 'relation_id_example' # str | The relation id.
direction = 'direction_example' # str | - `U` - Set the direction of the relation as undirectional.  - `S` - Set the direction as `id1` being the source and `id2` being the target.  - `T` - Set the direction as `id2` being the source and `id1` being the target. (optional)

try:
    # Update an item relation
    api_response = api_instance.update_item_relation(relation_id, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationApi->update_item_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | **str**| The relation id. | 
 **direction** | **str**| - &#x60;U&#x60; - Set the direction of the relation as undirectional.  - &#x60;S&#x60; - Set the direction as &#x60;id1&#x60; being the source and &#x60;id2&#x60; being the target.  - &#x60;T&#x60; - Set the direction as &#x60;id2&#x60; being the source and &#x60;id1&#x60; being the target. | [optional] 

### Return type

[**ItemRelationType**](ItemRelationType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The updated item described as an &lt;em&gt;ItemRelationDocument&lt;/em&gt;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

