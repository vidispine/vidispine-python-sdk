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

class NetworkType(object):
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
        'netmask': 'str',
        'bandwidth': 'int'
    }

    attribute_map = {
        'netmask': 'netmask',
        'bandwidth': 'bandwidth'
    }

    def __init__(self, netmask=None, bandwidth=None):  # noqa: E501
        """NetworkType - a model defined in OpenAPI"""  # noqa: E501

        self._netmask = None
        self._bandwidth = None
        self.discriminator = None

        self.netmask = netmask
        if bandwidth is not None:
            self.bandwidth = bandwidth

    @property
    def netmask(self):
        """Gets the netmask of this NetworkType.  # noqa: E501


        :return: The netmask of this NetworkType.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this NetworkType.


        :param netmask: The netmask of this NetworkType.  # noqa: E501
        :type: str
        """
        if netmask is None:
            raise ValueError("Invalid value for `netmask`, must not be `None`")  # noqa: E501

        self._netmask = netmask

    @property
    def bandwidth(self):
        """Gets the bandwidth of this NetworkType.  # noqa: E501


        :return: The bandwidth of this NetworkType.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this NetworkType.


        :param bandwidth: The bandwidth of this NetworkType.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

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
        if not isinstance(other, NetworkType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other