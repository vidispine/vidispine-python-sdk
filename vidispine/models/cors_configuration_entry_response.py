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

class CORSConfigurationEntryResponse(object):
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
        'allow_headers': 'list[str]',
        'allow_origin': 'str',
        'allow_methods': 'list[str]',
        'allow_other_header': 'list[KeyValuePairType]',
        'allow_max_age': 'int'
    }

    attribute_map = {
        'allow_headers': 'allowHeaders',
        'allow_origin': 'allowOrigin',
        'allow_methods': 'allowMethods',
        'allow_other_header': 'allowOtherHeader',
        'allow_max_age': 'allowMaxAge'
    }

    def __init__(self, allow_headers=None, allow_origin=None, allow_methods=None, allow_other_header=None, allow_max_age=None):  # noqa: E501
        """CORSConfigurationEntryResponse - a model defined in OpenAPI"""  # noqa: E501

        self._allow_headers = None
        self._allow_origin = None
        self._allow_methods = None
        self._allow_other_header = None
        self._allow_max_age = None
        self.discriminator = None

        if allow_headers is not None:
            self.allow_headers = allow_headers
        self.allow_origin = allow_origin
        if allow_methods is not None:
            self.allow_methods = allow_methods
        if allow_other_header is not None:
            self.allow_other_header = allow_other_header
        if allow_max_age is not None:
            self.allow_max_age = allow_max_age

    @property
    def allow_headers(self):
        """Gets the allow_headers of this CORSConfigurationEntryResponse.  # noqa: E501


        :return: The allow_headers of this CORSConfigurationEntryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._allow_headers

    @allow_headers.setter
    def allow_headers(self, allow_headers):
        """Sets the allow_headers of this CORSConfigurationEntryResponse.


        :param allow_headers: The allow_headers of this CORSConfigurationEntryResponse.  # noqa: E501
        :type: list[str]
        """

        self._allow_headers = allow_headers

    @property
    def allow_origin(self):
        """Gets the allow_origin of this CORSConfigurationEntryResponse.  # noqa: E501


        :return: The allow_origin of this CORSConfigurationEntryResponse.  # noqa: E501
        :rtype: str
        """
        return self._allow_origin

    @allow_origin.setter
    def allow_origin(self, allow_origin):
        """Sets the allow_origin of this CORSConfigurationEntryResponse.


        :param allow_origin: The allow_origin of this CORSConfigurationEntryResponse.  # noqa: E501
        :type: str
        """
        if allow_origin is None:
            raise ValueError("Invalid value for `allow_origin`, must not be `None`")  # noqa: E501

        self._allow_origin = allow_origin

    @property
    def allow_methods(self):
        """Gets the allow_methods of this CORSConfigurationEntryResponse.  # noqa: E501


        :return: The allow_methods of this CORSConfigurationEntryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._allow_methods

    @allow_methods.setter
    def allow_methods(self, allow_methods):
        """Sets the allow_methods of this CORSConfigurationEntryResponse.


        :param allow_methods: The allow_methods of this CORSConfigurationEntryResponse.  # noqa: E501
        :type: list[str]
        """

        self._allow_methods = allow_methods

    @property
    def allow_other_header(self):
        """Gets the allow_other_header of this CORSConfigurationEntryResponse.  # noqa: E501


        :return: The allow_other_header of this CORSConfigurationEntryResponse.  # noqa: E501
        :rtype: list[KeyValuePairType]
        """
        return self._allow_other_header

    @allow_other_header.setter
    def allow_other_header(self, allow_other_header):
        """Sets the allow_other_header of this CORSConfigurationEntryResponse.


        :param allow_other_header: The allow_other_header of this CORSConfigurationEntryResponse.  # noqa: E501
        :type: list[KeyValuePairType]
        """

        self._allow_other_header = allow_other_header

    @property
    def allow_max_age(self):
        """Gets the allow_max_age of this CORSConfigurationEntryResponse.  # noqa: E501


        :return: The allow_max_age of this CORSConfigurationEntryResponse.  # noqa: E501
        :rtype: int
        """
        return self._allow_max_age

    @allow_max_age.setter
    def allow_max_age(self, allow_max_age):
        """Sets the allow_max_age of this CORSConfigurationEntryResponse.


        :param allow_max_age: The allow_max_age of this CORSConfigurationEntryResponse.  # noqa: E501
        :type: int
        """

        self._allow_max_age = allow_max_age

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
        if not isinstance(other, CORSConfigurationEntryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other