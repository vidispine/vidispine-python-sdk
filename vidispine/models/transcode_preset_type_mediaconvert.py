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

class TranscodePresetTypeMediaconvert(object):
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
        'output_setting': 'list[str]',
        'other': 'list[str]',
        'input_setting': 'str'
    }

    attribute_map = {
        'output_setting': 'outputSetting',
        'other': 'other',
        'input_setting': 'inputSetting'
    }

    def __init__(self, output_setting=None, other=None, input_setting=None):  # noqa: E501
        """TranscodePresetTypeMediaconvert - a model defined in OpenAPI"""  # noqa: E501

        self._output_setting = None
        self._other = None
        self._input_setting = None
        self.discriminator = None

        if output_setting is not None:
            self.output_setting = output_setting
        if other is not None:
            self.other = other
        if input_setting is not None:
            self.input_setting = input_setting

    @property
    def output_setting(self):
        """Gets the output_setting of this TranscodePresetTypeMediaconvert.  # noqa: E501


        :return: The output_setting of this TranscodePresetTypeMediaconvert.  # noqa: E501
        :rtype: list[str]
        """
        return self._output_setting

    @output_setting.setter
    def output_setting(self, output_setting):
        """Sets the output_setting of this TranscodePresetTypeMediaconvert.


        :param output_setting: The output_setting of this TranscodePresetTypeMediaconvert.  # noqa: E501
        :type: list[str]
        """

        self._output_setting = output_setting

    @property
    def other(self):
        """Gets the other of this TranscodePresetTypeMediaconvert.  # noqa: E501


        :return: The other of this TranscodePresetTypeMediaconvert.  # noqa: E501
        :rtype: list[str]
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this TranscodePresetTypeMediaconvert.


        :param other: The other of this TranscodePresetTypeMediaconvert.  # noqa: E501
        :type: list[str]
        """

        self._other = other

    @property
    def input_setting(self):
        """Gets the input_setting of this TranscodePresetTypeMediaconvert.  # noqa: E501


        :return: The input_setting of this TranscodePresetTypeMediaconvert.  # noqa: E501
        :rtype: str
        """
        return self._input_setting

    @input_setting.setter
    def input_setting(self, input_setting):
        """Sets the input_setting of this TranscodePresetTypeMediaconvert.


        :param input_setting: The input_setting of this TranscodePresetTypeMediaconvert.  # noqa: E501
        :type: str
        """

        self._input_setting = input_setting

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
        if not isinstance(other, TranscodePresetTypeMediaconvert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
