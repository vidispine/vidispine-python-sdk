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

class FacetRangeType(object):
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
        'start': 'str',
        'integerorempty': 'str',
        'end': 'str'
    }

    attribute_map = {
        'start': 'start',
        'integerorempty': 'integerorempty',
        'end': 'end'
    }

    def __init__(self, start=None, integerorempty=None, end=None):  # noqa: E501
        """FacetRangeType - a model defined in OpenAPI"""  # noqa: E501

        self._start = None
        self._integerorempty = None
        self._end = None
        self.discriminator = None

        self.start = start
        if integerorempty is not None:
            self.integerorempty = integerorempty
        self.end = end

    @property
    def start(self):
        """Gets the start of this FacetRangeType.  # noqa: E501


        :return: The start of this FacetRangeType.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this FacetRangeType.


        :param start: The start of this FacetRangeType.  # noqa: E501
        :type: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def integerorempty(self):
        """Gets the integerorempty of this FacetRangeType.  # noqa: E501


        :return: The integerorempty of this FacetRangeType.  # noqa: E501
        :rtype: str
        """
        return self._integerorempty

    @integerorempty.setter
    def integerorempty(self, integerorempty):
        """Sets the integerorempty of this FacetRangeType.


        :param integerorempty: The integerorempty of this FacetRangeType.  # noqa: E501
        :type: str
        """
        if integerorempty is not None and not re.search(r'[0-9]{0,40}', integerorempty):  # noqa: E501
            raise ValueError(r"Invalid value for `integerorempty`, must be a follow pattern or equal to `/[0-9]{0,40}/`")  # noqa: E501

        self._integerorempty = integerorempty

    @property
    def end(self):
        """Gets the end of this FacetRangeType.  # noqa: E501


        :return: The end of this FacetRangeType.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this FacetRangeType.


        :param end: The end of this FacetRangeType.  # noqa: E501
        :type: str
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501

        self._end = end

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
        if not isinstance(other, FacetRangeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
