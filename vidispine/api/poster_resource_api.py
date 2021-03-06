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


class PosterResourceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_poster_export_job(self, uri, service, item_id, time, **kwargs):  # noqa: E501
        """Export a thumbnail  # noqa: E501

        Starts a job that writes the thumbnail or poster to a specific destination.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_poster_export_job(uri, service, item_id, time, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str uri: URI of export location of thumbnail or poster (required)
        :param str service: The service. (required)
        :param str item_id: The item id. (required)
        :param str time: The time. (required)
        :key list[str] jobmetadata: Additional information for the job task.
        :key str notification_data: Any additional data to include for notifications on this job.
        :key str format: Image format of destination.  E. g.  `tiff`.
        :key str notification: The placeholder job notification to use for this job.
        :key str priority: The priority to assign to the job.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: JobType.
                 If the method is called asynchronously, returns the request thread.
        :rtype: JobType or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.create_poster_export_job_with_http_info(uri, service, item_id, time, **kwargs)  # noqa: E501

    def create_poster_export_job_with_http_info(self, uri, service, item_id, time, **kwargs):  # noqa: E501
        """Export a thumbnail  # noqa: E501

        Starts a job that writes the thumbnail or poster to a specific destination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_poster_export_job_with_http_info(uri, service, item_id, time, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str uri: URI of export location of thumbnail or poster (required)
        :param str service: The service. (required)
        :param str item_id: The item id. (required)
        :param str time: The time. (required)
        :key list[str] jobmetadata: Additional information for the job task.
        :key str notification_data: Any additional data to include for notifications on this job.
        :key str format: Image format of destination.  E. g.  `tiff`.
        :key str notification: The placeholder job notification to use for this job.
        :key str priority: The priority to assign to the job.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(JobType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['uri', 'service', 'item_id', 'time', 'jobmetadata', 'notification_data', 'format', 'notification', 'priority']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_poster_export_job" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uri' is set
        if ('uri' not in local_var_params or
                local_var_params['uri'] is None):
            raise ApiValueError("Missing the required parameter `uri` when calling `create_poster_export_job`")  # noqa: E501
        # verify the required parameter 'service' is set
        if ('service' not in local_var_params or
                local_var_params['service'] is None):
            raise ApiValueError("Missing the required parameter `service` when calling `create_poster_export_job`")  # noqa: E501
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `create_poster_export_job`")  # noqa: E501
        # verify the required parameter 'time' is set
        if ('time' not in local_var_params or
                local_var_params['time'] is None):
            raise ApiValueError("Missing the required parameter `time` when calling `create_poster_export_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service' in local_var_params:
            path_params['service'] = local_var_params['service']  # noqa: E501
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501
        if 'time' in local_var_params:
            path_params['time'] = local_var_params['time']  # noqa: E501

        query_params = []
        if 'jobmetadata' in local_var_params:
            query_params.append(('jobmetadata', local_var_params['jobmetadata']))  # noqa: E501
            collection_formats['jobmetadata'] = 'multi'  # noqa: E501
        if 'notification_data' in local_var_params:
            query_params.append(('notificationData', local_var_params['notification_data']))  # noqa: E501
        if 'format' in local_var_params:
            query_params.append(('format', local_var_params['format']))  # noqa: E501
        if 'uri' in local_var_params:
            query_params.append(('uri', local_var_params['uri']))  # noqa: E501
        if 'notification' in local_var_params:
            query_params.append(('notification', local_var_params['notification']))  # noqa: E501
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
            '/poster/{service}/{item-id}/{time}/export', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_poster(self, service, item_id, time, **kwargs):  # noqa: E501
        """Delete a thumbnail  # noqa: E501

        Remove this thumbnail.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_poster(service, item_id, time, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str service: The service. (required)
        :param str item_id: The item id. (required)
        :param str time: The time. (required)
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
        return self.delete_poster_with_http_info(service, item_id, time, **kwargs)  # noqa: E501

    def delete_poster_with_http_info(self, service, item_id, time, **kwargs):  # noqa: E501
        """Delete a thumbnail  # noqa: E501

        Remove this thumbnail.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_poster_with_http_info(service, item_id, time, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str service: The service. (required)
        :param str item_id: The item id. (required)
        :param str time: The time. (required)
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

        all_params = ['service', 'item_id', 'time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_poster" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'service' is set
        if ('service' not in local_var_params or
                local_var_params['service'] is None):
            raise ApiValueError("Missing the required parameter `service` when calling `delete_poster`")  # noqa: E501
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `delete_poster`")  # noqa: E501
        # verify the required parameter 'time' is set
        if ('time' not in local_var_params or
                local_var_params['time'] is None):
            raise ApiValueError("Missing the required parameter `time` when calling `delete_poster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service' in local_var_params:
            path_params['service'] = local_var_params['service']  # noqa: E501
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501
        if 'time' in local_var_params:
            path_params['time'] = local_var_params['time']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/poster/{service}/{item-id}/{time}', 'DELETE',
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

    def delete_posters(self, service, item_id, **kwargs):  # noqa: E501
        """Delete all thumbnails  # noqa: E501

        Remove all thumbnails handled by this resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_posters(service, item_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str service: The service. (required)
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
        return self.delete_posters_with_http_info(service, item_id, **kwargs)  # noqa: E501

    def delete_posters_with_http_info(self, service, item_id, **kwargs):  # noqa: E501
        """Delete all thumbnails  # noqa: E501

        Remove all thumbnails handled by this resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_posters_with_http_info(service, item_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str service: The service. (required)
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

        all_params = ['service', 'item_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_posters" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'service' is set
        if ('service' not in local_var_params or
                local_var_params['service'] is None):
            raise ApiValueError("Missing the required parameter `service` when calling `delete_posters`")  # noqa: E501
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `delete_posters`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service' in local_var_params:
            path_params['service'] = local_var_params['service']  # noqa: E501
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
            '/poster/{service}/{item-id}', 'DELETE',
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

    def get_poster(self, service, item_id, time, **kwargs):  # noqa: E501
        """Retrieve the image representation  # noqa: E501

        Return the image representation of this thumbnail.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_poster(service, item_id, time, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str service: The service. (required)
        :param str item_id: The item id. (required)
        :param str time: The time. (required)
        :key str hash: The checksum of the image.
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: file.
                 If the method is called asynchronously, returns the request thread.
        :rtype: file or multiprocessing.pool.AsyncResult
        """
        kwargs['_return_http_data_only'] = True
        return self.get_poster_with_http_info(service, item_id, time, **kwargs)  # noqa: E501

    def get_poster_with_http_info(self, service, item_id, time, **kwargs):  # noqa: E501
        """Retrieve the image representation  # noqa: E501

        Return the image representation of this thumbnail.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_poster_with_http_info(service, item_id, time, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str service: The service. (required)
        :param str item_id: The item id. (required)
        :param str time: The time. (required)
        :key str hash: The checksum of the image.
        :key _return_http_data_only: response data without head status code
                                       and headers
        :key _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :key _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(file, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['service', 'item_id', 'time', 'hash']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_poster" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'service' is set
        if ('service' not in local_var_params or
                local_var_params['service'] is None):
            raise ApiValueError("Missing the required parameter `service` when calling `get_poster`")  # noqa: E501
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `get_poster`")  # noqa: E501
        # verify the required parameter 'time' is set
        if ('time' not in local_var_params or
                local_var_params['time'] is None):
            raise ApiValueError("Missing the required parameter `time` when calling `get_poster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service' in local_var_params:
            path_params['service'] = local_var_params['service']  # noqa: E501
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501
        if 'time' in local_var_params:
            path_params['time'] = local_var_params['time']  # noqa: E501

        query_params = []
        if 'hash' in local_var_params:
            query_params.append(('hash', local_var_params['hash']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['image/png', 'image/jpeg'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/poster/{service}/{item-id}/{time}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_posters(self, service, item_id, **kwargs):  # noqa: E501
        """List all thumbnails  # noqa: E501

        Returns thumbnail URIs on which further requests may be performed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_posters(service, item_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str service: The service. (required)
        :param str item_id: The item id. (required)
        :key bool noauth_url: - `true` Return URIs that do not need authentication.  - `false` (default) Return normal URIs
        :key bool url: - `true` - Return list of URLs.  - `false` (default) - Return list of ids.
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
        return self.get_posters_with_http_info(service, item_id, **kwargs)  # noqa: E501

    def get_posters_with_http_info(self, service, item_id, **kwargs):  # noqa: E501
        """List all thumbnails  # noqa: E501

        Returns thumbnail URIs on which further requests may be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_posters_with_http_info(service, item_id, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str service: The service. (required)
        :param str item_id: The item id. (required)
        :key bool noauth_url: - `true` Return URIs that do not need authentication.  - `false` (default) Return normal URIs
        :key bool url: - `true` - Return list of URLs.  - `false` (default) - Return list of ids.
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

        all_params = ['service', 'item_id', 'noauth_url', 'url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_posters" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'service' is set
        if ('service' not in local_var_params or
                local_var_params['service'] is None):
            raise ApiValueError("Missing the required parameter `service` when calling `get_posters`")  # noqa: E501
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `get_posters`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service' in local_var_params:
            path_params['service'] = local_var_params['service']  # noqa: E501
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501

        query_params = []
        if 'noauth_url' in local_var_params:
            query_params.append(('noauth-url', local_var_params['noauth_url']))  # noqa: E501
        if 'url' in local_var_params:
            query_params.append(('url', local_var_params['url']))  # noqa: E501

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
            '/poster/{service}/{item-id}', 'GET',
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

    def update_or_create_poster(self, service, item_id, time, body, **kwargs):  # noqa: E501
        """Update or create a thumbnail  # noqa: E501

        Create a new thumbnail at the specified time code. If a thumbnail with the specified time code already exists it is replaced.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_or_create_poster(service, item_id, time, body, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str service: The service. (required)
        :param str item_id: The item id. (required)
        :param str time: The time. (required)
        :param file body: Image to insert (required)
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
        return self.update_or_create_poster_with_http_info(service, item_id, time, body, **kwargs)  # noqa: E501

    def update_or_create_poster_with_http_info(self, service, item_id, time, body, **kwargs):  # noqa: E501
        """Update or create a thumbnail  # noqa: E501

        Create a new thumbnail at the specified time code. If a thumbnail with the specified time code already exists it is replaced.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_or_create_poster_with_http_info(service, item_id, time, body, async_req=True)
        >>> result = thread.get()

        :key bool async_req: execute request asynchronously
        :param str service: The service. (required)
        :param str item_id: The item id. (required)
        :param str time: The time. (required)
        :param file body: Image to insert (required)
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

        all_params = ['service', 'item_id', 'time', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_or_create_poster" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'service' is set
        if ('service' not in local_var_params or
                local_var_params['service'] is None):
            raise ApiValueError("Missing the required parameter `service` when calling `update_or_create_poster`")  # noqa: E501
        # verify the required parameter 'item_id' is set
        if ('item_id' not in local_var_params or
                local_var_params['item_id'] is None):
            raise ApiValueError("Missing the required parameter `item_id` when calling `update_or_create_poster`")  # noqa: E501
        # verify the required parameter 'time' is set
        if ('time' not in local_var_params or
                local_var_params['time'] is None):
            raise ApiValueError("Missing the required parameter `time` when calling `update_or_create_poster`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in local_var_params or
                local_var_params['body'] is None):
            raise ApiValueError("Missing the required parameter `body` when calling `update_or_create_poster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service' in local_var_params:
            path_params['service'] = local_var_params['service']  # noqa: E501
        if 'item_id' in local_var_params:
            path_params['item-id'] = local_var_params['item_id']  # noqa: E501
        if 'time' in local_var_params:
            path_params['time'] = local_var_params['time']  # noqa: E501

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
            ['image/png', 'image/jpeg'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/poster/{service}/{item-id}/{time}', 'PUT',
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
