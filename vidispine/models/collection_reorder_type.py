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

class CollectionReorderType(object):
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
        'item': 'list[CollectionReorderEntryType]',
        'library': 'list[CollectionReorderEntryType]',
        'collection': 'list[CollectionReorderEntryType]'
    }

    attribute_map = {
        'item': 'item',
        'library': 'library',
        'collection': 'collection'
    }

    def __init__(self, item=None, library=None, collection=None):  # noqa: E501
        """CollectionReorderType - a model defined in OpenAPI"""  # noqa: E501

        self._item = None
        self._library = None
        self._collection = None
        self.discriminator = None

        if item is not None:
            self.item = item
        if library is not None:
            self.library = library
        if collection is not None:
            self.collection = collection

    @property
    def item(self):
        """Gets the item of this CollectionReorderType.  # noqa: E501


        :return: The item of this CollectionReorderType.  # noqa: E501
        :rtype: list[CollectionReorderEntryType]
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this CollectionReorderType.


        :param item: The item of this CollectionReorderType.  # noqa: E501
        :type: list[CollectionReorderEntryType]
        """

        self._item = item

    @property
    def library(self):
        """Gets the library of this CollectionReorderType.  # noqa: E501


        :return: The library of this CollectionReorderType.  # noqa: E501
        :rtype: list[CollectionReorderEntryType]
        """
        return self._library

    @library.setter
    def library(self, library):
        """Sets the library of this CollectionReorderType.


        :param library: The library of this CollectionReorderType.  # noqa: E501
        :type: list[CollectionReorderEntryType]
        """

        self._library = library

    @property
    def collection(self):
        """Gets the collection of this CollectionReorderType.  # noqa: E501


        :return: The collection of this CollectionReorderType.  # noqa: E501
        :rtype: list[CollectionReorderEntryType]
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this CollectionReorderType.


        :param collection: The collection of this CollectionReorderType.  # noqa: E501
        :type: list[CollectionReorderEntryType]
        """

        self._collection = collection

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
        if not isinstance(other, CollectionReorderType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
