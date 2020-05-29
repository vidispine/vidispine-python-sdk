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

class MDObjectStrongReference(object):
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
        'ul': 'str',
        'name': 'str',
        'weak_reference': 'list[MDObjectWeakReference]',
        'strong_reference': 'list[MDObjectStrongReference]',
        'leaf': 'list[MDObjectLeaf]',
        'child': 'list[MDObjectNode]'
    }

    attribute_map = {
        'ul': 'ul',
        'name': 'name',
        'weak_reference': 'weakReference',
        'strong_reference': 'strongReference',
        'leaf': 'leaf',
        'child': 'child'
    }

    def __init__(self, ul=None, name=None, weak_reference=None, strong_reference=None, leaf=None, child=None):  # noqa: E501
        """MDObjectStrongReference - a model defined in OpenAPI"""  # noqa: E501

        self._ul = None
        self._name = None
        self._weak_reference = None
        self._strong_reference = None
        self._leaf = None
        self._child = None
        self.discriminator = None

        self.ul = ul
        if name is not None:
            self.name = name
        if weak_reference is not None:
            self.weak_reference = weak_reference
        if strong_reference is not None:
            self.strong_reference = strong_reference
        if leaf is not None:
            self.leaf = leaf
        if child is not None:
            self.child = child

    @property
    def ul(self):
        """Gets the ul of this MDObjectStrongReference.  # noqa: E501


        :return: The ul of this MDObjectStrongReference.  # noqa: E501
        :rtype: str
        """
        return self._ul

    @ul.setter
    def ul(self, ul):
        """Sets the ul of this MDObjectStrongReference.


        :param ul: The ul of this MDObjectStrongReference.  # noqa: E501
        :type: str
        """
        if ul is None:
            raise ValueError("Invalid value for `ul`, must not be `None`")  # noqa: E501

        self._ul = ul

    @property
    def name(self):
        """Gets the name of this MDObjectStrongReference.  # noqa: E501


        :return: The name of this MDObjectStrongReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MDObjectStrongReference.


        :param name: The name of this MDObjectStrongReference.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def weak_reference(self):
        """Gets the weak_reference of this MDObjectStrongReference.  # noqa: E501


        :return: The weak_reference of this MDObjectStrongReference.  # noqa: E501
        :rtype: list[MDObjectWeakReference]
        """
        return self._weak_reference

    @weak_reference.setter
    def weak_reference(self, weak_reference):
        """Sets the weak_reference of this MDObjectStrongReference.


        :param weak_reference: The weak_reference of this MDObjectStrongReference.  # noqa: E501
        :type: list[MDObjectWeakReference]
        """

        self._weak_reference = weak_reference

    @property
    def strong_reference(self):
        """Gets the strong_reference of this MDObjectStrongReference.  # noqa: E501


        :return: The strong_reference of this MDObjectStrongReference.  # noqa: E501
        :rtype: list[MDObjectStrongReference]
        """
        return self._strong_reference

    @strong_reference.setter
    def strong_reference(self, strong_reference):
        """Sets the strong_reference of this MDObjectStrongReference.


        :param strong_reference: The strong_reference of this MDObjectStrongReference.  # noqa: E501
        :type: list[MDObjectStrongReference]
        """

        self._strong_reference = strong_reference

    @property
    def leaf(self):
        """Gets the leaf of this MDObjectStrongReference.  # noqa: E501


        :return: The leaf of this MDObjectStrongReference.  # noqa: E501
        :rtype: list[MDObjectLeaf]
        """
        return self._leaf

    @leaf.setter
    def leaf(self, leaf):
        """Sets the leaf of this MDObjectStrongReference.


        :param leaf: The leaf of this MDObjectStrongReference.  # noqa: E501
        :type: list[MDObjectLeaf]
        """

        self._leaf = leaf

    @property
    def child(self):
        """Gets the child of this MDObjectStrongReference.  # noqa: E501


        :return: The child of this MDObjectStrongReference.  # noqa: E501
        :rtype: list[MDObjectNode]
        """
        return self._child

    @child.setter
    def child(self, child):
        """Sets the child of this MDObjectStrongReference.


        :param child: The child of this MDObjectStrongReference.  # noqa: E501
        :type: list[MDObjectNode]
        """

        self._child = child

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
        if not isinstance(other, MDObjectStrongReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
