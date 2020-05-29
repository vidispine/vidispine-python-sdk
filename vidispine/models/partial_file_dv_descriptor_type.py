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

class PartialFileDVDescriptorType(object):
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
        'frame_size': 'int',
        'frame_count': 'int'
    }

    attribute_map = {
        'frame_size': 'frameSize',
        'frame_count': 'frameCount'
    }

    def __init__(self, frame_size=None, frame_count=None):  # noqa: E501
        """PartialFileDVDescriptorType - a model defined in OpenAPI"""  # noqa: E501

        self._frame_size = None
        self._frame_count = None
        self.discriminator = None

        self.frame_size = frame_size
        self.frame_count = frame_count

    @property
    def frame_size(self):
        """Gets the frame_size of this PartialFileDVDescriptorType.  # noqa: E501


        :return: The frame_size of this PartialFileDVDescriptorType.  # noqa: E501
        :rtype: int
        """
        return self._frame_size

    @frame_size.setter
    def frame_size(self, frame_size):
        """Sets the frame_size of this PartialFileDVDescriptorType.


        :param frame_size: The frame_size of this PartialFileDVDescriptorType.  # noqa: E501
        :type: int
        """
        if frame_size is None:
            raise ValueError("Invalid value for `frame_size`, must not be `None`")  # noqa: E501

        self._frame_size = frame_size

    @property
    def frame_count(self):
        """Gets the frame_count of this PartialFileDVDescriptorType.  # noqa: E501


        :return: The frame_count of this PartialFileDVDescriptorType.  # noqa: E501
        :rtype: int
        """
        return self._frame_count

    @frame_count.setter
    def frame_count(self, frame_count):
        """Sets the frame_count of this PartialFileDVDescriptorType.


        :param frame_count: The frame_count of this PartialFileDVDescriptorType.  # noqa: E501
        :type: int
        """
        if frame_count is None:
            raise ValueError("Invalid value for `frame_count`, must not be `None`")  # noqa: E501

        self._frame_count = frame_count

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
        if not isinstance(other, PartialFileDVDescriptorType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
