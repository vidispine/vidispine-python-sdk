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

class BaseMediaInfoType(object):
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
        'bit_rate_mode': 'str',
        '_property': 'list[KeyValuePairType]',
        'source': 'str'
    }

    attribute_map = {
        'bit_rate_mode': 'Bit_rate_mode',
        '_property': 'property',
        'source': 'Source'
    }

    def __init__(self, bit_rate_mode=None, _property=None, source=None):  # noqa: E501
        """BaseMediaInfoType - a model defined in OpenAPI"""  # noqa: E501

        self._bit_rate_mode = None
        self.__property = None
        self._source = None
        self.discriminator = None

        if bit_rate_mode is not None:
            self.bit_rate_mode = bit_rate_mode
        if _property is not None:
            self._property = _property
        if source is not None:
            self.source = source

    @property
    def bit_rate_mode(self):
        """Gets the bit_rate_mode of this BaseMediaInfoType.  # noqa: E501


        :return: The bit_rate_mode of this BaseMediaInfoType.  # noqa: E501
        :rtype: str
        """
        return self._bit_rate_mode

    @bit_rate_mode.setter
    def bit_rate_mode(self, bit_rate_mode):
        """Sets the bit_rate_mode of this BaseMediaInfoType.


        :param bit_rate_mode: The bit_rate_mode of this BaseMediaInfoType.  # noqa: E501
        :type: str
        """

        self._bit_rate_mode = bit_rate_mode

    @property
    def _property(self):
        """Gets the _property of this BaseMediaInfoType.  # noqa: E501


        :return: The _property of this BaseMediaInfoType.  # noqa: E501
        :rtype: list[KeyValuePairType]
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this BaseMediaInfoType.


        :param _property: The _property of this BaseMediaInfoType.  # noqa: E501
        :type: list[KeyValuePairType]
        """

        self.__property = _property

    @property
    def source(self):
        """Gets the source of this BaseMediaInfoType.  # noqa: E501


        :return: The source of this BaseMediaInfoType.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BaseMediaInfoType.


        :param source: The source of this BaseMediaInfoType.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if not isinstance(other, BaseMediaInfoType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other