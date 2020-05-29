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

class MetadataFieldStringType(object):
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
        'min_length': 'int',
        'pattern': 'str',
        'max_length': 'int'
    }

    attribute_map = {
        'min_length': 'minLength',
        'pattern': 'pattern',
        'max_length': 'maxLength'
    }

    def __init__(self, min_length=None, pattern=None, max_length=None):  # noqa: E501
        """MetadataFieldStringType - a model defined in OpenAPI"""  # noqa: E501

        self._min_length = None
        self._pattern = None
        self._max_length = None
        self.discriminator = None

        if min_length is not None:
            self.min_length = min_length
        if pattern is not None:
            self.pattern = pattern
        if max_length is not None:
            self.max_length = max_length

    @property
    def min_length(self):
        """Gets the min_length of this MetadataFieldStringType.  # noqa: E501


        :return: The min_length of this MetadataFieldStringType.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this MetadataFieldStringType.


        :param min_length: The min_length of this MetadataFieldStringType.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def pattern(self):
        """Gets the pattern of this MetadataFieldStringType.  # noqa: E501


        :return: The pattern of this MetadataFieldStringType.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this MetadataFieldStringType.


        :param pattern: The pattern of this MetadataFieldStringType.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def max_length(self):
        """Gets the max_length of this MetadataFieldStringType.  # noqa: E501


        :return: The max_length of this MetadataFieldStringType.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this MetadataFieldStringType.


        :param max_length: The max_length of this MetadataFieldStringType.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

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
        if not isinstance(other, MetadataFieldStringType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
