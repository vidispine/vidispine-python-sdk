# vidispine.FileApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FileApi.md#create_file) | **POST** /storage/file/data | Upload a file to a storage
[**create_file_delete_job**](FileApi.md#create_file_delete_job) | **DELETE** /file/{file-id} | Delete a file
[**create_file_entity**](FileApi.md#create_file_entity) | **POST** /storage/file | Register a file
[**create_file_entity_on_storage**](FileApi.md#create_file_entity_on_storage) | **POST** /storage/{storage-id}/file | Register a file
[**create_file_in_storage**](FileApi.md#create_file_in_storage) | **POST** /storage/{storage-id}/file/data | Upload a file to a storage
[**create_file_move_or_copy_job**](FileApi.md#create_file_move_or_copy_job) | **POST** /file/{file-id}/storage/{target-storage-id} | Move/copy a file to another storage
[**create_file_temp_credentials**](FileApi.md#create_file_temp_credentials) | **POST** /file/{file-id}/uri | Generate temporary credentials
[**delete_file_entity**](FileApi.md#delete_file_entity) | **DELETE** /file/{file-id}/entity | Unregister a file
[**delete_file_metadata**](FileApi.md#delete_file_metadata) | **DELETE** /file/{file-id}/metadata | Delete all key-value pairs
[**delete_file_metadata_key**](FileApi.md#delete_file_metadata_key) | **DELETE** /file/{file-id}/metadata/{keypath} | Delete key-value pairs
[**get_file**](FileApi.md#get_file) | **GET** /file/{file-id} | Retrieve a file
[**get_file_data**](FileApi.md#get_file_data) | **GET** /file/{file-id}/data | Retrieve the file data
[**get_file_metadata**](FileApi.md#get_file_metadata) | **GET** /file/{file-id}/metadata | Retrieve all metadata
[**get_file_metadata_key**](FileApi.md#get_file_metadata_key) | **GET** /file/{file-id}/metadata/{keypath} | Retrieve the metadata for a specific key
[**get_files**](FileApi.md#get_files) | **GET** /storage/file | List all files in a storage
[**register_file_path**](FileApi.md#register_file_path) | **POST** /file/{file-id}/path | Register a new file path
[**reindex_file**](FileApi.md#reindex_file) | **PUT** /file/{file-id}/re-index | Re-index a file
[**remove_file_from_item**](FileApi.md#remove_file_from_item) | **PUT** /file/{file-id}/abandon | Remove a file from an item
[**restore_file**](FileApi.md#restore_file) | **PUT** /file/{file-id}/restore | Transitioning files From S3 to Glacier
[**update_file_data**](FileApi.md#update_file_data) | **POST** /file/{file-id}/data | Update or create file data
[**update_file_hash**](FileApi.md#update_file_hash) | **PUT** /file/{file-id}/hash/{hash} | Set file hash
[**update_file_metadata**](FileApi.md#update_file_metadata) | **PUT** /file/{file-id}/metadata | Create multiple key-value pairs
[**update_file_metadata_key**](FileApi.md#update_file_metadata_key) | **PUT** /file/{file-id}/metadata/{keypath} | Set the value for a specific key
[**update_file_state**](FileApi.md#update_file_state) | **PUT** /file/{file-id}/state/{state} | Update the file state


# **create_file**
> FileType create_file(body, state=state, uri=uri, transfer_priority=transfer_priority, transfer_id=transfer_id, path=path)

Upload a file to a storage

Creates a new file on a specific storage, with the given file data.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
body = '/path/to/file' # file | The raw essence data.
state = 'state_example' # str | The state of the file. (optional)
uri = 'uri_example' # str | The absolute file URI (should be relative to the URI of a storage method). (optional)
transfer_priority = 56 # int | An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. (optional)
transfer_id = 'transfer_id_example' # str | An id to assign the transfer to be able to refer to it. (optional)
path = 'path_example' # str | The path of the file on the storage. (optional)

try:
    # Upload a file to a storage
    api_response = api_instance.create_file(body, state=state, uri=uri, transfer_priority=transfer_priority, transfer_id=transfer_id, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file**| The raw essence data. | 
 **state** | **str**| The state of the file. | [optional] 
 **uri** | **str**| The absolute file URI (should be relative to the URI of a storage method). | [optional] 
 **transfer_priority** | **int**| An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. | [optional] 
 **transfer_id** | **str**| An id to assign the transfer to be able to refer to it. | [optional] 
 **path** | **str**| The path of the file on the storage. | [optional] 

### Return type

[**FileType**](FileType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | file id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_delete_job**
> JobType create_file_delete_job(file_id, jobmetadata=jobmetadata, notification_data=notification_data, priority=priority, notification=notification)

Delete a file

Starts a delete job for the specified file.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)

try:
    # Delete a file
    api_response = api_instance.create_file_delete_job(file_id, jobmetadata=jobmetadata, notification_data=notification_data, priority=priority, notification=notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->create_file_delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
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

# **create_file_entity**
> FileType create_file_entity(file_type, create_only=create_only)

Register a file

Creates a file entity in the database. Does not create any physical files. Either a storage id and path or an absolute URI may be given.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_type = vidispine.FileType() # FileType | <em>FileDocument</em> with the path or URI and file state.
create_only = True # bool | - `true` (default) - Fail if a file with that path already exists.  - `false` - Update the existing file if one exists, else create a new file entity. (optional) (default to True)

try:
    # Register a file
    api_response = api_instance.create_file_entity(file_type, create_only=create_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->create_file_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_type** | [**FileType**](FileType.md)| &lt;em&gt;FileDocument&lt;/em&gt; with the path or URI and file state. | 
 **create_only** | **bool**| - &#x60;true&#x60; (default) - Fail if a file with that path already exists.  - &#x60;false&#x60; - Update the existing file if one exists, else create a new file entity. | [optional] [default to True]

### Return type

[**FileType**](FileType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The id of the new or updated file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_entity_on_storage**
> FileType create_file_entity_on_storage(storage_id, file_type, create_only=create_only)

Register a file

Creates a file entity in the database. Does not create any physical files. Either a storage id and path or an absolute URI may be given.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
file_type = vidispine.FileType() # FileType | <em>FileDocument</em> with the path or URI and file state.
create_only = True # bool | - `true` (default) - Fail if a file with that path already exists.  - `false` - Update the existing file if one exists, else create a new file entity. (optional) (default to True)

try:
    # Register a file
    api_response = api_instance.create_file_entity_on_storage(storage_id, file_type, create_only=create_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->create_file_entity_on_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **file_type** | [**FileType**](FileType.md)| &lt;em&gt;FileDocument&lt;/em&gt; with the path or URI and file state. | 
 **create_only** | **bool**| - &#x60;true&#x60; (default) - Fail if a file with that path already exists.  - &#x60;false&#x60; - Update the existing file if one exists, else create a new file entity. | [optional] [default to True]

### Return type

[**FileType**](FileType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The id of the new or updated file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_in_storage**
> FileType create_file_in_storage(storage_id, body, state=state, uri=uri, transfer_priority=transfer_priority, transfer_id=transfer_id, path=path)

Upload a file to a storage

Creates a new file on a specific storage, with the given file data.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
storage_id = 'storage_id_example' # str | The storage id.
body = '/path/to/file' # file | The raw essence data.
state = 'state_example' # str | The state of the file. (optional)
uri = 'uri_example' # str | The absolute file URI (should be relative to the URI of a storage method). (optional)
transfer_priority = 56 # int | An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. (optional)
transfer_id = 'transfer_id_example' # str | An id to assign the transfer to be able to refer to it. (optional)
path = 'path_example' # str | The path of the file on the storage. (optional)

try:
    # Upload a file to a storage
    api_response = api_instance.create_file_in_storage(storage_id, body, state=state, uri=uri, transfer_priority=transfer_priority, transfer_id=transfer_id, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->create_file_in_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| The storage id. | 
 **body** | **file**| The raw essence data. | 
 **state** | **str**| The state of the file. | [optional] 
 **uri** | **str**| The absolute file URI (should be relative to the URI of a storage method). | [optional] 
 **transfer_priority** | **int**| An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. | [optional] 
 **transfer_id** | **str**| An id to assign the transfer to be able to refer to it. | [optional] 
 **path** | **str**| The path of the file on the storage. | [optional] 

### Return type

[**FileType**](FileType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | file id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_move_or_copy_job**
> JobType create_file_move_or_copy_job(file_id, target_storage_id, jobmetadata=jobmetadata, notification_data=notification_data, move=move, use_original_filename=use_original_filename, notification=notification, time_requirement=time_requirement, limit_rate=limit_rate, filename=filename, priority=priority)

Move/copy a file to another storage

Starts a move or copy job for the specified file.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
target_storage_id = 'target_storage_id_example' # str | The target storage id.
jobmetadata = ['jobmetadata_example'] # list[str] | Additional information for the job task. (optional)
notification_data = 'notification_data_example' # str | Any additional data to include for notifications on this job. (optional)
move = True # bool | - `true` - Delete the original file when the copy has finished.  - `false` - Just copy the file, and leave the original. (optional)
use_original_filename = False # bool | If set to `true`, the file will keep its original filename if available. (optional) (default to False)
notification = 'notification_example' # str | The placeholder job notification to use for this job. (optional)
time_requirement = 56 # int | Number of seconds the target file is required to exist before being moved due to storage rules etc. (optional)
limit_rate = 56 # int | Throttle the rate at which the transfer takes place (bytes/second). (optional)
filename = 'filename_example' # str | The desired target filename. (optional)
priority = 'MEDIUM' # str | The priority to assign to the job. (optional) (default to 'MEDIUM')

try:
    # Move/copy a file to another storage
    api_response = api_instance.create_file_move_or_copy_job(file_id, target_storage_id, jobmetadata=jobmetadata, notification_data=notification_data, move=move, use_original_filename=use_original_filename, notification=notification, time_requirement=time_requirement, limit_rate=limit_rate, filename=filename, priority=priority)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->create_file_move_or_copy_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
 **target_storage_id** | **str**| The target storage id. | 
 **jobmetadata** | [**list[str]**](str.md)| Additional information for the job task. | [optional] 
 **notification_data** | **str**| Any additional data to include for notifications on this job. | [optional] 
 **move** | **bool**| - &#x60;true&#x60; - Delete the original file when the copy has finished.  - &#x60;false&#x60; - Just copy the file, and leave the original. | [optional] 
 **use_original_filename** | **bool**| If set to &#x60;true&#x60;, the file will keep its original filename if available. | [optional] [default to False]
 **notification** | **str**| The placeholder job notification to use for this job. | [optional] 
 **time_requirement** | **int**| Number of seconds the target file is required to exist before being moved due to storage rules etc. | [optional] 
 **limit_rate** | **int**| Throttle the rate at which the transfer takes place (bytes/second). | [optional] 
 **filename** | **str**| The desired target filename. | [optional] 
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

# **create_file_temp_credentials**
> URIListType create_file_temp_credentials(file_id, write=write, scheme=scheme, duration=duration)

Generate temporary credentials

Generates temporary access credentials that give either READ or WRITE access directly to the file. By default, if the file is on S3 or Azure, this will try to create a read-only pre-signed URL for the file; if this fail or if the file is on another type of storage, it will try to create a proxy URL (with direct access to the file).  When using the s3 scheme there are certain prerequisites that need to be met regarding policies and trust relationships with the account in use.  The permission policy for the role will only require `s3:GetObject` and `s3:PutObject` permissions to use the basic features. If you intend to use this for multipart uploads you might also want to add the permissions for `s3:ListMultipartUploadParts` and `s3:AbortMultipartUpload`. Finally this role will also need a trust relationship with an account with access to the storage(s) as an intersection is made to decide permissions in the end.  Vidispine will then create a custom policy to limit the credentials to either GET or PUT as requested.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
write = False # bool | Sets permission to either READ or WRITE.   - `true` - Will give credentials with access to write.  This would also enable the optional permissions for `s3:ListMultipartUploadParts` and `s3:AbortMultipartUpload` if used together with the `s3` scheme.  - `false` (default) - Will give credentials with access to read. (optional) (default to False)
scheme = 'https' # str | Determines which type of URL / URI to be returned.   - `s3` Utilize AWS's AssumeRole to generate a temporary URI giving access to only the specific file.  Can be used either by setting the `stsAssumeRole` property to specify which role to assume when generating the credentials OR by leaving this unset which will make Vidispine try to use a role from an EC2 instance profile.  These will also look at the configuration property for `stsRegion` and use that region when making the call to the STS API.  - `https` (default) - Generates a temporary pre-signed HTTPS URL for either S3 or Azure, or a proxy URL (based on the configuration property `apiNoauthUri`) if on another type of storage.  - `http` - Same as `https` but will also allow HTTP URL's to be returned. (optional) (default to 'https')
duration = 56 # int | Optional, sets the duration of the temporary credentials in minutes.  Default is set to 15 minutes and the maximum is 720.  Changed in version 4. 17. 7: The minimum duration for pre-signed URLs is 1 minute and when using the S3 scheme the minimum is 15 minutes. (optional)

try:
    # Generate temporary credentials
    api_response = api_instance.create_file_temp_credentials(file_id, write=write, scheme=scheme, duration=duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->create_file_temp_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
 **write** | **bool**| Sets permission to either READ or WRITE.   - &#x60;true&#x60; - Will give credentials with access to write.  This would also enable the optional permissions for &#x60;s3:ListMultipartUploadParts&#x60; and &#x60;s3:AbortMultipartUpload&#x60; if used together with the &#x60;s3&#x60; scheme.  - &#x60;false&#x60; (default) - Will give credentials with access to read. | [optional] [default to False]
 **scheme** | **str**| Determines which type of URL / URI to be returned.   - &#x60;s3&#x60; Utilize AWS&#39;s AssumeRole to generate a temporary URI giving access to only the specific file.  Can be used either by setting the &#x60;stsAssumeRole&#x60; property to specify which role to assume when generating the credentials OR by leaving this unset which will make Vidispine try to use a role from an EC2 instance profile.  These will also look at the configuration property for &#x60;stsRegion&#x60; and use that region when making the call to the STS API.  - &#x60;https&#x60; (default) - Generates a temporary pre-signed HTTPS URL for either S3 or Azure, or a proxy URL (based on the configuration property &#x60;apiNoauthUri&#x60;) if on another type of storage.  - &#x60;http&#x60; - Same as &#x60;https&#x60; but will also allow HTTP URL&#39;s to be returned. | [optional] [default to &#39;https&#39;]
 **duration** | **int**| Optional, sets the duration of the temporary credentials in minutes.  Default is set to 15 minutes and the maximum is 720.  Changed in version 4. 17. 7: The minimum duration for pre-signed URLs is 1 minute and when using the S3 scheme the minimum is 15 minutes. | [optional] 

### Return type

[**URIListType**](URIListType.md)

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

# **delete_file_entity**
> delete_file_entity(file_id)

Unregister a file

Deletes a file entity from the database. Does not touch the physical file.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.

try:
    # Unregister a file
    api_instance.delete_file_entity(file_id)
except ApiException as e:
    print("Exception when calling FileApi->delete_file_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_file_metadata**
> delete_file_metadata(file_id)

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.

try:
    # Delete all key-value pairs
    api_instance.delete_file_metadata(file_id)
except ApiException as e:
    print("Exception when calling FileApi->delete_file_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_file_metadata_key**
> delete_file_metadata_key(file_id, keypath)

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Delete key-value pairs
    api_instance.delete_file_metadata_key(file_id, keypath)
except ApiException as e:
    print("Exception when calling FileApi->delete_file_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
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

# **get_file**
> FileType get_file(file_id, storage_type=storage_type, method_type=method_type, method_metadata=method_metadata, include_item=include_item, scheme=scheme)

Retrieve a file

Retrieves the information, such as file size, status and checksum, of a specific file.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
method_type = 'method_type_example' # str | Return URIs from storage methods with a particular type.  By default, return URLs with empty `methodType`. (optional)
method_metadata = ['method_metadata_example'] # list[str] | metadata used with storage method. (optional)
include_item = False # bool | - `true` - Return associated items, shapes, and components.  - `false` (default) - Do not return any information about associated items, shapes, and components. (optional) (default to False)
scheme = 'scheme_example' # str | URI scheme to return. (optional)

try:
    # Retrieve a file
    api_response = api_instance.get_file(file_id, storage_type=storage_type, method_type=method_type, method_metadata=method_metadata, include_item=include_item, scheme=scheme)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **method_type** | **str**| Return URIs from storage methods with a particular type.  By default, return URLs with empty &#x60;methodType&#x60;. | [optional] 
 **method_metadata** | [**list[str]**](str.md)| metadata used with storage method. | [optional] 
 **include_item** | **bool**| - &#x60;true&#x60; - Return associated items, shapes, and components.  - &#x60;false&#x60; (default) - Do not return any information about associated items, shapes, and components. | [optional] [default to False]
 **scheme** | **str**| URI scheme to return. | [optional] 

### Return type

[**FileType**](FileType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | TabbedTuple of file id, file path, file size, file status, timestamp |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_data**
> file get_file_data(file_id)

Retrieve the file data

Retrieves the raw file data.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.

try:
    # Retrieve the file data
    api_response = api_instance.get_file_data(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_file_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The raw file data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata**
> SimpleMetadataType get_file_metadata(file_id)

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.

try:
    # Retrieve all metadata
    api_response = api_instance.get_file_metadata(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_file_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 

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

# **get_file_metadata_key**
> str get_file_metadata_key(file_id, keypath)

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
keypath = 'keypath_example' # str | The keypath.

try:
    # Retrieve the metadata for a specific key
    api_response = api_instance.get_file_metadata_key(file_id, keypath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_file_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
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

# **get_files**
> FileListType get_files(storage_type=storage_type, first=first, prefix_first=prefix_first, number=number, storage_group=storage_group, ignorecase=ignorecase, prefix=prefix, exclude_queued=exclude_queued, wildcard=wildcard, state=state, algorithm=algorithm, method_type=method_type, prefix_number=prefix_number, method_metadata=method_metadata, storage=storage, scheme=scheme, recursive=recursive, cursor=cursor, id=id, count=count, sort=sort, hash=hash, filter=filter, include_item=include_item, path=path)

List all files in a storage

Retrieves the files for all or a specific storage.  There is a limit on how many files that can be returned for each call to this method. To get all files, iterate the calls.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
storage_type = 'storage_type_example' # str | Only return URIs for files from storages of this type. (optional)
first = 0 # int | From total list of files, start return list from specified number. (optional) (default to 0)
prefix_first = 0 # int | From total list of prefixes, start return list from specified number.  Note: this parameter has no effect if Elasticsearch is the search backend. (optional) (default to 0)
number = 10 # int | Return a maximum of specified number of files. (optional) (default to 10)
storage_group = 'storage_group_example' # str | Storage group id.  Return only files from storages specified in the storage group (optional)
ignorecase = True # bool | - `true` - Search file path case insensitively - `false` - Search file path case sensitively (optional)
prefix = True # bool | - `true` - Also include file prefixes that matches the criteria - `false` (default) - Do not include file prefixes (optional)
exclude_queued = True # bool | - `true` - Exclude the files that are queued for import - `false` (default) - Do not exclude the files that are queued for import (optional)
wildcard = False # bool | - `true` - Allow use of wildcards in path.  - `false` (default) - No wildcard handling of path. (optional) (default to False)
state = ['state_example'] # list[str] | Filter results by file state.  Can be used multiple times to select several states. (optional)
algorithm = 'algorithm_example' # str | Hash algorithm.  Search for hash values used by specified algorithm (optional)
method_type = 'method_type_example' # str | Return URIs from storage methods with a particular type.  By default, return URLs with empty `methodType`. (optional)
prefix_number = 10 # int | Return a maximum of specified number of prefixes. (optional) (default to 10)
method_metadata = ['method_metadata_example'] # list[str] | metadata used with storage method. (optional)
storage = ['storage_example'] # list[str] | List of storage ids.  Return only files from specific storages.  Same as `storage-id` in URL, but can be specified multiple times (optional)
scheme = 'scheme_example' # str | URI scheme to return. (optional)
recursive = True # bool | - `true` (default) - Return all files in tree.  - `false` - Return only files directly under specified path. (optional) (default to True)
cursor = 'cursor_example' # str | New in version 4. 16.   - `*` - The initial cursor.  - `string-from-search` - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When `cursor` is used, The value of `first` will be ignored.  Only metadata searches in the `generic` interval supports `cursor`. (optional)
id = ['id_example'] # list[str] | If multiple `id` query parameters are specified only those files are returned.  If no ids are specified, all files are returned. (optional)
count = True # bool | - `true` (default) - Return total number of hits in result - `false` - Do not return total number of hits in result, in order to produce results faster (optional) (default to True)
sort = ['sort_example'] # list[str] | Comma-separated list.   - `fileId` [ `asc` (default) | `desc` ] (default) - Order results by file id.  - `size` [ `asc` (default) | `desc` ] - Order results by file size (bytes).  - `state` [ `asc` (default) | `desc` ] - Order results by file state.  - `timestamp` [ `asc` (default) | `desc` ] - Order results by file timestamp.  - `filename` [ `asc` (default) | `desc` ] - Order results by filename.  - `extension` [ `asc` (default) | `desc` ] - Order results by file extension. (optional)
hash = ['hash_example'] # list[str] | List of hash values.  Only return files with specific hash value. (optional)
filter = 'all' # str | - `all` (default) - Return all files - `item` Only return files associated with an item.  - `noitem` Only return files not associated with any item. (optional) (default to 'all')
include_item = False # bool | - `true` - Return associated items, shapes, and components.  - `false` (default) - Do not return any information about associated items, shapes, and components. (optional) (default to False)
path = '/' # str | - *path* - Return files under this sub-path to storage.  - `/` (default) - Return all files. (optional) (default to '/')

try:
    # List all files in a storage
    api_response = api_instance.get_files(storage_type=storage_type, first=first, prefix_first=prefix_first, number=number, storage_group=storage_group, ignorecase=ignorecase, prefix=prefix, exclude_queued=exclude_queued, wildcard=wildcard, state=state, algorithm=algorithm, method_type=method_type, prefix_number=prefix_number, method_metadata=method_metadata, storage=storage, scheme=scheme, recursive=recursive, cursor=cursor, id=id, count=count, sort=sort, hash=hash, filter=filter, include_item=include_item, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_type** | **str**| Only return URIs for files from storages of this type. | [optional] 
 **first** | **int**| From total list of files, start return list from specified number. | [optional] [default to 0]
 **prefix_first** | **int**| From total list of prefixes, start return list from specified number.  Note: this parameter has no effect if Elasticsearch is the search backend. | [optional] [default to 0]
 **number** | **int**| Return a maximum of specified number of files. | [optional] [default to 10]
 **storage_group** | **str**| Storage group id.  Return only files from storages specified in the storage group | [optional] 
 **ignorecase** | **bool**| - &#x60;true&#x60; - Search file path case insensitively - &#x60;false&#x60; - Search file path case sensitively | [optional] 
 **prefix** | **bool**| - &#x60;true&#x60; - Also include file prefixes that matches the criteria - &#x60;false&#x60; (default) - Do not include file prefixes | [optional] 
 **exclude_queued** | **bool**| - &#x60;true&#x60; - Exclude the files that are queued for import - &#x60;false&#x60; (default) - Do not exclude the files that are queued for import | [optional] 
 **wildcard** | **bool**| - &#x60;true&#x60; - Allow use of wildcards in path.  - &#x60;false&#x60; (default) - No wildcard handling of path. | [optional] [default to False]
 **state** | [**list[str]**](str.md)| Filter results by file state.  Can be used multiple times to select several states. | [optional] 
 **algorithm** | **str**| Hash algorithm.  Search for hash values used by specified algorithm | [optional] 
 **method_type** | **str**| Return URIs from storage methods with a particular type.  By default, return URLs with empty &#x60;methodType&#x60;. | [optional] 
 **prefix_number** | **int**| Return a maximum of specified number of prefixes. | [optional] [default to 10]
 **method_metadata** | [**list[str]**](str.md)| metadata used with storage method. | [optional] 
 **storage** | [**list[str]**](str.md)| List of storage ids.  Return only files from specific storages.  Same as &#x60;storage-id&#x60; in URL, but can be specified multiple times | [optional] 
 **scheme** | **str**| URI scheme to return. | [optional] 
 **recursive** | **bool**| - &#x60;true&#x60; (default) - Return all files in tree.  - &#x60;false&#x60; - Return only files directly under specified path. | [optional] [default to True]
 **cursor** | **str**| New in version 4. 16.   - &#x60;*&#x60; - The initial cursor.  - &#x60;string-from-search&#x60; - Cursor string returned from the search results.  If set, the cursorMark / search after features from Solr/Elasticsearch would be used to improve the deep paging  performance during a search.  When &#x60;cursor&#x60; is used, The value of &#x60;first&#x60; will be ignored.  Only metadata searches in the &#x60;generic&#x60; interval supports &#x60;cursor&#x60;. | [optional] 
 **id** | [**list[str]**](str.md)| If multiple &#x60;id&#x60; query parameters are specified only those files are returned.  If no ids are specified, all files are returned. | [optional] 
 **count** | **bool**| - &#x60;true&#x60; (default) - Return total number of hits in result - &#x60;false&#x60; - Do not return total number of hits in result, in order to produce results faster | [optional] [default to True]
 **sort** | [**list[str]**](str.md)| Comma-separated list.   - &#x60;fileId&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] (default) - Order results by file id.  - &#x60;size&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file size (bytes).  - &#x60;state&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file state.  - &#x60;timestamp&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file timestamp.  - &#x60;filename&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by filename.  - &#x60;extension&#x60; [ &#x60;asc&#x60; (default) | &#x60;desc&#x60; ] - Order results by file extension. | [optional] 
 **hash** | [**list[str]**](str.md)| List of hash values.  Only return files with specific hash value. | [optional] 
 **filter** | **str**| - &#x60;all&#x60; (default) - Return all files - &#x60;item&#x60; Only return files associated with an item.  - &#x60;noitem&#x60; Only return files not associated with any item. | [optional] [default to &#39;all&#39;]
 **include_item** | **bool**| - &#x60;true&#x60; - Return associated items, shapes, and components.  - &#x60;false&#x60; (default) - Do not return any information about associated items, shapes, and components. | [optional] [default to False]
 **path** | **str**| - *path* - Return files under this sub-path to storage.  - &#x60;/&#x60; (default) - Return all files. | [optional] [default to &#39;/&#39;]

### Return type

[**FileListType**](FileListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CRLF-delimited list of file ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_file_path**
> FileType register_file_path(path, file_id, state=state, duplicate=duplicate, storage=storage)

Register a new file path

Registers a new file, with the new path, and change all relevant components to point to the new file instead. The old file is marked for deletion. Hence, caller should first do the physical move, then issue this command.  The path of file entities in Vidispine is immutable. This command is used when a file is moved manually (without Vidispine), and caller wants to register the new path.  Use the `duplicate` parameter to add another file as a duplicate. The file at the new location will be added to all components that the file is already a part of. No file entities will be removed.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
path = 'path_example' # str | The new path.
file_id = 'file_id_example' # str | The file id.
state = 'state_example' # str | New state of the file.  (OPEN, CLOSED, etc). (optional)
duplicate = False # bool | - `true` - The file at the target path is a duplicate of this file.  The old file entity will NOT be removed.  - `false` (default) - This target path is the new location.  This old file entity will be removed. (optional) (default to False)
storage = 'storage_example' # str | The new storage, if omitted, the same storage. (optional)

try:
    # Register a new file path
    api_response = api_instance.register_file_path(path, file_id, state=state, duplicate=duplicate, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->register_file_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The new path. | 
 **file_id** | **str**| The file id. | 
 **state** | **str**| New state of the file.  (OPEN, CLOSED, etc). | [optional] 
 **duplicate** | **bool**| - &#x60;true&#x60; - The file at the target path is a duplicate of this file.  The old file entity will NOT be removed.  - &#x60;false&#x60; (default) - This target path is the new location.  This old file entity will be removed. | [optional] [default to False]
 **storage** | **str**| The new storage, if omitted, the same storage. | [optional] 

### Return type

[**FileType**](FileType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | File id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reindex_file**
> str reindex_file(file_id)

Re-index a file

Queues a single file for re-index.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.

try:
    # Re-index a file
    api_response = api_instance.reindex_file(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->reindex_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 

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

# **remove_file_from_item**
> remove_file_from_item(file_id, item=item)

Remove a file from an item

Disassociates (disconnects) the physical file from the item. The shape which the file resided in will still exist, but there is no longer any connection between the file and the shape or item.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
item = 'item_example' # str | The item from which the file in unassociated (optional)

try:
    # Remove a file from an item
    api_instance.remove_file_from_item(file_id, item=item)
except ApiException as e:
    print("Exception when calling FileApi->remove_file_from_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
 **item** | **str**| The item from which the file in unassociated | [optional] 

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

# **restore_file**
> str restore_file(expiration_in_days, file_id, retrieval_tier=retrieval_tier, extra_data=extra_data)

Transitioning files From S3 to Glacier

Triggers a request to Glacier to initiate a restore.  Once the restore is complete, the file will be put in CLOSED state, and will be available for direct access.  The `expirationInDays` parameter has to be set and specifies how long the restored files should be available. Once it has expired, it will be removed from direct access and once again end up in the ARCHIVED state.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
expiration_in_days = 56 # int | How long the restored files should be available.
file_id = 'file_id_example' # str | The file id.
retrieval_tier = 'retrieval_tier_example' # str | Sets the Glacier retrieval tier to use when restoring the file. (optional)
extra_data = ['extra_data_example'] # list[str] | Additional parameters relevant for the restore, in the form of `key=value`.  Specify multiple parameters using multiple query parameters.  <dl><dh>`expirationInDays={number-of-days}`</dh><dd>How long the restored files should be available. </dd></dl> Deprecated since version 4. 9: Use the  `expirationInDays`  query parameter instead. (optional)

try:
    # Transitioning files From S3 to Glacier
    api_response = api_instance.restore_file(expiration_in_days, file_id, retrieval_tier=retrieval_tier, extra_data=extra_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->restore_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expiration_in_days** | **int**| How long the restored files should be available. | 
 **file_id** | **str**| The file id. | 
 **retrieval_tier** | **str**| Sets the Glacier retrieval tier to use when restoring the file. | [optional] 
 **extra_data** | [**list[str]**](str.md)| Additional parameters relevant for the restore, in the form of &#x60;key&#x3D;value&#x60;.  Specify multiple parameters using multiple query parameters.  &lt;dl&gt;&lt;dh&gt;&#x60;expirationInDays&#x3D;{number-of-days}&#x60;&lt;/dh&gt;&lt;dd&gt;How long the restored files should be available. &lt;/dd&gt;&lt;/dl&gt; Deprecated since version 4. 9: Use the  &#x60;expirationInDays&#x60;  query parameter instead. | [optional] 

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
**0** | Informational text. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_data**
> FileType update_file_data(file_id, body, transfer_priority=transfer_priority, transfer_id=transfer_id)

Update or create file data

Uploads the file data for a specific file, overwriting any existing file data for the file.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
body = '/path/to/file' # file | The raw file data.
transfer_priority = 56 # int | An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. (optional)
transfer_id = 'transfer_id_example' # str | An id to assign the transfer to be able to refer to it. (optional)

try:
    # Update or create file data
    api_response = api_instance.update_file_data(file_id, body, transfer_priority=transfer_priority, transfer_id=transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->update_file_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
 **body** | **file**| The raw file data. | 
 **transfer_priority** | **int**| An integer between 1 and 1000 that indicates what priority the transfer should be given in relation to other transfers.  A transfer with a high priority value is considered more important than a transfer with a low priority value. | [optional] 
 **transfer_id** | **str**| An id to assign the transfer to be able to refer to it. | [optional] 

### Return type

[**FileType**](FileType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_hash**
> update_file_hash(file_id, hash, algorithm=algorithm)

Set file hash

Set a new hash value of a file.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
hash = 'hash_example' # str | The hash.
algorithm = 'algorithm_example' # str | Hash algorithm of the new hash.  If omitted, the default SHA-1 hash is set. (optional)

try:
    # Set file hash
    api_instance.update_file_hash(file_id, hash, algorithm=algorithm)
except ApiException as e:
    print("Exception when calling FileApi->update_file_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
 **hash** | **str**| The hash. | 
 **algorithm** | **str**| Hash algorithm of the new hash.  If omitted, the default SHA-1 hash is set. | [optional] 

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

# **update_file_metadata**
> update_file_metadata(file_id, simple_metadata_type)

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
simple_metadata_type = vidispine.SimpleMetadataType() # SimpleMetadataType | 

try:
    # Create multiple key-value pairs
    api_instance.update_file_metadata(file_id, simple_metadata_type)
except ApiException as e:
    print("Exception when calling FileApi->update_file_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
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

# **update_file_metadata_key**
> update_file_metadata_key(file_id, keypath, body)

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
file_id = 'file_id_example' # str | The file id.
keypath = 'keypath_example' # str | The keypath.
body = 'body_example' # str | The raw string value.

try:
    # Set the value for a specific key
    api_instance.update_file_metadata_key(file_id, keypath, body)
except ApiException as e:
    print("Exception when calling FileApi->update_file_metadata_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The file id. | 
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

# **update_file_state**
> FileType update_file_state(state, file_id)

Update the file state

Changes the state of the specified file to the given state.  Can for example be used after writing a file to a storage, to immediately mark it as CLOSED and no longer growing.

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
api_instance = vidispine.FileApi(vidispine.ApiClient(configuration))
state = 'state_example' # str | The new state of the file.
file_id = 'file_id_example' # str | The file id.

try:
    # Update the file state
    api_response = api_instance.update_file_state(state, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->update_file_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The new state of the file. | 
 **file_id** | **str**| The file id. | 

### Return type

[**FileType**](FileType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The id of the file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

