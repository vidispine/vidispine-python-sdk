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


class ExportLocationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_export_location(self, location_name, **kwargs):  # noqa: E501
        """Delete an export location  # noqa: E501

        Delete the export location with the specified name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_export_location(location_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str location_name: The location name. (required)
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
        return self.delete_export_location_with_http_info(location_name, **kwargs)  # noqa: E501

    def delete_export_location_with_http_info(self, location_name, **kwargs):  # noqa: E501
        """Delete an export location  # noqa: E501

        Delete the export location with the specified name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_export_location_with_http_info(location_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str location_name: The location name. (required)
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

        all_params = ['location_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_export_location" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_name' is set
        if ('location_name' not in local_var_params or
                local_var_params['location_name'] is None):
            raise ApiValueError("Missing the required parameter `location_name` when calling `delete_export_location`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_name' in local_var_params:
            path_params['location-name'] = local_var_params['location_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/export-location/{location-name}', 'DELETE',
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

    def get_export_location(self, location_name, **kwargs):  # noqa: E501
        """Retrieve an export location  # noqa: E501

        Return information about the export location with the specified name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_export_location(location_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str location_name: The location name. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ExportLocationType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: ExportLocationType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_export_location_with_http_info(location_name, **kwargs)  # noqa: E501

    def get_export_location_with_http_info(self, location_name, **kwargs):  # noqa: E501
        """Retrieve an export location  # noqa: E501

        Return information about the export location with the specified name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_export_location_with_http_info(location_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str location_name: The location name. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ExportLocationType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['location_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_export_location" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_name' is set
        if ('location_name' not in local_var_params or
                local_var_params['location_name'] is None):
            raise ApiValueError("Missing the required parameter `location_name` when calling `get_export_location`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_name' in local_var_params:
            path_params['location-name'] = local_var_params['location_name']  # noqa: E501

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
            '/export-location/{location-name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExportLocationType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_export_location_script(self, location_name, **kwargs):  # noqa: E501
        """Retrieve the export location script  # noqa: E501

        Retrieves the script on an export location.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_export_location_script(location_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str location_name: The location name. (required)
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
        return self.get_export_location_script_with_http_info(location_name, **kwargs)  # noqa: E501

    def get_export_location_script_with_http_info(self, location_name, **kwargs):  # noqa: E501
        """Retrieve the export location script  # noqa: E501

        Retrieves the script on an export location.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_export_location_script_with_http_info(location_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str location_name: The location name. (required)
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

        all_params = ['location_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_export_location_script" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_name' is set
        if ('location_name' not in local_var_params or
                local_var_params['location_name'] is None):
            raise ApiValueError("Missing the required parameter `location_name` when calling `get_export_location_script`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_name' in local_var_params:
            path_params['location-name'] = local_var_params['location_name']  # noqa: E501

        query_params = []

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
            '/export-location/{location-name}/script', 'GET',
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

    def get_export_locations(self, **kwargs):  # noqa: E501
        """List all export locations  # noqa: E501

        List all defined export locations.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_export_locations(async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ExportLocationListType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: ExportLocationListType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_export_locations_with_http_info(**kwargs)  # noqa: E501

    def get_export_locations_with_http_info(self, **kwargs):  # noqa: E501
        """List all export locations  # noqa: E501

        List all defined export locations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_export_locations_with_http_info(async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ExportLocationListType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_export_locations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/export-location', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExportLocationListType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_export_location_script(self, location_name, body, **kwargs):  # noqa: E501
        """Update the export location script  # noqa: E501

        Updates the script of an existing export location.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_export_location_script(location_name, body, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str location_name: The location name. (required)
        :param str body: (required)
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
        return self.update_export_location_script_with_http_info(location_name, body, **kwargs)  # noqa: E501

    def update_export_location_script_with_http_info(self, location_name, body, **kwargs):  # noqa: E501
        """Update the export location script  # noqa: E501

        Updates the script of an existing export location.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_export_location_script_with_http_info(location_name, body, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str location_name: The location name. (required)
        :param str body: (required)
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

        all_params = ['location_name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_export_location_script" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_name' is set
        if ('location_name' not in local_var_params or
                local_var_params['location_name'] is None):
            raise ApiValueError("Missing the required parameter `location_name` when calling `update_export_location_script`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in local_var_params or
                local_var_params['body'] is None):
            raise ApiValueError("Missing the required parameter `body` when calling `update_export_location_script`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_name' in local_var_params:
            path_params['location-name'] = local_var_params['location_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/export-location/{location-name}/script', 'PUT',
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

    def update_or_create_export_location(self, location_name, export_location_type, **kwargs):  # noqa: E501
        """Update or create an export location  # noqa: E501

        Create a new export location, or if there already is one with that name, update it.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_or_create_export_location(location_name, export_location_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str location_name: The location name. (required)
        :param ExportLocationType export_location_type: (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ExportLocationType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: ExportLocationType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.update_or_create_export_location_with_http_info(location_name, export_location_type, **kwargs)  # noqa: E501

    def update_or_create_export_location_with_http_info(self, location_name, export_location_type, **kwargs):  # noqa: E501
        """Update or create an export location  # noqa: E501

        Create a new export location, or if there already is one with that name, update it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_or_create_export_location_with_http_info(location_name, export_location_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str location_name: The location name. (required)
        :param ExportLocationType export_location_type: (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ExportLocationType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['location_name', 'export_location_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_or_create_export_location" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'location_name' is set
        if ('location_name' not in local_var_params or
                local_var_params['location_name'] is None):
            raise ApiValueError("Missing the required parameter `location_name` when calling `update_or_create_export_location`")  # noqa: E501
        # verify the required parameter 'export_location_type' is set
        if ('export_location_type' not in local_var_params or
                local_var_params['export_location_type'] is None):
            raise ApiValueError("Missing the required parameter `export_location_type` when calling `update_or_create_export_location`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location_name' in local_var_params:
            path_params['location-name'] = local_var_params['location_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'export_location_type' in local_var_params:
            body_params = local_var_params['export_location_type']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/export-location/{location-name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExportLocationType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
