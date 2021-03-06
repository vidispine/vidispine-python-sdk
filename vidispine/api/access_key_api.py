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


class AccessKeyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_user_access_key(self, username, **kwargs):  # noqa: E501
        """Create an access key  # noqa: E501

        Generates a new access key and secret for the specified user. The only time the access key secret will be available is in the response of this request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_user_access_key(username, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :key str name: A friendly name/description of the key.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AccessKeyType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: AccessKeyType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.create_user_access_key_with_http_info(username, **kwargs)  # noqa: E501

    def create_user_access_key_with_http_info(self, username, **kwargs):  # noqa: E501
        """Create an access key  # noqa: E501

        Generates a new access key and secret for the specified user. The only time the access key secret will be available is in the response of this request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_access_key_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :key str name: A friendly name/description of the key.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AccessKeyType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user_access_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ApiValueError("Missing the required parameter `username` when calling `create_user_access_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))  # noqa: E501

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
            '/user/{username}/key', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessKeyType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user_access_key(self, username, key_id, **kwargs):  # noqa: E501
        """Delete an access key  # noqa: E501

        Removes the specific access key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user_access_key(username, key_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :param str key_id: The key id. (required)
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
        return self.delete_user_access_key_with_http_info(username, key_id, **kwargs)  # noqa: E501

    def delete_user_access_key_with_http_info(self, username, key_id, **kwargs):  # noqa: E501
        """Delete an access key  # noqa: E501

        Removes the specific access key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_access_key_with_http_info(username, key_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :param str key_id: The key id. (required)
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

        all_params = ['username', 'key_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_access_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ApiValueError("Missing the required parameter `username` when calling `delete_user_access_key`")  # noqa: E501
        # verify the required parameter 'key_id' is set
        if ('key_id' not in local_var_params or
                local_var_params['key_id'] is None):
            raise ApiValueError("Missing the required parameter `key_id` when calling `delete_user_access_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501
        if 'key_id' in local_var_params:
            path_params['key-id'] = local_var_params['key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/user/{username}/key/{key-id}', 'DELETE',
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

    def get_user_access_key(self, username, key_id, **kwargs):  # noqa: E501
        """Retrieve an access key  # noqa: E501

        Retrieves a specific access key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_access_key(username, key_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :param str key_id: The key id. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AccessKeyType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: AccessKeyType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_access_key_with_http_info(username, key_id, **kwargs)  # noqa: E501

    def get_user_access_key_with_http_info(self, username, key_id, **kwargs):  # noqa: E501
        """Retrieve an access key  # noqa: E501

        Retrieves a specific access key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_access_key_with_http_info(username, key_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :param str key_id: The key id. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AccessKeyType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username', 'key_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_access_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ApiValueError("Missing the required parameter `username` when calling `get_user_access_key`")  # noqa: E501
        # verify the required parameter 'key_id' is set
        if ('key_id' not in local_var_params or
                local_var_params['key_id'] is None):
            raise ApiValueError("Missing the required parameter `key_id` when calling `get_user_access_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501
        if 'key_id' in local_var_params:
            path_params['key-id'] = local_var_params['key_id']  # noqa: E501

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
            '/user/{username}/key/{key-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessKeyType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_access_keys(self, username, **kwargs):  # noqa: E501
        """List all access keys for a user  # noqa: E501

        Retrieves the access keys for the specified user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_access_keys(username, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AccessKeyListType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: AccessKeyListType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_access_keys_with_http_info(username, **kwargs)  # noqa: E501

    def get_user_access_keys_with_http_info(self, username, **kwargs):  # noqa: E501
        """List all access keys for a user  # noqa: E501

        Retrieves the access keys for the specified user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_access_keys_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AccessKeyListType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_access_keys" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ApiValueError("Missing the required parameter `username` when calling `get_user_access_keys`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

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
            '/user/{username}/key', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessKeyListType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_user_access_key(self, username, key_id, access_key_type, **kwargs):  # noqa: E501
        """Update an access key  # noqa: E501

        Updates the name and/or status of a specific access key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_user_access_key(username, key_id, access_key_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :param str key_id: The key id. (required)
        :param AccessKeyType access_key_type: (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AccessKeyType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: AccessKeyType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.update_user_access_key_with_http_info(username, key_id, access_key_type, **kwargs)  # noqa: E501

    def update_user_access_key_with_http_info(self, username, key_id, access_key_type, **kwargs):  # noqa: E501
        """Update an access key  # noqa: E501

        Updates the name and/or status of a specific access key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_access_key_with_http_info(username, key_id, access_key_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str username: The username. (required)
        :param str key_id: The key id. (required)
        :param AccessKeyType access_key_type: (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AccessKeyType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username', 'key_id', 'access_key_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user_access_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ApiValueError("Missing the required parameter `username` when calling `update_user_access_key`")  # noqa: E501
        # verify the required parameter 'key_id' is set
        if ('key_id' not in local_var_params or
                local_var_params['key_id'] is None):
            raise ApiValueError("Missing the required parameter `key_id` when calling `update_user_access_key`")  # noqa: E501
        # verify the required parameter 'access_key_type' is set
        if ('access_key_type' not in local_var_params or
                local_var_params['access_key_type'] is None):
            raise ApiValueError("Missing the required parameter `access_key_type` when calling `update_user_access_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501
        if 'key_id' in local_var_params:
            path_params['key-id'] = local_var_params['key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'access_key_type' in local_var_params:
            body_params = local_var_params['access_key_type']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/user/{username}/key/{key-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessKeyType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
