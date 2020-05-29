# coding: utf-8

"""
    Vidispine API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.x
    Contact: info@vidispine.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vidispine.models import *
from vidispine.api_client import ApiClient
from vidispine.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ItemBulkyMetadataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_item_bulky_metadata(self, item_id, bulky_metadata_type, **kwargs):  # noqa: E501
        """Insert values in bulk  # noqa: E501

        Inserts all key-value pairs from a given document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_item_bulky_metadata(item_id, bulky_metadata_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :param BulkyMetadataType bulky_metadata_type: (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None.
                 If the method is called asynchronously, returns the request thread.
        :rtype: None or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.add_item_bulky_metadata_with_http_info(item_id, bulky_metadata_type, **kwargs)  # noqa: E501

    def add_item_bulky_metadata_with_http_info(self, item_id, bulky_metadata_type, **kwargs):  # noqa: E501
        """Insert values in bulk  # noqa: E501

        Inserts all key-value pairs from a given document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_item_bulky_metadata_with_http_info(item_id, bulky_metadata_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :param BulkyMetadataType bulky_metadata_type: (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['item_id', 'bulky_metadata_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_item_bulky_metadata" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `add_item_bulky_metadata`")  # noqa: E501
        # verify the required parameter 'bulky_metadata_type' is set
        if ('bulky_metadata_type' not in local_var_params or
                local_var_params['bulky_metadata_type'] is None):
            raise ApiValueError("Missing the required parameter `bulky_metadata_type` when calling `add_item_bulky_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bulky_metadata_type' in local_var_params:
            body_params = local_var_params['bulky_metadata_type']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/item/{item-id}/metadata/bulky/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_item_bulky_metadata_key(self, item_id, key, **kwargs):  # noqa: E501
        """Remove values  # noqa: E501

        Removes all the values for a certain key over the specified interval.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_item_bulky_metadata_key(item_id, key, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :param str key: The key. (required)
        :key str end: A time code that defines the end of the interval.
        :key str start: A time code that defines the start of the interval.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None.
                 If the method is called asynchronously, returns the request thread.
        :rtype: None or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_item_bulky_metadata_key_with_http_info(item_id, key, **kwargs)  # noqa: E501

    def delete_item_bulky_metadata_key_with_http_info(self, item_id, key, **kwargs):  # noqa: E501
        """Remove values  # noqa: E501

        Removes all the values for a certain key over the specified interval.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_item_bulky_metadata_key_with_http_info(item_id, key, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :param str key: The key. (required)
        :key str end: A time code that defines the end of the interval.
        :key str start: A time code that defines the start of the interval.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['item_id', 'key', 'end', 'start']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_item_bulky_metadata_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `delete_item_bulky_metadata_key`")  # noqa: E501
        # verify the required parameter 'key' is set
        if ('key' not in local_var_params or
                local_var_params['key'] is None):
            raise ApiValueError("Missing the required parameter `key` when calling `delete_item_bulky_metadata_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/item/{item-id}/metadata/bulky/{key}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_item_bulky_metadata_keys(self, item_id, **kwargs):  # noqa: E501
        """Delete all keys used in the bulky metadata  # noqa: E501

        Removes all the keys in the bulky metadata.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_item_bulky_metadata_keys(item_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None.
                 If the method is called asynchronously, returns the request thread.
        :rtype: None or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_item_bulky_metadata_keys_with_http_info(item_id, **kwargs)  # noqa: E501

    def delete_item_bulky_metadata_keys_with_http_info(self, item_id, **kwargs):  # noqa: E501
        """Delete all keys used in the bulky metadata  # noqa: E501

        Removes all the keys in the bulky metadata.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_item_bulky_metadata_keys_with_http_info(item_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['item_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_item_bulky_metadata_keys" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `delete_item_bulky_metadata_keys`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/item/{item-id}/metadata/bulky/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_item_bulky_metadata_key(self, item_id, key, **kwargs):  # noqa: E501
        """Read values  # noqa: E501

        Retrieves all values of a certain key over a specified interval. All values for that key can be retrieved by specifying start as \"-INF\" and end as \"+INF\".  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_item_bulky_metadata_key(item_id, key, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :param str key: The key. (required)
        :key str end: A time code that defines the end of the interval.
        :key str start: A time code that defines the start of the interval.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BulkyMetadataType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: BulkyMetadataType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_item_bulky_metadata_key_with_http_info(item_id, key, **kwargs)  # noqa: E501

    def get_item_bulky_metadata_key_with_http_info(self, item_id, key, **kwargs):  # noqa: E501
        """Read values  # noqa: E501

        Retrieves all values of a certain key over a specified interval. All values for that key can be retrieved by specifying start as \"-INF\" and end as \"+INF\".  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_bulky_metadata_key_with_http_info(item_id, key, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :param str key: The key. (required)
        :key str end: A time code that defines the end of the interval.
        :key str start: A time code that defines the start of the interval.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BulkyMetadataType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['item_id', 'key', 'end', 'start']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_bulky_metadata_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `get_item_bulky_metadata_key`")  # noqa: E501
        # verify the required parameter 'key' is set
        if ('key' not in local_var_params or
                local_var_params['key'] is None):
            raise ApiValueError("Missing the required parameter `key` when calling `get_item_bulky_metadata_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/item/{item-id}/metadata/bulky/{key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BulkyMetadataType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_item_bulky_metadata_keys(self, item_id, **kwargs):  # noqa: E501
        """Retrieve all keys used in the bulky metadata  # noqa: E501

        Retrieves a list of all keys in the bulky metadata.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_item_bulky_metadata_keys(item_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: URIListType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: URIListType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_item_bulky_metadata_keys_with_http_info(item_id, **kwargs)  # noqa: E501

    def get_item_bulky_metadata_keys_with_http_info(self, item_id, **kwargs):  # noqa: E501
        """Retrieve all keys used in the bulky metadata  # noqa: E501

        Retrieves a list of all keys in the bulky metadata.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_item_bulky_metadata_keys_with_http_info(item_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(URIListType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['item_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_bulky_metadata_keys" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `get_item_bulky_metadata_keys`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/item/{item-id}/metadata/bulky/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='URIListType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_item_bulky_metadata_key(self, item_id, key, body, **kwargs):  # noqa: E501
        """Insert values  # noqa: E501

        Inserts a value at the specified interval for the given key. If the key already has a value at that specific interval then that value will be overwritten.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_item_bulky_metadata_key(item_id, key, body, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :param str key: The key. (required)
        :param str body: The value to set. (required)
        :key str item_track: The track in the item.
        :key str end: A time code that defines the end of the interval.
        :key int channel: The audio channel index.
        :key int stream: The stream index.
        :key str start: A time code that defines the start of the interval.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None.
                 If the method is called asynchronously, returns the request thread.
        :rtype: None or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.update_item_bulky_metadata_key_with_http_info(item_id, key, body, **kwargs)  # noqa: E501

    def update_item_bulky_metadata_key_with_http_info(self, item_id, key, body, **kwargs):  # noqa: E501
        """Insert values  # noqa: E501

        Inserts a value at the specified interval for the given key. If the key already has a value at that specific interval then that value will be overwritten.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_item_bulky_metadata_key_with_http_info(item_id, key, body, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :param str key: The key. (required)
        :param str body: The value to set. (required)
        :key str item_track: The track in the item.
        :key str end: A time code that defines the end of the interval.
        :key int channel: The audio channel index.
        :key int stream: The stream index.
        :key str start: A time code that defines the start of the interval.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['item_id', 'key', 'body', 'item_track', 'end', 'channel', 'stream', 'start']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_item_bulky_metadata_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `update_item_bulky_metadata_key`")  # noqa: E501
        # verify the required parameter 'key' is set
        if ('key' not in local_var_params or
                local_var_params['key'] is None):
            raise ApiValueError("Missing the required parameter `key` when calling `update_item_bulky_metadata_key`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in local_var_params or
                local_var_params['body'] is None):
            raise ApiValueError("Missing the required parameter `body` when calling `update_item_bulky_metadata_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []
        if 'item_track' in local_var_params:
            query_params.append(('itemTrack', local_var_params['item_track']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'channel' in local_var_params:
            query_params.append(('channel', local_var_params['channel']))  # noqa: E501
        if 'stream' in local_var_params:
            query_params.append(('stream', local_var_params['stream']))  # noqa: E501
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/item/{item-id}/metadata/bulky/{key}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
