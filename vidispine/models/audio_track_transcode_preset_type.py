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

class AudioTrackTranscodePresetType(object):
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
        'framerate': 'TimeBaseType',
        'preset': 'list[str]',
        'mix': 'list[AudioTranscodePresetMixType]',
        'codec': 'str',
        'bitrate': 'int',
        'setting': 'list[KeyValuePairType]',
        'channel': 'list[int]'
    }

    attribute_map = {
        'framerate': 'framerate',
        'preset': 'preset',
        'mix': 'mix',
        'codec': 'codec',
        'bitrate': 'bitrate',
        'setting': 'setting',
        'channel': 'channel'
    }

    def __init__(self, framerate=None, preset=None, mix=None, codec=None, bitrate=None, setting=None, channel=None):  # noqa: E501
        """AudioTrackTranscodePresetType - a model defined in OpenAPI"""  # noqa: E501

        self._framerate = None
        self._preset = None
        self._mix = None
        self._codec = None
        self._bitrate = None
        self._setting = None
        self._channel = None
        self.discriminator = None

        if framerate is not None:
            self.framerate = framerate
        if preset is not None:
            self.preset = preset
        if mix is not None:
            self.mix = mix
        if codec is not None:
            self.codec = codec
        if bitrate is not None:
            self.bitrate = bitrate
        if setting is not None:
            self.setting = setting
        if channel is not None:
            self.channel = channel

    @property
    def framerate(self):
        """Gets the framerate of this AudioTrackTranscodePresetType.  # noqa: E501


        :return: The framerate of this AudioTrackTranscodePresetType.  # noqa: E501
        :rtype: TimeBaseType
        """
        return self._framerate

    @framerate.setter
    def framerate(self, framerate):
        """Sets the framerate of this AudioTrackTranscodePresetType.


        :param framerate: The framerate of this AudioTrackTranscodePresetType.  # noqa: E501
        :type: TimeBaseType
        """

        self._framerate = framerate

    @property
    def preset(self):
        """Gets the preset of this AudioTrackTranscodePresetType.  # noqa: E501


        :return: The preset of this AudioTrackTranscodePresetType.  # noqa: E501
        :rtype: list[str]
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this AudioTrackTranscodePresetType.


        :param preset: The preset of this AudioTrackTranscodePresetType.  # noqa: E501
        :type: list[str]
        """

        self._preset = preset

    @property
    def mix(self):
        """Gets the mix of this AudioTrackTranscodePresetType.  # noqa: E501


        :return: The mix of this AudioTrackTranscodePresetType.  # noqa: E501
        :rtype: list[AudioTranscodePresetMixType]
        """
        return self._mix

    @mix.setter
    def mix(self, mix):
        """Sets the mix of this AudioTrackTranscodePresetType.


        :param mix: The mix of this AudioTrackTranscodePresetType.  # noqa: E501
        :type: list[AudioTranscodePresetMixType]
        """

        self._mix = mix

    @property
    def codec(self):
        """Gets the codec of this AudioTrackTranscodePresetType.  # noqa: E501


        :return: The codec of this AudioTrackTranscodePresetType.  # noqa: E501
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this AudioTrackTranscodePresetType.


        :param codec: The codec of this AudioTrackTranscodePresetType.  # noqa: E501
        :type: str
        """

        self._codec = codec

    @property
    def bitrate(self):
        """Gets the bitrate of this AudioTrackTranscodePresetType.  # noqa: E501


        :return: The bitrate of this AudioTrackTranscodePresetType.  # noqa: E501
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this AudioTrackTranscodePresetType.


        :param bitrate: The bitrate of this AudioTrackTranscodePresetType.  # noqa: E501
        :type: int
        """

        self._bitrate = bitrate

    @property
    def setting(self):
        """Gets the setting of this AudioTrackTranscodePresetType.  # noqa: E501


        :return: The setting of this AudioTrackTranscodePresetType.  # noqa: E501
        :rtype: list[KeyValuePairType]
        """
        return self._setting

    @setting.setter
    def setting(self, setting):
        """Sets the setting of this AudioTrackTranscodePresetType.


        :param setting: The setting of this AudioTrackTranscodePresetType.  # noqa: E501
        :type: list[KeyValuePairType]
        """

        self._setting = setting

    @property
    def channel(self):
        """Gets the channel of this AudioTrackTranscodePresetType.  # noqa: E501


        :return: The channel of this AudioTrackTranscodePresetType.  # noqa: E501
        :rtype: list[int]
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this AudioTrackTranscodePresetType.


        :param channel: The channel of this AudioTrackTranscodePresetType.  # noqa: E501
        :type: list[int]
        """

        self._channel = channel

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
        if not isinstance(other, AudioTrackTranscodePresetType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
