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


class CatalogMeasurementUnit(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, measurement_unit=None, precision=None):
        """
        CatalogMeasurementUnit - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'measurement_unit': 'MeasurementUnit',
            'precision': 'int'
        }

        self.attribute_map = {
            'measurement_unit': 'measurement_unit',
            'precision': 'precision'
        }

        self._measurement_unit = measurement_unit
        self._precision = precision

    @property
    def measurement_unit(self):
        """
        Gets the measurement_unit of this CatalogMeasurementUnit.
        Indicates the unit used to measure the quantity of a catalog item variation.

        :return: The measurement_unit of this CatalogMeasurementUnit.
        :rtype: MeasurementUnit
        """
        return self._measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, measurement_unit):
        """
        Sets the measurement_unit of this CatalogMeasurementUnit.
        Indicates the unit used to measure the quantity of a catalog item variation.

        :param measurement_unit: The measurement_unit of this CatalogMeasurementUnit.
        :type: MeasurementUnit
        """

        self._measurement_unit = measurement_unit

    @property
    def precision(self):
        """
        Gets the precision of this CatalogMeasurementUnit.
         Represents the maximum number of positions allowed after the decimal in quantities measured with this unit. For example, if the precision is 2, then an itemization’s quantity can be 0.01, 0.12, etc.  Min: 0  Max: 5  Default: 3

        :return: The precision of this CatalogMeasurementUnit.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this CatalogMeasurementUnit.
         Represents the maximum number of positions allowed after the decimal in quantities measured with this unit. For example, if the precision is 2, then an itemization’s quantity can be 0.01, 0.12, etc.  Min: 0  Max: 5  Default: 3

        :param precision: The precision of this CatalogMeasurementUnit.
        :type: int
        """

        self._precision = precision

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
