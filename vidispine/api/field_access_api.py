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


class FieldAccessApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_metadata_field_access_control(self, field_name, metadata_field_access_control_type, **kwargs):  # noqa: E501
        """Create an access control entry  # noqa: E501

        Creates an entry in the access control list and returns the created entry together with its id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_metadata_field_access_control(field_name, metadata_field_access_control_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str field_name: The field name. (required)
        :param MetadataFieldAccessControlType metadata_field_access_control_type: (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: MetadataFieldAccessControlType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: MetadataFieldAccessControlType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.create_metadata_field_access_control_with_http_info(field_name, metadata_field_access_control_type, **kwargs)  # noqa: E501

    def create_metadata_field_access_control_with_http_info(self, field_name, metadata_field_access_control_type, **kwargs):  # noqa: E501
        """Create an access control entry  # noqa: E501

        Creates an entry in the access control list and returns the created entry together with its id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_metadata_field_access_control_with_http_info(field_name, metadata_field_access_control_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str field_name: The field name. (required)
        :param MetadataFieldAccessControlType metadata_field_access_control_type: (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(MetadataFieldAccessControlType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['field_name', 'metadata_field_access_control_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_metadata_field_access_control" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'field_name' is set
        if ('field_name' not in local_var_params or
                local_var_params['field_name'] is None):
            raise ApiValueError("Missing the required parameter `field_name` when calling `create_metadata_field_access_control`")  # noqa: E501
        # verify the required parameter 'metadata_field_access_control_type' is set
        if ('metadata_field_access_control_type' not in local_var_params or
                local_var_params['metadata_field_access_control_type'] is None):
            raise ApiValueError("Missing the required parameter `metadata_field_access_control_type` when calling `create_metadata_field_access_control`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field_name' in local_var_params:
            path_params['field-name'] = local_var_params['field_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'metadata_field_access_control_type' in local_var_params:
            body_params = local_var_params['metadata_field_access_control_type']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/metadata-field/{field-name}/access', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MetadataFieldAccessControlType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_metadata_field_access_control(self, field_name, access_id, **kwargs):  # noqa: E501
        """Delete an access control entry  # noqa: E501

        Removes the access control entry with the specified id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_metadata_field_access_control(field_name, access_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str field_name: The field name. (required)
        :param str access_id: The access id. (required)
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
        return self.delete_metadata_field_access_control_with_http_info(field_name, access_id, **kwargs)  # noqa: E501

    def delete_metadata_field_access_control_with_http_info(self, field_name, access_id, **kwargs):  # noqa: E501
        """Delete an access control entry  # noqa: E501

        Removes the access control entry with the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_metadata_field_access_control_with_http_info(field_name, access_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str field_name: The field name. (required)
        :param str access_id: The access id. (required)
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

        all_params = ['field_name', 'access_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_metadata_field_access_control" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'field_name' is set
        if ('field_name' not in local_var_params or
                local_var_params['field_name'] is None):
            raise ApiValueError("Missing the required parameter `field_name` when calling `delete_metadata_field_access_control`")  # noqa: E501
        # verify the required parameter 'access_id' is set
        if ('access_id' not in local_var_params or
                local_var_params['access_id'] is None):
            raise ApiValueError("Missing the required parameter `access_id` when calling `delete_metadata_field_access_control`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field_name' in local_var_params:
            path_params['field-name'] = local_var_params['field_name']  # noqa: E501
        if 'access_id' in local_var_params:
            path_params['access-id'] = local_var_params['access_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/metadata-field/{field-name}/access/{access-id}', 'DELETE',
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

    def get_metadata_field_access_controls(self, field_name, **kwargs):  # noqa: E501
        """Retrieve an access control list  # noqa: E501

        Returns the access control list that is applied to the specified field or group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_metadata_field_access_controls(field_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str field_name: The field name. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: MetadataFieldAccessControlListType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: MetadataFieldAccessControlListType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_metadata_field_access_controls_with_http_info(field_name, **kwargs)  # noqa: E501

    def get_metadata_field_access_controls_with_http_info(self, field_name, **kwargs):  # noqa: E501
        """Retrieve an access control list  # noqa: E501

        Returns the access control list that is applied to the specified field or group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metadata_field_access_controls_with_http_info(field_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str field_name: The field name. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(MetadataFieldAccessControlListType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['field_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metadata_field_access_controls" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'field_name' is set
        if ('field_name' not in local_var_params or
                local_var_params['field_name'] is None):
            raise ApiValueError("Missing the required parameter `field_name` when calling `get_metadata_field_access_controls`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field_name' in local_var_params:
            path_params['field-name'] = local_var_params['field_name']  # noqa: E501

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
            '/metadata-field/{field-name}/access', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MetadataFieldAccessControlListType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
