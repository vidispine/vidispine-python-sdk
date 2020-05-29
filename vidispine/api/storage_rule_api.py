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


class StorageRuleApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_shape_tag_default_storage_rule(self, **kwargs):  # noqa: E501
        """Delete a default rule  # noqa: E501

        Deletes the default rule.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_shape_tag_default_storage_rule(async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
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
        return self.delete_shape_tag_default_storage_rule_with_http_info(**kwargs)  # noqa: E501

    def delete_shape_tag_default_storage_rule_with_http_info(self, **kwargs):  # noqa: E501
        """Delete a default rule  # noqa: E501

        Deletes the default rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_shape_tag_default_storage_rule_with_http_info(async_req=True)
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
        :return: None
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
                    " to method delete_shape_tag_default_storage_rule" % key
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
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/shape-tag/storage-rule', 'DELETE',
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

    def delete_shape_tag_storage_rule(self, tag_name, **kwargs):  # noqa: E501
        """Delete a storage rule  # noqa: E501

        Deletes a specific rule.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_shape_tag_storage_rule(tag_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str tag_name: The tag name. (required)
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
        return self.delete_shape_tag_storage_rule_with_http_info(tag_name, **kwargs)  # noqa: E501

    def delete_shape_tag_storage_rule_with_http_info(self, tag_name, **kwargs):  # noqa: E501
        """Delete a storage rule  # noqa: E501

        Deletes a specific rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_shape_tag_storage_rule_with_http_info(tag_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str tag_name: The tag name. (required)
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

        all_params = ['tag_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_shape_tag_storage_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag_name' is set
        if ('tag_name' not in local_var_params or
                local_var_params['tag_name'] is None):
            raise ApiValueError("Missing the required parameter `tag_name` when calling `delete_shape_tag_storage_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_name' in local_var_params:
            path_params['tag-name'] = local_var_params['tag_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/shape-tag/storage-rule/{tag-name}', 'DELETE',
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

    def get_shape_tag_storage_rule(self, tag_name, **kwargs):  # noqa: E501
        """Retrieve a a storage rule  # noqa: E501

        Returns the rule that is applied to a certain shape tag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_shape_tag_storage_rule(tag_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str tag_name: The tag name. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: StorageRuleType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: StorageRuleType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_shape_tag_storage_rule_with_http_info(tag_name, **kwargs)  # noqa: E501

    def get_shape_tag_storage_rule_with_http_info(self, tag_name, **kwargs):  # noqa: E501
        """Retrieve a a storage rule  # noqa: E501

        Returns the rule that is applied to a certain shape tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shape_tag_storage_rule_with_http_info(tag_name, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str tag_name: The tag name. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(StorageRuleType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tag_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shape_tag_storage_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag_name' is set
        if ('tag_name' not in local_var_params or
                local_var_params['tag_name'] is None):
            raise ApiValueError("Missing the required parameter `tag_name` when calling `get_shape_tag_storage_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_name' in local_var_params:
            path_params['tag-name'] = local_var_params['tag_name']  # noqa: E501

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
            '/shape-tag/storage-rule/{tag-name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StorageRuleType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_shape_tag_storage_rules(self, **kwargs):  # noqa: E501
        """List all storage rules for an entity  # noqa: E501

        Retrieves all storage rules that are applied on a certain entity in a certain resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_shape_tag_storage_rules(async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: StorageRulesType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: StorageRulesType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_shape_tag_storage_rules_with_http_info(**kwargs)  # noqa: E501

    def get_shape_tag_storage_rules_with_http_info(self, **kwargs):  # noqa: E501
        """List all storage rules for an entity  # noqa: E501

        Retrieves all storage rules that are applied on a certain entity in a certain resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shape_tag_storage_rules_with_http_info(async_req=True)
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
        :return: tuple(StorageRulesType, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_shape_tag_storage_rules" % key
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
            '/shape-tag/storage-rule', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StorageRulesType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_storage_rules(self, **kwargs):  # noqa: E501
        """List all storage rules  # noqa: E501

        Retrieves all storage-rules that matches the given parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_storage_rules(async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :key list[str] tag: Comma-separated list of tags to retrieve, if not specified rules of all tag types will be retrieved.
        :key list[str] type: Comma-separated list of types to retrieve, if not specified all types will be retrieved.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: StorageRulesType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: StorageRulesType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_storage_rules_with_http_info(**kwargs)  # noqa: E501

    def get_storage_rules_with_http_info(self, **kwargs):  # noqa: E501
        """List all storage rules  # noqa: E501

        Retrieves all storage-rules that matches the given parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :key list[str] tag: Comma-separated list of tags to retrieve, if not specified rules of all tag types will be retrieved.
        :key list[str] type: Comma-separated list of types to retrieve, if not specified all types will be retrieved.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(StorageRulesType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tag', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_storage_rules" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))  # noqa: E501
            collection_formats['tag'] = 'csv'  # noqa: E501
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501
            collection_formats['type'] = 'csv'  # noqa: E501

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
            '/storage-rule/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StorageRulesType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_shape_tag_default_storage_rule(self, storage_rule_type, **kwargs):  # noqa: E501
        """Set a default rule  # noqa: E501

        Sets the default rule.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_shape_tag_default_storage_rule(storage_rule_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param StorageRuleType storage_rule_type: (required)
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
        return self.update_shape_tag_default_storage_rule_with_http_info(storage_rule_type, **kwargs)  # noqa: E501

    def update_shape_tag_default_storage_rule_with_http_info(self, storage_rule_type, **kwargs):  # noqa: E501
        """Set a default rule  # noqa: E501

        Sets the default rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_shape_tag_default_storage_rule_with_http_info(storage_rule_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param StorageRuleType storage_rule_type: (required)
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

        all_params = ['storage_rule_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_shape_tag_default_storage_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'storage_rule_type' is set
        if ('storage_rule_type' not in local_var_params or
                local_var_params['storage_rule_type'] is None):
            raise ApiValueError("Missing the required parameter `storage_rule_type` when calling `update_shape_tag_default_storage_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'storage_rule_type' in local_var_params:
            body_params = local_var_params['storage_rule_type']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/shape-tag/storage-rule', 'PUT',
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

    def update_shape_tag_storage_rule(self, tag_name, storage_rule_type, **kwargs):  # noqa: E501
        """Set a storage rule  # noqa: E501

        Updates a storage rule applied to a certain shape tag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_shape_tag_storage_rule(tag_name, storage_rule_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str tag_name: The tag name. (required)
        :param StorageRuleType storage_rule_type: (required)
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
        return self.update_shape_tag_storage_rule_with_http_info(tag_name, storage_rule_type, **kwargs)  # noqa: E501

    def update_shape_tag_storage_rule_with_http_info(self, tag_name, storage_rule_type, **kwargs):  # noqa: E501
        """Set a storage rule  # noqa: E501

        Updates a storage rule applied to a certain shape tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_shape_tag_storage_rule_with_http_info(tag_name, storage_rule_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str tag_name: The tag name. (required)
        :param StorageRuleType storage_rule_type: (required)
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

        all_params = ['tag_name', 'storage_rule_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_shape_tag_storage_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag_name' is set
        if ('tag_name' not in local_var_params or
                local_var_params['tag_name'] is None):
            raise ApiValueError("Missing the required parameter `tag_name` when calling `update_shape_tag_storage_rule`")  # noqa: E501
        # verify the required parameter 'storage_rule_type' is set
        if ('storage_rule_type' not in local_var_params or
                local_var_params['storage_rule_type'] is None):
            raise ApiValueError("Missing the required parameter `storage_rule_type` when calling `update_shape_tag_storage_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_name' in local_var_params:
            path_params['tag-name'] = local_var_params['tag_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'storage_rule_type' in local_var_params:
            body_params = local_var_params['storage_rule_type']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/shape-tag/storage-rule/{tag-name}', 'PUT',
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