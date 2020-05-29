# vidispine.ConfigurationApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_configuration_property**](ConfigurationApi.md#delete_configuration_property) | **DELETE** /configuration/properties/{key} | Delete a configuration property
[**delete_database_purging_configuration**](ConfigurationApi.md#delete_database_purging_configuration) | **DELETE** /configuration/purging | Remove the database purging configuration
[**delete_ftp_pool_configuration**](ConfigurationApi.md#delete_ftp_pool_configuration) | **DELETE** /configuration/ftp-pool | Delete the FTP pool
[**delete_job_pool_configuration**](ConfigurationApi.md#delete_job_pool_configuration) | **DELETE** /configuration/job-pool | Delete all job pools
[**delete_job_pool_with_priority**](ConfigurationApi.md#delete_job_pool_with_priority) | **DELETE** /configuration/job-pool/{priority} | Delete a job pool
[**delete_o_auth2_configuration**](ConfigurationApi.md#delete_o_auth2_configuration) | **DELETE** /configuration/auth | Delete the OAuth2 configuration
[**get_configuration**](ConfigurationApi.md#get_configuration) | **GET** /configuration | Configuration resources
[**get_configuration_properties**](ConfigurationApi.md#get_configuration_properties) | **GET** /configuration/properties | Lis tall configuration properties
[**get_configuration_property**](ConfigurationApi.md#get_configuration_property) | **GET** /configuration/properties/{key} | Retrieve a configuration property
[**get_cors_configuration**](ConfigurationApi.md#get_cors_configuration) | **GET** /configuration/cors | Retrieve the CORS configuration
[**get_database_purging_configuration**](ConfigurationApi.md#get_database_purging_configuration) | **GET** /configuration/purging | Retrieve the database purging configuration
[**get_ftp_pool_configuration**](ConfigurationApi.md#get_ftp_pool_configuration) | **GET** /configuration/ftp-pool | Retrieve the FTP pool configuration
[**get_indexing_configuration**](ConfigurationApi.md#get_indexing_configuration) | **GET** /configuration/indexing | Retrieve the indexing configuration
[**get_job_pool_configuration**](ConfigurationApi.md#get_job_pool_configuration) | **GET** /configuration/job-pool | Retrieve the job pool configuration
[**get_log_report_configuration**](ConfigurationApi.md#get_log_report_configuration) | **GET** /configuration/logreport | Retrieve the log report configuration
[**get_metrics_configuration**](ConfigurationApi.md#get_metrics_configuration) | **GET** /configuration/metrics | Retrieve the metrics configuration
[**get_o_auth2_configuration**](ConfigurationApi.md#get_o_auth2_configuration) | **GET** /configuration/auth | Retrieve the OAuth2 configuration
[**get_path_alias_configuration**](ConfigurationApi.md#get_path_alias_configuration) | **GET** /configuration/path-alias | Retrieve the path alias configuration
[**update_configuration_properties**](ConfigurationApi.md#update_configuration_properties) | **POST** /configuration/properties | Create/update multiple configuration properties
[**update_configuration_property**](ConfigurationApi.md#update_configuration_property) | **PUT** /configuration/properties | Create/update a configuration property
[**update_cors_configuration**](ConfigurationApi.md#update_cors_configuration) | **PUT** /configuration/cors | Update the CORS configuration
[**update_database_purging_configuration**](ConfigurationApi.md#update_database_purging_configuration) | **PUT** /configuration/purging | Update the database purging configuration
[**update_ftp_pool_configuration**](ConfigurationApi.md#update_ftp_pool_configuration) | **PUT** /configuration/ftp-pool | Update the FTP pool configuration
[**update_indexing_configuration**](ConfigurationApi.md#update_indexing_configuration) | **PUT** /configuration/indexing | Update the indexing configuration
[**update_job_pool_configuration**](ConfigurationApi.md#update_job_pool_configuration) | **PUT** /configuration/job-pool | Update the job pool configuration
[**update_log_report_configuration**](ConfigurationApi.md#update_log_report_configuration) | **PUT** /configuration/logreport | Update the log report configuration
[**update_metrics_configuration**](ConfigurationApi.md#update_metrics_configuration) | **PUT** /configuration/metrics | Update the metrics configuration
[**update_o_auth2_configuration**](ConfigurationApi.md#update_o_auth2_configuration) | **PUT** /configuration/auth | Update the OAuth2 configuration
[**update_path_alias_configuration**](ConfigurationApi.md#update_path_alias_configuration) | **PUT** /configuration/path-alias | Update the path alias configuration


# **delete_configuration_property**
> delete_configuration_property(key)

Delete a configuration property

Removes a configuration property.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
key = 'key_example' # str | The key.

try:
    # Delete a configuration property
    api_instance.delete_configuration_property(key)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_configuration_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key. | 

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

# **delete_database_purging_configuration**
> delete_database_purging_configuration()

Remove the database purging configuration

Removes all database purging configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Remove the database purging configuration
    api_instance.delete_database_purging_configuration()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_database_purging_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **delete_ftp_pool_configuration**
> delete_ftp_pool_configuration()

Delete the FTP pool

Deletes the FTP connection pool.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Delete the FTP pool
    api_instance.delete_ftp_pool_configuration()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_ftp_pool_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **delete_job_pool_configuration**
> delete_job_pool_configuration()

Delete all job pools

Deletes all job pools.  Note that the max concurrent jobs setting will *not* be affected.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Delete all job pools
    api_instance.delete_job_pool_configuration()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_job_pool_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **delete_job_pool_with_priority**
> delete_job_pool_with_priority(priority)

Delete a job pool

Deletes the job pool with the given priority threshold.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
priority = 'priority_example' # str | The priority.

try:
    # Delete a job pool
    api_instance.delete_job_pool_with_priority(priority)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_job_pool_with_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **priority** | **str**| The priority. | 

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

# **delete_o_auth2_configuration**
> delete_o_auth2_configuration()

Delete the OAuth2 configuration

Deletes and resets the current OAuth2 configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Delete the OAuth2 configuration
    api_instance.delete_o_auth2_configuration()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_o_auth2_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **get_configuration**
> URIListType get_configuration()

Configuration resources

Returns the available configuration resource endpoints.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Configuration resources
    api_response = api_instance.get_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**0** | CRLF-delimited list of names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_properties**
> ConfigurationPropertyListType get_configuration_properties()

Lis tall configuration properties

Returns a document containing all configuration properties set in the system.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Lis tall configuration properties
    api_response = api_instance.get_configuration_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationPropertyListType**](ConfigurationPropertyListType.md)

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

# **get_configuration_property**
> ConfigurationPropertyType get_configuration_property(key)

Retrieve a configuration property

Returns a document or string containing all current setting for a configuration property.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
key = 'key_example' # str | The key.

try:
    # Retrieve a configuration property
    api_response = api_instance.get_configuration_property(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key. | 

### Return type

[**ConfigurationPropertyType**](ConfigurationPropertyType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | String value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cors_configuration**
> CORSConfigurationType get_cors_configuration()

Retrieve the CORS configuration

Returns the current CORS configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the CORS configuration
    api_response = api_instance.get_cors_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_cors_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CORSConfigurationType**](CORSConfigurationType.md)

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

# **get_database_purging_configuration**
> DatabasePurgingConfigurationType get_database_purging_configuration()

Retrieve the database purging configuration

Returns the current database purging configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the database purging configuration
    api_response = api_instance.get_database_purging_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_database_purging_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DatabasePurgingConfigurationType**](DatabasePurgingConfigurationType.md)

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

# **get_ftp_pool_configuration**
> FtpPoolConfigurationType get_ftp_pool_configuration()

Retrieve the FTP pool configuration

Returns the current FTP connection pool configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the FTP pool configuration
    api_response = api_instance.get_ftp_pool_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_ftp_pool_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FtpPoolConfigurationType**](FtpPoolConfigurationType.md)

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

# **get_indexing_configuration**
> IndexingConfigurationType get_indexing_configuration()

Retrieve the indexing configuration

Returns the current indexing configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the indexing configuration
    api_response = api_instance.get_indexing_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_indexing_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IndexingConfigurationType**](IndexingConfigurationType.md)

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

# **get_job_pool_configuration**
> JobPoolListType get_job_pool_configuration()

Retrieve the job pool configuration

Returns the current job pool configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the job pool configuration
    api_response = api_instance.get_job_pool_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_job_pool_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JobPoolListType**](JobPoolListType.md)

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

# **get_log_report_configuration**
> LogReportConfigurationType get_log_report_configuration()

Retrieve the log report configuration

Returns the current LogReport configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the log report configuration
    api_response = api_instance.get_log_report_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_log_report_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogReportConfigurationType**](LogReportConfigurationType.md)

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

# **get_metrics_configuration**
> MetricsConfigurationType get_metrics_configuration()

Retrieve the metrics configuration

Returns the current metrics configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the metrics configuration
    api_response = api_instance.get_metrics_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_metrics_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetricsConfigurationType**](MetricsConfigurationType.md)

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

# **get_o_auth2_configuration**
> OAuth2ConfigurationType get_o_auth2_configuration()

Retrieve the OAuth2 configuration

Returns the current OAuth2 configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the OAuth2 configuration
    api_response = api_instance.get_o_auth2_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_o_auth2_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuth2ConfigurationType**](OAuth2ConfigurationType.md)

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

# **get_path_alias_configuration**
> PathAliasConfigurationType get_path_alias_configuration()

Retrieve the path alias configuration

Returns the current path alias configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the path alias configuration
    api_response = api_instance.get_path_alias_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_path_alias_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PathAliasConfigurationType**](PathAliasConfigurationType.md)

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

# **update_configuration_properties**
> update_configuration_properties(configuration_property_list_type)

Create/update multiple configuration properties

Creates or updates multiple configuration properties at once, using a ConfigurationPropertyListDocument.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
configuration_property_list_type = vidispine.ConfigurationPropertyListType() # ConfigurationPropertyListType | 

try:
    # Create/update multiple configuration properties
    api_instance.update_configuration_properties(configuration_property_list_type)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_configuration_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_property_list_type** | [**ConfigurationPropertyListType**](ConfigurationPropertyListType.md)|  | 

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

# **update_configuration_property**
> update_configuration_property(configuration_property_type)

Create/update a configuration property

Creates or updates a configuration property.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
configuration_property_type = vidispine.ConfigurationPropertyType() # ConfigurationPropertyType | 

try:
    # Create/update a configuration property
    api_instance.update_configuration_property(configuration_property_type)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_configuration_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_property_type** | [**ConfigurationPropertyType**](ConfigurationPropertyType.md)|  | 

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

# **update_cors_configuration**
> update_cors_configuration(cors_configuration_type)

Update the CORS configuration

Updates the CORS configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
cors_configuration_type = vidispine.CORSConfigurationType() # CORSConfigurationType | 

try:
    # Update the CORS configuration
    api_instance.update_cors_configuration(cors_configuration_type)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_cors_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cors_configuration_type** | [**CORSConfigurationType**](CORSConfigurationType.md)|  | 

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

# **update_database_purging_configuration**
> update_database_purging_configuration(database_purging_configuration_type)

Update the database purging configuration

Updates the database purging configuration. Note that if a category element is missing, e.g. `auditTrail`, that category is left unchanged. To remove a particular category, use an empty element, `&lt;auditTrail/&gt;`.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
database_purging_configuration_type = vidispine.DatabasePurgingConfigurationType() # DatabasePurgingConfigurationType | 

try:
    # Update the database purging configuration
    api_instance.update_database_purging_configuration(database_purging_configuration_type)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_database_purging_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_purging_configuration_type** | [**DatabasePurgingConfigurationType**](DatabasePurgingConfigurationType.md)|  | 

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

# **update_ftp_pool_configuration**
> update_ftp_pool_configuration(ftp_pool_configuration_type)

Update the FTP pool configuration

Updates the FTP connection pool configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
ftp_pool_configuration_type = vidispine.FtpPoolConfigurationType() # FtpPoolConfigurationType | 

try:
    # Update the FTP pool configuration
    api_instance.update_ftp_pool_configuration(ftp_pool_configuration_type)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_ftp_pool_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ftp_pool_configuration_type** | [**FtpPoolConfigurationType**](FtpPoolConfigurationType.md)|  | 

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

# **update_indexing_configuration**
> update_indexing_configuration(indexing_configuration_type)

Update the indexing configuration

Updates the indexing configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
indexing_configuration_type = vidispine.IndexingConfigurationType() # IndexingConfigurationType | 

try:
    # Update the indexing configuration
    api_instance.update_indexing_configuration(indexing_configuration_type)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_indexing_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexing_configuration_type** | [**IndexingConfigurationType**](IndexingConfigurationType.md)|  | 

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

# **update_job_pool_configuration**
> update_job_pool_configuration(job_pool_list_type)

Update the job pool configuration

Updates the job pool configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
job_pool_list_type = vidispine.JobPoolListType() # JobPoolListType | 

try:
    # Update the job pool configuration
    api_instance.update_job_pool_configuration(job_pool_list_type)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_job_pool_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_pool_list_type** | [**JobPoolListType**](JobPoolListType.md)|  | 

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

# **update_log_report_configuration**
> update_log_report_configuration(log_report_configuration_type)

Update the log report configuration

Updates the LogReport configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
log_report_configuration_type = vidispine.LogReportConfigurationType() # LogReportConfigurationType | 

try:
    # Update the log report configuration
    api_instance.update_log_report_configuration(log_report_configuration_type)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_log_report_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_report_configuration_type** | [**LogReportConfigurationType**](LogReportConfigurationType.md)|  | 

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

# **update_metrics_configuration**
> update_metrics_configuration(metrics_configuration_type)

Update the metrics configuration

Updates the metrics configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
metrics_configuration_type = vidispine.MetricsConfigurationType() # MetricsConfigurationType | 

try:
    # Update the metrics configuration
    api_instance.update_metrics_configuration(metrics_configuration_type)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_metrics_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics_configuration_type** | [**MetricsConfigurationType**](MetricsConfigurationType.md)|  | 

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

# **update_o_auth2_configuration**
> OAuth2ConfigurationType update_o_auth2_configuration(o_auth2_configuration_type)

Update the OAuth2 configuration

Updates the OAuth2 configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
o_auth2_configuration_type = vidispine.OAuth2ConfigurationType() # OAuth2ConfigurationType | 

try:
    # Update the OAuth2 configuration
    api_response = api_instance.update_o_auth2_configuration(o_auth2_configuration_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_o_auth2_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth2_configuration_type** | [**OAuth2ConfigurationType**](OAuth2ConfigurationType.md)|  | 

### Return type

[**OAuth2ConfigurationType**](OAuth2ConfigurationType.md)

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

# **update_path_alias_configuration**
> update_path_alias_configuration(path_alias_configuration_type)

Update the path alias configuration

Updates the path alias configuration.

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
api_instance = vidispine.ConfigurationApi(vidispine.ApiClient(configuration))
path_alias_configuration_type = vidispine.PathAliasConfigurationType() # PathAliasConfigurationType | 

try:
    # Update the path alias configuration
    api_instance.update_path_alias_configuration(path_alias_configuration_type)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_path_alias_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_alias_configuration_type** | [**PathAliasConfigurationType**](PathAliasConfigurationType.md)|  | 

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

