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

class NLEJobType(object):
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
        'sequence': 'list[NLEJobSequenceType]',
        'output2': 'list[NLEJob2OutputType]',
        'pause_frame': 'int',
        'frame_rate': 'FrameRateType',
        'audio_clip': 'list[AudioClipType]',
        'video_clip': 'list[VideoClipType]',
        'height': 'int',
        'width': 'int',
        'dar': 'AspectRatioType',
        'output': 'list[NLEJobOutputType]',
        'sample_rate': 'int',
        'subtitle_clip': 'list[SubtitleClipType]'
    }

    attribute_map = {
        'sequence': 'sequence',
        'output2': 'output2',
        'pause_frame': 'pauseFrame',
        'frame_rate': 'frameRate',
        'audio_clip': 'audioClip',
        'video_clip': 'videoClip',
        'height': 'height',
        'width': 'width',
        'dar': 'dar',
        'output': 'output',
        'sample_rate': 'sampleRate',
        'subtitle_clip': 'subtitleClip'
    }

    def __init__(self, sequence=None, output2=None, pause_frame=None, frame_rate=None, audio_clip=None, video_clip=None, height=None, width=None, dar=None, output=None, sample_rate=None, subtitle_clip=None):  # noqa: E501
        """NLEJobType - a model defined in OpenAPI"""  # noqa: E501

        self._sequence = None
        self._output2 = None
        self._pause_frame = None
        self._frame_rate = None
        self._audio_clip = None
        self._video_clip = None
        self._height = None
        self._width = None
        self._dar = None
        self._output = None
        self._sample_rate = None
        self._subtitle_clip = None
        self.discriminator = None

        if sequence is not None:
            self.sequence = sequence
        if output2 is not None:
            self.output2 = output2
        if pause_frame is not None:
            self.pause_frame = pause_frame
        self.frame_rate = frame_rate
        if audio_clip is not None:
            self.audio_clip = audio_clip
        if video_clip is not None:
            self.video_clip = video_clip
        self.height = height
        self.width = width
        self.dar = dar
        if output is not None:
            self.output = output
        self.sample_rate = sample_rate
        if subtitle_clip is not None:
            self.subtitle_clip = subtitle_clip

    @property
    def sequence(self):
        """Gets the sequence of this NLEJobType.  # noqa: E501


        :return: The sequence of this NLEJobType.  # noqa: E501
        :rtype: list[NLEJobSequenceType]
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this NLEJobType.


        :param sequence: The sequence of this NLEJobType.  # noqa: E501
        :type: list[NLEJobSequenceType]
        """

        self._sequence = sequence

    @property
    def output2(self):
        """Gets the output2 of this NLEJobType.  # noqa: E501


        :return: The output2 of this NLEJobType.  # noqa: E501
        :rtype: list[NLEJob2OutputType]
        """
        return self._output2

    @output2.setter
    def output2(self, output2):
        """Sets the output2 of this NLEJobType.


        :param output2: The output2 of this NLEJobType.  # noqa: E501
        :type: list[NLEJob2OutputType]
        """

        self._output2 = output2

    @property
    def pause_frame(self):
        """Gets the pause_frame of this NLEJobType.  # noqa: E501


        :return: The pause_frame of this NLEJobType.  # noqa: E501
        :rtype: int
        """
        return self._pause_frame

    @pause_frame.setter
    def pause_frame(self, pause_frame):
        """Sets the pause_frame of this NLEJobType.


        :param pause_frame: The pause_frame of this NLEJobType.  # noqa: E501
        :type: int
        """

        self._pause_frame = pause_frame

    @property
    def frame_rate(self):
        """Gets the frame_rate of this NLEJobType.  # noqa: E501


        :return: The frame_rate of this NLEJobType.  # noqa: E501
        :rtype: FrameRateType
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this NLEJobType.


        :param frame_rate: The frame_rate of this NLEJobType.  # noqa: E501
        :type: FrameRateType
        """
        if frame_rate is None:
            raise ValueError("Invalid value for `frame_rate`, must not be `None`")  # noqa: E501

        self._frame_rate = frame_rate

    @property
    def audio_clip(self):
        """Gets the audio_clip of this NLEJobType.  # noqa: E501


        :return: The audio_clip of this NLEJobType.  # noqa: E501
        :rtype: list[AudioClipType]
        """
        return self._audio_clip

    @audio_clip.setter
    def audio_clip(self, audio_clip):
        """Sets the audio_clip of this NLEJobType.


        :param audio_clip: The audio_clip of this NLEJobType.  # noqa: E501
        :type: list[AudioClipType]
        """

        self._audio_clip = audio_clip

    @property
    def video_clip(self):
        """Gets the video_clip of this NLEJobType.  # noqa: E501


        :return: The video_clip of this NLEJobType.  # noqa: E501
        :rtype: list[VideoClipType]
        """
        return self._video_clip

    @video_clip.setter
    def video_clip(self, video_clip):
        """Sets the video_clip of this NLEJobType.


        :param video_clip: The video_clip of this NLEJobType.  # noqa: E501
        :type: list[VideoClipType]
        """

        self._video_clip = video_clip

    @property
    def height(self):
        """Gets the height of this NLEJobType.  # noqa: E501


        :return: The height of this NLEJobType.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this NLEJobType.


        :param height: The height of this NLEJobType.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def width(self):
        """Gets the width of this NLEJobType.  # noqa: E501


        :return: The width of this NLEJobType.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this NLEJobType.


        :param width: The width of this NLEJobType.  # noqa: E501
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def dar(self):
        """Gets the dar of this NLEJobType.  # noqa: E501


        :return: The dar of this NLEJobType.  # noqa: E501
        :rtype: AspectRatioType
        """
        return self._dar

    @dar.setter
    def dar(self, dar):
        """Sets the dar of this NLEJobType.


        :param dar: The dar of this NLEJobType.  # noqa: E501
        :type: AspectRatioType
        """
        if dar is None:
            raise ValueError("Invalid value for `dar`, must not be `None`")  # noqa: E501

        self._dar = dar

    @property
    def output(self):
        """Gets the output of this NLEJobType.  # noqa: E501


        :return: The output of this NLEJobType.  # noqa: E501
        :rtype: list[NLEJobOutputType]
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this NLEJobType.


        :param output: The output of this NLEJobType.  # noqa: E501
        :type: list[NLEJobOutputType]
        """

        self._output = output

    @property
    def sample_rate(self):
        """Gets the sample_rate of this NLEJobType.  # noqa: E501


        :return: The sample_rate of this NLEJobType.  # noqa: E501
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this NLEJobType.


        :param sample_rate: The sample_rate of this NLEJobType.  # noqa: E501
        :type: int
        """
        if sample_rate is None:
            raise ValueError("Invalid value for `sample_rate`, must not be `None`")  # noqa: E501

        self._sample_rate = sample_rate

    @property
    def subtitle_clip(self):
        """Gets the subtitle_clip of this NLEJobType.  # noqa: E501


        :return: The subtitle_clip of this NLEJobType.  # noqa: E501
        :rtype: list[SubtitleClipType]
        """
        return self._subtitle_clip

    @subtitle_clip.setter
    def subtitle_clip(self, subtitle_clip):
        """Sets the subtitle_clip of this NLEJobType.


        :param subtitle_clip: The subtitle_clip of this NLEJobType.  # noqa: E501
        :type: list[SubtitleClipType]
        """

        self._subtitle_clip = subtitle_clip

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
        if not isinstance(other, NLEJobType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other