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

class ResourceType(object):
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
        'vidinet': 'VidinetServiceType',
        'external_transcoder': 'ExternalTranscoderType',
        'network': 'NetworkType',
        'unknown': 'str',
        'cerify': 'CerifyType',
        'mxfserver': 'MXFServerResourceType',
        'transcoder': 'TranscoderType',
        'cloudconvert': 'CloudConvertType',
        'thumbnail': 'ThumbnailServiceType',
        'state': 'str',
        'signiant': 'SigniantType',
        'eidr': 'EidrType',
        'ldap': 'LDAPResourceType',
        'id': 'str',
        'finalcutserver': 'FinalCutServerType'
    }

    attribute_map = {
        'vidinet': 'vidinet',
        'external_transcoder': 'externalTranscoder',
        'network': 'network',
        'unknown': 'unknown',
        'cerify': 'cerify',
        'mxfserver': 'mxfserver',
        'transcoder': 'transcoder',
        'cloudconvert': 'cloudconvert',
        'thumbnail': 'thumbnail',
        'state': 'state',
        'signiant': 'signiant',
        'eidr': 'eidr',
        'ldap': 'ldap',
        'id': 'id',
        'finalcutserver': 'finalcutserver'
    }

    def __init__(self, vidinet=None, external_transcoder=None, network=None, unknown=None, cerify=None, mxfserver=None, transcoder=None, cloudconvert=None, thumbnail=None, state=None, signiant=None, eidr=None, ldap=None, id=None, finalcutserver=None):  # noqa: E501
        """ResourceType - a model defined in OpenAPI"""  # noqa: E501

        self._vidinet = None
        self._external_transcoder = None
        self._network = None
        self._unknown = None
        self._cerify = None
        self._mxfserver = None
        self._transcoder = None
        self._cloudconvert = None
        self._thumbnail = None
        self._state = None
        self._signiant = None
        self._eidr = None
        self._ldap = None
        self._id = None
        self._finalcutserver = None
        self.discriminator = None

        if vidinet is not None:
            self.vidinet = vidinet
        if external_transcoder is not None:
            self.external_transcoder = external_transcoder
        if network is not None:
            self.network = network
        if unknown is not None:
            self.unknown = unknown
        if cerify is not None:
            self.cerify = cerify
        if mxfserver is not None:
            self.mxfserver = mxfserver
        if transcoder is not None:
            self.transcoder = transcoder
        if cloudconvert is not None:
            self.cloudconvert = cloudconvert
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if state is not None:
            self.state = state
        if signiant is not None:
            self.signiant = signiant
        if eidr is not None:
            self.eidr = eidr
        if ldap is not None:
            self.ldap = ldap
        if id is not None:
            self.id = id
        if finalcutserver is not None:
            self.finalcutserver = finalcutserver

    @property
    def vidinet(self):
        """Gets the vidinet of this ResourceType.  # noqa: E501


        :return: The vidinet of this ResourceType.  # noqa: E501
        :rtype: VidinetServiceType
        """
        return self._vidinet

    @vidinet.setter
    def vidinet(self, vidinet):
        """Sets the vidinet of this ResourceType.


        :param vidinet: The vidinet of this ResourceType.  # noqa: E501
        :type: VidinetServiceType
        """

        self._vidinet = vidinet

    @property
    def external_transcoder(self):
        """Gets the external_transcoder of this ResourceType.  # noqa: E501


        :return: The external_transcoder of this ResourceType.  # noqa: E501
        :rtype: ExternalTranscoderType
        """
        return self._external_transcoder

    @external_transcoder.setter
    def external_transcoder(self, external_transcoder):
        """Sets the external_transcoder of this ResourceType.


        :param external_transcoder: The external_transcoder of this ResourceType.  # noqa: E501
        :type: ExternalTranscoderType
        """

        self._external_transcoder = external_transcoder

    @property
    def network(self):
        """Gets the network of this ResourceType.  # noqa: E501


        :return: The network of this ResourceType.  # noqa: E501
        :rtype: NetworkType
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this ResourceType.


        :param network: The network of this ResourceType.  # noqa: E501
        :type: NetworkType
        """

        self._network = network

    @property
    def unknown(self):
        """Gets the unknown of this ResourceType.  # noqa: E501


        :return: The unknown of this ResourceType.  # noqa: E501
        :rtype: str
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this ResourceType.


        :param unknown: The unknown of this ResourceType.  # noqa: E501
        :type: str
        """

        self._unknown = unknown

    @property
    def cerify(self):
        """Gets the cerify of this ResourceType.  # noqa: E501


        :return: The cerify of this ResourceType.  # noqa: E501
        :rtype: CerifyType
        """
        return self._cerify

    @cerify.setter
    def cerify(self, cerify):
        """Sets the cerify of this ResourceType.


        :param cerify: The cerify of this ResourceType.  # noqa: E501
        :type: CerifyType
        """

        self._cerify = cerify

    @property
    def mxfserver(self):
        """Gets the mxfserver of this ResourceType.  # noqa: E501


        :return: The mxfserver of this ResourceType.  # noqa: E501
        :rtype: MXFServerResourceType
        """
        return self._mxfserver

    @mxfserver.setter
    def mxfserver(self, mxfserver):
        """Sets the mxfserver of this ResourceType.


        :param mxfserver: The mxfserver of this ResourceType.  # noqa: E501
        :type: MXFServerResourceType
        """

        self._mxfserver = mxfserver

    @property
    def transcoder(self):
        """Gets the transcoder of this ResourceType.  # noqa: E501


        :return: The transcoder of this ResourceType.  # noqa: E501
        :rtype: TranscoderType
        """
        return self._transcoder

    @transcoder.setter
    def transcoder(self, transcoder):
        """Sets the transcoder of this ResourceType.


        :param transcoder: The transcoder of this ResourceType.  # noqa: E501
        :type: TranscoderType
        """

        self._transcoder = transcoder

    @property
    def cloudconvert(self):
        """Gets the cloudconvert of this ResourceType.  # noqa: E501


        :return: The cloudconvert of this ResourceType.  # noqa: E501
        :rtype: CloudConvertType
        """
        return self._cloudconvert

    @cloudconvert.setter
    def cloudconvert(self, cloudconvert):
        """Sets the cloudconvert of this ResourceType.


        :param cloudconvert: The cloudconvert of this ResourceType.  # noqa: E501
        :type: CloudConvertType
        """

        self._cloudconvert = cloudconvert

    @property
    def thumbnail(self):
        """Gets the thumbnail of this ResourceType.  # noqa: E501


        :return: The thumbnail of this ResourceType.  # noqa: E501
        :rtype: ThumbnailServiceType
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this ResourceType.


        :param thumbnail: The thumbnail of this ResourceType.  # noqa: E501
        :type: ThumbnailServiceType
        """

        self._thumbnail = thumbnail

    @property
    def state(self):
        """Gets the state of this ResourceType.  # noqa: E501


        :return: The state of this ResourceType.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ResourceType.


        :param state: The state of this ResourceType.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def signiant(self):
        """Gets the signiant of this ResourceType.  # noqa: E501


        :return: The signiant of this ResourceType.  # noqa: E501
        :rtype: SigniantType
        """
        return self._signiant

    @signiant.setter
    def signiant(self, signiant):
        """Sets the signiant of this ResourceType.


        :param signiant: The signiant of this ResourceType.  # noqa: E501
        :type: SigniantType
        """

        self._signiant = signiant

    @property
    def eidr(self):
        """Gets the eidr of this ResourceType.  # noqa: E501


        :return: The eidr of this ResourceType.  # noqa: E501
        :rtype: EidrType
        """
        return self._eidr

    @eidr.setter
    def eidr(self, eidr):
        """Sets the eidr of this ResourceType.


        :param eidr: The eidr of this ResourceType.  # noqa: E501
        :type: EidrType
        """

        self._eidr = eidr

    @property
    def ldap(self):
        """Gets the ldap of this ResourceType.  # noqa: E501


        :return: The ldap of this ResourceType.  # noqa: E501
        :rtype: LDAPResourceType
        """
        return self._ldap

    @ldap.setter
    def ldap(self, ldap):
        """Sets the ldap of this ResourceType.


        :param ldap: The ldap of this ResourceType.  # noqa: E501
        :type: LDAPResourceType
        """

        self._ldap = ldap

    @property
    def id(self):
        """Gets the id of this ResourceType.  # noqa: E501


        :return: The id of this ResourceType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceType.


        :param id: The id of this ResourceType.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._id = id

    @property
    def finalcutserver(self):
        """Gets the finalcutserver of this ResourceType.  # noqa: E501


        :return: The finalcutserver of this ResourceType.  # noqa: E501
        :rtype: FinalCutServerType
        """
        return self._finalcutserver

    @finalcutserver.setter
    def finalcutserver(self, finalcutserver):
        """Sets the finalcutserver of this ResourceType.


        :param finalcutserver: The finalcutserver of this ResourceType.  # noqa: E501
        :type: FinalCutServerType
        """

        self._finalcutserver = finalcutserver

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
        if not isinstance(other, ResourceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
