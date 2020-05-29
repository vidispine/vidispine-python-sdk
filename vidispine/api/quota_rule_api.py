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


class QuotaRuleApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_quota_rule(self, quota_rule_type, **kwargs):  # noqa: E501
        """Create a quota rule  # noqa: E501

        Creates a quota rule with the filters and resource limits as specified in the quota rule document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_quota_rule(quota_rule_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param QuotaRuleType quota_rule_type: (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: QuotaRuleType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: QuotaRuleType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.create_quota_rule_with_http_info(quota_rule_type, **kwargs)  # noqa: E501

    def create_quota_rule_with_http_info(self, quota_rule_type, **kwargs):  # noqa: E501
        """Create a quota rule  # noqa: E501

        Creates a quota rule with the filters and resource limits as specified in the quota rule document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_quota_rule_with_http_info(quota_rule_type, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param QuotaRuleType quota_rule_type: (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(QuotaRuleType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['quota_rule_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_quota_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'quota_rule_type' is set
        if ('quota_rule_type' not in local_var_params or
                local_var_params['quota_rule_type'] is None):
            raise ApiValueError("Missing the required parameter `quota_rule_type` when calling `create_quota_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'quota_rule_type' in local_var_params:
            body_params = local_var_params['quota_rule_type']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/quota/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuotaRuleType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_quota_rule(self, rule_id, **kwargs):  # noqa: E501
        """Delete a quota rule  # noqa: E501

        Deletes the quota rule.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_quota_rule(rule_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str rule_id: The rule id. (required)
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
        return self.delete_quota_rule_with_http_info(rule_id, **kwargs)  # noqa: E501

    def delete_quota_rule_with_http_info(self, rule_id, **kwargs):  # noqa: E501
        """Delete a quota rule  # noqa: E501

        Deletes the quota rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_quota_rule_with_http_info(rule_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str rule_id: The rule id. (required)
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

        all_params = ['rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_quota_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in local_var_params or
                local_var_params['rule_id'] is None):
            raise ApiValueError("Missing the required parameter `rule_id` when calling `delete_quota_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule-id'] = local_var_params['rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/quota/{rule-id}', 'DELETE',
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

    def evaluate_quota_rule(self, rule_id, **kwargs):  # noqa: E501
        """Evaluate a quota rule  # noqa: E501

        Immediately calculates the resource usage as defined by a quota rule.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.evaluate_quota_rule(rule_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str rule_id: The rule id. (required)
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
        return self.evaluate_quota_rule_with_http_info(rule_id, **kwargs)  # noqa: E501

    def evaluate_quota_rule_with_http_info(self, rule_id, **kwargs):  # noqa: E501
        """Evaluate a quota rule  # noqa: E501

        Immediately calculates the resource usage as defined by a quota rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.evaluate_quota_rule_with_http_info(rule_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str rule_id: The rule id. (required)
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

        all_params = ['rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method evaluate_quota_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in local_var_params or
                local_var_params['rule_id'] is None):
            raise ApiValueError("Missing the required parameter `rule_id` when calling `evaluate_quota_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule-id'] = local_var_params['rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/quota/{rule-id}/evaluate', 'PUT',
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

    def get_quota_rule(self, rule_id, **kwargs):  # noqa: E501
        """Retrieve a quota rule  # noqa: E501

        Retrieves a specific quota rule.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_quota_rule(rule_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str rule_id: The rule id. (required)
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: QuotaRuleType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: QuotaRuleType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_quota_rule_with_http_info(rule_id, **kwargs)  # noqa: E501

    def get_quota_rule_with_http_info(self, rule_id, **kwargs):  # noqa: E501
        """Retrieve a quota rule  # noqa: E501

        Retrieves a specific quota rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quota_rule_with_http_info(rule_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str rule_id: The rule id. (required)
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(QuotaRuleType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_quota_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in local_var_params or
                local_var_params['rule_id'] is None):
            raise ApiValueError("Missing the required parameter `rule_id` when calling `get_quota_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule-id'] = local_var_params['rule_id']  # noqa: E501

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
            '/quota/{rule-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuotaRuleType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_quota_rules(self, **kwargs):  # noqa: E501
        """List all quota rules  # noqa: E501

        Returns the quota rules that exist in the system.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_quota_rules(async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :key list[str] content: Comma-separated list of addition content to retrieve.
        :key bool exceeded: - `true` - Returns only rules where the usage of a resource exceeds the limit that has been specified for a rule.  - `false` (default) - Returns rules regardless of the current resource usage.
        :key list[str] filter: Comma-separated list of key-value pairs (in the format key=value) that can be used to filter the result set.  Valid key values are: `user`, `group`, `storage`, `storageGroup`, `collection`, `library` and `tag`.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: QuotaRuleListType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: QuotaRuleListType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_quota_rules_with_http_info(**kwargs)  # noqa: E501

    def get_quota_rules_with_http_info(self, **kwargs):  # noqa: E501
        """List all quota rules  # noqa: E501

        Returns the quota rules that exist in the system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quota_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :key list[str] content: Comma-separated list of addition content to retrieve.
        :key bool exceeded: - `true` - Returns only rules where the usage of a resource exceeds the limit that has been specified for a rule.  - `false` (default) - Returns rules regardless of the current resource usage.
        :key list[str] filter: Comma-separated list of key-value pairs (in the format key=value) that can be used to filter the result set.  Valid key values are: `user`, `group`, `storage`, `storageGroup`, `collection`, `library` and `tag`.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(QuotaRuleListType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['content', 'exceeded', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_quota_rules" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'content' in local_var_params:
            query_params.append(('content', local_var_params['content']))  # noqa: E501
            collection_formats['content'] = 'csv'  # noqa: E501
        if 'exceeded' in local_var_params:
            query_params.append(('exceeded', local_var_params['exceeded']))  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501

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
            '/quota/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuotaRuleListType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)