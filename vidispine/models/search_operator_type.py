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

class SearchOperatorType(object):
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
        'group': 'list[SearchGroupType]',
        'reference': 'list[str]',
        'field': 'list[SearchFieldType]',
        'text': 'list[ItemSearchTextValueType]',
        'item': 'ItemCriterionType',
        'shape': 'ShapeCriterionType',
        'file': 'CriterionType',
        'operator': 'list[SearchOperatorType]',
        'operation': 'str'
    }

    attribute_map = {
        'group': 'group',
        'reference': 'reference',
        'field': 'field',
        'text': 'text',
        'item': 'item',
        'shape': 'shape',
        'file': 'file',
        'operator': 'operator',
        'operation': 'operation'
    }

    def __init__(self, group=None, reference=None, field=None, text=None, item=None, shape=None, file=None, operator=None, operation=None):  # noqa: E501
        """SearchOperatorType - a model defined in OpenAPI"""  # noqa: E501

        self._group = None
        self._reference = None
        self._field = None
        self._text = None
        self._item = None
        self._shape = None
        self._file = None
        self._operator = None
        self._operation = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if reference is not None:
            self.reference = reference
        if field is not None:
            self.field = field
        if text is not None:
            self.text = text
        if item is not None:
            self.item = item
        if shape is not None:
            self.shape = shape
        if file is not None:
            self.file = file
        if operator is not None:
            self.operator = operator
        self.operation = operation

    @property
    def group(self):
        """Gets the group of this SearchOperatorType.  # noqa: E501


        :return: The group of this SearchOperatorType.  # noqa: E501
        :rtype: list[SearchGroupType]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this SearchOperatorType.


        :param group: The group of this SearchOperatorType.  # noqa: E501
        :type: list[SearchGroupType]
        """

        self._group = group

    @property
    def reference(self):
        """Gets the reference of this SearchOperatorType.  # noqa: E501


        :return: The reference of this SearchOperatorType.  # noqa: E501
        :rtype: list[str]
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SearchOperatorType.


        :param reference: The reference of this SearchOperatorType.  # noqa: E501
        :type: list[str]
        """

        self._reference = reference

    @property
    def field(self):
        """Gets the field of this SearchOperatorType.  # noqa: E501


        :return: The field of this SearchOperatorType.  # noqa: E501
        :rtype: list[SearchFieldType]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this SearchOperatorType.


        :param field: The field of this SearchOperatorType.  # noqa: E501
        :type: list[SearchFieldType]
        """

        self._field = field

    @property
    def text(self):
        """Gets the text of this SearchOperatorType.  # noqa: E501


        :return: The text of this SearchOperatorType.  # noqa: E501
        :rtype: list[ItemSearchTextValueType]
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SearchOperatorType.


        :param text: The text of this SearchOperatorType.  # noqa: E501
        :type: list[ItemSearchTextValueType]
        """

        self._text = text

    @property
    def item(self):
        """Gets the item of this SearchOperatorType.  # noqa: E501


        :return: The item of this SearchOperatorType.  # noqa: E501
        :rtype: ItemCriterionType
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this SearchOperatorType.


        :param item: The item of this SearchOperatorType.  # noqa: E501
        :type: ItemCriterionType
        """

        self._item = item

    @property
    def shape(self):
        """Gets the shape of this SearchOperatorType.  # noqa: E501


        :return: The shape of this SearchOperatorType.  # noqa: E501
        :rtype: ShapeCriterionType
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this SearchOperatorType.


        :param shape: The shape of this SearchOperatorType.  # noqa: E501
        :type: ShapeCriterionType
        """

        self._shape = shape

    @property
    def file(self):
        """Gets the file of this SearchOperatorType.  # noqa: E501


        :return: The file of this SearchOperatorType.  # noqa: E501
        :rtype: CriterionType
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this SearchOperatorType.


        :param file: The file of this SearchOperatorType.  # noqa: E501
        :type: CriterionType
        """

        self._file = file

    @property
    def operator(self):
        """Gets the operator of this SearchOperatorType.  # noqa: E501


        :return: The operator of this SearchOperatorType.  # noqa: E501
        :rtype: list[SearchOperatorType]
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this SearchOperatorType.


        :param operator: The operator of this SearchOperatorType.  # noqa: E501
        :type: list[SearchOperatorType]
        """

        self._operator = operator

    @property
    def operation(self):
        """Gets the operation of this SearchOperatorType.  # noqa: E501


        :return: The operation of this SearchOperatorType.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this SearchOperatorType.


        :param operation: The operation of this SearchOperatorType.  # noqa: E501
        :type: str
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501
        allowed_values = ["AND", "OR", "NOT"]  # noqa: E501
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
        if not isinstance(other, SearchOperatorType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other