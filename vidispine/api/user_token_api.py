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


class UserTokenApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_auth_token(self, **kwargs):  # noqa: E501
        """Retrieve an authentication token  # noqa: E501

        Creates a authentication token for the calling user. This token can be used for calling the API without specifying username or password.  Useful when users authenticate using an alias and the actual username of the user is not known.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_auth_token(async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :key bool auto_refresh: - `true` - The expiration clock is reset with every API call.  - `false` (default) - The token always expires after `seconds` seconds after the token was created.
        :key int seconds: The duration of the token.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AuthenticationTokenType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: AuthenticationTokenType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_auth_token_with_http_info(**kwargs)  # noqa: E501

    def get_auth_token_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve an authentication token  # noqa: E501

        Creates a authentication token for the calling user. This token can be used for calling the API without specifying username or password.  Useful when users authenticate using an alias and the actual username of the user is not known.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auth_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :key bool auto_refresh: - `true` - The expiration clock is reset with every API call.  - `false` (default) - The token always expires after `seconds` seconds after the token was created.
        :key int seconds: The duration of the token.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AuthenticationTokenType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['auto_refresh', 'seconds']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auth_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'auto_refresh' in local_var_params:
            query_params.append(('autoRefresh', local_var_params['auto_refresh']))  # noqa: E501
        if 'seconds' in local_var_params:
            query_params.append(('seconds', local_var_params['seconds']))  # noqa: E501

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
            '/token', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthenticationTokenType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_auth_token(self, username, **kwargs):  # noqa: E501
        """Retrieve an authentication token for a specific user  # noqa: E501

        Creates a authentication token for a user. This token can be used for calling the API without specifying username or password.  The username path parameter must match the calling user's credentials, unless the calling user has `_administrator` role.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_auth_token(username, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :key bool auto_refresh: - `true` - The expiration clock is reset with every API call.  - `false` (default) - The token always expires after `seconds` seconds after the token was created.
        :key int seconds: The duration of the token.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str.
                 If the method is called asynchronously, returns the request thread.
        :rtype: str or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_auth_token_with_http_info(username, **kwargs)  # noqa: E501

    def get_user_auth_token_with_http_info(self, username, **kwargs):  # noqa: E501
        """Retrieve an authentication token for a specific user  # noqa: E501

        Creates a authentication token for a user. This token can be used for calling the API without specifying username or password.  The username path parameter must match the calling user's credentials, unless the calling user has `_administrator` role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_auth_token_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :key bool auto_refresh: - `true` - The expiration clock is reset with every API call.  - `false` (default) - The token always expires after `seconds` seconds after the token was created.
        :key int seconds: The duration of the token.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username', 'auto_refresh', 'seconds']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_auth_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ApiValueError("Missing the required parameter `username` when calling `get_user_auth_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = []
        if 'auto_refresh' in local_var_params:
            query_params.append(('autoRefresh', local_var_params['auto_refresh']))  # noqa: E501
        if 'seconds' in local_var_params:
            query_params.append(('seconds', local_var_params['seconds']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/user/{username}/token', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)