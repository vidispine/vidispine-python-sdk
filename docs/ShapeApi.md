# vidispine.ShapeApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_file_to_component**](ShapeApi.md#add_file_to_component) | **PUT** /item/{id}/shape/{shape-id}/component/{component-id}/file/{file-id} | Associate a file with a component
[**add_shape_mime_type**](ShapeApi.md#add_shape_mime_type) | **PUT** /item/{id}/shape/{shape-id}/mime/{mime-type} | Add a mime type to a shape
[**add_shape_tag**](ShapeApi.md#add_shape_tag) | **PUT** /item/{item-id}/shape/{shape-id}/tag/{tag-name} | Add a tag to a shape
[**copy_component_to_component**](ShapeApi.md#copy_component_to_component) | **POST** /item/{id}/shape/{shape-id}/component/{component-id}/copy/item/{target-id}/shape/{target-shape-id}/component/{target-component-id} | Copy a component to another shape/component
[**copy_component_to_shape**](ShapeApi.md#copy_component_to_shape) | **POST** /item/{id}/shape/{shape-id}/component/{component-id}/copy/item/{target-id}/shape/{target-shape-id} | Copy a component to another shape
[**copy_shape_essence_version**](ShapeApi.md#copy_shape_essence_version) | **POST** /item/{id}/shape/{shape-id}/version | Copy an essence version of a shape to a new version
[**copy_shape_essence_version_to_version**](ShapeApi.md#copy_shape_essence_version_to_version) | **PUT** /item/{id}/shape/{shape-id}/version/{new-version} | Copy an essence version of a shape to a specific version
[**create_placeholder_component**](ShapeApi.md#create_placeholder_component) | **POST** /item/{id}/shape/{shape-id}/component/placeholder | Create a placeholder component
[**create_shape_deduction_job**](ShapeApi.md#create_shape_deduction_job) | **POST** /item/{item-id}/shape/{shape-id}/update | Re-run a shape deduction on an existing shape
[**create_shape_export_job**](ShapeApi.md#create_shape_export_job) | **POST** /item/{item-id}/shape/{shape-id}/export | Start an export job for a single shape
[**create_shape_imf_export_job**](ShapeApi.md#create_shape_imf_export_job) | **POST** /item/{item-id}/shape/{shape-id}/export/imp | Start an export job of an shape to an IMF package
[**create_shape_placeholder**](ShapeApi.md#create_shape_placeholder) | **POST** /item/{id}/shape/placeholder | Create a placeholder shape
[**create_shape_thumbnail_job**](ShapeApi.md#create_shape_thumbnail_job) | **POST** /item/{item-id}/shape/{shape-id}/thumbnail | Start a thumbnail job
[**create_shape_transcode_job**](ShapeApi.md#create_shape_transcode_job) | **POST** /item/{item-id}/shape/{shape-id}/transcode | Transcode a specific shape
[**delete_component**](ShapeApi.md#delete_component) | **DELETE** /item/{id}/shape/{shape-id}/component/{component-id} | Delete a component
[**delete_component_metadata**](ShapeApi.md#delete_component_metadata) | **DELETE** /item/{item-id}/shape/{shape-id}/component/{component-id}/metadata | Delete all key-value pairs
[**delete_component_metadata_key**](ShapeApi.md#delete_component_metadata_key) | **DELETE** /item/{item-id}/shape/{shape-id}/component/{component-id}/metadata/{keypath} | Delete key-value pairs
[**delete_shape**](ShapeApi.md#delete_shape) | **DELETE** /item/{id}/shape/{shape-id} | Delete a shape
[**delete_shape_essence_version**](ShapeApi.md#delete_shape_essence_version) | **DELETE** /item/{id}/shape/version/{version} | Delete an essence version
[**delete_shape_metadata**](ShapeApi.md#delete_shape_metadata) | **DELETE** /item/{item-id}/shape/{shape-id}/metadata | Delete all key-value pairs
[**delete_shape_metadata_key**](ShapeApi.md#delete_shape_metadata_key) | **DELETE** /item/{item-id}/shape/{shape-id}/metadata/{keypath} | Delete key-value pairs
[**delete_shape_mime_type**](ShapeApi.md#delete_shape_mime_type) | **DELETE** /item/{id}/shape/{shape-id}/mime/{mime-type} | Remove a mime type from a shape
[**delete_shapes**](ShapeApi.md#delete_shapes) | **DELETE** /item/{id}/shape/ | Delete all shapes
[**get_component**](ShapeApi.md#get_component) | **GET** /item/{id}/shape/{shape-id}/component/{component-id} | Retrieve a component
[**get_component_metadata**](ShapeApi.md#get_component_metadata) | **GET** /item/{item-id}/shape/{shape-id}/component/{component-id}/metadata | Retrieve all metadata
[**get_component_metadata_key**](ShapeApi.md#get_component_metadata_key) | **GET** /item/{item-id}/shape/{shape-id}/component/{component-id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_components**](ShapeApi.md#get_components) | **GET** /item/{id}/shape/{shape-id}/component | List all components for a shape
[**get_shape**](ShapeApi.md#get_shape) | **GET** /item/{id}/shape/{shape-id} | Retrieve a shape
[**get_shape_cpl**](ShapeApi.md#get_shape_cpl) | **GET** /item/{id}/shape/{shape-id}/cpl | Retrieve a shape as an IMF CPL
[**get_shape_essence_version**](ShapeApi.md#get_shape_essence_version) | **GET** /item/{id}/shape/version/{version} | Retrieve an essence version
[**get_shape_files**](ShapeApi.md#get_shape_files) | **GET** /item/{id}/shape/{shape-id}/file | List all files for a shape
[**get_shape_graph**](ShapeApi.md#get_shape_graph) | **GET** /item/{id}/shape/{shape-id}/graph | Retrieve a graphical representation of a shape
[**get_shape_graph_dot**](ShapeApi.md#get_shape_graph_dot) | **GET** /item/{id}/shape/{shape-id}/graph/dot | Retrieve a shape as a dot file
[**get_shape_metadata**](ShapeApi.md#get_shape_metadata) | **GET** /item/{item-id}/shape/{shape-id}/metadata | Retrieve all metadata
[**get_shape_metadata_key**](ShapeApi.md#get_shape_metadata_key) | **GET** /item/{item-id}/shape/{shape-id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_shape_mime_types**](ShapeApi.md#get_shape_mime_types) | **GET** /item/{id}/shape/{shape-id}/mime/ | List all mime types for a shape
[**get_shape_storage_rules**](ShapeApi.md#get_shape_storage_rules) | **GET** /item/{item-id}/shape/{shape-id}/storage-rule | List all storage rules that applies to a certain shape
[**get_shape_tags**](ShapeApi.md#get_shape_tags) | **GET** /item/{item-id}/shape/{shape-id}/tag/ | List all tags for a shape
[**get_shape_versions**](ShapeApi.md#get_shape_versions) | **GET** /item/{id}/shape/version | List all essence versions
[**get_shapes**](ShapeApi.md#get_shapes) | **GET** /item/{id}/shape | List all shapes
[**import_component**](ShapeApi.md#import_component) | **POST** /item/{id}/shape/{shape-id}/component | Import a component using a URI or an existing file
[**import_shape**](ShapeApi.md#import_shape) | **POST** /item/{id}/shape | Import a shape using a URI or an existing file
[**import_shape_create**](ShapeApi.md#import_shape_create) | **POST** /item/{id}/shape/create | Create a shape using shape technical information
[**import_shape_essence**](ShapeApi.md#import_shape_essence) | **POST** /item/{id}/shape/essence | Import an essence version using a URI or an existing file
[**import_shape_essence_raw**](ShapeApi.md#import_shape_essence_raw) | **POST** /item/{id}/shape/essence/raw | Import an essence version using the request body
[**import_shape_imf_package**](ShapeApi.md#import_shape_imf_package) | **POST** /item/{id}/shape/imp | Import a shape from an IMF package
[**import_shape_raw**](ShapeApi.md#import_shape_raw) | **POST** /item/{id}/shape/raw | Import a shape using the request body
[**move_component_to_component**](ShapeApi.md#move_component_to_component) | **POST** /item/{id}/shape/{shape-id}/component/{component-id}/move/item/{target-id}/shape/{target-shape-id}/component/{target-component-id} | Move a component to another shape/component
[**move_component_to_shape**](ShapeApi.md#move_component_to_shape) | **POST** /item/{id}/shape/{shape-id}/component/{component-id}/move/item/{target-id}/shape/{target-shape-id} | Move a component to another shape
[**remove_file_from_component**](ShapeApi.md#remove_file_from_component) | **DELETE** /item/{id}/shape/{shape-id}/component/{component-id}/file/{file-id} | Remove a file from a component
[**remove_shape_tag**](ShapeApi.md#remove_shape_tag) | **DELETE** /item/{item-id}/shape/{shape-id}/tag/{tag-name} | Remove a tag from a shape
[**update_component_metadata**](ShapeApi.md#update_component_metadata) | **PUT** /item/{item-id}/shape/{shape-id}/component/{component-id}/metadata | Create multiple key-value pairs
[**update_component_metadata_key**](ShapeApi.md#update_component_metadata_key) | **PUT** /item/{item-id}/shape/{shape-id}/component/{component-id}/metadata/{keypath} | Set the value for a specific key
[**update_shape_metadata**](ShapeApi.md#update_shape_metadata) | **PUT** /item/{item-id}/shape/{shape-id}/metadata | Create multiple key-value pairs
[**update_shape_metadata_key**](ShapeApi.md#update_shape_metadata_key) | **PUT** /item/{item-id}/shape/{shape-id}/metadata/{keypath} | Set the value for a specific key
[**update_shape_placeholder**](ShapeApi.md#update_shape_placeholder) | **PUT** /item/{id}/shape/{shape-id}/placeholder | Update a placeholder shape


# **add_file_to_component**
> ComponentType add_file_to_component(id, shape_id, component_id, file_id, allow_reimport=allow_reimport)

Associate a file with a component

Attaches the specified file to the specified component

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
file_id = 'file_id_example' # str | The file id.
allow_reimport = False # bool | - `true` - Associate the file regardless of whether it already belongs to a component.  - `false` (default) - Only files that do not already belong to a component can be associated. (optional) (default to False)

try:
    # Associate a file with a component
    api_response = api_instance.add_file_to_component(id, shape_id, component_id, file_id, allow_reimport=allow_reimport)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->add_file_to_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
 **file_id** | **str**| The file id. | 
 **allow_reimport** | **bool**| - &#x60;true&#x60; - Associate the file regardless of whether it already belongs to a component.  - &#x60;false&#x60; (default) - Only files that do not already belong to a component can be associated. | [optional] [default to False]

### Return type

[**ComponentType**](ComponentType.md)

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

# **add_shape_mime_type**
> add_shape_mime_type(id, shape_id, mime_type)

Add a mime type to a shape

Adds a new mime type to the shape. This operation does nothing if the shape already has the mime-type.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
mime_type = 'mime_type_example' # str | The mime type.

try:
    # Add a mime type to a shape
    api_instance.add_shape_mime_type(id, shape_id, mime_type)
except ApiException as e:
    print("Exception when calling ShapeApi->add_shape_mime_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **mime_type** | **str**| The mime type. | 

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

# **add_shape_tag**
> add_shape_tag(item_id, shape_id, tag_name)

Add a tag to a shape

Adds shape tag with the given name to the specified shape. If the shape already has that tag, this operation does nothing.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Add a tag to a shape
    api_instance.add_shape_tag(item_id, shape_id, tag_name)
except ApiException as e:
    print("Exception when calling ShapeApi->add_shape_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **tag_name** | **str**| The tag name. | 

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

# **copy_component_to_component**
> ShapeType copy_component_to_component(id, shape_id, component_id, target_id, target_shape_id, target_component_id, index=index, keep_metadata=keep_metadata)

Copy a component to another shape/component

Copy this component to another shape, replacing a specific component by id.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
target_id = 'target_id_example' # str | The target id.
target_shape_id = 'target_shape_id_example' # str | The target shape id.
target_component_id = 'target_component_id_example' # str | The target component id.
index = 56 # int | The component index (track) of component.  If the target shape has a component with this index, then it will be replaced/removed. (optional)
keep_metadata = False # bool | - `true` - Preserve the metadata from the replaced component.  - `false` (default) - Discard any metadata from the replaced component. (optional) (default to False)

try:
    # Copy a component to another shape/component
    api_response = api_instance.copy_component_to_component(id, shape_id, component_id, target_id, target_shape_id, target_component_id, index=index, keep_metadata=keep_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->copy_component_to_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
 **target_id** | **str**| The target id. | 
 **target_shape_id** | **str**| The target shape id. | 
 **target_component_id** | **str**| The target component id. | 
 **index** | **int**| The component index (track) of component.  If the target shape has a component with this index, then it will be replaced/removed. | [optional] 
 **keep_metadata** | **bool**| - &#x60;true&#x60; - Preserve the metadata from the replaced component.  - &#x60;false&#x60; (default) - Discard any metadata from the replaced component. | [optional] [default to False]

### Return type

[**ShapeType**](ShapeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;ShapeDocument&lt;/em&gt; from the target shape. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_component_to_shape**
> ShapeType copy_component_to_shape(id, shape_id, component_id, target_id, target_shape_id, index=index, keep_metadata=keep_metadata)

Copy a component to another shape

Copy this component to another shape.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
target_id = 'target_id_example' # str | The target id.
target_shape_id = 'target_shape_id_example' # str | The target shape id.
index = 56 # int | The component index (track) of component.  If the target shape has a component with this index, then it will be replaced/removed. (optional)
keep_metadata = False # bool | - `true` - Preserve the metadata from the replaced component.  - `false` (default) - Discard any metadata from the replaced component. (optional) (default to False)

try:
    # Copy a component to another shape
    api_response = api_instance.copy_component_to_shape(id, shape_id, component_id, target_id, target_shape_id, index=index, keep_metadata=keep_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->copy_component_to_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
 **target_id** | **str**| The target id. | 
 **target_shape_id** | **str**| The target shape id. | 
 **index** | **int**| The component index (track) of component.  If the target shape has a component with this index, then it will be replaced/removed. | [optional] 
 **keep_metadata** | **bool**| - &#x60;true&#x60; - Preserve the metadata from the replaced component.  - &#x60;false&#x60; (default) - Discard any metadata from the replaced component. | [optional] [default to False]

### Return type

[**ShapeType**](ShapeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;ShapeDocument&lt;/em&gt; from the target shape. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_shape_essence_version**
> ShapeType copy_shape_essence_version(id, shape_id)

Copy an essence version of a shape to a new version

Copies the specified shape to a new shape, with the new latest essence version number.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # Copy an essence version of a shape to a new version
    api_response = api_instance.copy_shape_essence_version(id, shape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->copy_shape_essence_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 

### Return type

[**ShapeType**](ShapeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;ShapeDocument&lt;/em&gt; containing the new shape. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_shape_essence_version_to_version**
> ShapeType copy_shape_essence_version_to_version(id, shape_id, new_version)

Copy an essence version of a shape to a specific version

Copies the specified shape to a new shape, with the given essence version number.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
new_version = 'new_version_example' # str | The new version.

try:
    # Copy an essence version of a shape to a specific version
    api_response = api_instance.copy_shape_essence_version_to_version(id, shape_id, new_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->copy_shape_essence_version_to_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **new_version** | **str**| The new version. | 

### Return type

[**ShapeType**](ShapeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;ShapeDocument&lt;/em&gt; containing the new shape. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_placeholder_component**
> ComponentType create_placeholder_component(type, id, shape_id, index=index)

Create a placeholder component

Creates an new placeholder component for a specific shape.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of component.
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
index = 56 # int | The component index (track) of new component. (optional)

try:
    # Create a placeholder component
    api_response = api_instance.create_placeholder_component(type, id, shape_id, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->create_placeholder_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of component. | 
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **index** | **int**| The component index (track) of new component. | [optional] 

### Return type

[**ComponentType**](ComponentType.md)

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

# **create_shape_deduction_job**
> JobType create_shape_deduction_job(item_id, shape_id, jobmetadata=jobmetadata, notification_data=notification_data, priority=priority, notification=notification)

Re-run a shape deduction on an existing shape

Starts a new shape deduction job for the specified shape.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)

try:
    # Re-run a shape deduction on an existing shape
    api_response = api_instance.create_shape_deduction_job(item_id, shape_id, jobmetadata=jobmetadata, notification_data=notification_data, priority=priority, notification=notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->create_shape_deduction_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 

### Return type

[**JobType**](JobType.md)

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

# **create_shape_export_job**
> JobType create_shape_export_job(item_id, shape_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, projection=projection, notification=notification, use_original_component_filename=use_original_component_filename, start=start, end=end, priority=priority, allow_missing=allow_missing, uri=uri, metadata=metadata, location_name=location_name)

Start an export job for a single shape

Creates a new export job that will copy a file from the specified shape to a remote location.  If the URI ends with a \"/\" the URI is assumed to describe a folder and the file will retain its existing filename. Otherwise it is assumed that the URI describes a file and that filename will be used.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
track = ["*"] # list[str] | Comma-separated list of item track ids.  Can include wildcards, e. g.  `A*`.  Can also contain component ids. (optional) (default to ["*"])
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
use_original_filename = False # bool | If set to `true`, the file(s) will be exported with their original filename if available. (optional) (default to False)
projection = 'projection_example' # str | Defines the projection to use when exporting the metadata. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
use_original_component_filename = True # bool | If set to `true`, the file(s) will be exported with their original component filename if available. (optional)
start = 'start_example' # str | Defines a start time code for the media. (optional)
end = 'end_example' # str | Defines an end time code for the media. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
allow_missing = True # bool | - `true` (default) - Job will be started and the missing files will be ignored.  - `false` - Job won't be started if there are missing files. (optional) (default to True)
uri = 'uri_example' # str | A URI to the destination of the file. (optional)
metadata = False # bool | - `true` - Metadata will also be exported to side-car XML file.  - `false` (default) - No metadata is exported. (optional) (default to False)
location_name = 'location_name_example' # str | The name of an export location. (optional)

try:
    # Start an export job for a single shape
    api_response = api_instance.create_shape_export_job(item_id, shape_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, projection=projection, notification=notification, use_original_component_filename=use_original_component_filename, start=start, end=end, priority=priority, allow_missing=allow_missing, uri=uri, metadata=metadata, location_name=location_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->create_shape_export_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **track** | [**list[str]**](str.md)| Comma-separated list of item track ids.  Can include wildcards, e. g.  &#x60;A*&#x60;.  Can also contain component ids. | [optional] [default to [&quot;*&quot;]]
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **use_original_filename** | **bool**| If set to &#x60;true&#x60;, the file(s) will be exported with their original filename if available. | [optional] [default to False]
 **projection** | **str**| Defines the projection to use when exporting the metadata. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **use_original_component_filename** | **bool**| If set to &#x60;true&#x60;, the file(s) will be exported with their original component filename if available. | [optional] 
 **start** | **str**| Defines a start time code for the media. | [optional] 
 **end** | **str**| Defines an end time code for the media. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **allow_missing** | **bool**| - &#x60;true&#x60; (default) - Job will be started and the missing files will be ignored.  - &#x60;false&#x60; - Job won&#39;t be started if there are missing files. | [optional] [default to True]
 **uri** | **str**| A URI to the destination of the file. | [optional] 
 **metadata** | **bool**| - &#x60;true&#x60; - Metadata will also be exported to side-car XML file.  - &#x60;false&#x60; (default) - No metadata is exported. | [optional] [default to False]
 **location_name** | **str**| The name of an export location. | [optional] 

### Return type

[**JobType**](JobType.md)

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

# **create_shape_imf_export_job**
> JobType create_shape_imf_export_job(item_id, shape_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, priority=priority, uri=uri, notification=notification, cpl_track=cpl_track, start=start, projection=projection, end=end, use_original_component_filename=use_original_component_filename, allow_missing=allow_missing, metadata=metadata, location_name=location_name)

Start an export job of an shape to an IMF package

Creates a new export job that will create an IMF package as a remote location. URI must end with an \"/\" to denote a folder.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
track = ["*"] # list[str] | Comma-separated list of item track ids.  Can include wildcards, e. g.  `A*`.  Can also contain component ids. (optional) (default to ["*"])
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
use_original_filename = False # bool | If set to `true`, the file(s) will be exported with their original filename if available. (optional) (default to False)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
uri = 'uri_example' # str | A URI to the destination of the file. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
cpl_track = ['cpl_track_example'] # list[str] | Comma-separated list of item track ids to include in the CPL.  Can include wildcards, e. g.  `A*`.  Can also contain component ids.  Default is the same as the track parameter. (optional)
start = 'start_example' # str | Defines a start time_code for the media. (optional)
projection = 'projection_example' # str | Defines the projection to use when exporting the metadata. (optional)
end = 'end_example' # str | Defines an end time_code for the media. (optional)
use_original_component_filename = True # bool | If set to `true`, the file(s) will be exported with their original component filename if available. (optional)
allow_missing = True # bool | - `true` (default) - Job will be started and the missing files will be ignored.  - `false` - Job won't be started if there are missing files. (optional) (default to True)
metadata = False # bool | - `true` - Metadata will also be exported to side-car XML file.  - `false` (default) - No metadata is exported. (optional) (default to False)
location_name = 'location_name_example' # str | The name of an export location. (optional)

try:
    # Start an export job of an shape to an IMF package
    api_response = api_instance.create_shape_imf_export_job(item_id, shape_id, jobmetadata=jobmetadata, track=track, notification_data=notification_data, use_original_filename=use_original_filename, priority=priority, uri=uri, notification=notification, cpl_track=cpl_track, start=start, projection=projection, end=end, use_original_component_filename=use_original_component_filename, allow_missing=allow_missing, metadata=metadata, location_name=location_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->create_shape_imf_export_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **track** | [**list[str]**](str.md)| Comma-separated list of item track ids.  Can include wildcards, e. g.  &#x60;A*&#x60;.  Can also contain component ids. | [optional] [default to [&quot;*&quot;]]
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **use_original_filename** | **bool**| If set to &#x60;true&#x60;, the file(s) will be exported with their original filename if available. | [optional] [default to False]
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **uri** | **str**| A URI to the destination of the file. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **cpl_track** | [**list[str]**](str.md)| Comma-separated list of item track ids to include in the CPL.  Can include wildcards, e. g.  &#x60;A*&#x60;.  Can also contain component ids.  Default is the same as the track parameter. | [optional] 
 **start** | **str**| Defines a start time_code for the media. | [optional] 
 **projection** | **str**| Defines the projection to use when exporting the metadata. | [optional] 
 **end** | **str**| Defines an end time_code for the media. | [optional] 
 **use_original_component_filename** | **bool**| If set to &#x60;true&#x60;, the file(s) will be exported with their original component filename if available. | [optional] 
 **allow_missing** | **bool**| - &#x60;true&#x60; (default) - Job will be started and the missing files will be ignored.  - &#x60;false&#x60; - Job won&#39;t be started if there are missing files. | [optional] [default to True]
 **metadata** | **bool**| - &#x60;true&#x60; - Metadata will also be exported to side-car XML file.  - &#x60;false&#x60; (default) - No metadata is exported. | [optional] [default to False]
 **location_name** | **str**| The name of an export location. | [optional] 

### Return type

[**JobType**](JobType.md)

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

# **create_shape_placeholder**
> str create_shape_placeholder(id, simple_metadata_type, binary=binary, audio=audio, tag=tag, container=container, video=video, frame_duration=frame_duration)

Create a placeholder shape

Creates an new placeholder shape for a specific item.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 
binary = 56 # int | The number of binary components (optional)
audio = 56 # int | The number of audio components (optional)
tag = 'tag_example' # str | Comma-separated shape tags to be added to the shape. (optional)
container = 56 # int | The number of container components (optional)
video = 56 # int | The number of video components (optional)
frame_duration = 'frame_duration_example' # str | duration for each image in the sequence. (optional)

try:
    # Create a placeholder shape
    api_response = api_instance.create_shape_placeholder(id, simple_metadata_type, binary=binary, audio=audio, tag=tag, container=container, video=video, frame_duration=frame_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->create_shape_placeholder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **simple_metadata_type** | [**SimpleMetadataType**](SimpleMetadataType.md)|  | 
 **binary** | **int**| The number of binary components | [optional] 
 **audio** | **int**| The number of audio components | [optional] 
 **tag** | **str**| Comma-separated shape tags to be added to the shape. | [optional] 
 **container** | **int**| The number of container components | [optional] 
 **video** | **int**| The number of video components | [optional] 
 **frame_duration** | **str**| duration for each image in the sequence. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The id of the new shape. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shape_thumbnail_job**
> JobType create_shape_thumbnail_job(item_id, shape_id, thumbnail_width=thumbnail_width, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, tag=tag, poster_format=poster_format, notification=notification, poster_width=poster_width, priority=priority, create_thumbnails=create_thumbnails, thumbnail_height=thumbnail_height, create_posters=create_posters, poster_height=poster_height, thumbnail_period=thumbnail_period, resource_id=resource_id)

Start a thumbnail job

Creates a new thumbnail job with the specified parameters. Note that a job cannot both create thumbnails at specified intervals and posters. Creating thumbnails according to transcoder rules and creating posters is however allowed.  Changed in version 5.0: For multi-layer PSD/PSB files, only a thumbnail of all layers flattened will be generated by default.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
thumbnail_width = 56 # int | The width of the thumbnails.  If `thumbnailWidth` is specified, `thumbnailHeight` must also be specified. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
tag = 'tag_example' # str | Include additional video settings from this transcode preset.  Resolution settings in the tag are overridden by query parameters `thumbnailHeight` and `thumbnailWidth`. (optional)
poster_format = 'jpeg' # str | - `jpeg` (default) - Creates posters in JPEG format.  - `png` - Creates posters in PNG format. (optional) (default to 'jpeg')
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
poster_width = 56 # int | The width of the posters. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
create_thumbnails = False # bool | - `true` - Creates thumbnails according to default transcoder rules.  - *t1*, . . .  - Thumbnails will be created on the specified, comma-separated, time codes.  - `false` (default) - No thumbnails will be created. (optional) (default to False)
thumbnail_height = 56 # int | The height of the thumbnails.  If `thumbnailHeight` is specified, `thumbnailWidth` must also be specified. (optional)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
poster_height = 56 # int | The height of the posters. (optional)
thumbnail_period = 'thumbnail_period_example' # str | Timecode string specifying the interval of the thumbnails.  It should be a decimal integer when working with multi-page images/PDFs, meaning every N page(s). (optional)
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)

try:
    # Start a thumbnail job
    api_response = api_instance.create_shape_thumbnail_job(item_id, shape_id, thumbnail_width=thumbnail_width, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, tag=tag, poster_format=poster_format, notification=notification, poster_width=poster_width, priority=priority, create_thumbnails=create_thumbnails, thumbnail_height=thumbnail_height, create_posters=create_posters, poster_height=poster_height, thumbnail_period=thumbnail_period, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->create_shape_thumbnail_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **thumbnail_width** | **int**| The width of the thumbnails.  If &#x60;thumbnailWidth&#x60; is specified, &#x60;thumbnailHeight&#x60; must also be specified. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **tag** | **str**| Include additional video settings from this transcode preset.  Resolution settings in the tag are overridden by query parameters &#x60;thumbnailHeight&#x60; and &#x60;thumbnailWidth&#x60;. | [optional] 
 **poster_format** | **str**| - &#x60;jpeg&#x60; (default) - Creates posters in JPEG format.  - &#x60;png&#x60; - Creates posters in PNG format. | [optional] [default to &#39;jpeg&#39;]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **poster_width** | **int**| The width of the posters. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **create_thumbnails** | **bool**| - &#x60;true&#x60; - Creates thumbnails according to default transcoder rules.  - *t1*, . . .  - Thumbnails will be created on the specified, comma-separated, time codes.  - &#x60;false&#x60; (default) - No thumbnails will be created. | [optional] [default to False]
 **thumbnail_height** | **int**| The height of the thumbnails.  If &#x60;thumbnailHeight&#x60; is specified, &#x60;thumbnailWidth&#x60; must also be specified. | [optional] 
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **poster_height** | **int**| The height of the posters. | [optional] 
 **thumbnail_period** | **str**| Timecode string specifying the interval of the thumbnails.  It should be a decimal integer when working with multi-page images/PDFs, meaning every N page(s). | [optional] 
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 

### Return type

[**JobType**](JobType.md)

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

# **create_shape_transcode_job**
> JobType create_shape_transcode_job(item_id, shape_id, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, tag=tag, storage_id=storage_id, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, destination_item=destination_item, create_posters=create_posters, override_fast_start=override_fast_start, resource_id=resource_id, priority=priority, original=original)

Transcode a specific shape

Starts a new job that transcode a specific shape on an item to a number of shapes according to the given shape tags.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
thumbnail_service = 'thumbnail_service_example' # str | Identifies which thumbnail resource that should be used. (optional)
tag = ['tag_example'] # list[str] | Comma-separated list of shape tags, that specify the desired output. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored.  New in version 4. 16. (optional)
require_fast_start = True # bool | - `true` (default) - Try to put the index tables (header) in front of the file.  - `false` - Put header at end of file. (optional) (default to True)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
fast_start_length = 'fast_start_length_example' # str | Estimated duration of the clip in seconds. (optional)
create_thumbnails = False # bool | - `true` - Creates thumbnails according to default transcoder rules.  - `false` (default) - No thumbnails will be created. (optional) (default to False)
destination_item = 'destination_item_example' # str | An item id, to which the new new shape will be associated. (optional)
create_posters = 'create_posters_example' # str | A list of time codes to use for creating posters. (optional)
override_fast_start = True # bool | - `true` (default) - Use transcoder's estimate of the duration for allocating header space in MOV files and similar files.  - `false` - Do not use the transcoder's estimate of the duration. (optional) (default to True)
resource_id = 'resource_id_example' # str | The transcoder resource to use to execute the transcode. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
original = 'original_example' # str | If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. (optional)

try:
    # Transcode a specific shape
    api_response = api_instance.create_shape_transcode_job(item_id, shape_id, jobmetadata=jobmetadata, notification_data=notification_data, thumbnail_service=thumbnail_service, tag=tag, storage_id=storage_id, require_fast_start=require_fast_start, notification=notification, fast_start_length=fast_start_length, create_thumbnails=create_thumbnails, destination_item=destination_item, create_posters=create_posters, override_fast_start=override_fast_start, resource_id=resource_id, priority=priority, original=original)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->create_shape_transcode_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **thumbnail_service** | **str**| Identifies which thumbnail resource that should be used. | [optional] 
 **tag** | [**list[str]**](str.md)| Comma-separated list of shape tags, that specify the desired output. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored.  New in version 4. 16. | [optional] 
 **require_fast_start** | **bool**| - &#x60;true&#x60; (default) - Try to put the index tables (header) in front of the file.  - &#x60;false&#x60; - Put header at end of file. | [optional] [default to True]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **fast_start_length** | **str**| Estimated duration of the clip in seconds. | [optional] 
 **create_thumbnails** | **bool**| - &#x60;true&#x60; - Creates thumbnails according to default transcoder rules.  - &#x60;false&#x60; (default) - No thumbnails will be created. | [optional] [default to False]
 **destination_item** | **str**| An item id, to which the new new shape will be associated. | [optional] 
 **create_posters** | **str**| A list of time codes to use for creating posters. | [optional] 
 **override_fast_start** | **bool**| - &#x60;true&#x60; (default) - Use transcoder&#39;s estimate of the duration for allocating header space in MOV files and similar files.  - &#x60;false&#x60; - Do not use the transcoder&#39;s estimate of the duration. | [optional] [default to True]
 **resource_id** | **str**| The transcoder resource to use to execute the transcode. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **original** | **str**| If specified, should be one of the tags specified in the tag parameter.  Specifies that the original shape tag will be reset to the shape created to this tag. | [optional] 

### Return type

[**JobType**](JobType.md)

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

# **delete_component**
> delete_component(id, shape_id, component_id, keep_files=keep_files)

Delete a component

Removes the component from the shape. Any files belonging to the component is not Copy this component to another shape, replacing a specific component by id.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
keep_files = False # bool | - `true` - Keep the files belong to this shape.  - `false` (default) - Remove the files belong to this shape. (optional) (default to False)

try:
    # Delete a component
    api_instance.delete_component(id, shape_id, component_id, keep_files=keep_files)
except ApiException as e:
    print("Exception when calling ShapeApi->delete_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
 **keep_files** | **bool**| - &#x60;true&#x60; - Keep the files belong to this shape.  - &#x60;false&#x60; (default) - Remove the files belong to this shape. | [optional] [default to False]

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

# **delete_component_metadata**
> delete_component_metadata(item_id, shape_id, component_id)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.

try:
    # Delete all key-value pairs
    api_instance.delete_component_metadata(item_id, shape_id, component_id)
except ApiException as e:
    print("Exception when calling ShapeApi->delete_component_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 

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

# **delete_component_metadata_key**
> delete_component_metadata_key(item_id, shape_id, component_id, keypath)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_component_metadata_key(item_id, shape_id, component_id, keypath)
except ApiException as e:
    print("Exception when calling ShapeApi->delete_component_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
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

# **delete_shape**
> URIListType delete_shape(id, shape_id, keep_files=keep_files, url=url, update_metadata=update_metadata)

Delete a shape

Removes the specified shape. This will remove all components and and mark files for deletion, unless files are used in other shapes.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
keep_files = False # bool | - `true` - Keep the files belong to this shape.  - `false` (default) - Remove the files belong to this shape. (optional) (default to False)
url = False # bool | - `true` - Instead of shape ids, return the full paths of the shapes in the response document.  - `false` (default) - Only return the ids of the remaining shapes. (optional) (default to False)
update_metadata = True # bool | - `true` - Remove the item metadata that is generate from this shape - `false` (default) - Keep the item metadata that is generate from this shape (optional)

try:
    # Delete a shape
    api_response = api_instance.delete_shape(id, shape_id, keep_files=keep_files, url=url, update_metadata=update_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->delete_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **keep_files** | **bool**| - &#x60;true&#x60; - Keep the files belong to this shape.  - &#x60;false&#x60; (default) - Remove the files belong to this shape. | [optional] [default to False]
 **url** | **bool**| - &#x60;true&#x60; - Instead of shape ids, return the full paths of the shapes in the response document.  - &#x60;false&#x60; (default) - Only return the ids of the remaining shapes. | [optional] [default to False]
 **update_metadata** | **bool**| - &#x60;true&#x60; - Remove the item metadata that is generate from this shape - &#x60;false&#x60; (default) - Keep the item metadata that is generate from this shape | [optional] 

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
**0** | CRLF-delimited list of ids or URLs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shape_essence_version**
> delete_shape_essence_version(id, version)

Delete an essence version

Deletes all shapes associated with the specified version. Thumbnails connected to the version will also be deleted.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
version = 'version_example' # str | The version.

try:
    # Delete an essence version
    api_instance.delete_shape_essence_version(id, version)
except ApiException as e:
    print("Exception when calling ShapeApi->delete_shape_essence_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **version** | **str**| The version. | 

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

# **delete_shape_metadata**
> delete_shape_metadata(item_id, shape_id)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # Delete all key-value pairs
    api_instance.delete_shape_metadata(item_id, shape_id)
except ApiException as e:
    print("Exception when calling ShapeApi->delete_shape_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 

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

# **delete_shape_metadata_key**
> delete_shape_metadata_key(item_id, shape_id, keypath)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_shape_metadata_key(item_id, shape_id, keypath)
except ApiException as e:
    print("Exception when calling ShapeApi->delete_shape_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
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

# **delete_shape_mime_type**
> delete_shape_mime_type(id, shape_id, mime_type)

Remove a mime type from a shape

Removes a mime type from the shape.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
mime_type = 'mime_type_example' # str | The mime type.

try:
    # Remove a mime type from a shape
    api_instance.delete_shape_mime_type(id, shape_id, mime_type)
except ApiException as e:
    print("Exception when calling ShapeApi->delete_shape_mime_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **mime_type** | **str**| The mime type. | 

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

# **delete_shapes**
> delete_shapes(id, keep_files=keep_files)

Delete all shapes

Removes all shapes, regardless of essence version, for the specified item. This will remove all components and mark files for deletion, unless files are used in other shapes.  To delete all shapes for a specific essence version, see `DELETE /item/(id)/shape/version/(version)`.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
keep_files = False # bool | - `true` - Keep the files belong to the shapes.  - `false` (default) - Remove the files belong to the shapes. (optional) (default to False)

try:
    # Delete all shapes
    api_instance.delete_shapes(id, keep_files=keep_files)
except ApiException as e:
    print("Exception when calling ShapeApi->delete_shapes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **keep_files** | **bool**| - &#x60;true&#x60; - Keep the files belong to the shapes.  - &#x60;false&#x60; (default) - Remove the files belong to the shapes. | [optional] [default to False]

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

# **get_component**
> ComponentType get_component(id, shape_id, component_id, full=full)

Retrieve a component

Returns all files, or the complete component information, for a specified component.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
full = False # bool | - `true` - Return the component information.  - `false` (default) - Return all files. (optional) (default to False)

try:
    # Retrieve a component
    api_response = api_instance.get_component(id, shape_id, component_id, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
 **full** | **bool**| - &#x60;true&#x60; - Return the component information.  - &#x60;false&#x60; (default) - Return all files. | [optional] [default to False]

### Return type

[**ComponentType**](ComponentType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List of file URLs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_metadata**
> SimpleMetadataType get_component_metadata(item_id, shape_id, component_id)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_component_metadata(item_id, shape_id, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_component_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 

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

# **get_component_metadata_key**
> str get_component_metadata_key(item_id, shape_id, component_id, keypath)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_component_metadata_key(item_id, shape_id, component_id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_component_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
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

# **get_components**
> ComponentListType get_components(id, shape_id)

List all components for a shape

Returns all components for a specified shape. Currently, this call returns the same information as the return shape, but is available for orthogonality.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # List all components for a shape
    api_response = api_instance.get_components(id, shape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 

### Return type

[**ComponentListType**](ComponentListType.md)

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

# **get_shape**
> ShapeType get_shape(id, shape_id, storage_type=storage_type, include_placeholder=include_placeholder, method_metadata=method_metadata, transient=transient, scheme=scheme, method_type=method_type)

Retrieve a shape

Returns a shape for a specified item.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
include_placeholder = False # bool | - `true` - Include expected but not yet imported components in the shape.  - `false` (default) - Do not include placeholder components. (optional) (default to False)
method_metadata = ['method_metadata_example'] # list[str] | metadata used with storage method. (optional)
transient = False # bool | - `true` - Return the shape by inspecting the file on disk.  Use with growing files to get an as up-to-date shape as possible.  - `false` (default) - Return the shape that was last read from the file. (optional) (default to False)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
method_type = 'method_type_example' # str | Return URIs from storage methods with a particular type.  By default, return URLs with empty `methodType`. (optional)

try:
    # Retrieve a shape
    api_response = api_instance.get_shape(id, shape_id, storage_type=storage_type, include_placeholder=include_placeholder, method_metadata=method_metadata, transient=transient, scheme=scheme, method_type=method_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **include_placeholder** | **bool**| - &#x60;true&#x60; - Include expected but not yet imported components in the shape.  - &#x60;false&#x60; (default) - Do not include placeholder components. | [optional] [default to False]
 **method_metadata** | [**list[str]**](str.md)| metadata used with storage method. | [optional] 
 **transient** | **bool**| - &#x60;true&#x60; - Return the shape by inspecting the file on disk.  Use with growing files to get an as up-to-date shape as possible.  - &#x60;false&#x60; (default) - Return the shape that was last read from the file. | [optional] [default to False]
 **scheme** | **str**| URI scheme to return. | [optional] 
 **method_type** | **str**| Return URIs from storage methods with a particular type.  By default, return URLs with empty &#x60;methodType&#x60;. | [optional] 

### Return type

[**ShapeType**](ShapeType.md)

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

# **get_shape_cpl**
> str get_shape_cpl(id, shape_id)

Retrieve a shape as an IMF CPL

Returns component information as CPL.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # Retrieve a shape as an IMF CPL
    api_response = api_instance.get_shape_cpl(id, shape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_cpl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shape_essence_version**
> EssenceVersionType get_shape_essence_version(id, version)

Retrieve an essence version

Returns a list of shapes from the specified version.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
version = 'version_example' # str | The version.

try:
    # Retrieve an essence version
    api_response = api_instance.get_shape_essence_version(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_essence_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **version** | **str**| The version. | 

### Return type

[**EssenceVersionType**](EssenceVersionType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;EssenceVersionDocument&lt;/em&gt; containing all the shapes with the specified version. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shape_files**
> FileListType get_shape_files(id, shape_id, storage_type=storage_type, method_metadata=method_metadata, closed_files=closed_files, scheme=scheme, include_item=include_item, method_type=method_type)

List all files for a shape

Returns all files that are associated with the specified shape.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
method_metadata = ['method_metadata_example'] # list[str] | metadata used with storage method. (optional)
closed_files = True # bool | - `true` (default) - Return only files that are closed.  - `false` - Return all files. (optional) (default to True)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
include_item = False # bool | - `true` - Return associated items, shapes, and components.  - `false` (default) - Do not return any information about associated items, shapes, and components. (optional) (default to False)
method_type = 'method_type_example' # str | Return URIs from storage methods with a particular type.  By default, return URLs with empty `methodType`. (optional)

try:
    # List all files for a shape
    api_response = api_instance.get_shape_files(id, shape_id, storage_type=storage_type, method_metadata=method_metadata, closed_files=closed_files, scheme=scheme, include_item=include_item, method_type=method_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **method_metadata** | [**list[str]**](str.md)| metadata used with storage method. | [optional] 
 **closed_files** | **bool**| - &#x60;true&#x60; (default) - Return only files that are closed.  - &#x60;false&#x60; - Return all files. | [optional] [default to True]
 **scheme** | **str**| URI scheme to return. | [optional] 
 **include_item** | **bool**| - &#x60;true&#x60; - Return associated items, shapes, and components.  - &#x60;false&#x60; (default) - Do not return any information about associated items, shapes, and components. | [optional] [default to False]
 **method_type** | **str**| Return URIs from storage methods with a particular type.  By default, return URLs with empty &#x60;methodType&#x60;. | [optional] 

### Return type

[**FileListType**](FileListType.md)

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

# **get_shape_graph**
> file get_shape_graph(id, shape_id)

Retrieve a graphical representation of a shape

Shows components and tracks in a graphical format.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # Retrieve a graphical representation of a shape
    api_response = api_instance.get_shape_graph(id, shape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 

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

# **get_shape_graph_dot**
> str get_shape_graph_dot(id, shape_id)

Retrieve a shape as a dot file

Shows components and tracks in a graphical format in dot format, for further processing.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # Retrieve a shape as a dot file
    api_response = api_instance.get_shape_graph_dot(id, shape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_graph_dot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 

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

# **get_shape_metadata**
> SimpleMetadataType get_shape_metadata(item_id, shape_id)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_shape_metadata(item_id, shape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 

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

# **get_shape_metadata_key**
> str get_shape_metadata_key(item_id, shape_id, keypath)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_shape_metadata_key(item_id, shape_id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
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

# **get_shape_mime_types**
> URIListType get_shape_mime_types(id, shape_id)

List all mime types for a shape

Lists all mime types that are set on the shape. These can also be seen the *ShapeDocument* of the shape.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.

try:
    # List all mime types for a shape
    api_response = api_instance.get_shape_mime_types(id, shape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_mime_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 

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
**0** | CRLF-delimited list of mime types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shape_storage_rules**
> StorageRulesType get_shape_storage_rules(item_id, shape_id, all=all)

List all storage rules that applies to a certain shape

Retrieves the storage rules that applies to a certain shape in a sorted manner. The rules are sorted according to priority, with the most important rule being first and the least important rule being last.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
all = False # bool | - `true` - Return all rules, regardless whether another rule overwrites it or not.  - `false` (default) - Return only rules that are in effect. (optional) (default to False)

try:
    # List all storage rules that applies to a certain shape
    api_response = api_instance.get_shape_storage_rules(item_id, shape_id, all=all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_storage_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **all** | **bool**| - &#x60;true&#x60; - Return all rules, regardless whether another rule overwrites it or not.  - &#x60;false&#x60; (default) - Return only rules that are in effect. | [optional] [default to False]

### Return type

[**StorageRulesType**](StorageRulesType.md)

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

# **get_shape_tags**
> URIListType get_shape_tags(item_id, shape_id, url=url)

List all tags for a shape

Retrieves all shape tags associated with a certain shape.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
url = False # bool | - `true` - Return list of URLs.  - `false` (default) - Return list of ids. (optional) (default to False)

try:
    # List all tags for a shape
    api_response = api_instance.get_shape_tags(item_id, shape_id, url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **url** | **bool**| - &#x60;true&#x60; - Return list of URLs.  - &#x60;false&#x60; (default) - Return list of ids. | [optional] [default to False]

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
**0** | A list of the tags. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shape_versions**
> EssenceVersionListType get_shape_versions(id)

List all essence versions

Returns a list containing URLs to all essence versions of the item.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # List all essence versions
    api_response = api_instance.get_shape_versions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shape_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

### Return type

[**EssenceVersionListType**](EssenceVersionListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;EssenceVersionListDocument&lt;/em&gt; containing information to all essence versions of the item. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shapes**
> URIListType get_shapes(id, version=version, placeholder=placeholder, url=url, tag=tag)

List all shapes

Returns all existing shapes for a specified item.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
version = 'latest' # str | - *essence-version-id* - Return shapes for a specified version.  - `all` - Return shapes for all versions.  - `latest` (default) - Return shapes for the latest version.  - `latest-per-shapetag` - Return shapes with the highest essence version number per shape tag. (optional) (default to 'latest')
placeholder = 'false' # str | - `true` - Only return placeholder shapes.  - `false` (default) - Only return non-placeholder shapes.  - `all` - Return all shapes. (optional) (default to 'false')
url = False # bool | - `true` - Return list of URLs.  - `false` (default) - Return list of ids. (optional) (default to False)
tag = ['tag_example'] # list[str] | Comma-separated list.  Only return shapes with these tags. (optional)

try:
    # List all shapes
    api_response = api_instance.get_shapes(id, version=version, placeholder=placeholder, url=url, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->get_shapes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **version** | **str**| - *essence-version-id* - Return shapes for a specified version.  - &#x60;all&#x60; - Return shapes for all versions.  - &#x60;latest&#x60; (default) - Return shapes for the latest version.  - &#x60;latest-per-shapetag&#x60; - Return shapes with the highest essence version number per shape tag. | [optional] [default to &#39;latest&#39;]
 **placeholder** | **str**| - &#x60;true&#x60; - Only return placeholder shapes.  - &#x60;false&#x60; (default) - Only return non-placeholder shapes.  - &#x60;all&#x60; - Return all shapes. | [optional] [default to &#39;false&#39;]
 **url** | **bool**| - &#x60;true&#x60; - Return list of URLs.  - &#x60;false&#x60; (default) - Return list of ids. | [optional] [default to False]
 **tag** | [**list[str]**](str.md)| Comma-separated list.  Only return shapes with these tags. | [optional] 

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
**0** | CRLF-delimited list of ids or URLs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_component**
> JobType import_component(id, shape_id, jobmetadata=jobmetadata, notification_data=notification_data, uri=uri, notification=notification, allow_reimport=allow_reimport, file_id=file_id, priority=priority)

Import a component using a URI or an existing file

Starts a job that imports a component to an existing shape. The shape must be a media shape and must not be a placeholder.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
uri = 'uri_example' # str | The URI to the file containing the new shape. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
allow_reimport = True # bool | - `true` - Import the file to this shape even if the file is already importing or is already part of another item.  - `false` (default) Reject the request if the file with the given id has already been imported or is currently importing. (optional)
file_id = 'file_id_example' # str | The id of the file that contains the new shape. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Import a component using a URI or an existing file
    api_response = api_instance.import_component(id, shape_id, jobmetadata=jobmetadata, notification_data=notification_data, uri=uri, notification=notification, allow_reimport=allow_reimport, file_id=file_id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->import_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **uri** | **str**| The URI to the file containing the new shape. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **allow_reimport** | **bool**| - &#x60;true&#x60; - Import the file to this shape even if the file is already importing or is already part of another item.  - &#x60;false&#x60; (default) Reject the request if the file with the given id has already been imported or is currently importing. | [optional] 
 **file_id** | **str**| The id of the file that contains the new shape. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]

### Return type

[**JobType**](JobType.md)

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

# **import_shape**
> JobType import_shape(id, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, tag=tag, uri=uri, notification=notification, allow_reimport=allow_reimport, file_id=file_id, priority=priority)

Import a shape using a URI or an existing file

Starts a new shape import job using either a URI or a file id.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
tag = 'tag_example' # str | The tags to assign to the new shape. (optional)
uri = 'uri_example' # str | A URI to the file that will be imported.  Make sure to percent encode the URI.  Must be specified unless `fileId` is specified. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
allow_reimport = True # bool | - `true` - Import the file to this shape even if the file is already importing or is already part of another item.  - `false` (default) Reject the request if the file with the given id has already been imported or is currently importing. (optional)
file_id = 'file_id_example' # str | The id of the file that contains the essence.  Must be specified unless `uri` is specified. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Import a shape using a URI or an existing file
    api_response = api_instance.import_shape(id, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, tag=tag, uri=uri, notification=notification, allow_reimport=allow_reimport, file_id=file_id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->import_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **tag** | **str**| The tags to assign to the new shape. | [optional] 
 **uri** | **str**| A URI to the file that will be imported.  Make sure to percent encode the URI.  Must be specified unless &#x60;fileId&#x60; is specified. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **allow_reimport** | **bool**| - &#x60;true&#x60; - Import the file to this shape even if the file is already importing or is already part of another item.  - &#x60;false&#x60; (default) Reject the request if the file with the given id has already been imported or is currently importing. | [optional] 
 **file_id** | **str**| The id of the file that contains the essence.  Must be specified unless &#x60;uri&#x60; is specified. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shape_create**
> ShapeType import_shape_create(id, shape_type, tag=tag, update_item_metadata=update_item_metadata)

Create a shape using shape technical information

Creates a new shape using the supplied information.  Changed in version 4.17.2: If the shape document has components that reference files (by id), then these files will be associated with the corresponding component.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_type = vidispine.ShapeType() # ShapeType | 
tag = 'tag_example' # str | The tags to assign to the new shape. (optional)
update_item_metadata = False # bool | If the shape is tagged `original` and this query parameter is `true`, the item's system metadata (e. g.  `durationSeconds`) is updated. (optional) (default to False)

try:
    # Create a shape using shape technical information
    api_response = api_instance.import_shape_create(id, shape_type, tag=tag, update_item_metadata=update_item_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->import_shape_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_type** | [**ShapeType**](ShapeType.md)|  | 
 **tag** | **str**| The tags to assign to the new shape. | [optional] 
 **update_item_metadata** | **bool**| If the shape is tagged &#x60;original&#x60; and this query parameter is &#x60;true&#x60;, the item&#39;s system metadata (e. g.  &#x60;durationSeconds&#x60;) is updated. | [optional] [default to False]

### Return type

[**ShapeType**](ShapeType.md)

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

# **import_shape_essence**
> JobType import_shape_essence(id, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, tag=tag, uri=uri, notification=notification, allow_reimport=allow_reimport, file_id=file_id, priority=priority)

Import an essence version using a URI or an existing file

Starts a new essence import job using either a URI or a file id.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
tag = 'tag_example' # str | The tags to assign to the new shape. (optional)
uri = 'uri_example' # str | A URI to the file that will be imported.  Make sure to percent encode the URI.  Must be specified unless `fileId` is specified. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
allow_reimport = True # bool | - `true` - Import the file to this shape even if the file is already importing or is already part of another item.  - `false` (default) Reject the request if the file with the given id has already been imported or is currently importing. (optional)
file_id = 'file_id_example' # str | The id of the file that contains the essence.  Must be specified unless `uri` is specified. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Import an essence version using a URI or an existing file
    api_response = api_instance.import_shape_essence(id, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, tag=tag, uri=uri, notification=notification, allow_reimport=allow_reimport, file_id=file_id, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->import_shape_essence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **tag** | **str**| The tags to assign to the new shape. | [optional] 
 **uri** | **str**| A URI to the file that will be imported.  Make sure to percent encode the URI.  Must be specified unless &#x60;fileId&#x60; is specified. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **allow_reimport** | **bool**| - &#x60;true&#x60; - Import the file to this shape even if the file is already importing or is already part of another item.  - &#x60;false&#x60; (default) Reject the request if the file with the given id has already been imported or is currently importing. | [optional] 
 **file_id** | **str**| The id of the file that contains the essence.  Must be specified unless &#x60;uri&#x60; is specified. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shape_essence_raw**
> JobType import_shape_essence_raw(id, body, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, tag=tag, transfer_priority=transfer_priority, notification=notification, priority=priority, filename=filename, transfer_id=transfer_id)

Import an essence version using the request body

Starts a new essence import job using the data in the request data.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
body = '/path/to/file' # file | The raw essence data.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
tag = 'tag_example' # str | The tags to assign to the new shape. (optional)
transfer_priority = 56 # int | An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
filename = 'filename_example' # str | The filename to be stored as original filename (optional)
transfer_id = 'transfer_id_example' # str | An id to assign the transfer to be able to refer to it. (optional)

try:
    # Import an essence version using the request body
    api_response = api_instance.import_shape_essence_raw(id, body, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, tag=tag, transfer_priority=transfer_priority, notification=notification, priority=priority, filename=filename, transfer_id=transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->import_shape_essence_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **body** | **file**| The raw essence data. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **tag** | **str**| The tags to assign to the new shape. | [optional] 
 **transfer_priority** | **int**| An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **filename** | **str**| The filename to be stored as original filename | [optional] 
 **transfer_id** | **str**| An id to assign the transfer to be able to refer to it. | [optional] 

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shape_imf_package**
> JobType import_shape_imf_package(id, remove_old_essence_files=remove_old_essence_files, notification_data=notification_data, storage_id=storage_id, tag=tag, uri=uri, notification=notification, jobmetadata=jobmetadata, import_tag=import_tag, priority=priority)

Import a shape from an IMF package

Starts a new shape import job using a URI of an IMF asset map

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
remove_old_essence_files = False # bool | - `true` - Remove files associated with shapes with same tags and lower essence version.  - `false` (default) - Keep the files belong to the shapes. (optional) (default to False)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
tag = 'tag_example' # str | The tags to assign to the new shape. (optional)
uri = 'uri_example' # str | The URI of the asset map (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
import_tag = ["original"] # list[str] | A list of shape tags that the created shape will be associated with. (optional) (default to ["original"])
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Import a shape from an IMF package
    api_response = api_instance.import_shape_imf_package(id, remove_old_essence_files=remove_old_essence_files, notification_data=notification_data, storage_id=storage_id, tag=tag, uri=uri, notification=notification, jobmetadata=jobmetadata, import_tag=import_tag, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->import_shape_imf_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **remove_old_essence_files** | **bool**| - &#x60;true&#x60; - Remove files associated with shapes with same tags and lower essence version.  - &#x60;false&#x60; (default) - Keep the files belong to the shapes. | [optional] [default to False]
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **tag** | **str**| The tags to assign to the new shape. | [optional] 
 **uri** | **str**| The URI of the asset map | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **import_tag** | [**list[str]**](str.md)| A list of shape tags that the created shape will be associated with. | [optional] [default to [&quot;original&quot;]]
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shape_raw**
> JobType import_shape_raw(id, body, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, tag=tag, transfer_priority=transfer_priority, notification=notification, priority=priority, filename=filename, transfer_id=transfer_id)

Import a shape using the request body

Starts a new shape import job using the data in the request data.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
body = '/path/to/file' # file | The raw essence data.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
storage_id = 'storage_id_example' # str | Identifier of storage where essence file is to be stored. (optional)
tag = 'tag_example' # str | The tags to assign to the new shape. (optional)
transfer_priority = 56 # int | An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. (optional)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
filename = 'filename_example' # str | The filename to be stored as original filename (optional)
transfer_id = 'transfer_id_example' # str | An id to assign the transfer to be able to refer to it. (optional)

try:
    # Import a shape using the request body
    api_response = api_instance.import_shape_raw(id, body, jobmetadata=jobmetadata, notification_data=notification_data, storage_id=storage_id, tag=tag, transfer_priority=transfer_priority, notification=notification, priority=priority, filename=filename, transfer_id=transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->import_shape_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **body** | **file**| The raw essence data. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **storage_id** | **str**| Identifier of storage where essence file is to be stored. | [optional] 
 **tag** | **str**| The tags to assign to the new shape. | [optional] 
 **transfer_priority** | **int**| An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. | [optional] 
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **priority** | **str**| The priority to assign to the job. | [optional] [default to &#39;MEDIUM&#39;]
 **filename** | **str**| The filename to be stored as original filename | [optional] 
 **transfer_id** | **str**| An id to assign the transfer to be able to refer to it. | [optional] 

### Return type

[**JobType**](JobType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;JobDocument&lt;/em&gt; that describes the import job. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_component_to_component**
> ShapeType move_component_to_component(id, shape_id, component_id, target_id, target_shape_id, target_component_id, index=index, keep_metadata=keep_metadata)

Move a component to another shape/component

Move this component to another shape, replacing a specific component by id.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
target_id = 'target_id_example' # str | The target id.
target_shape_id = 'target_shape_id_example' # str | The target shape id.
target_component_id = 'target_component_id_example' # str | The target component id.
index = 56 # int | The component index (track) of component.  If the target shape has a component with this index, then it will be replaced/removed. (optional)
keep_metadata = False # bool | - `true` - Preserve the metadata from the replaced component.  - `false` (default) - Discard any metadata from the replaced component. (optional) (default to False)

try:
    # Move a component to another shape/component
    api_response = api_instance.move_component_to_component(id, shape_id, component_id, target_id, target_shape_id, target_component_id, index=index, keep_metadata=keep_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->move_component_to_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
 **target_id** | **str**| The target id. | 
 **target_shape_id** | **str**| The target shape id. | 
 **target_component_id** | **str**| The target component id. | 
 **index** | **int**| The component index (track) of component.  If the target shape has a component with this index, then it will be replaced/removed. | [optional] 
 **keep_metadata** | **bool**| - &#x60;true&#x60; - Preserve the metadata from the replaced component.  - &#x60;false&#x60; (default) - Discard any metadata from the replaced component. | [optional] [default to False]

### Return type

[**ShapeType**](ShapeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;ShapeDocument&lt;/em&gt; from the target shape. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_component_to_shape**
> ShapeType move_component_to_shape(id, shape_id, component_id, target_id, target_shape_id, index=index, keep_metadata=keep_metadata)

Move a component to another shape

Move this component to another shape.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
target_id = 'target_id_example' # str | The target id.
target_shape_id = 'target_shape_id_example' # str | The target shape id.
index = 56 # int | The component index (track) of component.  If the target shape has a component with this index, then it will be replaced/removed. (optional)
keep_metadata = False # bool | - `true` - Preserve the metadata from the replaced component.  - `false` (default) - Discard any metadata from the replaced component. (optional) (default to False)

try:
    # Move a component to another shape
    api_response = api_instance.move_component_to_shape(id, shape_id, component_id, target_id, target_shape_id, index=index, keep_metadata=keep_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->move_component_to_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
 **target_id** | **str**| The target id. | 
 **target_shape_id** | **str**| The target shape id. | 
 **index** | **int**| The component index (track) of component.  If the target shape has a component with this index, then it will be replaced/removed. | [optional] 
 **keep_metadata** | **bool**| - &#x60;true&#x60; - Preserve the metadata from the replaced component.  - &#x60;false&#x60; (default) - Discard any metadata from the replaced component. | [optional] [default to False]

### Return type

[**ShapeType**](ShapeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | &lt;em&gt;ShapeDocument&lt;/em&gt; from the target shape. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_file_from_component**
> remove_file_from_component(id, shape_id, component_id, file_id)

Remove a file from a component

Removes the specified file from the specified component

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
file_id = 'file_id_example' # str | The file id.

try:
    # Remove a file from a component
    api_instance.remove_file_from_component(id, shape_id, component_id, file_id)
except ApiException as e:
    print("Exception when calling ShapeApi->remove_file_from_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
 **file_id** | **str**| The file id. | 

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

# **remove_shape_tag**
> remove_shape_tag(item_id, shape_id, tag_name)

Remove a tag from a shape

Removes a tag with the given name from the specified shape.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
tag_name = 'tag_name_example' # str | The tag name.

try:
    # Remove a tag from a shape
    api_instance.remove_shape_tag(item_id, shape_id, tag_name)
except ApiException as e:
    print("Exception when calling ShapeApi->remove_shape_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **tag_name** | **str**| The tag name. | 

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

# **update_component_metadata**
> update_component_metadata(item_id, shape_id, component_id, simple_metadata_type)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_component_metadata(item_id, shape_id, component_id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling ShapeApi->update_component_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
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

# **update_component_metadata_key**
> update_component_metadata_key(item_id, shape_id, component_id, keypath, body)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
component_id = 'component_id_example' # str | The component id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_component_metadata_key(item_id, shape_id, component_id, keypath, body)
except ApiException as e:
    print("Exception when calling ShapeApi->update_component_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
 **component_id** | **str**| The component id. | 
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

# **update_shape_metadata**
> update_shape_metadata(item_id, shape_id, simple_metadata_type)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_shape_metadata(item_id, shape_id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling ShapeApi->update_shape_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
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

# **update_shape_metadata_key**
> update_shape_metadata_key(item_id, shape_id, keypath, body)

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape_id = 'shape_id_example' # str | The shape id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_shape_metadata_key(item_id, shape_id, keypath, body)
except ApiException as e:
    print("Exception when calling ShapeApi->update_shape_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape_id** | **str**| The shape id. | 
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

# **update_shape_placeholder**
> update_shape_placeholder(id, shape_id, simple_metadata_type, tag=tag, video=video, binary=binary, audio=audio, container=container)

Update a placeholder shape

Updates the expected number of container, video, audio and binary components for a specific placeholder shape.

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
api_instance = vidispine.ShapeApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.
shape_id = 'shape_id_example' # str | The shape id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 
tag = 'tag_example' # str | Comma-separated shape tags to be added to the shape. (optional)
video = 56 # int | The number of video components (optional)
binary = 56 # int | The number of binary components (optional)
audio = 56 # int | The number of audio components (optional)
container = 56 # int | The number of container components (optional)

try:
    # Update a placeholder shape
    api_instance.update_shape_placeholder(id, shape_id, simple_metadata_type, tag=tag, video=video, binary=binary, audio=audio, container=container)
except ApiException as e:
    print("Exception when calling ShapeApi->update_shape_placeholder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 
 **shape_id** | **str**| The shape id. | 
 **simple_metadata_type** | [**SimpleMetadataType**](SimpleMetadataType.md)|  | 
 **tag** | **str**| Comma-separated shape tags to be added to the shape. | [optional] 
 **video** | **int**| The number of video components | [optional] 
 **binary** | **int**| The number of binary components | [optional] 
 **audio** | **int**| The number of audio components | [optional] 
 **container** | **int**| The number of container components | [optional] 

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

