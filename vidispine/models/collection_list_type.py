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

class CollectionListType(object):
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
        'autocomplete': 'list[AutocompleteResponseType]',
        'hits': 'int',
        'collection': 'list[CollectionType]',
        'facet': 'list[FacetType]',
        'next_cursor': 'str',
        'suggestion': 'list[SuggestionResultType]'
    }

    attribute_map = {
        'autocomplete': 'autocomplete',
        'hits': 'hits',
        'collection': 'collection',
        'facet': 'facet',
        'next_cursor': 'nextCursor',
        'suggestion': 'suggestion'
    }

    def __init__(self, autocomplete=None, hits=None, collection=None, facet=None, next_cursor=None, suggestion=None):  # noqa: E501
        """CollectionListType - a model defined in OpenAPI"""  # noqa: E501

        self._autocomplete = None
        self._hits = None
        self._collection = None
        self._facet = None
        self._next_cursor = None
        self._suggestion = None
        self.discriminator = None

        if autocomplete is not None:
            self.autocomplete = autocomplete
        if hits is not None:
            self.hits = hits
        if collection is not None:
            self.collection = collection
        if facet is not None:
            self.facet = facet
        if next_cursor is not None:
            self.next_cursor = next_cursor
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def autocomplete(self):
        """Gets the autocomplete of this CollectionListType.  # noqa: E501


        :return: The autocomplete of this CollectionListType.  # noqa: E501
        :rtype: list[AutocompleteResponseType]
        """
        return self._autocomplete

    @autocomplete.setter
    def autocomplete(self, autocomplete):
        """Sets the autocomplete of this CollectionListType.


        :param autocomplete: The autocomplete of this CollectionListType.  # noqa: E501
        :type: list[AutocompleteResponseType]
        """

        self._autocomplete = autocomplete

    @property
    def hits(self):
        """Gets the hits of this CollectionListType.  # noqa: E501


        :return: The hits of this CollectionListType.  # noqa: E501
        :rtype: int
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this CollectionListType.


        :param hits: The hits of this CollectionListType.  # noqa: E501
        :type: int
        """

        self._hits = hits

    @property
    def collection(self):
        """Gets the collection of this CollectionListType.  # noqa: E501


        :return: The collection of this CollectionListType.  # noqa: E501
        :rtype: list[CollectionType]
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this CollectionListType.


        :param collection: The collection of this CollectionListType.  # noqa: E501
        :type: list[CollectionType]
        """

        self._collection = collection

    @property
    def facet(self):
        """Gets the facet of this CollectionListType.  # noqa: E501


        :return: The facet of this CollectionListType.  # noqa: E501
        :rtype: list[FacetType]
        """
        return self._facet

    @facet.setter
    def facet(self, facet):
        """Sets the facet of this CollectionListType.


        :param facet: The facet of this CollectionListType.  # noqa: E501
        :type: list[FacetType]
        """

        self._facet = facet

    @property
    def next_cursor(self):
        """Gets the next_cursor of this CollectionListType.  # noqa: E501


        :return: The next_cursor of this CollectionListType.  # noqa: E501
        :rtype: str
        """
        return self._next_cursor

    @next_cursor.setter
    def next_cursor(self, next_cursor):
        """Sets the next_cursor of this CollectionListType.


        :param next_cursor: The next_cursor of this CollectionListType.  # noqa: E501
        :type: str
        """

        self._next_cursor = next_cursor

    @property
    def suggestion(self):
        """Gets the suggestion of this CollectionListType.  # noqa: E501


        :return: The suggestion of this CollectionListType.  # noqa: E501
        :rtype: list[SuggestionResultType]
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this CollectionListType.


        :param suggestion: The suggestion of this CollectionListType.  # noqa: E501
        :type: list[SuggestionResultType]
        """

        self._suggestion = suggestion

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
        if not isinstance(other, CollectionListType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
