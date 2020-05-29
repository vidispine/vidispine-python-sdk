# vidispine.EntitySiteRuleApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_site_rule**](EntitySiteRuleApi.md#create_entity_site_rule) | **POST** /{type}/{entity-id}/site-rule | Create a site rule
[**delete_entity_site_rule**](EntitySiteRuleApi.md#delete_entity_site_rule) | **DELETE** /{type}/{entity-id}/site-rule/{id} | Delete a site rule
[**get_entity_site_rule**](EntitySiteRuleApi.md#get_entity_site_rule) | **GET** /{type}/{entity-id}/site-rule/{id} | Retrieve a site rule
[**get_entity_site_rules**](EntitySiteRuleApi.md#get_entity_site_rules) | **GET** /{type}/{entity-id}/site-rule | List all site rules for an entity
[**update_entity_site_rule**](EntitySiteRuleApi.md#update_entity_site_rule) | **PUT** /{type}/{entity-id}/site-rule/{id} | Update a site rule


# **create_entity_site_rule**
> SiteRuleType create_entity_site_rule(type, entity_id, site_rule_type)

Create a site rule

Creates a new site rule for an entity.

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
api_instance = vidispine.EntitySiteRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
site_rule_type = vidispine.SiteRuleType() # SiteRuleType | 

try:
    # Create a site rule
    api_response = api_instance.create_entity_site_rule(type, entity_id, site_rule_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitySiteRuleApi->create_entity_site_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **site_rule_type** | [**SiteRuleType**](SiteRuleType.md)|  | 

### Return type

[**SiteRuleType**](SiteRuleType.md)

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

# **delete_entity_site_rule**
> delete_entity_site_rule(type, entity_id, id)

Delete a site rule

Deletes a site rule.

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
api_instance = vidispine.EntitySiteRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
id = 'id_example' # str | The id.

try:
    # Delete a site rule
    api_instance.delete_entity_site_rule(type, entity_id, id)
except ApiException as e:
    print("Exception when calling EntitySiteRuleApi->delete_entity_site_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
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

# **get_entity_site_rule**
> SiteRuleType get_entity_site_rule(type, entity_id, id)

Retrieve a site rule

Retrieves a specific site rule.

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
api_instance = vidispine.EntitySiteRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
id = 'id_example' # str | The id.

try:
    # Retrieve a site rule
    api_response = api_instance.get_entity_site_rule(type, entity_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitySiteRuleApi->get_entity_site_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **id** | **str**| The id. | 

### Return type

[**SiteRuleType**](SiteRuleType.md)

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

# **get_entity_site_rules**
> SiteRuleListType get_entity_site_rules(type, entity_id)

List all site rules for an entity

Retrieves all site rules for the given entity/entities.

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
api_instance = vidispine.EntitySiteRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.

try:
    # List all site rules for an entity
    api_response = api_instance.get_entity_site_rules(type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitySiteRuleApi->get_entity_site_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 

### Return type

[**SiteRuleListType**](SiteRuleListType.md)

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

# **update_entity_site_rule**
> SiteRuleType update_entity_site_rule(type, entity_id, id, site_rule_type)

Update a site rule

Updates a site rule.

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
api_instance = vidispine.EntitySiteRuleApi(vidispine.ApiClient(configuration))
type = 'type_example' # str | The type of entity.
entity_id = 'entity_id_example' # str | The entity id.
id = 'id_example' # str | The id.
site_rule_type = vidispine.SiteRuleType() # SiteRuleType | 

try:
    # Update a site rule
    api_response = api_instance.update_entity_site_rule(type, entity_id, id, site_rule_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitySiteRuleApi->update_entity_site_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of entity. | 
 **entity_id** | **str**| The entity id. | 
 **id** | **str**| The id. | 
 **site_rule_type** | [**SiteRuleType**](SiteRuleType.md)|  | 

### Return type

[**SiteRuleType**](SiteRuleType.md)

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

