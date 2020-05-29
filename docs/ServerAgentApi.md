# vidispine.ServerAgentApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_server_agent**](ServerAgentApi.md#delete_server_agent) | **DELETE** /vxa/{uuid} | Delete a server agent
[**get_server_agent**](ServerAgentApi.md#get_server_agent) | **GET** /vxa/{uuid} | Retrieve a server agent
[**get_server_agent_configuration**](ServerAgentApi.md#get_server_agent_configuration) | **GET** /vxa/{uuid}/configuration | Retrieve the server agent configuration
[**get_server_agents**](ServerAgentApi.md#get_server_agents) | **GET** /vxa | List all server agents
[**register_server_agent**](ServerAgentApi.md#register_server_agent) | **PUT** /vxa/enable-ssh | Register a server agent


# **delete_server_agent**
> delete_server_agent(uuid)

Delete a server agent

Removes the VSA from the system

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
api_instance = vidispine.ServerAgentApi(vidispine.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid.

try:
    # Delete a server agent
    api_instance.delete_server_agent(uuid)
except ApiException as e:
    print("Exception when calling ServerAgentApi->delete_server_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid. | 

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

# **get_server_agent**
> VXAType get_server_agent(uuid)

Retrieve a server agent

Retrieves a specific VSA. As an alternative to the UUID, the name of the VSA can be used instead. The name syntax only works if the name is unique among the VSAs.

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
api_instance = vidispine.ServerAgentApi(vidispine.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid.

try:
    # Retrieve a server agent
    api_response = api_instance.get_server_agent(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerAgentApi->get_server_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid. | 

### Return type

[**VXAType**](VXAType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;VXADocument&lt;/em&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_agent_configuration**
> str get_server_agent_configuration(uuid)

Retrieve the server agent configuration

Returns the client-side configuration of the VSA.

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
api_instance = vidispine.ServerAgentApi(vidispine.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid.

try:
    # Retrieve the server agent configuration
    api_response = api_instance.get_server_agent_configuration(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerAgentApi->get_server_agent_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A JSON object with the settings and current status of the VSA. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_agents**
> VXAListType get_server_agents()

List all server agents

Returns all VSAs.

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
api_instance = vidispine.ServerAgentApi(vidispine.ApiClient(configuration))

try:
    # List all server agents
    api_response = api_instance.get_server_agents()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerAgentApi->get_server_agents: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VXAListType**](VXAListType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A &lt;em&gt;VXAListDocument&lt;/em&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_server_agent**
> str register_server_agent(vsip=vsip, uuid=uuid, ws=ws, vsport=vsport, vxaname=vxaname)

Register a server agent

Registers a new VSA node in the system.

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
api_instance = vidispine.ServerAgentApi(vidispine.ApiClient(configuration))
vsip = ['vsip_example'] # list[str] | The address to which the VSA should connect.  Can be specified multiple times for a cluster configuration. (optional)
uuid = 'uuid_example' # str | The UUID of the VSA.  If not set, Vidispine will assign a UUID. (optional)
ws = ['ws_example'] # list[str] | The URI to the API endpoint.  Used to enable WebSocket tunneling, as an alternative to `vsip`/`vsport`.  Can be specified multiple times for a cluster configuration. (optional)
vsport = ['vsport_example'] # list[str] | The port to which the VSA should connect.  Can be specified multiple times for a cluster configuration. (optional)
vxaname = 'vxaname_example' # str | The name of the VSA. (optional)

try:
    # Register a server agent
    api_response = api_instance.register_server_agent(vsip=vsip, uuid=uuid, ws=ws, vsport=vsport, vxaname=vxaname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerAgentApi->register_server_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vsip** | [**list[str]**](str.md)| The address to which the VSA should connect.  Can be specified multiple times for a cluster configuration. | [optional] 
 **uuid** | **str**| The UUID of the VSA.  If not set, Vidispine will assign a UUID. | [optional] 
 **ws** | [**list[str]**](str.md)| The URI to the API endpoint.  Used to enable WebSocket tunneling, as an alternative to &#x60;vsip&#x60;/&#x60;vsport&#x60;.  Can be specified multiple times for a cluster configuration. | [optional] 
 **vsport** | [**list[str]**](str.md)| The port to which the VSA should connect.  Can be specified multiple times for a cluster configuration. | [optional] 
 **vxaname** | **str**| The name of the VSA. | [optional] 

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
**0** | A text configuration to be added on the VSA&#39;s configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

