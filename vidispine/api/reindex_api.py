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


class ReindexApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_reindex_status(self, index, **kwargs):  # noqa: E501
        """Retrieve reindex status  # noqa: E501

        Gets information about a reindex process, i.e., progress and whether it is finished.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_reindex_status(index, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str index: The index. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ReindexRequestType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: ReindexRequestType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_reindex_status_with_http_info(index, **kwargs)  # noqa: E501

    def get_reindex_status_with_http_info(self, index, **kwargs):  # noqa: E501
        """Retrieve reindex status  # noqa: E501

        Gets information about a reindex process, i.e., progress and whether it is finished.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reindex_status_with_http_info(index, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str index: The index. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ReindexRequestType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_reindex_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in local_var_params or
                local_var_params['index'] is None):
            raise ApiValueError("Missing the required parameter `index` when calling `get_reindex_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'index' in local_var_params:
            path_params['index'] = local_var_params['index']  # noqa: E501

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
            '/reindex/{index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReindexRequestType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reindex(self, index, **kwargs):  # noqa: E501
        """Request a reindex  # noqa: E501

        Starts a reindex. If a reindex of the same type is already in progress, it is restarted.  The types than can be reindexed are: item, collection, ACL, file, thumbnail and document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reindex(index, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str index: The index to rebuild. (required)
        :key str status: If current status is `FINISHED` or `ABORTED` then `PAUSED`, `ABORTED` and `IN_PROGRESS` are no-ops.   - `IN_QUEUE` (default) - To start or restart reindex.  - `PAUSED` - To pause reindex.  - `ABORTED` - To cancel reindex.  - `IN_PROGRESS`/`IN PROGRESS` - To resume a paused reindex.
        :key int priority: The priority of this reindex request compare to other request.  Requests with a larger/higher priority will be processed first.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ReindexRequestType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: ReindexRequestType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.reindex_with_http_info(index, **kwargs)  # noqa: E501

    def reindex_with_http_info(self, index, **kwargs):  # noqa: E501
        """Request a reindex  # noqa: E501

        Starts a reindex. If a reindex of the same type is already in progress, it is restarted.  The types than can be reindexed are: item, collection, ACL, file, thumbnail and document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reindex_with_http_info(index, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str index: The index to rebuild. (required)
        :key str status: If current status is `FINISHED` or `ABORTED` then `PAUSED`, `ABORTED` and `IN_PROGRESS` are no-ops.   - `IN_QUEUE` (default) - To start or restart reindex.  - `PAUSED` - To pause reindex.  - `ABORTED` - To cancel reindex.  - `IN_PROGRESS`/`IN PROGRESS` - To resume a paused reindex.
        :key int priority: The priority of this reindex request compare to other request.  Requests with a larger/higher priority will be processed first.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ReindexRequestType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['index', 'status', 'priority']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reindex" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in local_var_params or
                local_var_params['index'] is None):
            raise ApiValueError("Missing the required parameter `index` when calling `reindex`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'index' in local_var_params:
            path_params['index'] = local_var_params['index']  # noqa: E501

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'priority' in local_var_params:
            query_params.append(('priority', local_var_params['priority']))  # noqa: E501

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
            '/reindex/{index}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReindexRequestType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
