# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class InventoryApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def batch_change_inventory(self, body, **kwargs):
        """
        BatchChangeInventory
        Applies adjustments and counts to the provided item quantities.  On success: returns the current calculated counts for all objects referenced in the request. On failure: returns a list of related errors.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.batch_change_inventory(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BatchChangeInventoryRequest body: An object containing the fields to POST for the request.  See the corresponding object definition for field details. (required)
        :return: BatchChangeInventoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_change_inventory" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `batch_change_inventory`")


        resource_path = '/v2/inventory/batch-change'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        header_params['Square-Version'] = "2019-06-12"
        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BatchChangeInventoryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def batch_retrieve_inventory_changes(self, body, **kwargs):
        """
        BatchRetrieveInventoryChanges
        Returns historical physical counts and adjustments based on the provided filter criteria.  Results are paginated and sorted in ascending order according their `occurred_at` timestamp (oldest first).  BatchRetrieveInventoryChanges is a catch-all query endpoint for queries that cannot be handled by other, simpler endpoints.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.batch_retrieve_inventory_changes(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BatchRetrieveInventoryChangesRequest body: An object containing the fields to POST for the request.  See the corresponding object definition for field details. (required)
        :return: BatchRetrieveInventoryChangesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_retrieve_inventory_changes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `batch_retrieve_inventory_changes`")


        resource_path = '/v2/inventory/batch-retrieve-changes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        header_params['Square-Version'] = "2019-06-12"
        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BatchRetrieveInventoryChangesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def batch_retrieve_inventory_counts(self, body, **kwargs):
        """
        BatchRetrieveInventoryCounts
        Returns current counts for the provided [CatalogObject](#type-catalogobject)s at the requested [Location](#type-location)s.  Results are paginated and sorted in descending order according to their `calculated_at` timestamp (newest first).  When `updated_after` is specified, only counts that have changed since that time (based on the server timestamp for the most recent change) are returned. This allows clients to perform a \"sync\" operation, for example in response to receiving a Webhook notification.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.batch_retrieve_inventory_counts(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BatchRetrieveInventoryCountsRequest body: An object containing the fields to POST for the request.  See the corresponding object definition for field details. (required)
        :return: BatchRetrieveInventoryCountsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_retrieve_inventory_counts" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `batch_retrieve_inventory_counts`")


        resource_path = '/v2/inventory/batch-retrieve-counts'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        header_params['Square-Version'] = "2019-06-12"
        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BatchRetrieveInventoryCountsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def retrieve_inventory_adjustment(self, adjustment_id, **kwargs):
        """
        RetrieveInventoryAdjustment
        Returns the [InventoryAdjustment](#type-inventoryadjustment) object with the provided `adjustment_id`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retrieve_inventory_adjustment(adjustment_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str adjustment_id: ID of the [InventoryAdjustment](#type-inventoryadjustment) to retrieve. (required)
        :return: RetrieveInventoryAdjustmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['adjustment_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_inventory_adjustment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'adjustment_id' is set
        if ('adjustment_id' not in params) or (params['adjustment_id'] is None):
            raise ValueError("Missing the required parameter `adjustment_id` when calling `retrieve_inventory_adjustment`")


        resource_path = '/v2/inventory/adjustment/{adjustment_id}'.replace('{format}', 'json')
        path_params = {}
        if 'adjustment_id' in params:
            path_params['adjustment_id'] = params['adjustment_id']

        query_params = {}

        header_params = {}
        header_params['Square-Version'] = "2019-06-12"
        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RetrieveInventoryAdjustmentResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def retrieve_inventory_changes(self, catalog_object_id, **kwargs):
        """
        RetrieveInventoryChanges
        Returns a set of physical counts and inventory adjustments for the provided [CatalogObject](#type-catalogobject) at the requested [Location](#type-location)s.  Results are paginated and sorted in descending order according to their `occurred_at` timestamp (newest first).  There are no limits on how far back the caller can page. This endpoint is useful when displaying recent changes for a specific item. For more sophisticated queries, use a batch endpoint.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retrieve_inventory_changes(catalog_object_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str catalog_object_id: ID of the [CatalogObject](#type-catalogobject) to retrieve. (required)
        :param str location_ids: The [Location](#type-location) IDs to look up as a comma-separated list. An empty list queries all locations.
        :param str cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See [Pagination](/basics/api101/pagination) for more information.
        :return: RetrieveInventoryChangesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_object_id', 'location_ids', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_inventory_changes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'catalog_object_id' is set
        if ('catalog_object_id' not in params) or (params['catalog_object_id'] is None):
            raise ValueError("Missing the required parameter `catalog_object_id` when calling `retrieve_inventory_changes`")


        resource_path = '/v2/inventory/{catalog_object_id}/changes'.replace('{format}', 'json')
        path_params = {}
        if 'catalog_object_id' in params:
            path_params['catalog_object_id'] = params['catalog_object_id']

        query_params = {}
        if 'location_ids' in params and params['location_ids'] is not None:
            query_params['location_ids'] = params['location_ids']
        if 'cursor' in params and params['cursor'] is not None:
            query_params['cursor'] = params['cursor']

        header_params = {}
        header_params['Square-Version'] = "2019-06-12"
        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RetrieveInventoryChangesResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def retrieve_inventory_count(self, catalog_object_id, **kwargs):
        """
        RetrieveInventoryCount
        Retrieves the current calculated stock count for a given [CatalogObject](#type-catalogobject) at a given set of [Location](#type-location)s. Responses are paginated and unsorted. For more sophisticated queries, use a batch endpoint.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retrieve_inventory_count(catalog_object_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str catalog_object_id: ID of the [CatalogObject](#type-catalogobject) to retrieve. (required)
        :param str location_ids: The [Location](#type-location) IDs to look up as a comma-separated list. An empty list queries all locations.
        :param str cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See [Pagination](/basics/api101/pagination) for more information.
        :return: RetrieveInventoryCountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_object_id', 'location_ids', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_inventory_count" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'catalog_object_id' is set
        if ('catalog_object_id' not in params) or (params['catalog_object_id'] is None):
            raise ValueError("Missing the required parameter `catalog_object_id` when calling `retrieve_inventory_count`")


        resource_path = '/v2/inventory/{catalog_object_id}'.replace('{format}', 'json')
        path_params = {}
        if 'catalog_object_id' in params:
            path_params['catalog_object_id'] = params['catalog_object_id']

        query_params = {}
        if 'location_ids' in params and params['location_ids'] is not None:
            query_params['location_ids'] = params['location_ids']
        if 'cursor' in params and params['cursor'] is not None:
            query_params['cursor'] = params['cursor']

        header_params = {}
        header_params['Square-Version'] = "2019-06-12"
        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RetrieveInventoryCountResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def retrieve_inventory_physical_count(self, physical_count_id, **kwargs):
        """
        RetrieveInventoryPhysicalCount
        Returns the [InventoryPhysicalCount](#type-inventoryphysicalcount) object with the provided `physical_count_id`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retrieve_inventory_physical_count(physical_count_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str physical_count_id: ID of the [InventoryPhysicalCount](#type-inventoryphysicalcount) to retrieve. (required)
        :return: RetrieveInventoryPhysicalCountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['physical_count_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_inventory_physical_count" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'physical_count_id' is set
        if ('physical_count_id' not in params) or (params['physical_count_id'] is None):
            raise ValueError("Missing the required parameter `physical_count_id` when calling `retrieve_inventory_physical_count`")


        resource_path = '/v2/inventory/physical-count/{physical_count_id}'.replace('{format}', 'json')
        path_params = {}
        if 'physical_count_id' in params:
            path_params['physical_count_id'] = params['physical_count_id']

        query_params = {}

        header_params = {}
        header_params['Square-Version'] = "2019-06-12"
        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RetrieveInventoryPhysicalCountResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        
