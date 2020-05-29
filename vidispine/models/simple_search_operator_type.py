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

class SimpleSearchOperatorType(object):
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
        'field': 'list[SimpleSearchFieldType]',
        'operation': 'str'
    }

    attribute_map = {
        'field': 'field',
        'operation': 'operation'
    }

    def __init__(self, field=None, operation=None):  # noqa: E501
        """SimpleSearchOperatorType - a model defined in OpenAPI"""  # noqa: E501

        self._field = None
        self._operation = None
        self.discriminator = None

        if field is not None:
            self.field = field
        self.operation = operation

    @property
    def field(self):
        """Gets the field of this SimpleSearchOperatorType.  # noqa: E501


        :return: The field of this SimpleSearchOperatorType.  # noqa: E501
        :rtype: list[SimpleSearchFieldType]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this SimpleSearchOperatorType.


        :param field: The field of this SimpleSearchOperatorType.  # noqa: E501
        :type: list[SimpleSearchFieldType]
        """

        self._field = field

    @property
    def operation(self):
        """Gets the operation of this SimpleSearchOperatorType.  # noqa: E501


        :return: The operation of this SimpleSearchOperatorType.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this SimpleSearchOperatorType.


        :param operation: The operation of this SimpleSearchOperatorType.  # noqa: E501
        :type: str
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501
        allowed_values = ["AND", "OR"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

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
        if not isinstance(other, SimpleSearchOperatorType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other