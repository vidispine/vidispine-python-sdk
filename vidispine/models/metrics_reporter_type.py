# coding: utf-8

"""
    Vidispine API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.x
    Contact: info@vidispine.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from . import *

class MetricsReporterType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'exclude': 'list[str]',
        'include': 'list[str]'
    }

    attribute_map = {
        'exclude': 'exclude',
        'include': 'include'
    }

    def __init__(self, exclude=None, include=None):  # noqa: E501
        """MetricsReporterType - a model defined in OpenAPI"""  # noqa: E501

        self._exclude = None
        self._include = None
        self.discriminator = None

        if exclude is not None:
            self.exclude = exclude
        if include is not None:
            self.include = include

    @property
    def exclude(self):
        """Gets the exclude of this MetricsReporterType.  # noqa: E501


        :return: The exclude of this MetricsReporterType.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """Sets the exclude of this MetricsReporterType.


        :param exclude: The exclude of this MetricsReporterType.  # noqa: E501
        :type: list[str]
        """

        self._exclude = exclude

    @property
    def include(self):
        """Gets the include of this MetricsReporterType.  # noqa: E501


        :return: The include of this MetricsReporterType.  # noqa: E501
        :rtype: list[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this MetricsReporterType.


        :param include: The include of this MetricsReporterType.  # noqa: E501
        :type: list[str]
        """

        self._include = include

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetricsReporterType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
