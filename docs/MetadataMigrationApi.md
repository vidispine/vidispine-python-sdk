# vidispine.MetadataMigrationApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata_migration**](MetadataMigrationApi.md#create_metadata_migration) | **POST** /metadata/migration | Create a metadata migration
[**get_metadata_migration**](MetadataMigrationApi.md#get_metadata_migration) | **GET** /metadata/migration/{id} | Retrieve a metadata migration
[**get_metadata_migrations**](MetadataMigrationApi.md#get_metadata_migrations) | **GET** /metadata/migration | List all metadata migrations


# **create_metadata_migration**
> str create_metadata_migration(metadata_schema_migration_type)

Create a metadata migration

Creates a new metadata migration.

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
api_instance = vidispine.MetadataMigrationApi(vidispine.ApiClient(configuration))
metadata_schema_migration_type = vidispine.MetadataSchemaMigrationType() # MetadataSchemaMigrationType | 

try:
    # Create a metadata migration
    api_response = api_instance.create_metadata_migration(metadata_schema_migration_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataMigrationApi->create_metadata_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_schema_migration_type** | [**MetadataSchemaMigrationType**](MetadataSchemaMigrationType.md)|  | 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_migration**
> MetadataSchemaMigrationType get_metadata_migration(id)

Retrieve a metadata migration

Shows a single metadata migration.

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
api_instance = vidispine.MetadataMigrationApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # Retrieve a metadata migration
    api_response = api_instance.get_metadata_migration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataMigrationApi->get_metadata_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

### Return type

[**MetadataSchemaMigrationType**](MetadataSchemaMigrationType.md)

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

# **get_metadata_migrations**
> MetadataSchemaMigrationListType get_metadata_migrations()

List all metadata migrations

Lists all metadata migrations defined in the system.

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
api_instance = vidispine.MetadataMigrationApi(vidispine.ApiClient(configuration))

try:
    # List all metadata migrations
    api_response = api_instance.get_metadata_migrations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataMigrationApi->get_metadata_migrations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataSchemaMigrationListType**](MetadataSchemaMigrationListType.md)

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

