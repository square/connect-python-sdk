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


from pprint import pformat
from six import iteritems
import re


class BatchRetrieveInventoryChangesRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, catalog_object_ids=None, location_ids=None, types=None, states=None, updated_after=None, updated_before=None, cursor=None):
        """
        BatchRetrieveInventoryChangesRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'catalog_object_ids': 'list[str]',
            'location_ids': 'list[str]',
            'types': 'list[str]',
            'states': 'list[str]',
            'updated_after': 'str',
            'updated_before': 'str',
            'cursor': 'str'
        }

        self.attribute_map = {
            'catalog_object_ids': 'catalog_object_ids',
            'location_ids': 'location_ids',
            'types': 'types',
            'states': 'states',
            'updated_after': 'updated_after',
            'updated_before': 'updated_before',
            'cursor': 'cursor'
        }

        self._catalog_object_ids = catalog_object_ids
        self._location_ids = location_ids
        self._types = types
        self._states = states
        self._updated_after = updated_after
        self._updated_before = updated_before
        self._cursor = cursor

    @property
    def catalog_object_ids(self):
        """
        Gets the catalog_object_ids of this BatchRetrieveInventoryChangesRequest.
        Filters results by [CatalogObject](#type-catalogobject) ID. Only applied when set. Default: unset.

        :return: The catalog_object_ids of this BatchRetrieveInventoryChangesRequest.
        :rtype: list[str]
        """
        return self._catalog_object_ids

    @catalog_object_ids.setter
    def catalog_object_ids(self, catalog_object_ids):
        """
        Sets the catalog_object_ids of this BatchRetrieveInventoryChangesRequest.
        Filters results by [CatalogObject](#type-catalogobject) ID. Only applied when set. Default: unset.

        :param catalog_object_ids: The catalog_object_ids of this BatchRetrieveInventoryChangesRequest.
        :type: list[str]
        """

        self._catalog_object_ids = catalog_object_ids

    @property
    def location_ids(self):
        """
        Gets the location_ids of this BatchRetrieveInventoryChangesRequest.
        Filters results by [Location](#type-location) ID. Only applied when set. Default: unset.

        :return: The location_ids of this BatchRetrieveInventoryChangesRequest.
        :rtype: list[str]
        """
        return self._location_ids

    @location_ids.setter
    def location_ids(self, location_ids):
        """
        Sets the location_ids of this BatchRetrieveInventoryChangesRequest.
        Filters results by [Location](#type-location) ID. Only applied when set. Default: unset.

        :param location_ids: The location_ids of this BatchRetrieveInventoryChangesRequest.
        :type: list[str]
        """

        self._location_ids = location_ids

    @property
    def types(self):
        """
        Gets the types of this BatchRetrieveInventoryChangesRequest.
        Filters results by [InventoryChangeType](#type-inventorychangetype). Default: [`PHYSICAL_COUNT`, `ADJUSTMENT`]. `TRANSFER` is not supported as a filter.

        :return: The types of this BatchRetrieveInventoryChangesRequest.
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this BatchRetrieveInventoryChangesRequest.
        Filters results by [InventoryChangeType](#type-inventorychangetype). Default: [`PHYSICAL_COUNT`, `ADJUSTMENT`]. `TRANSFER` is not supported as a filter.

        :param types: The types of this BatchRetrieveInventoryChangesRequest.
        :type: list[str]
        """

        self._types = types

    @property
    def states(self):
        """
        Gets the states of this BatchRetrieveInventoryChangesRequest.
        Filters `ADJUSTMENT` query results by [InventoryState](#type-inventorystate). Only applied when set. Default: unset.

        :return: The states of this BatchRetrieveInventoryChangesRequest.
        :rtype: list[str]
        """
        return self._states

    @states.setter
    def states(self, states):
        """
        Sets the states of this BatchRetrieveInventoryChangesRequest.
        Filters `ADJUSTMENT` query results by [InventoryState](#type-inventorystate). Only applied when set. Default: unset.

        :param states: The states of this BatchRetrieveInventoryChangesRequest.
        :type: list[str]
        """

        self._states = states

    @property
    def updated_after(self):
        """
        Gets the updated_after of this BatchRetrieveInventoryChangesRequest.
        Provided as an RFC 3339 timestamp. Returns results whose `created_at` or `calculated_at` value is after the given time. Default: UNIX epoch (`1970-01-01T00:00:00Z`).

        :return: The updated_after of this BatchRetrieveInventoryChangesRequest.
        :rtype: str
        """
        return self._updated_after

    @updated_after.setter
    def updated_after(self, updated_after):
        """
        Sets the updated_after of this BatchRetrieveInventoryChangesRequest.
        Provided as an RFC 3339 timestamp. Returns results whose `created_at` or `calculated_at` value is after the given time. Default: UNIX epoch (`1970-01-01T00:00:00Z`).

        :param updated_after: The updated_after of this BatchRetrieveInventoryChangesRequest.
        :type: str
        """

        self._updated_after = updated_after

    @property
    def updated_before(self):
        """
        Gets the updated_before of this BatchRetrieveInventoryChangesRequest.
        Provided as an RFC 3339 timestamp. Returns results whose `created_at` or `calculated_at` value is strictly before the given time. Default: UNIX epoch (`1970-01-01T00:00:00Z`).

        :return: The updated_before of this BatchRetrieveInventoryChangesRequest.
        :rtype: str
        """
        return self._updated_before

    @updated_before.setter
    def updated_before(self, updated_before):
        """
        Sets the updated_before of this BatchRetrieveInventoryChangesRequest.
        Provided as an RFC 3339 timestamp. Returns results whose `created_at` or `calculated_at` value is strictly before the given time. Default: UNIX epoch (`1970-01-01T00:00:00Z`).

        :param updated_before: The updated_before of this BatchRetrieveInventoryChangesRequest.
        :type: str
        """

        self._updated_before = updated_before

    @property
    def cursor(self):
        """
        Gets the cursor of this BatchRetrieveInventoryChangesRequest.
        A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See [Paginating results](#paginatingresults) for more information.

        :return: The cursor of this BatchRetrieveInventoryChangesRequest.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this BatchRetrieveInventoryChangesRequest.
        A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See [Paginating results](#paginatingresults) for more information.

        :param cursor: The cursor of this BatchRetrieveInventoryChangesRequest.
        :type: str
        """

        self._cursor = cursor

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other