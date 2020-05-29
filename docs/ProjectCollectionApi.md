# vidispine.ProjectCollectionApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectCollectionApi.md#create_project) | **POST** /collection/project | Create a project collection
[**inspect_project**](ProjectCollectionApi.md#inspect_project) | **POST** /collection/project/inspect | Inspect a project file


# **create_project**
> URIListType create_project(project_type)

Create a project collection

Creates a project collection with the given name and metadata.

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
api_instance = vidispine.ProjectCollectionApi(vidispine.ApiClient(configuration))
project_type = vidispine.ProjectType() # ProjectType | 

try:
    # Create a project collection
    api_response = api_instance.create_project(project_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectCollectionApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_type** | [**ProjectType**](ProjectType.md)|  | 

### Return type

[**URIListType**](URIListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspect_project**
> ProjectFileType inspect_project(essence_mappings_type, type=type, uri=uri)

Inspect a project file

Returns a document listing the sequences and assets referenced from a given project file.

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
api_instance = vidispine.ProjectCollectionApi(vidispine.ApiClient(configuration))
essence_mappings_type = vidispine.EssenceMappingsType() # EssenceMappingsType | 
type = 'type_example' # str | The file format. (optional)
uri = 'uri_example' # str | The location of the file to inspect. (optional)

try:
    # Inspect a project file
    api_response = api_instance.inspect_project(essence_mappings_type, type=type, uri=uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectCollectionApi->inspect_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **essence_mappings_type** | [**EssenceMappingsType**](EssenceMappingsType.md)|  | 
 **type** | **str**| The file format. | [optional] 
 **uri** | **str**| The location of the file to inspect. | [optional] 

### Return type

[**ProjectFileType**](ProjectFileType.md)

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

