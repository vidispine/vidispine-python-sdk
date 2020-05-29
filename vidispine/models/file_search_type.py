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

class FileSearchType(object):
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
        'sort': 'list[ItemSearchTypeSort]',
        'facet': 'list[ItemSearchTypeFacet]',
        'group': 'list[SearchGroupType]',
        'suggestion': 'SuggestionSearchType',
        'reference': 'list[str]',
        'item': 'ItemCriterionType',
        'facet_filter': 'list[ItemSearchTypeFacetFilter]',
        'text': 'list[ItemSearchTextValueType]',
        'version': 'int',
        'filter': 'list[SearchFilterType]',
        'field': 'list[SearchFieldType]',
        'shape': 'ShapeCriterionType',
        'intervals': 'str',
        'cursor': 'str',
        'file': 'CriterionType',
        'operator': 'SearchOperatorType',
        'highlight': 'ItemSearchTypeHighlight',
        'autocomplete': 'list[AutocompleteRequestType]'
    }

    attribute_map = {
        'sort': 'sort',
        'facet': 'facet',
        'group': 'group',
        'suggestion': 'suggestion',
        'reference': 'reference',
        'item': 'item',
        'facet_filter': 'facetFilter',
        'text': 'text',
        'version': 'version',
        'filter': 'filter',
        'field': 'field',
        'shape': 'shape',
        'intervals': 'intervals',
        'cursor': 'cursor',
        'file': 'file',
        'operator': 'operator',
        'highlight': 'highlight',
        'autocomplete': 'autocomplete'
    }

    def __init__(self, sort=None, facet=None, group=None, suggestion=None, reference=None, item=None, facet_filter=None, text=None, version=None, filter=None, field=None, shape=None, intervals=None, cursor=None, file=None, operator=None, highlight=None, autocomplete=None):  # noqa: E501
        """FileSearchType - a model defined in OpenAPI"""  # noqa: E501

        self._sort = None
        self._facet = None
        self._group = None
        self._suggestion = None
        self._reference = None
        self._item = None
        self._facet_filter = None
        self._text = None
        self._version = None
        self._filter = None
        self._field = None
        self._shape = None
        self._intervals = None
        self._cursor = None
        self._file = None
        self._operator = None
        self._highlight = None
        self._autocomplete = None
        self.discriminator = None

        if sort is not None:
            self.sort = sort
        if facet is not None:
            self.facet = facet
        if group is not None:
            self.group = group
        if suggestion is not None:
            self.suggestion = suggestion
        if reference is not None:
            self.reference = reference
        if item is not None:
            self.item = item
        if facet_filter is not None:
            self.facet_filter = facet_filter
        if text is not None:
            self.text = text
        if version is not None:
            self.version = version
        if filter is not None:
            self.filter = filter
        if field is not None:
            self.field = field
        if shape is not None:
            self.shape = shape
        if intervals is not None:
            self.intervals = intervals
        if cursor is not None:
            self.cursor = cursor
        if file is not None:
            self.file = file
        if operator is not None:
            self.operator = operator
        if highlight is not None:
            self.highlight = highlight
        if autocomplete is not None:
            self.autocomplete = autocomplete

    @property
    def sort(self):
        """Gets the sort of this FileSearchType.  # noqa: E501


        :return: The sort of this FileSearchType.  # noqa: E501
        :rtype: list[ItemSearchTypeSort]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this FileSearchType.


        :param sort: The sort of this FileSearchType.  # noqa: E501
        :type: list[ItemSearchTypeSort]
        """

        self._sort = sort

    @property
    def facet(self):
        """Gets the facet of this FileSearchType.  # noqa: E501


        :return: The facet of this FileSearchType.  # noqa: E501
        :rtype: list[ItemSearchTypeFacet]
        """
        return self._facet

    @facet.setter
    def facet(self, facet):
        """Sets the facet of this FileSearchType.


        :param facet: The facet of this FileSearchType.  # noqa: E501
        :type: list[ItemSearchTypeFacet]
        """

        self._facet = facet

    @property
    def group(self):
        """Gets the group of this FileSearchType.  # noqa: E501


        :return: The group of this FileSearchType.  # noqa: E501
        :rtype: list[SearchGroupType]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this FileSearchType.


        :param group: The group of this FileSearchType.  # noqa: E501
        :type: list[SearchGroupType]
        """

        self._group = group

    @property
    def suggestion(self):
        """Gets the suggestion of this FileSearchType.  # noqa: E501


        :return: The suggestion of this FileSearchType.  # noqa: E501
        :rtype: SuggestionSearchType
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this FileSearchType.


        :param suggestion: The suggestion of this FileSearchType.  # noqa: E501
        :type: SuggestionSearchType
        """

        self._suggestion = suggestion

    @property
    def reference(self):
        """Gets the reference of this FileSearchType.  # noqa: E501


        :return: The reference of this FileSearchType.  # noqa: E501
        :rtype: list[str]
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this FileSearchType.


        :param reference: The reference of this FileSearchType.  # noqa: E501
        :type: list[str]
        """

        self._reference = reference

    @property
    def item(self):
        """Gets the item of this FileSearchType.  # noqa: E501


        :return: The item of this FileSearchType.  # noqa: E501
        :rtype: ItemCriterionType
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this FileSearchType.


        :param item: The item of this FileSearchType.  # noqa: E501
        :type: ItemCriterionType
        """

        self._item = item

    @property
    def facet_filter(self):
        """Gets the facet_filter of this FileSearchType.  # noqa: E501


        :return: The facet_filter of this FileSearchType.  # noqa: E501
        :rtype: list[ItemSearchTypeFacetFilter]
        """
        return self._facet_filter

    @facet_filter.setter
    def facet_filter(self, facet_filter):
        """Sets the facet_filter of this FileSearchType.


        :param facet_filter: The facet_filter of this FileSearchType.  # noqa: E501
        :type: list[ItemSearchTypeFacetFilter]
        """

        self._facet_filter = facet_filter

    @property
    def text(self):
        """Gets the text of this FileSearchType.  # noqa: E501


        :return: The text of this FileSearchType.  # noqa: E501
        :rtype: list[ItemSearchTextValueType]
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FileSearchType.


        :param text: The text of this FileSearchType.  # noqa: E501
        :type: list[ItemSearchTextValueType]
        """

        self._text = text

    @property
    def version(self):
        """Gets the version of this FileSearchType.  # noqa: E501


        :return: The version of this FileSearchType.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FileSearchType.


        :param version: The version of this FileSearchType.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def filter(self):
        """Gets the filter of this FileSearchType.  # noqa: E501


        :return: The filter of this FileSearchType.  # noqa: E501
        :rtype: list[SearchFilterType]
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this FileSearchType.


        :param filter: The filter of this FileSearchType.  # noqa: E501
        :type: list[SearchFilterType]
        """

        self._filter = filter

    @property
    def field(self):
        """Gets the field of this FileSearchType.  # noqa: E501


        :return: The field of this FileSearchType.  # noqa: E501
        :rtype: list[SearchFieldType]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this FileSearchType.


        :param field: The field of this FileSearchType.  # noqa: E501
        :type: list[SearchFieldType]
        """

        self._field = field

    @property
    def shape(self):
        """Gets the shape of this FileSearchType.  # noqa: E501


        :return: The shape of this FileSearchType.  # noqa: E501
        :rtype: ShapeCriterionType
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this FileSearchType.


        :param shape: The shape of this FileSearchType.  # noqa: E501
        :type: ShapeCriterionType
        """

        self._shape = shape

    @property
    def intervals(self):
        """Gets the intervals of this FileSearchType.  # noqa: E501


        :return: The intervals of this FileSearchType.  # noqa: E501
        :rtype: str
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        """Sets the intervals of this FileSearchType.


        :param intervals: The intervals of this FileSearchType.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "generic", "timed"]  # noqa: E501
        if intervals not in allowed_values:
            raise ValueError(
                "Invalid value for `intervals` ({0}), must be one of {1}"  # noqa: E501
                .format(intervals, allowed_values)
            )

        self._intervals = intervals

    @property
    def cursor(self):
        """Gets the cursor of this FileSearchType.  # noqa: E501


        :return: The cursor of this FileSearchType.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this FileSearchType.


        :param cursor: The cursor of this FileSearchType.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def file(self):
        """Gets the file of this FileSearchType.  # noqa: E501


        :return: The file of this FileSearchType.  # noqa: E501
        :rtype: CriterionType
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FileSearchType.


        :param file: The file of this FileSearchType.  # noqa: E501
        :type: CriterionType
        """

        self._file = file

    @property
    def operator(self):
        """Gets the operator of this FileSearchType.  # noqa: E501


        :return: The operator of this FileSearchType.  # noqa: E501
        :rtype: SearchOperatorType
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this FileSearchType.


        :param operator: The operator of this FileSearchType.  # noqa: E501
        :type: SearchOperatorType
        """

        self._operator = operator

    @property
    def highlight(self):
        """Gets the highlight of this FileSearchType.  # noqa: E501


        :return: The highlight of this FileSearchType.  # noqa: E501
        :rtype: ItemSearchTypeHighlight
        """
        return self._highlight

    @highlight.setter
    def highlight(self, highlight):
        """Sets the highlight of this FileSearchType.


        :param highlight: The highlight of this FileSearchType.  # noqa: E501
        :type: ItemSearchTypeHighlight
        """

        self._highlight = highlight

    @property
    def autocomplete(self):
        """Gets the autocomplete of this FileSearchType.  # noqa: E501


        :return: The autocomplete of this FileSearchType.  # noqa: E501
        :rtype: list[AutocompleteRequestType]
        """
        return self._autocomplete

    @autocomplete.setter
    def autocomplete(self, autocomplete):
        """Sets the autocomplete of this FileSearchType.


        :param autocomplete: The autocomplete of this FileSearchType.  # noqa: E501
        :type: list[AutocompleteRequestType]
        """

        self._autocomplete = autocomplete

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
        if not isinstance(other, FileSearchType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
