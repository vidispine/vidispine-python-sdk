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

class SequenceMediaType(object):
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
        'source_in': 'TimeCodeType',
        'effect': 'list[EffectType]',
        'source_track': 'int',
        'item': 'str',
        '_in': 'TimeCodeType',
        'source_out': 'TimeCodeType',
        'out': 'TimeCodeType'
    }

    attribute_map = {
        'source_in': 'sourceIn',
        'effect': 'effect',
        'source_track': 'sourceTrack',
        'item': 'item',
        '_in': 'in',
        'source_out': 'sourceOut',
        'out': 'out'
    }

    def __init__(self, source_in=None, effect=None, source_track=None, item=None, _in=None, source_out=None, out=None):  # noqa: E501
        """SequenceMediaType - a model defined in OpenAPI"""  # noqa: E501

        self._source_in = None
        self._effect = None
        self._source_track = None
        self._item = None
        self.__in = None
        self._source_out = None
        self._out = None
        self.discriminator = None

        if source_in is not None:
            self.source_in = source_in
        if effect is not None:
            self.effect = effect
        self.source_track = source_track
        self.item = item
        if _in is not None:
            self._in = _in
        if source_out is not None:
            self.source_out = source_out
        if out is not None:
            self.out = out

    @property
    def source_in(self):
        """Gets the source_in of this SequenceMediaType.  # noqa: E501


        :return: The source_in of this SequenceMediaType.  # noqa: E501
        :rtype: TimeCodeType
        """
        return self._source_in

    @source_in.setter
    def source_in(self, source_in):
        """Sets the source_in of this SequenceMediaType.


        :param source_in: The source_in of this SequenceMediaType.  # noqa: E501
        :type: TimeCodeType
        """

        self._source_in = source_in

    @property
    def effect(self):
        """Gets the effect of this SequenceMediaType.  # noqa: E501


        :return: The effect of this SequenceMediaType.  # noqa: E501
        :rtype: list[EffectType]
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this SequenceMediaType.


        :param effect: The effect of this SequenceMediaType.  # noqa: E501
        :type: list[EffectType]
        """

        self._effect = effect

    @property
    def source_track(self):
        """Gets the source_track of this SequenceMediaType.  # noqa: E501


        :return: The source_track of this SequenceMediaType.  # noqa: E501
        :rtype: int
        """
        return self._source_track

    @source_track.setter
    def source_track(self, source_track):
        """Sets the source_track of this SequenceMediaType.


        :param source_track: The source_track of this SequenceMediaType.  # noqa: E501
        :type: int
        """
        if source_track is None:
            raise ValueError("Invalid value for `source_track`, must not be `None`")  # noqa: E501

        self._source_track = source_track

    @property
    def item(self):
        """Gets the item of this SequenceMediaType.  # noqa: E501


        :return: The item of this SequenceMediaType.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this SequenceMediaType.


        :param item: The item of this SequenceMediaType.  # noqa: E501
        :type: str
        """
        if item is None:
            raise ValueError("Invalid value for `item`, must not be `None`")  # noqa: E501
        if item is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', item):  # noqa: E501
            raise ValueError(r"Invalid value for `item`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._item = item

    @property
    def _in(self):
        """Gets the _in of this SequenceMediaType.  # noqa: E501


        :return: The _in of this SequenceMediaType.  # noqa: E501
        :rtype: TimeCodeType
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this SequenceMediaType.


        :param _in: The _in of this SequenceMediaType.  # noqa: E501
        :type: TimeCodeType
        """

        self.__in = _in

    @property
    def source_out(self):
        """Gets the source_out of this SequenceMediaType.  # noqa: E501


        :return: The source_out of this SequenceMediaType.  # noqa: E501
        :rtype: TimeCodeType
        """
        return self._source_out

    @source_out.setter
    def source_out(self, source_out):
        """Sets the source_out of this SequenceMediaType.


        :param source_out: The source_out of this SequenceMediaType.  # noqa: E501
        :type: TimeCodeType
        """

        self._source_out = source_out

    @property
    def out(self):
        """Gets the out of this SequenceMediaType.  # noqa: E501


        :return: The out of this SequenceMediaType.  # noqa: E501
        :rtype: TimeCodeType
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this SequenceMediaType.


        :param out: The out of this SequenceMediaType.  # noqa: E501
        :type: TimeCodeType
        """

        self._out = out

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
        if not isinstance(other, SequenceMediaType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
