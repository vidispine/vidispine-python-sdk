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


class CostEstimationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_cost_estimate(self, path, **kwargs):  # noqa: E501
        """Request a cost estimate  # noqa: E501

        Requests a cost estimate for performing a specific operation.  The same query parameters and request body as used by the target request should be specified in the cost estimate request.  No additional roles or permissions are required to request a cost estimate. If a user has permission to for example transcode an item, then that user may also request a cost estimate for that operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_cost_estimate(path, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str path: The path. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CostEstimateType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: CostEstimateType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.create_cost_estimate_with_http_info(path, **kwargs)  # noqa: E501

    def create_cost_estimate_with_http_info(self, path, **kwargs):  # noqa: E501
        """Request a cost estimate  # noqa: E501

        Requests a cost estimate for performing a specific operation.  The same query parameters and request body as used by the target request should be specified in the cost estimate request.  No additional roles or permissions are required to request a cost estimate. If a user has permission to for example transcode an item, then that user may also request a cost estimate for that operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cost_estimate_with_http_info(path, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str path: The path. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CostEstimateType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_cost_estimate" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in local_var_params or
                local_var_params['path'] is None):
            raise ApiValueError("Missing the required parameter `path` when calling `create_cost_estimate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']  # noqa: E501

        query_params = []

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
            '/cost/{path}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CostEstimateType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cost_estimate(self, id, **kwargs):  # noqa: E501
        """Retrieve the cost estimate results  # noqa: E501

        Retrieves the cost estimate.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cost_estimate(id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str id: The id. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CostEstimateType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: CostEstimateType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_cost_estimate_with_http_info(id, **kwargs)  # noqa: E501

    def get_cost_estimate_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve the cost estimate results  # noqa: E501

        Retrieves the cost estimate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cost_estimate_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str id: The id. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CostEstimateType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cost_estimate" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `get_cost_estimate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

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
            '/cost/estimate/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CostEstimateType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
