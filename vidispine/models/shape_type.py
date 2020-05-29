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

class ShapeType(object):
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
        'mime_type': 'list[str]',
        'video_component': 'list[VideoComponentType]',
        'uuid': 'str',
        'created': 'datetime',
        'audio_component': 'list[AudioComponentType]',
        'descriptor_component': 'list[DescriptorComponentType]',
        'essence_version': 'int',
        'binary_component': 'list[BinaryComponentType]',
        'subtitle_component': 'list[SubtitleComponentType]',
        'item': 'list[ShapeTypeItem]',
        'tag': 'list[str]',
        'container_component': 'ContainerComponentType',
        'id': 'str',
        'metadata': 'SimpleMetadataType'
    }

    attribute_map = {
        'mime_type': 'mimeType',
        'video_component': 'videoComponent',
        'uuid': 'uuid',
        'created': 'created',
        'audio_component': 'audioComponent',
        'descriptor_component': 'descriptorComponent',
        'essence_version': 'essenceVersion',
        'binary_component': 'binaryComponent',
        'subtitle_component': 'subtitleComponent',
        'item': 'item',
        'tag': 'tag',
        'container_component': 'containerComponent',
        'id': 'id',
        'metadata': 'metadata'
    }

    def __init__(self, mime_type=None, video_component=None, uuid=None, created=None, audio_component=None, descriptor_component=None, essence_version=None, binary_component=None, subtitle_component=None, item=None, tag=None, container_component=None, id=None, metadata=None):  # noqa: E501
        """ShapeType - a model defined in OpenAPI"""  # noqa: E501

        self._mime_type = None
        self._video_component = None
        self._uuid = None
        self._created = None
        self._audio_component = None
        self._descriptor_component = None
        self._essence_version = None
        self._binary_component = None
        self._subtitle_component = None
        self._item = None
        self._tag = None
        self._container_component = None
        self._id = None
        self._metadata = None
        self.discriminator = None

        if mime_type is not None:
            self.mime_type = mime_type
        if video_component is not None:
            self.video_component = video_component
        if uuid is not None:
            self.uuid = uuid
        if created is not None:
            self.created = created
        if audio_component is not None:
            self.audio_component = audio_component
        if descriptor_component is not None:
            self.descriptor_component = descriptor_component
        if essence_version is not None:
            self.essence_version = essence_version
        if binary_component is not None:
            self.binary_component = binary_component
        if subtitle_component is not None:
            self.subtitle_component = subtitle_component
        if item is not None:
            self.item = item
        if tag is not None:
            self.tag = tag
        if container_component is not None:
            self.container_component = container_component
        if id is not None:
            self.id = id
        if metadata is not None:
            self.metadata = metadata

    @property
    def mime_type(self):
        """Gets the mime_type of this ShapeType.  # noqa: E501


        :return: The mime_type of this ShapeType.  # noqa: E501
        :rtype: list[str]
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this ShapeType.


        :param mime_type: The mime_type of this ShapeType.  # noqa: E501
        :type: list[str]
        """

        self._mime_type = mime_type

    @property
    def video_component(self):
        """Gets the video_component of this ShapeType.  # noqa: E501


        :return: The video_component of this ShapeType.  # noqa: E501
        :rtype: list[VideoComponentType]
        """
        return self._video_component

    @video_component.setter
    def video_component(self, video_component):
        """Sets the video_component of this ShapeType.


        :param video_component: The video_component of this ShapeType.  # noqa: E501
        :type: list[VideoComponentType]
        """

        self._video_component = video_component

    @property
    def uuid(self):
        """Gets the uuid of this ShapeType.  # noqa: E501


        :return: The uuid of this ShapeType.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ShapeType.


        :param uuid: The uuid of this ShapeType.  # noqa: E501
        :type: str
        """
        if uuid is not None and not re.search(r'[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}', uuid):  # noqa: E501
            raise ValueError(r"Invalid value for `uuid`, must be a follow pattern or equal to `/[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}/`")  # noqa: E501

        self._uuid = uuid

    @property
    def created(self):
        """Gets the created of this ShapeType.  # noqa: E501


        :return: The created of this ShapeType.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShapeType.


        :param created: The created of this ShapeType.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def audio_component(self):
        """Gets the audio_component of this ShapeType.  # noqa: E501


        :return: The audio_component of this ShapeType.  # noqa: E501
        :rtype: list[AudioComponentType]
        """
        return self._audio_component

    @audio_component.setter
    def audio_component(self, audio_component):
        """Sets the audio_component of this ShapeType.


        :param audio_component: The audio_component of this ShapeType.  # noqa: E501
        :type: list[AudioComponentType]
        """

        self._audio_component = audio_component

    @property
    def descriptor_component(self):
        """Gets the descriptor_component of this ShapeType.  # noqa: E501


        :return: The descriptor_component of this ShapeType.  # noqa: E501
        :rtype: list[DescriptorComponentType]
        """
        return self._descriptor_component

    @descriptor_component.setter
    def descriptor_component(self, descriptor_component):
        """Sets the descriptor_component of this ShapeType.


        :param descriptor_component: The descriptor_component of this ShapeType.  # noqa: E501
        :type: list[DescriptorComponentType]
        """

        self._descriptor_component = descriptor_component

    @property
    def essence_version(self):
        """Gets the essence_version of this ShapeType.  # noqa: E501


        :return: The essence_version of this ShapeType.  # noqa: E501
        :rtype: int
        """
        return self._essence_version

    @essence_version.setter
    def essence_version(self, essence_version):
        """Sets the essence_version of this ShapeType.


        :param essence_version: The essence_version of this ShapeType.  # noqa: E501
        :type: int
        """

        self._essence_version = essence_version

    @property
    def binary_component(self):
        """Gets the binary_component of this ShapeType.  # noqa: E501


        :return: The binary_component of this ShapeType.  # noqa: E501
        :rtype: list[BinaryComponentType]
        """
        return self._binary_component

    @binary_component.setter
    def binary_component(self, binary_component):
        """Sets the binary_component of this ShapeType.


        :param binary_component: The binary_component of this ShapeType.  # noqa: E501
        :type: list[BinaryComponentType]
        """

        self._binary_component = binary_component

    @property
    def subtitle_component(self):
        """Gets the subtitle_component of this ShapeType.  # noqa: E501


        :return: The subtitle_component of this ShapeType.  # noqa: E501
        :rtype: list[SubtitleComponentType]
        """
        return self._subtitle_component

    @subtitle_component.setter
    def subtitle_component(self, subtitle_component):
        """Sets the subtitle_component of this ShapeType.


        :param subtitle_component: The subtitle_component of this ShapeType.  # noqa: E501
        :type: list[SubtitleComponentType]
        """

        self._subtitle_component = subtitle_component

    @property
    def item(self):
        """Gets the item of this ShapeType.  # noqa: E501


        :return: The item of this ShapeType.  # noqa: E501
        :rtype: list[ShapeTypeItem]
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this ShapeType.


        :param item: The item of this ShapeType.  # noqa: E501
        :type: list[ShapeTypeItem]
        """

        self._item = item

    @property
    def tag(self):
        """Gets the tag of this ShapeType.  # noqa: E501


        :return: The tag of this ShapeType.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ShapeType.


        :param tag: The tag of this ShapeType.  # noqa: E501
        :type: list[str]
        """

        self._tag = tag

    @property
    def container_component(self):
        """Gets the container_component of this ShapeType.  # noqa: E501


        :return: The container_component of this ShapeType.  # noqa: E501
        :rtype: ContainerComponentType
        """
        return self._container_component

    @container_component.setter
    def container_component(self, container_component):
        """Sets the container_component of this ShapeType.


        :param container_component: The container_component of this ShapeType.  # noqa: E501
        :type: ContainerComponentType
        """

        self._container_component = container_component

    @property
    def id(self):
        """Gets the id of this ShapeType.  # noqa: E501


        :return: The id of this ShapeType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShapeType.


        :param id: The id of this ShapeType.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this ShapeType.  # noqa: E501


        :return: The metadata of this ShapeType.  # noqa: E501
        :rtype: SimpleMetadataType
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ShapeType.


        :param metadata: The metadata of this ShapeType.  # noqa: E501
        :type: SimpleMetadataType
        """

        self._metadata = metadata

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
        if not isinstance(other, ShapeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other