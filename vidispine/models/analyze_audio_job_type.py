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

class AnalyzeAudioJobType(object):
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
        'otif': 'list[OtifPresetType]'
    }

    attribute_map = {
        'otif': 'otif'
    }

    def __init__(self, otif=None):  # noqa: E501
        """AnalyzeAudioJobType - a model defined in OpenAPI"""  # noqa: E501

        self._otif = None
        self.discriminator = None

        if otif is not None:
            self.otif = otif

    @property
    def otif(self):
        """Gets the otif of this AnalyzeAudioJobType.  # noqa: E501


        :return: The otif of this AnalyzeAudioJobType.  # noqa: E501
        :rtype: list[OtifPresetType]
        """
        return self._otif

    @otif.setter
    def otif(self, otif):
        """Sets the otif of this AnalyzeAudioJobType.


        :param otif: The otif of this AnalyzeAudioJobType.  # noqa: E501
        :type: list[OtifPresetType]
        """

        self._otif = otif

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
        if not isinstance(other, AnalyzeAudioJobType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
