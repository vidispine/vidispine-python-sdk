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

class SequenceTransitionType(object):
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
        'border_color': 'str',
        'reverse': 'bool',
        'transition': 'str',
        'horiz_repeat': 'int',
        'border_width': 'int',
        'vert_repeat': 'int',
        '_in': 'TimeCodeType',
        'end_percentage': 'int',
        'start_percentage': 'int',
        'wipe': 'int',
        'out': 'TimeCodeType'
    }

    attribute_map = {
        'border_color': 'borderColor',
        'reverse': 'reverse',
        'transition': 'transition',
        'horiz_repeat': 'horizRepeat',
        'border_width': 'borderWidth',
        'vert_repeat': 'vertRepeat',
        '_in': 'in',
        'end_percentage': 'endPercentage',
        'start_percentage': 'startPercentage',
        'wipe': 'wipe',
        'out': 'out'
    }

    def __init__(self, border_color=None, reverse=None, transition=None, horiz_repeat=None, border_width=None, vert_repeat=None, _in=None, end_percentage=None, start_percentage=None, wipe=None, out=None):  # noqa: E501
        """SequenceTransitionType - a model defined in OpenAPI"""  # noqa: E501

        self._border_color = None
        self._reverse = None
        self._transition = None
        self._horiz_repeat = None
        self._border_width = None
        self._vert_repeat = None
        self.__in = None
        self._end_percentage = None
        self._start_percentage = None
        self._wipe = None
        self._out = None
        self.discriminator = None

        if border_color is not None:
            self.border_color = border_color
        if reverse is not None:
            self.reverse = reverse
        self.transition = transition
        if horiz_repeat is not None:
            self.horiz_repeat = horiz_repeat
        if border_width is not None:
            self.border_width = border_width
        if vert_repeat is not None:
            self.vert_repeat = vert_repeat
        self._in = _in
        if end_percentage is not None:
            self.end_percentage = end_percentage
        if start_percentage is not None:
            self.start_percentage = start_percentage
        if wipe is not None:
            self.wipe = wipe
        self.out = out

    @property
    def border_color(self):
        """Gets the border_color of this SequenceTransitionType.  # noqa: E501


        :return: The border_color of this SequenceTransitionType.  # noqa: E501
        :rtype: str
        """
        return self._border_color

    @border_color.setter
    def border_color(self, border_color):
        """Sets the border_color of this SequenceTransitionType.


        :param border_color: The border_color of this SequenceTransitionType.  # noqa: E501
        :type: str
        """

        self._border_color = border_color

    @property
    def reverse(self):
        """Gets the reverse of this SequenceTransitionType.  # noqa: E501


        :return: The reverse of this SequenceTransitionType.  # noqa: E501
        :rtype: bool
        """
        return self._reverse

    @reverse.setter
    def reverse(self, reverse):
        """Sets the reverse of this SequenceTransitionType.


        :param reverse: The reverse of this SequenceTransitionType.  # noqa: E501
        :type: bool
        """

        self._reverse = reverse

    @property
    def transition(self):
        """Gets the transition of this SequenceTransitionType.  # noqa: E501


        :return: The transition of this SequenceTransitionType.  # noqa: E501
        :rtype: str
        """
        return self._transition

    @transition.setter
    def transition(self, transition):
        """Sets the transition of this SequenceTransitionType.


        :param transition: The transition of this SequenceTransitionType.  # noqa: E501
        :type: str
        """
        if transition is None:
            raise ValueError("Invalid value for `transition`, must not be `None`")  # noqa: E501

        self._transition = transition

    @property
    def horiz_repeat(self):
        """Gets the horiz_repeat of this SequenceTransitionType.  # noqa: E501


        :return: The horiz_repeat of this SequenceTransitionType.  # noqa: E501
        :rtype: int
        """
        return self._horiz_repeat

    @horiz_repeat.setter
    def horiz_repeat(self, horiz_repeat):
        """Sets the horiz_repeat of this SequenceTransitionType.


        :param horiz_repeat: The horiz_repeat of this SequenceTransitionType.  # noqa: E501
        :type: int
        """

        self._horiz_repeat = horiz_repeat

    @property
    def border_width(self):
        """Gets the border_width of this SequenceTransitionType.  # noqa: E501


        :return: The border_width of this SequenceTransitionType.  # noqa: E501
        :rtype: int
        """
        return self._border_width

    @border_width.setter
    def border_width(self, border_width):
        """Sets the border_width of this SequenceTransitionType.


        :param border_width: The border_width of this SequenceTransitionType.  # noqa: E501
        :type: int
        """

        self._border_width = border_width

    @property
    def vert_repeat(self):
        """Gets the vert_repeat of this SequenceTransitionType.  # noqa: E501


        :return: The vert_repeat of this SequenceTransitionType.  # noqa: E501
        :rtype: int
        """
        return self._vert_repeat

    @vert_repeat.setter
    def vert_repeat(self, vert_repeat):
        """Sets the vert_repeat of this SequenceTransitionType.


        :param vert_repeat: The vert_repeat of this SequenceTransitionType.  # noqa: E501
        :type: int
        """

        self._vert_repeat = vert_repeat

    @property
    def _in(self):
        """Gets the _in of this SequenceTransitionType.  # noqa: E501


        :return: The _in of this SequenceTransitionType.  # noqa: E501
        :rtype: TimeCodeType
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this SequenceTransitionType.


        :param _in: The _in of this SequenceTransitionType.  # noqa: E501
        :type: TimeCodeType
        """
        if _in is None:
            raise ValueError("Invalid value for `_in`, must not be `None`")  # noqa: E501

        self.__in = _in

    @property
    def end_percentage(self):
        """Gets the end_percentage of this SequenceTransitionType.  # noqa: E501


        :return: The end_percentage of this SequenceTransitionType.  # noqa: E501
        :rtype: int
        """
        return self._end_percentage

    @end_percentage.setter
    def end_percentage(self, end_percentage):
        """Sets the end_percentage of this SequenceTransitionType.


        :param end_percentage: The end_percentage of this SequenceTransitionType.  # noqa: E501
        :type: int
        """

        self._end_percentage = end_percentage

    @property
    def start_percentage(self):
        """Gets the start_percentage of this SequenceTransitionType.  # noqa: E501


        :return: The start_percentage of this SequenceTransitionType.  # noqa: E501
        :rtype: int
        """
        return self._start_percentage

    @start_percentage.setter
    def start_percentage(self, start_percentage):
        """Sets the start_percentage of this SequenceTransitionType.


        :param start_percentage: The start_percentage of this SequenceTransitionType.  # noqa: E501
        :type: int
        """

        self._start_percentage = start_percentage

    @property
    def wipe(self):
        """Gets the wipe of this SequenceTransitionType.  # noqa: E501


        :return: The wipe of this SequenceTransitionType.  # noqa: E501
        :rtype: int
        """
        return self._wipe

    @wipe.setter
    def wipe(self, wipe):
        """Sets the wipe of this SequenceTransitionType.


        :param wipe: The wipe of this SequenceTransitionType.  # noqa: E501
        :type: int
        """

        self._wipe = wipe

    @property
    def out(self):
        """Gets the out of this SequenceTransitionType.  # noqa: E501


        :return: The out of this SequenceTransitionType.  # noqa: E501
        :rtype: TimeCodeType
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this SequenceTransitionType.


        :param out: The out of this SequenceTransitionType.  # noqa: E501
        :type: TimeCodeType
        """
        if out is None:
            raise ValueError("Invalid value for `out`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, SequenceTransitionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
