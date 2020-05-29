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

class AudioComponentTypeAllOf(object):
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
        'channel_count': 'int',
        'frame_size': 'int',
        'channel_layout': 'int',
        'sample_format': 'str',
        'media_info': 'AudioMediaInfoType',
        'block_align': 'int'
    }

    attribute_map = {
        'channel_count': 'channelCount',
        'frame_size': 'frameSize',
        'channel_layout': 'channelLayout',
        'sample_format': 'sampleFormat',
        'media_info': 'mediaInfo',
        'block_align': 'blockAlign'
    }

    def __init__(self, channel_count=None, frame_size=None, channel_layout=None, sample_format=None, media_info=None, block_align=None):  # noqa: E501
        """AudioComponentTypeAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._channel_count = None
        self._frame_size = None
        self._channel_layout = None
        self._sample_format = None
        self._media_info = None
        self._block_align = None
        self.discriminator = None

        self.channel_count = channel_count
        if frame_size is not None:
            self.frame_size = frame_size
        if channel_layout is not None:
            self.channel_layout = channel_layout
        if sample_format is not None:
            self.sample_format = sample_format
        if media_info is not None:
            self.media_info = media_info
        if block_align is not None:
            self.block_align = block_align

    @property
    def channel_count(self):
        """Gets the channel_count of this AudioComponentTypeAllOf.  # noqa: E501


        :return: The channel_count of this AudioComponentTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._channel_count

    @channel_count.setter
    def channel_count(self, channel_count):
        """Sets the channel_count of this AudioComponentTypeAllOf.


        :param channel_count: The channel_count of this AudioComponentTypeAllOf.  # noqa: E501
        :type: int
        """
        if channel_count is None:
            raise ValueError("Invalid value for `channel_count`, must not be `None`")  # noqa: E501

        self._channel_count = channel_count

    @property
    def frame_size(self):
        """Gets the frame_size of this AudioComponentTypeAllOf.  # noqa: E501


        :return: The frame_size of this AudioComponentTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._frame_size

    @frame_size.setter
    def frame_size(self, frame_size):
        """Sets the frame_size of this AudioComponentTypeAllOf.


        :param frame_size: The frame_size of this AudioComponentTypeAllOf.  # noqa: E501
        :type: int
        """

        self._frame_size = frame_size

    @property
    def channel_layout(self):
        """Gets the channel_layout of this AudioComponentTypeAllOf.  # noqa: E501


        :return: The channel_layout of this AudioComponentTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        """Sets the channel_layout of this AudioComponentTypeAllOf.


        :param channel_layout: The channel_layout of this AudioComponentTypeAllOf.  # noqa: E501
        :type: int
        """

        self._channel_layout = channel_layout

    @property
    def sample_format(self):
        """Gets the sample_format of this AudioComponentTypeAllOf.  # noqa: E501


        :return: The sample_format of this AudioComponentTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._sample_format

    @sample_format.setter
    def sample_format(self, sample_format):
        """Sets the sample_format of this AudioComponentTypeAllOf.


        :param sample_format: The sample_format of this AudioComponentTypeAllOf.  # noqa: E501
        :type: str
        """

        self._sample_format = sample_format

    @property
    def media_info(self):
        """Gets the media_info of this AudioComponentTypeAllOf.  # noqa: E501


        :return: The media_info of this AudioComponentTypeAllOf.  # noqa: E501
        :rtype: AudioMediaInfoType
        """
        return self._media_info

    @media_info.setter
    def media_info(self, media_info):
        """Sets the media_info of this AudioComponentTypeAllOf.


        :param media_info: The media_info of this AudioComponentTypeAllOf.  # noqa: E501
        :type: AudioMediaInfoType
        """

        self._media_info = media_info

    @property
    def block_align(self):
        """Gets the block_align of this AudioComponentTypeAllOf.  # noqa: E501


        :return: The block_align of this AudioComponentTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._block_align

    @block_align.setter
    def block_align(self, block_align):
        """Sets the block_align of this AudioComponentTypeAllOf.


        :param block_align: The block_align of this AudioComponentTypeAllOf.  # noqa: E501
        :type: int
        """

        self._block_align = block_align

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
        if not isinstance(other, AudioComponentTypeAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
