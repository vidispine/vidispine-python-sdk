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

class ComplexJobVideoOutputTypeAllOf(object):
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
        'gop_size': 'int',
        'force_cfr': 'bool',
        'disable_frame_dup_drop': 'bool',
        'display_y_offset': 'RationalType',
        'display_width': 'RationalType',
        'rc_initial_buffer_occupancy': 'int',
        'detect_faces': 'ComplexJobVideoOutputTypeAllOfDetectFaces',
        'max_bitrate': 'int',
        'generate_thumbnails': 'ComplexJobVideoOutputTypeAllOfGenerateThumbnails',
        'image_quality': 'int',
        'strip_parameter_sets': 'bool',
        'overlay': 'list[OverlayType]',
        'add_parameter_sets': 'bool',
        'generate_posters': 'ComplexJobVideoOutputTypeAllOfGeneratePosters',
        'display_x_offset': 'RationalType',
        'burn_timecode': 'bool',
        'scaling': 'ScalingType',
        'pixel_format': 'str',
        'parameter_sets': 'str',
        'text_overlay': 'list[TextOverlayType]',
        'level': 'int',
        'max_b_frames': 'int',
        'container_sar': 'AspectRatioType',
        'color_siting': 'int',
        'min_bitrate': 'int',
        'rc_buffer_size': 'int',
        'display_height': 'RationalType',
        'resolution': 'ResolutionType'
    }

    attribute_map = {
        'gop_size': 'gopSize',
        'force_cfr': 'forceCFR',
        'disable_frame_dup_drop': 'disableFrameDupDrop',
        'display_y_offset': 'displayYOffset',
        'display_width': 'displayWidth',
        'rc_initial_buffer_occupancy': 'rcInitialBufferOccupancy',
        'detect_faces': 'detectFaces',
        'max_bitrate': 'maxBitrate',
        'generate_thumbnails': 'generateThumbnails',
        'image_quality': 'imageQuality',
        'strip_parameter_sets': 'stripParameterSets',
        'overlay': 'overlay',
        'add_parameter_sets': 'addParameterSets',
        'generate_posters': 'generatePosters',
        'display_x_offset': 'displayXOffset',
        'burn_timecode': 'burnTimecode',
        'scaling': 'scaling',
        'pixel_format': 'pixelFormat',
        'parameter_sets': 'parameterSets',
        'text_overlay': 'textOverlay',
        'level': 'level',
        'max_b_frames': 'maxBFrames',
        'container_sar': 'containerSAR',
        'color_siting': 'colorSiting',
        'min_bitrate': 'minBitrate',
        'rc_buffer_size': 'rcBufferSize',
        'display_height': 'displayHeight',
        'resolution': 'resolution'
    }

    def __init__(self, gop_size=None, force_cfr=None, disable_frame_dup_drop=None, display_y_offset=None, display_width=None, rc_initial_buffer_occupancy=None, detect_faces=None, max_bitrate=None, generate_thumbnails=None, image_quality=None, strip_parameter_sets=None, overlay=None, add_parameter_sets=None, generate_posters=None, display_x_offset=None, burn_timecode=None, scaling=None, pixel_format=None, parameter_sets=None, text_overlay=None, level=None, max_b_frames=None, container_sar=None, color_siting=None, min_bitrate=None, rc_buffer_size=None, display_height=None, resolution=None):  # noqa: E501
        """ComplexJobVideoOutputTypeAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._gop_size = None
        self._force_cfr = None
        self._disable_frame_dup_drop = None
        self._display_y_offset = None
        self._display_width = None
        self._rc_initial_buffer_occupancy = None
        self._detect_faces = None
        self._max_bitrate = None
        self._generate_thumbnails = None
        self._image_quality = None
        self._strip_parameter_sets = None
        self._overlay = None
        self._add_parameter_sets = None
        self._generate_posters = None
        self._display_x_offset = None
        self._burn_timecode = None
        self._scaling = None
        self._pixel_format = None
        self._parameter_sets = None
        self._text_overlay = None
        self._level = None
        self._max_b_frames = None
        self._container_sar = None
        self._color_siting = None
        self._min_bitrate = None
        self._rc_buffer_size = None
        self._display_height = None
        self._resolution = None
        self.discriminator = None

        if gop_size is not None:
            self.gop_size = gop_size
        if force_cfr is not None:
            self.force_cfr = force_cfr
        if disable_frame_dup_drop is not None:
            self.disable_frame_dup_drop = disable_frame_dup_drop
        if display_y_offset is not None:
            self.display_y_offset = display_y_offset
        if display_width is not None:
            self.display_width = display_width
        if rc_initial_buffer_occupancy is not None:
            self.rc_initial_buffer_occupancy = rc_initial_buffer_occupancy
        if detect_faces is not None:
            self.detect_faces = detect_faces
        if max_bitrate is not None:
            self.max_bitrate = max_bitrate
        if generate_thumbnails is not None:
            self.generate_thumbnails = generate_thumbnails
        if image_quality is not None:
            self.image_quality = image_quality
        if strip_parameter_sets is not None:
            self.strip_parameter_sets = strip_parameter_sets
        if overlay is not None:
            self.overlay = overlay
        if add_parameter_sets is not None:
            self.add_parameter_sets = add_parameter_sets
        if generate_posters is not None:
            self.generate_posters = generate_posters
        if display_x_offset is not None:
            self.display_x_offset = display_x_offset
        if burn_timecode is not None:
            self.burn_timecode = burn_timecode
        if scaling is not None:
            self.scaling = scaling
        if pixel_format is not None:
            self.pixel_format = pixel_format
        if parameter_sets is not None:
            self.parameter_sets = parameter_sets
        if text_overlay is not None:
            self.text_overlay = text_overlay
        if level is not None:
            self.level = level
        if max_b_frames is not None:
            self.max_b_frames = max_b_frames
        if container_sar is not None:
            self.container_sar = container_sar
        if color_siting is not None:
            self.color_siting = color_siting
        if min_bitrate is not None:
            self.min_bitrate = min_bitrate
        if rc_buffer_size is not None:
            self.rc_buffer_size = rc_buffer_size
        if display_height is not None:
            self.display_height = display_height
        if resolution is not None:
            self.resolution = resolution

    @property
    def gop_size(self):
        """Gets the gop_size of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The gop_size of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._gop_size

    @gop_size.setter
    def gop_size(self, gop_size):
        """Sets the gop_size of this ComplexJobVideoOutputTypeAllOf.


        :param gop_size: The gop_size of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: int
        """

        self._gop_size = gop_size

    @property
    def force_cfr(self):
        """Gets the force_cfr of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The force_cfr of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._force_cfr

    @force_cfr.setter
    def force_cfr(self, force_cfr):
        """Sets the force_cfr of this ComplexJobVideoOutputTypeAllOf.


        :param force_cfr: The force_cfr of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._force_cfr = force_cfr

    @property
    def disable_frame_dup_drop(self):
        """Gets the disable_frame_dup_drop of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The disable_frame_dup_drop of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._disable_frame_dup_drop

    @disable_frame_dup_drop.setter
    def disable_frame_dup_drop(self, disable_frame_dup_drop):
        """Sets the disable_frame_dup_drop of this ComplexJobVideoOutputTypeAllOf.


        :param disable_frame_dup_drop: The disable_frame_dup_drop of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._disable_frame_dup_drop = disable_frame_dup_drop

    @property
    def display_y_offset(self):
        """Gets the display_y_offset of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The display_y_offset of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: RationalType
        """
        return self._display_y_offset

    @display_y_offset.setter
    def display_y_offset(self, display_y_offset):
        """Sets the display_y_offset of this ComplexJobVideoOutputTypeAllOf.


        :param display_y_offset: The display_y_offset of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: RationalType
        """

        self._display_y_offset = display_y_offset

    @property
    def display_width(self):
        """Gets the display_width of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The display_width of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: RationalType
        """
        return self._display_width

    @display_width.setter
    def display_width(self, display_width):
        """Sets the display_width of this ComplexJobVideoOutputTypeAllOf.


        :param display_width: The display_width of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: RationalType
        """

        self._display_width = display_width

    @property
    def rc_initial_buffer_occupancy(self):
        """Gets the rc_initial_buffer_occupancy of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The rc_initial_buffer_occupancy of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._rc_initial_buffer_occupancy

    @rc_initial_buffer_occupancy.setter
    def rc_initial_buffer_occupancy(self, rc_initial_buffer_occupancy):
        """Sets the rc_initial_buffer_occupancy of this ComplexJobVideoOutputTypeAllOf.


        :param rc_initial_buffer_occupancy: The rc_initial_buffer_occupancy of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: int
        """

        self._rc_initial_buffer_occupancy = rc_initial_buffer_occupancy

    @property
    def detect_faces(self):
        """Gets the detect_faces of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The detect_faces of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: ComplexJobVideoOutputTypeAllOfDetectFaces
        """
        return self._detect_faces

    @detect_faces.setter
    def detect_faces(self, detect_faces):
        """Sets the detect_faces of this ComplexJobVideoOutputTypeAllOf.


        :param detect_faces: The detect_faces of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: ComplexJobVideoOutputTypeAllOfDetectFaces
        """

        self._detect_faces = detect_faces

    @property
    def max_bitrate(self):
        """Gets the max_bitrate of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The max_bitrate of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._max_bitrate

    @max_bitrate.setter
    def max_bitrate(self, max_bitrate):
        """Sets the max_bitrate of this ComplexJobVideoOutputTypeAllOf.


        :param max_bitrate: The max_bitrate of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: int
        """

        self._max_bitrate = max_bitrate

    @property
    def generate_thumbnails(self):
        """Gets the generate_thumbnails of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The generate_thumbnails of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: ComplexJobVideoOutputTypeAllOfGenerateThumbnails
        """
        return self._generate_thumbnails

    @generate_thumbnails.setter
    def generate_thumbnails(self, generate_thumbnails):
        """Sets the generate_thumbnails of this ComplexJobVideoOutputTypeAllOf.


        :param generate_thumbnails: The generate_thumbnails of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: ComplexJobVideoOutputTypeAllOfGenerateThumbnails
        """

        self._generate_thumbnails = generate_thumbnails

    @property
    def image_quality(self):
        """Gets the image_quality of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The image_quality of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._image_quality

    @image_quality.setter
    def image_quality(self, image_quality):
        """Sets the image_quality of this ComplexJobVideoOutputTypeAllOf.


        :param image_quality: The image_quality of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: int
        """

        self._image_quality = image_quality

    @property
    def strip_parameter_sets(self):
        """Gets the strip_parameter_sets of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The strip_parameter_sets of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._strip_parameter_sets

    @strip_parameter_sets.setter
    def strip_parameter_sets(self, strip_parameter_sets):
        """Sets the strip_parameter_sets of this ComplexJobVideoOutputTypeAllOf.


        :param strip_parameter_sets: The strip_parameter_sets of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._strip_parameter_sets = strip_parameter_sets

    @property
    def overlay(self):
        """Gets the overlay of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The overlay of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: list[OverlayType]
        """
        return self._overlay

    @overlay.setter
    def overlay(self, overlay):
        """Sets the overlay of this ComplexJobVideoOutputTypeAllOf.


        :param overlay: The overlay of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: list[OverlayType]
        """

        self._overlay = overlay

    @property
    def add_parameter_sets(self):
        """Gets the add_parameter_sets of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The add_parameter_sets of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._add_parameter_sets

    @add_parameter_sets.setter
    def add_parameter_sets(self, add_parameter_sets):
        """Sets the add_parameter_sets of this ComplexJobVideoOutputTypeAllOf.


        :param add_parameter_sets: The add_parameter_sets of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._add_parameter_sets = add_parameter_sets

    @property
    def generate_posters(self):
        """Gets the generate_posters of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The generate_posters of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: ComplexJobVideoOutputTypeAllOfGeneratePosters
        """
        return self._generate_posters

    @generate_posters.setter
    def generate_posters(self, generate_posters):
        """Sets the generate_posters of this ComplexJobVideoOutputTypeAllOf.


        :param generate_posters: The generate_posters of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: ComplexJobVideoOutputTypeAllOfGeneratePosters
        """

        self._generate_posters = generate_posters

    @property
    def display_x_offset(self):
        """Gets the display_x_offset of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The display_x_offset of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: RationalType
        """
        return self._display_x_offset

    @display_x_offset.setter
    def display_x_offset(self, display_x_offset):
        """Sets the display_x_offset of this ComplexJobVideoOutputTypeAllOf.


        :param display_x_offset: The display_x_offset of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: RationalType
        """

        self._display_x_offset = display_x_offset

    @property
    def burn_timecode(self):
        """Gets the burn_timecode of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The burn_timecode of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._burn_timecode

    @burn_timecode.setter
    def burn_timecode(self, burn_timecode):
        """Sets the burn_timecode of this ComplexJobVideoOutputTypeAllOf.


        :param burn_timecode: The burn_timecode of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._burn_timecode = burn_timecode

    @property
    def scaling(self):
        """Gets the scaling of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The scaling of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: ScalingType
        """
        return self._scaling

    @scaling.setter
    def scaling(self, scaling):
        """Sets the scaling of this ComplexJobVideoOutputTypeAllOf.


        :param scaling: The scaling of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: ScalingType
        """

        self._scaling = scaling

    @property
    def pixel_format(self):
        """Gets the pixel_format of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The pixel_format of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._pixel_format

    @pixel_format.setter
    def pixel_format(self, pixel_format):
        """Sets the pixel_format of this ComplexJobVideoOutputTypeAllOf.


        :param pixel_format: The pixel_format of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: str
        """

        self._pixel_format = pixel_format

    @property
    def parameter_sets(self):
        """Gets the parameter_sets of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The parameter_sets of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._parameter_sets

    @parameter_sets.setter
    def parameter_sets(self, parameter_sets):
        """Sets the parameter_sets of this ComplexJobVideoOutputTypeAllOf.


        :param parameter_sets: The parameter_sets of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: str
        """

        self._parameter_sets = parameter_sets

    @property
    def text_overlay(self):
        """Gets the text_overlay of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The text_overlay of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: list[TextOverlayType]
        """
        return self._text_overlay

    @text_overlay.setter
    def text_overlay(self, text_overlay):
        """Sets the text_overlay of this ComplexJobVideoOutputTypeAllOf.


        :param text_overlay: The text_overlay of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: list[TextOverlayType]
        """

        self._text_overlay = text_overlay

    @property
    def level(self):
        """Gets the level of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The level of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ComplexJobVideoOutputTypeAllOf.


        :param level: The level of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def max_b_frames(self):
        """Gets the max_b_frames of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The max_b_frames of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._max_b_frames

    @max_b_frames.setter
    def max_b_frames(self, max_b_frames):
        """Sets the max_b_frames of this ComplexJobVideoOutputTypeAllOf.


        :param max_b_frames: The max_b_frames of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: int
        """

        self._max_b_frames = max_b_frames

    @property
    def container_sar(self):
        """Gets the container_sar of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The container_sar of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: AspectRatioType
        """
        return self._container_sar

    @container_sar.setter
    def container_sar(self, container_sar):
        """Sets the container_sar of this ComplexJobVideoOutputTypeAllOf.


        :param container_sar: The container_sar of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: AspectRatioType
        """

        self._container_sar = container_sar

    @property
    def color_siting(self):
        """Gets the color_siting of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The color_siting of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._color_siting

    @color_siting.setter
    def color_siting(self, color_siting):
        """Sets the color_siting of this ComplexJobVideoOutputTypeAllOf.


        :param color_siting: The color_siting of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: int
        """

        self._color_siting = color_siting

    @property
    def min_bitrate(self):
        """Gets the min_bitrate of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The min_bitrate of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, min_bitrate):
        """Sets the min_bitrate of this ComplexJobVideoOutputTypeAllOf.


        :param min_bitrate: The min_bitrate of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: int
        """

        self._min_bitrate = min_bitrate

    @property
    def rc_buffer_size(self):
        """Gets the rc_buffer_size of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The rc_buffer_size of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._rc_buffer_size

    @rc_buffer_size.setter
    def rc_buffer_size(self, rc_buffer_size):
        """Sets the rc_buffer_size of this ComplexJobVideoOutputTypeAllOf.


        :param rc_buffer_size: The rc_buffer_size of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: int
        """

        self._rc_buffer_size = rc_buffer_size

    @property
    def display_height(self):
        """Gets the display_height of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The display_height of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: RationalType
        """
        return self._display_height

    @display_height.setter
    def display_height(self, display_height):
        """Sets the display_height of this ComplexJobVideoOutputTypeAllOf.


        :param display_height: The display_height of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :type: RationalType
        """

        self._display_height = display_height

    @property
    def resolution(self):
        """Gets the resolution of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501


        :return: The resolution of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
        :rtype: ResolutionType
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ComplexJobVideoOutputTypeAllOf.


        :param resolution: The resolution of this ComplexJobVideoOutputTypeAllOf.  # noqa: E501
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
        if not isinstance(other, ComplexJobVideoOutputTypeAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
