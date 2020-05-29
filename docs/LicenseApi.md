# vidispine.LicenseApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_slave**](LicenseApi.md#delete_slave) | **DELETE** /license/slave/{id} | Delete a slave instance
[**get_license**](LicenseApi.md#get_license) | **GET** /license | Retrieve the license file
[**get_slave**](LicenseApi.md#get_slave) | **GET** /license/slave/{id} | List slave license status
[**get_slave_license**](LicenseApi.md#get_slave_license) | **GET** /license/slave/{id}/license | Retrieve a slave license file
[**get_slave_license_by_id**](LicenseApi.md#get_slave_license_by_id) | **GET** /license/slave/license/{id} | List installed slave licenses by id
[**get_slave_licenses**](LicenseApi.md#get_slave_licenses) | **GET** /license/slave/license | List all installed slave licenses
[**get_slaves**](LicenseApi.md#get_slaves) | **GET** /license/slave | List all slaves
[**install_slave_license**](LicenseApi.md#install_slave_license) | **POST** /license/slave | Install a slave license on a master node
[**install_slave_license_from_path**](LicenseApi.md#install_slave_license_from_path) | **PUT** /license/slave | Install a slave license on a master node


# **delete_slave**
> delete_slave(id)

Delete a slave instance

Removes the slave with the given id.

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
api_instance = vidispine.LicenseApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # Delete a slave instance
    api_instance.delete_slave(id)
except ApiException as e:
    print("Exception when calling LicenseApi->delete_slave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

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

# **get_license**
> str get_license()

Retrieve the license file

Retrieves the contents of the installed license file.

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
api_instance = vidispine.LicenseApi(vidispine.ApiClient(configuration))

try:
    # Retrieve the license file
    api_response = api_instance.get_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**0** | The contents of the license file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slave**
> VersionType get_slave(id)

List slave license status

Returns information about the slave with the given id.

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
api_instance = vidispine.LicenseApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # List slave license status
    api_response = api_instance.get_slave(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_slave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

### Return type

[**VersionType**](VersionType.md)

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

# **get_slave_license**
> SlaveLicenseType get_slave_license(id)

Retrieve a slave license file

Returns the slave license for a specific slave.

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
api_instance = vidispine.LicenseApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # Retrieve a slave license file
    api_response = api_instance.get_slave_license(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_slave_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

### Return type

[**SlaveLicenseType**](SlaveLicenseType.md)

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

# **get_slave_license_by_id**
> SlaveLicenseType get_slave_license_by_id(id)

List installed slave licenses by id

Returns the detail of an installed slave license with the given id

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
api_instance = vidispine.LicenseApi(vidispine.ApiClient(configuration))
id = 'id_example' # str | The id.

try:
    # List installed slave licenses by id
    api_response = api_instance.get_slave_license_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_slave_license_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id. | 

### Return type

[**SlaveLicenseType**](SlaveLicenseType.md)

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

# **get_slave_licenses**
> SlaveLicenseListType get_slave_licenses()

List all installed slave licenses

Returns the `id` and `SlaveIdentifier` of all installed slave license on a master

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
api_instance = vidispine.LicenseApi(vidispine.ApiClient(configuration))

try:
    # List all installed slave licenses
    api_response = api_instance.get_slave_licenses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_slave_licenses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SlaveLicenseListType**](SlaveLicenseListType.md)

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

# **get_slaves**
> SlaveListType get_slaves()

List all slaves

Returns a list of all the slave nodes connected to this master. Slaves that have not been seen for more than 180 minutes will not be available.

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
api_instance = vidispine.LicenseApi(vidispine.ApiClient(configuration))

try:
    # List all slaves
    api_response = api_instance.get_slaves()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_slaves: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SlaveListType**](SlaveListType.md)

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

# **install_slave_license**
> SlaveLicenseType install_slave_license(body)

Install a slave license on a master node

Installs a slave license.

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
api_instance = vidispine.LicenseApi(vidispine.ApiClient(configuration))
body = 'body_example' # str | The content of the slave license file.

try:
    # Install a slave license on a master node
    api_response = api_instance.install_slave_license(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->install_slave_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| The content of the slave license file. | 

### Return type

[**SlaveLicenseType**](SlaveLicenseType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_slave_license_from_path**
> SlaveLicenseType install_slave_license_from_path(path)

Install a slave license on a master node

Installs the slave license file with the given path.

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
api_instance = vidispine.LicenseApi(vidispine.ApiClient(configuration))
path = 'path_example' # str | The name of the slave license file.

try:
    # Install a slave license on a master node
    api_response = api_instance.install_slave_license_from_path(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->install_slave_license_from_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The name of the slave license file. | 

### Return type

[**SlaveLicenseType**](SlaveLicenseType.md)

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

