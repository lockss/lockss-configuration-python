# coding: utf-8

"""
    LOCKSS Configuration Service REST API

    API of the LOCKSS Configuration REST Service  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: lockss-support@lockss.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lockss_configuration.api_client import ApiClient


class AusApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_au_config(self, auid, **kwargs):  # noqa: E501
        """Delete the the configuration of an AU  # noqa: E501

        Delete the configuration of an AU given the AU identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_au_config(auid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auid: The identifier of the AU for which the configuration is\\ \\ to be deleted (required)
        :return: ConfigExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_au_config_with_http_info(auid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_au_config_with_http_info(auid, **kwargs)  # noqa: E501
            return data

    def delete_au_config_with_http_info(self, auid, **kwargs):  # noqa: E501
        """Delete the the configuration of an AU  # noqa: E501

        Delete the configuration of an AU given the AU identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_au_config_with_http_info(auid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auid: The identifier of the AU for which the configuration is\\ \\ to be deleted (required)
        :return: ConfigExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_au_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auid' is set
        if ('auid' not in params or
                params['auid'] is None):
            raise ValueError("Missing the required parameter `auid` when calling `delete_au_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auid' in params:
            path_params['auid'] = params['auid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/aus/{auid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigExchange',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_au_config(self, **kwargs):  # noqa: E501
        """Get the configurations of all AUs  # noqa: E501

        Get the configuration of all AUs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_au_config(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ConfigExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_au_config_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_au_config_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_au_config_with_http_info(self, **kwargs):  # noqa: E501
        """Get the configurations of all AUs  # noqa: E501

        Get the configuration of all AUs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_au_config_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ConfigExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_au_config" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/aus', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigExchange',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_au_config(self, auid, **kwargs):  # noqa: E501
        """Get the configuration of an AU  # noqa: E501

        Get the configuration of an AU given the AU identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_au_config(auid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auid: The identifier of the AU for which the configuration is\\ \\ requested (required)
        :return: ConfigExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_au_config_with_http_info(auid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_au_config_with_http_info(auid, **kwargs)  # noqa: E501
            return data

    def get_au_config_with_http_info(self, auid, **kwargs):  # noqa: E501
        """Get the configuration of an AU  # noqa: E501

        Get the configuration of an AU given the AU identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_au_config_with_http_info(auid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auid: The identifier of the AU for which the configuration is\\ \\ requested (required)
        :return: ConfigExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_au_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auid' is set
        if ('auid' not in params or
                params['auid'] is None):
            raise ValueError("Missing the required parameter `auid` when calling `get_au_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auid' in params:
            path_params['auid'] = params['auid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/aus/{auid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigExchange',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_au_config(self, auid, config_exchange, **kwargs):  # noqa: E501
        """Store the configuration of an AU  # noqa: E501

        Store the configuration of an AU given the AU identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_au_config(auid, config_exchange, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auid: The identifier of the AU for which the configuration is\\ \\ to be stored (required)
        :param ConfigExchange config_exchange: The configuration items to be stored (required)
        :return: ConfigExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.put_au_config_with_http_info(auid, config_exchange, **kwargs)  # noqa: E501
        else:
            (data) = self.put_au_config_with_http_info(auid, config_exchange, **kwargs)  # noqa: E501
            return data

    def put_au_config_with_http_info(self, auid, config_exchange, **kwargs):  # noqa: E501
        """Store the configuration of an AU  # noqa: E501

        Store the configuration of an AU given the AU identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.put_au_config_with_http_info(auid, config_exchange, async=True)
        >>> result = thread.get()

        :param async bool
        :param str auid: The identifier of the AU for which the configuration is\\ \\ to be stored (required)
        :param ConfigExchange config_exchange: The configuration items to be stored (required)
        :return: ConfigExchange
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['auid', 'config_exchange']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_au_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'auid' is set
        if ('auid' not in params or
                params['auid'] is None):
            raise ValueError("Missing the required parameter `auid` when calling `put_au_config`")  # noqa: E501
        # verify the required parameter 'config_exchange' is set
        if ('config_exchange' not in params or
                params['config_exchange'] is None):
            raise ValueError("Missing the required parameter `config_exchange` when calling `put_au_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auid' in params:
            path_params['auid'] = params['auid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'config_exchange' in params:
            body_params = params['config_exchange']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/aus/{auid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigExchange',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
