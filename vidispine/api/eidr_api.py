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


class EidrApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def synchronize_eidr_item(self, item_id, **kwargs):  # noqa: E501
        """Synchronize EIDR metadata  # noqa: E501

        Synchronizes `item(s)` metadata that are out of date. An item is considered out of date if the EIDR record has changed or if the included projections have changed.  Returns a list of synchronized items with the metadata that was written to the item.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.synchronize_eidr_item(item_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :key bool force_sync: - `true` - force metadata write to item.  - `false` - (default)
        :key str eidr_resource: If set, the resource identified by this id will be used instead of first found EIDR resource.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: MetadataListType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: MetadataListType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.synchronize_eidr_item_with_http_info(item_id, **kwargs)  # noqa: E501

    def synchronize_eidr_item_with_http_info(self, item_id, **kwargs):  # noqa: E501
        """Synchronize EIDR metadata  # noqa: E501

        Synchronizes `item(s)` metadata that are out of date. An item is considered out of date if the EIDR record has changed or if the included projections have changed.  Returns a list of synchronized items with the metadata that was written to the item.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.synchronize_eidr_item_with_http_info(item_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str item_id: The item id. (required)
        :key bool force_sync: - `true` - force metadata write to item.  - `false` - (default)
        :key str eidr_resource: If set, the resource identified by this id will be used instead of first found EIDR resource.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(MetadataListType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['item_id', 'force_sync', 'eidr_resource']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method synchronize_eidr_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `synchronize_eidr_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501

        query_params = []
        if 'force_sync' in local_var_params:
            query_params.append(('forceSync', local_var_params['force_sync']))  # noqa: E501
        if 'eidr_resource' in local_var_params:
            query_params.append(('eidrResource', local_var_params['eidr_resource']))  # noqa: E501

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
            '/item/{item-id}/eidr/sync', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MetadataListType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def synchronize_eidr_library(self, library_id, **kwargs):  # noqa: E501
        """Synchronize EIDR metadata  # noqa: E501

        Synchronizes `item(s)` metadata that are out of date. An item is considered out of date if the EIDR record has changed or if the included projections have changed.  Returns a list of synchronized items with the metadata that was written to the item.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.synchronize_eidr_library(library_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str library_id: The library id. (required)
        :key bool force_sync: - `true` - force metadata write to item.  - `false` - (default)
        :key str eidr_resource: If set, the resource identified by this id will be used instead of first found EIDR resource.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: MetadataListType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: MetadataListType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.synchronize_eidr_library_with_http_info(library_id, **kwargs)  # noqa: E501

    def synchronize_eidr_library_with_http_info(self, library_id, **kwargs):  # noqa: E501
        """Synchronize EIDR metadata  # noqa: E501

        Synchronizes `item(s)` metadata that are out of date. An item is considered out of date if the EIDR record has changed or if the included projections have changed.  Returns a list of synchronized items with the metadata that was written to the item.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.synchronize_eidr_library_with_http_info(library_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str library_id: The library id. (required)
        :key bool force_sync: - `true` - force metadata write to item.  - `false` - (default)
        :key str eidr_resource: If set, the resource identified by this id will be used instead of first found EIDR resource.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(MetadataListType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['library_id', 'force_sync', 'eidr_resource']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method synchronize_eidr_library" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'library_id' is set
        if ('library_id' not in local_var_params or
                local_var_params['library_id'] is None):
            raise ApiValueError("Missing the required parameter `library_id` when calling `synchronize_eidr_library`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'library_id' in local_var_params:
            path_params['library-id'] = local_var_params['library_id']  # noqa: E501

        query_params = []
        if 'force_sync' in local_var_params:
            query_params.append(('forceSync', local_var_params['force_sync']))  # noqa: E501
        if 'eidr_resource' in local_var_params:
            query_params.append(('eidrResource', local_var_params['eidr_resource']))  # noqa: E501

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
            '/library/{library-id}/eidr/sync', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MetadataListType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)