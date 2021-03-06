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

class ComplexJobVideoOutputTypeAllOfGenerateThumbnails(object):
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
        'min_delay': 'TimeCodeType',
        'max_delay': 'TimeCodeType',
        'detector_plugin': 'str',
        'bulky_metadata_uri': 'str',
        'uri': 'list[str]',
        'period': 'TimeCodeType',
        'background': 'str',
        'resolution': 'ResolutionType'
    }

    attribute_map = {
        'min_delay': 'minDelay',
        'max_delay': 'maxDelay',
        'detector_plugin': 'detectorPlugin',
        'bulky_metadata_uri': 'bulkyMetadataURI',
        'uri': 'uri',
        'period': 'period',
        'background': 'background',
        'resolution': 'resolution'
    }

    def __init__(self, min_delay=None, max_delay=None, detector_plugin=None, bulky_metadata_uri=None, uri=None, period=None, background=None, resolution=None):  # noqa: E501
        """ComplexJobVideoOutputTypeAllOfGenerateThumbnails - a model defined in OpenAPI"""  # noqa: E501

        self._min_delay = None
        self._max_delay = None
        self._detector_plugin = None
        self._bulky_metadata_uri = None
        self._uri = None
        self._period = None
        self._background = None
        self._resolution = None
        self.discriminator = None

        if min_delay is not None:
            self.min_delay = min_delay
        if max_delay is not None:
            self.max_delay = max_delay
        if detector_plugin is not None:
            self.detector_plugin = detector_plugin
        if bulky_metadata_uri is not None:
            self.bulky_metadata_uri = bulky_metadata_uri
        if uri is not None:
            self.uri = uri
        if period is not None:
            self.period = period
        if background is not None:
            self.background = background
        if resolution is not None:
            self.resolution = resolution

    @property
    def min_delay(self):
        """Gets the min_delay of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501


        :return: The min_delay of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :rtype: TimeCodeType
        """
        return self._min_delay

    @min_delay.setter
    def min_delay(self, min_delay):
        """Sets the min_delay of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.


        :param min_delay: The min_delay of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :type: TimeCodeType
        """

        self._min_delay = min_delay

    @property
    def max_delay(self):
        """Gets the max_delay of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501


        :return: The max_delay of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :rtype: TimeCodeType
        """
        return self._max_delay

    @max_delay.setter
    def max_delay(self, max_delay):
        """Sets the max_delay of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.


        :param max_delay: The max_delay of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :type: TimeCodeType
        """

        self._max_delay = max_delay

    @property
    def detector_plugin(self):
        """Gets the detector_plugin of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501


        :return: The detector_plugin of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :rtype: str
        """
        return self._detector_plugin

    @detector_plugin.setter
    def detector_plugin(self, detector_plugin):
        """Sets the detector_plugin of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.


        :param detector_plugin: The detector_plugin of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :type: str
        """

        self._detector_plugin = detector_plugin

    @property
    def bulky_metadata_uri(self):
        """Gets the bulky_metadata_uri of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501


        :return: The bulky_metadata_uri of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :rtype: str
        """
        return self._bulky_metadata_uri

    @bulky_metadata_uri.setter
    def bulky_metadata_uri(self, bulky_metadata_uri):
        """Sets the bulky_metadata_uri of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.


        :param bulky_metadata_uri: The bulky_metadata_uri of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :type: str
        """

        self._bulky_metadata_uri = bulky_metadata_uri

    @property
    def uri(self):
        """Gets the uri of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501


        :return: The uri of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :rtype: list[str]
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.


        :param uri: The uri of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :type: list[str]
        """

        self._uri = uri

    @property
    def period(self):
        """Gets the period of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501


        :return: The period of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :rtype: TimeCodeType
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.


        :param period: The period of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :type: TimeCodeType
        """

        self._period = period

    @property
    def background(self):
        """Gets the background of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501


        :return: The background of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :rtype: str
        """
        return self._background

    @background.setter
    def background(self, background):
        """Sets the background of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.


        :param background: The background of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :type: str
        """

        self._background = background

    @property
    def resolution(self):
        """Gets the resolution of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501


        :return: The resolution of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :rtype: ResolutionType
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.


        :param resolution: The resolution of this ComplexJobVideoOutputTypeAllOfGenerateThumbnails.  # noqa: E501
        :type: ResolutionType
        """

        self._resolution = resolution

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
        if not isinstance(other, ComplexJobVideoOutputTypeAllOfGenerateThumbnails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
