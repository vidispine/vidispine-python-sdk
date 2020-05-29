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

class SubtitleClipType(object):
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
        'vertical_base': 'str',
        'y_rel': 'float',
        'font': 'str',
        'size': 'int',
        'outline_size': 'int',
        'size_rel': 'float',
        'x_rel': 'float',
        'language': 'str',
        'line': 'list[str]',
        'a': 'int',
        'b': 'int',
        'outline': 'str',
        'g': 'int',
        'outline_g': 'int',
        'align': 'str',
        'outline_b': 'int',
        'outline_a': 'int',
        'r': 'int',
        'horizontal_base': 'str',
        'y': 'int',
        'x': 'int',
        'outline_r': 'int'
    }

    attribute_map = {
        'vertical_base': 'verticalBase',
        'y_rel': 'yRel',
        'font': 'font',
        'size': 'size',
        'outline_size': 'outlineSize',
        'size_rel': 'sizeRel',
        'x_rel': 'xRel',
        'language': 'language',
        'line': 'line',
        'a': 'a',
        'b': 'b',
        'outline': 'outline',
        'g': 'g',
        'outline_g': 'outlineG',
        'align': 'align',
        'outline_b': 'outlineB',
        'outline_a': 'outlineA',
        'r': 'r',
        'horizontal_base': 'horizontalBase',
        'y': 'y',
        'x': 'x',
        'outline_r': 'outlineR'
    }

    def __init__(self, vertical_base=None, y_rel=None, font=None, size=None, outline_size=None, size_rel=None, x_rel=None, language=None, line=None, a=None, b=None, outline=None, g=None, outline_g=None, align=None, outline_b=None, outline_a=None, r=None, horizontal_base=None, y=None, x=None, outline_r=None):  # noqa: E501
        """SubtitleClipType - a model defined in OpenAPI"""  # noqa: E501

        self._vertical_base = None
        self._y_rel = None
        self._font = None
        self._size = None
        self._outline_size = None
        self._size_rel = None
        self._x_rel = None
        self._language = None
        self._line = None
        self._a = None
        self._b = None
        self._outline = None
        self._g = None
        self._outline_g = None
        self._align = None
        self._outline_b = None
        self._outline_a = None
        self._r = None
        self._horizontal_base = None
        self._y = None
        self._x = None
        self._outline_r = None
        self.discriminator = None

        if vertical_base is not None:
            self.vertical_base = vertical_base
        if y_rel is not None:
            self.y_rel = y_rel
        if font is not None:
            self.font = font
        if size is not None:
            self.size = size
        if outline_size is not None:
            self.outline_size = outline_size
        if size_rel is not None:
            self.size_rel = size_rel
        if x_rel is not None:
            self.x_rel = x_rel
        if language is not None:
            self.language = language
        if line is not None:
            self.line = line
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        if outline is not None:
            self.outline = outline
        if g is not None:
            self.g = g
        if outline_g is not None:
            self.outline_g = outline_g
        if align is not None:
            self.align = align
        if outline_b is not None:
            self.outline_b = outline_b
        if outline_a is not None:
            self.outline_a = outline_a
        if r is not None:
            self.r = r
        if horizontal_base is not None:
            self.horizontal_base = horizontal_base
        if y is not None:
            self.y = y
        if x is not None:
            self.x = x
        if outline_r is not None:
            self.outline_r = outline_r

    @property
    def vertical_base(self):
        """Gets the vertical_base of this SubtitleClipType.  # noqa: E501


        :return: The vertical_base of this SubtitleClipType.  # noqa: E501
        :rtype: str
        """
        return self._vertical_base

    @vertical_base.setter
    def vertical_base(self, vertical_base):
        """Sets the vertical_base of this SubtitleClipType.


        :param vertical_base: The vertical_base of this SubtitleClipType.  # noqa: E501
        :type: str
        """

        self._vertical_base = vertical_base

    @property
    def y_rel(self):
        """Gets the y_rel of this SubtitleClipType.  # noqa: E501


        :return: The y_rel of this SubtitleClipType.  # noqa: E501
        :rtype: float
        """
        return self._y_rel

    @y_rel.setter
    def y_rel(self, y_rel):
        """Sets the y_rel of this SubtitleClipType.


        :param y_rel: The y_rel of this SubtitleClipType.  # noqa: E501
        :type: float
        """

        self._y_rel = y_rel

    @property
    def font(self):
        """Gets the font of this SubtitleClipType.  # noqa: E501


        :return: The font of this SubtitleClipType.  # noqa: E501
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """Sets the font of this SubtitleClipType.


        :param font: The font of this SubtitleClipType.  # noqa: E501
        :type: str
        """

        self._font = font

    @property
    def size(self):
        """Gets the size of this SubtitleClipType.  # noqa: E501


        :return: The size of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SubtitleClipType.


        :param size: The size of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def outline_size(self):
        """Gets the outline_size of this SubtitleClipType.  # noqa: E501


        :return: The outline_size of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._outline_size

    @outline_size.setter
    def outline_size(self, outline_size):
        """Sets the outline_size of this SubtitleClipType.


        :param outline_size: The outline_size of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._outline_size = outline_size

    @property
    def size_rel(self):
        """Gets the size_rel of this SubtitleClipType.  # noqa: E501


        :return: The size_rel of this SubtitleClipType.  # noqa: E501
        :rtype: float
        """
        return self._size_rel

    @size_rel.setter
    def size_rel(self, size_rel):
        """Sets the size_rel of this SubtitleClipType.


        :param size_rel: The size_rel of this SubtitleClipType.  # noqa: E501
        :type: float
        """

        self._size_rel = size_rel

    @property
    def x_rel(self):
        """Gets the x_rel of this SubtitleClipType.  # noqa: E501


        :return: The x_rel of this SubtitleClipType.  # noqa: E501
        :rtype: float
        """
        return self._x_rel

    @x_rel.setter
    def x_rel(self, x_rel):
        """Sets the x_rel of this SubtitleClipType.


        :param x_rel: The x_rel of this SubtitleClipType.  # noqa: E501
        :type: float
        """

        self._x_rel = x_rel

    @property
    def language(self):
        """Gets the language of this SubtitleClipType.  # noqa: E501


        :return: The language of this SubtitleClipType.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SubtitleClipType.


        :param language: The language of this SubtitleClipType.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def line(self):
        """Gets the line of this SubtitleClipType.  # noqa: E501


        :return: The line of this SubtitleClipType.  # noqa: E501
        :rtype: list[str]
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this SubtitleClipType.


        :param line: The line of this SubtitleClipType.  # noqa: E501
        :type: list[str]
        """

        self._line = line

    @property
    def a(self):
        """Gets the a of this SubtitleClipType.  # noqa: E501


        :return: The a of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._a

    @a.setter
    def a(self, a):
        """Sets the a of this SubtitleClipType.


        :param a: The a of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._a = a

    @property
    def b(self):
        """Gets the b of this SubtitleClipType.  # noqa: E501


        :return: The b of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this SubtitleClipType.


        :param b: The b of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._b = b

    @property
    def outline(self):
        """Gets the outline of this SubtitleClipType.  # noqa: E501


        :return: The outline of this SubtitleClipType.  # noqa: E501
        :rtype: str
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this SubtitleClipType.


        :param outline: The outline of this SubtitleClipType.  # noqa: E501
        :type: str
        """

        self._outline = outline

    @property
    def g(self):
        """Gets the g of this SubtitleClipType.  # noqa: E501


        :return: The g of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._g

    @g.setter
    def g(self, g):
        """Sets the g of this SubtitleClipType.


        :param g: The g of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._g = g

    @property
    def outline_g(self):
        """Gets the outline_g of this SubtitleClipType.  # noqa: E501


        :return: The outline_g of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._outline_g

    @outline_g.setter
    def outline_g(self, outline_g):
        """Sets the outline_g of this SubtitleClipType.


        :param outline_g: The outline_g of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._outline_g = outline_g

    @property
    def align(self):
        """Gets the align of this SubtitleClipType.  # noqa: E501


        :return: The align of this SubtitleClipType.  # noqa: E501
        :rtype: str
        """
        return self._align

    @align.setter
    def align(self, align):
        """Sets the align of this SubtitleClipType.


        :param align: The align of this SubtitleClipType.  # noqa: E501
        :type: str
        """

        self._align = align

    @property
    def outline_b(self):
        """Gets the outline_b of this SubtitleClipType.  # noqa: E501


        :return: The outline_b of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._outline_b

    @outline_b.setter
    def outline_b(self, outline_b):
        """Sets the outline_b of this SubtitleClipType.


        :param outline_b: The outline_b of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._outline_b = outline_b

    @property
    def outline_a(self):
        """Gets the outline_a of this SubtitleClipType.  # noqa: E501


        :return: The outline_a of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._outline_a

    @outline_a.setter
    def outline_a(self, outline_a):
        """Sets the outline_a of this SubtitleClipType.


        :param outline_a: The outline_a of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._outline_a = outline_a

    @property
    def r(self):
        """Gets the r of this SubtitleClipType.  # noqa: E501


        :return: The r of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._r

    @r.setter
    def r(self, r):
        """Sets the r of this SubtitleClipType.


        :param r: The r of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._r = r

    @property
    def horizontal_base(self):
        """Gets the horizontal_base of this SubtitleClipType.  # noqa: E501


        :return: The horizontal_base of this SubtitleClipType.  # noqa: E501
        :rtype: str
        """
        return self._horizontal_base

    @horizontal_base.setter
    def horizontal_base(self, horizontal_base):
        """Sets the horizontal_base of this SubtitleClipType.


        :param horizontal_base: The horizontal_base of this SubtitleClipType.  # noqa: E501
        :type: str
        """

        self._horizontal_base = horizontal_base

    @property
    def y(self):
        """Gets the y of this SubtitleClipType.  # noqa: E501


        :return: The y of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this SubtitleClipType.


        :param y: The y of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._y = y

    @property
    def x(self):
        """Gets the x of this SubtitleClipType.  # noqa: E501


        :return: The x of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this SubtitleClipType.


        :param x: The x of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._x = x

    @property
    def outline_r(self):
        """Gets the outline_r of this SubtitleClipType.  # noqa: E501


        :return: The outline_r of this SubtitleClipType.  # noqa: E501
        :rtype: int
        """
        return self._outline_r

    @outline_r.setter
    def outline_r(self, outline_r):
        """Sets the outline_r of this SubtitleClipType.


        :param outline_r: The outline_r of this SubtitleClipType.  # noqa: E501
        :type: int
        """

        self._outline_r = outline_r

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
        if not isinstance(other, SubtitleClipType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other