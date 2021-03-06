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

class MetadataSchemaRenameOperationType(object):
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
        'to': 'str',
        '_from': 'MetadataSchemaHierarchyType'
    }

    attribute_map = {
        'to': 'to',
        '_from': 'from'
    }

    def __init__(self, to=None, _from=None):  # noqa: E501
        """MetadataSchemaRenameOperationType - a model defined in OpenAPI"""  # noqa: E501

        self._to = None
        self.__from = None
        self.discriminator = None

        self.to = to
        self._from = _from

    @property
    def to(self):
        """Gets the to of this MetadataSchemaRenameOperationType.  # noqa: E501


        :return: The to of this MetadataSchemaRenameOperationType.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this MetadataSchemaRenameOperationType.


        :param to: The to of this MetadataSchemaRenameOperationType.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def _from(self):
        """Gets the _from of this MetadataSchemaRenameOperationType.  # noqa: E501


        :return: The _from of this MetadataSchemaRenameOperationType.  # noqa: E501
        :rtype: MetadataSchemaHierarchyType
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this MetadataSchemaRenameOperationType.


        :param _from: The _from of this MetadataSchemaRenameOperationType.  # noqa: E501
        :type: MetadataSchemaHierarchyType
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

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
        if not isinstance(other, MetadataSchemaRenameOperationType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
