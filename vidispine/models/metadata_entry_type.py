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

class MetadataEntryType(object):
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
        'field': 'MetadataFieldValueType',
        'group': 'MetadataGroupValueType',
        'value': 'MetadataValueType',
        'source': 'MetadataEntryTypeSource'
    }

    attribute_map = {
        'field': 'field',
        'group': 'group',
        'value': 'value',
        'source': 'source'
    }

    def __init__(self, field=None, group=None, value=None, source=None):  # noqa: E501
        """MetadataEntryType - a model defined in OpenAPI"""  # noqa: E501

        self._field = None
        self._group = None
        self._value = None
        self._source = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if group is not None:
            self.group = group
        if value is not None:
            self.value = value
        if source is not None:
            self.source = source

    @property
    def field(self):
        """Gets the field of this MetadataEntryType.  # noqa: E501


        :return: The field of this MetadataEntryType.  # noqa: E501
        :rtype: MetadataFieldValueType
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this MetadataEntryType.


        :param field: The field of this MetadataEntryType.  # noqa: E501
        :type: MetadataFieldValueType
        """

        self._field = field

    @property
    def group(self):
        """Gets the group of this MetadataEntryType.  # noqa: E501


        :return: The group of this MetadataEntryType.  # noqa: E501
        :rtype: MetadataGroupValueType
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this MetadataEntryType.


        :param group: The group of this MetadataEntryType.  # noqa: E501
        :type: MetadataGroupValueType
        """

        self._group = group

    @property
    def value(self):
        """Gets the value of this MetadataEntryType.  # noqa: E501


        :return: The value of this MetadataEntryType.  # noqa: E501
        :rtype: MetadataValueType
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MetadataEntryType.


        :param value: The value of this MetadataEntryType.  # noqa: E501
        :type: MetadataValueType
        """

        self._value = value

    @property
    def source(self):
        """Gets the source of this MetadataEntryType.  # noqa: E501


        :return: The source of this MetadataEntryType.  # noqa: E501
        :rtype: MetadataEntryTypeSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this MetadataEntryType.


        :param source: The source of this MetadataEntryType.  # noqa: E501
        :type: MetadataEntryTypeSource
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
        if not isinstance(other, MetadataEntryType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
