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

class ShapeListType(object):
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
        'facet': 'list[FacetType]',
        'hits': 'int',
        'shape': 'list[ShapeType]',
        'suggestion': 'list[SuggestionResultType]'
    }

    attribute_map = {
        'facet': 'facet',
        'hits': 'hits',
        'shape': 'shape',
        'suggestion': 'suggestion'
    }

    def __init__(self, facet=None, hits=None, shape=None, suggestion=None):  # noqa: E501
        """ShapeListType - a model defined in OpenAPI"""  # noqa: E501

        self._facet = None
        self._hits = None
        self._shape = None
        self._suggestion = None
        self.discriminator = None

        if facet is not None:
            self.facet = facet
        if hits is not None:
            self.hits = hits
        if shape is not None:
            self.shape = shape
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def facet(self):
        """Gets the facet of this ShapeListType.  # noqa: E501


        :return: The facet of this ShapeListType.  # noqa: E501
        :rtype: list[FacetType]
        """
        return self._facet

    @facet.setter
    def facet(self, facet):
        """Sets the facet of this ShapeListType.


        :param facet: The facet of this ShapeListType.  # noqa: E501
        :type: list[FacetType]
        """

        self._facet = facet

    @property
    def hits(self):
        """Gets the hits of this ShapeListType.  # noqa: E501


        :return: The hits of this ShapeListType.  # noqa: E501
        :rtype: int
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this ShapeListType.


        :param hits: The hits of this ShapeListType.  # noqa: E501
        :type: int
        """

        self._hits = hits

    @property
    def shape(self):
        """Gets the shape of this ShapeListType.  # noqa: E501


        :return: The shape of this ShapeListType.  # noqa: E501
        :rtype: list[ShapeType]
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this ShapeListType.


        :param shape: The shape of this ShapeListType.  # noqa: E501
        :type: list[ShapeType]
        """

        self._shape = shape

    @property
    def suggestion(self):
        """Gets the suggestion of this ShapeListType.  # noqa: E501


        :return: The suggestion of this ShapeListType.  # noqa: E501
        :rtype: list[SuggestionResultType]
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this ShapeListType.


        :param suggestion: The suggestion of this ShapeListType.  # noqa: E501
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
        if not isinstance(other, ShapeListType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
