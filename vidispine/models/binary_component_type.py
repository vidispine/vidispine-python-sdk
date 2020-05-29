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

class BinaryComponentType(object):
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
        'id': 'str',
        'file': 'list[FileType]',
        'metadata': 'list[KeyValuePairType]',
        'media_info': 'BaseMediaInfoType',
        'length': 'int',
        'encoding': 'str',
        'offset': 'int',
        'format': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file': 'file',
        'metadata': 'metadata',
        'media_info': 'mediaInfo',
        'length': 'length',
        'encoding': 'encoding',
        'offset': 'offset',
        'format': 'format'
    }

    def __init__(self, id=None, file=None, metadata=None, media_info=None, length=None, encoding=None, offset=None, format=None):  # noqa: E501
        """BinaryComponentType - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._file = None
        self._metadata = None
        self._media_info = None
        self._length = None
        self._encoding = None
        self._offset = None
        self._format = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file is not None:
            self.file = file
        if metadata is not None:
            self.metadata = metadata
        if media_info is not None:
            self.media_info = media_info
        if length is not None:
            self.length = length
        if encoding is not None:
            self.encoding = encoding
        if offset is not None:
            self.offset = offset
        if format is not None:
            self.format = format

    @property
    def id(self):
        """Gets the id of this BinaryComponentType.  # noqa: E501


        :return: The id of this BinaryComponentType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BinaryComponentType.


        :param id: The id of this BinaryComponentType.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._id = id

    @property
    def file(self):
        """Gets the file of this BinaryComponentType.  # noqa: E501


        :return: The file of this BinaryComponentType.  # noqa: E501
        :rtype: list[FileType]
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this BinaryComponentType.


        :param file: The file of this BinaryComponentType.  # noqa: E501
        :type: list[FileType]
        """

        self._file = file

    @property
    def metadata(self):
        """Gets the metadata of this BinaryComponentType.  # noqa: E501


        :return: The metadata of this BinaryComponentType.  # noqa: E501
        :rtype: list[KeyValuePairType]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this BinaryComponentType.


        :param metadata: The metadata of this BinaryComponentType.  # noqa: E501
        :type: list[KeyValuePairType]
        """

        self._metadata = metadata

    @property
    def media_info(self):
        """Gets the media_info of this BinaryComponentType.  # noqa: E501


        :return: The media_info of this BinaryComponentType.  # noqa: E501
        :rtype: BaseMediaInfoType
        """
        return self._media_info

    @media_info.setter
    def media_info(self, media_info):
        """Sets the media_info of this BinaryComponentType.


        :param media_info: The media_info of this BinaryComponentType.  # noqa: E501
        :type: BaseMediaInfoType
        """

        self._media_info = media_info

    @property
    def length(self):
        """Gets the length of this BinaryComponentType.  # noqa: E501


        :return: The length of this BinaryComponentType.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this BinaryComponentType.


        :param length: The length of this BinaryComponentType.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def encoding(self):
        """Gets the encoding of this BinaryComponentType.  # noqa: E501


        :return: The encoding of this BinaryComponentType.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this BinaryComponentType.


        :param encoding: The encoding of this BinaryComponentType.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

    @property
    def offset(self):
        """Gets the offset of this BinaryComponentType.  # noqa: E501


        :return: The offset of this BinaryComponentType.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BinaryComponentType.


        :param offset: The offset of this BinaryComponentType.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def format(self):
        """Gets the format of this BinaryComponentType.  # noqa: E501


        :return: The format of this BinaryComponentType.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this BinaryComponentType.


        :param format: The format of this BinaryComponentType.  # noqa: E501
        :type: str
        """

        self._format = format

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
        if not isinstance(other, BinaryComponentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
