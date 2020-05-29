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

class MetadataSchemaDeleteOperationType(object):
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
        'type': 'str',
        'target': 'MetadataSchemaHierarchyType'
    }

    attribute_map = {
        'type': 'type',
        'target': 'target'
    }

    def __init__(self, type=None, target=None):  # noqa: E501
        """MetadataSchemaDeleteOperationType - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._target = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.target = target

    @property
    def type(self):
        """Gets the type of this MetadataSchemaDeleteOperationType.  # noqa: E501


        :return: The type of this MetadataSchemaDeleteOperationType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MetadataSchemaDeleteOperationType.


        :param type: The type of this MetadataSchemaDeleteOperationType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def target(self):
        """Gets the target of this MetadataSchemaDeleteOperationType.  # noqa: E501


        :return: The target of this MetadataSchemaDeleteOperationType.  # noqa: E501
        :rtype: MetadataSchemaHierarchyType
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this MetadataSchemaDeleteOperationType.


        :param target: The target of this MetadataSchemaDeleteOperationType.  # noqa: E501
        :type: MetadataSchemaHierarchyType
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

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
        if not isinstance(other, MetadataSchemaDeleteOperationType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
