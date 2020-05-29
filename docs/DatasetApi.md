# vidispine.DatasetApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_metadata_dataset**](DatasetApi.md#delete_metadata_dataset) | **DELETE** /metadata/dataset/{name} | Delete a dataset
[**get_metadata_dataset**](DatasetApi.md#get_metadata_dataset) | **GET** /metadata/dataset/{name} | Retrieve a dataset
[**get_metadata_datasets**](DatasetApi.md#get_metadata_datasets) | **GET** /metadata/dataset | List all datasets
[**update_or_create_metadata_dataset**](DatasetApi.md#update_or_create_metadata_dataset) | **PUT** /metadata/dataset/{name} | Update or create a dataset


# **delete_metadata_dataset**
> delete_metadata_dataset(name)

Delete a dataset

Removes the metadata dataset with the specified name.

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
api_instance = vidispine.DatasetApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.

try:
    # Delete a dataset
    api_instance.delete_metadata_dataset(name)
except ApiException as e:
    print("Exception when calling DatasetApi->delete_metadata_dataset: %s\n" % e)
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

# **get_metadata_dataset**
> str get_metadata_dataset(name)

Retrieve a dataset

Retrieves the metadata dataset with the specified name. The returned serialization format of the RDF model is `RDF/XML` or `TURTLE` depending on the request header.

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
api_instance = vidispine.DatasetApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.

try:
    # Retrieve a dataset
    api_response = api_instance.get_metadata_dataset(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->get_metadata_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/rdf+xml, text/turtle, application/ld+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The RDF model. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_datasets**
> MetadataDatasetListType get_metadata_datasets()

List all datasets

Retrieves the list of metadata datasets.

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
api_instance = vidispine.DatasetApi(vidispine.ApiClient(configuration))

try:
    # List all datasets
    api_response = api_instance.get_metadata_datasets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->get_metadata_datasets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataDatasetListType**](MetadataDatasetListType.md)

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

# **update_or_create_metadata_dataset**
> str update_or_create_metadata_dataset(name, body, id_seed=id_seed)

Update or create a dataset

Updates or creates the existing dataset with the specified name.

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
api_instance = vidispine.DatasetApi(vidispine.ApiClient(configuration))
name = 'name_example' # str | The name.
body = 'body_example' # str | The RDF model.
id_seed = 'id_seed_example' # str | A property name in the RDF model.  If the id of a subject is not provided in the model, the value of this property will be used to generate an id for this subject.  If not set or the subject doesn't have this property, a random id will be generated. (optional)

try:
    # Update or create a dataset
    api_response = api_instance.update_or_create_metadata_dataset(name, body, id_seed=id_seed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->update_or_create_metadata_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name. | 
 **body** | **str**| The RDF model. | 
 **id_seed** | **str**| A property name in the RDF model.  If the id of a subject is not provided in the model, the value of this property will be used to generate an id for this subject.  If not set or the subject doesn&#39;t have this property, a random id will be generated. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/rdf+xml, text/turtle, application/ld+json
 - **Accept**: application/rdf+xml, text/turtle, application/ld+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The RDF model. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

