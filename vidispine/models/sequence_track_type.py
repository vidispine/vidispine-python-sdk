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

class SequenceTrackType(object):
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
        'audio': 'bool',
        'segment': 'list[SequenceMediaType]',
        'transition': 'list[SequenceTransitionType]'
    }

    attribute_map = {
        'audio': 'audio',
        'segment': 'segment',
        'transition': 'transition'
    }

    def __init__(self, audio=None, segment=None, transition=None):  # noqa: E501
        """SequenceTrackType - a model defined in OpenAPI"""  # noqa: E501

        self._audio = None
        self._segment = None
        self._transition = None
        self.discriminator = None

        if audio is not None:
            self.audio = audio
        if segment is not None:
            self.segment = segment
        if transition is not None:
            self.transition = transition

    @property
    def audio(self):
        """Gets the audio of this SequenceTrackType.  # noqa: E501


        :return: The audio of this SequenceTrackType.  # noqa: E501
        :rtype: bool
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this SequenceTrackType.


        :param audio: The audio of this SequenceTrackType.  # noqa: E501
        :type: bool
        """

        self._audio = audio

    @property
    def segment(self):
        """Gets the segment of this SequenceTrackType.  # noqa: E501


        :return: The segment of this SequenceTrackType.  # noqa: E501
        :rtype: list[SequenceMediaType]
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """Sets the segment of this SequenceTrackType.


        :param segment: The segment of this SequenceTrackType.  # noqa: E501
        :type: list[SequenceMediaType]
        """

        self._segment = segment

    @property
    def transition(self):
        """Gets the transition of this SequenceTrackType.  # noqa: E501


        :return: The transition of this SequenceTrackType.  # noqa: E501
        :rtype: list[SequenceTransitionType]
        """
        return self._transition

    @transition.setter
    def transition(self, transition):
        """Sets the transition of this SequenceTrackType.


        :param transition: The transition of this SequenceTrackType.  # noqa: E501
        :type: list[SequenceTransitionType]
        """

        self._transition = transition

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
        if not isinstance(other, SequenceTrackType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other