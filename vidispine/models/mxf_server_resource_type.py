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

class MXFServerResourceType(object):
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
        'import_shapes': 'str',
        'database_name': 'str',
        'url': 'str',
        'description': 'str',
        'mxf_server_user_id': 'int',
        'enforce_quota': 'bool',
        'file_import_pattern': 'str',
        'mxf_server_path_to_storage': 'str',
        'atom_shapes': 'str',
        'user_workspace_url': 'str',
        'storage_id': 'str',
        'mxf_server_workspace_path': 'str',
        'detect_atom': 'bool',
        'workspace_url': 'str',
        'metadata': 'SimpleMetadataType'
    }

    attribute_map = {
        'import_shapes': 'importShapes',
        'database_name': 'databaseName',
        'url': 'url',
        'description': 'description',
        'mxf_server_user_id': 'mxfServerUserId',
        'enforce_quota': 'enforceQuota',
        'file_import_pattern': 'fileImportPattern',
        'mxf_server_path_to_storage': 'mxfServerPathToStorage',
        'atom_shapes': 'atomShapes',
        'user_workspace_url': 'userWorkspaceUrl',
        'storage_id': 'storageId',
        'mxf_server_workspace_path': 'mxfServerWorkspacePath',
        'detect_atom': 'detectAtom',
        'workspace_url': 'workspaceUrl',
        'metadata': 'metadata'
    }

    def __init__(self, import_shapes=None, database_name=None, url=None, description=None, mxf_server_user_id=None, enforce_quota=None, file_import_pattern=None, mxf_server_path_to_storage=None, atom_shapes=None, user_workspace_url=None, storage_id=None, mxf_server_workspace_path=None, detect_atom=None, workspace_url=None, metadata=None):  # noqa: E501
        """MXFServerResourceType - a model defined in OpenAPI"""  # noqa: E501

        self._import_shapes = None
        self._database_name = None
        self._url = None
        self._description = None
        self._mxf_server_user_id = None
        self._enforce_quota = None
        self._file_import_pattern = None
        self._mxf_server_path_to_storage = None
        self._atom_shapes = None
        self._user_workspace_url = None
        self._storage_id = None
        self._mxf_server_workspace_path = None
        self._detect_atom = None
        self._workspace_url = None
        self._metadata = None
        self.discriminator = None

        if import_shapes is not None:
            self.import_shapes = import_shapes
        self.database_name = database_name
        self.url = url
        if description is not None:
            self.description = description
        self.mxf_server_user_id = mxf_server_user_id
        if enforce_quota is not None:
            self.enforce_quota = enforce_quota
        if file_import_pattern is not None:
            self.file_import_pattern = file_import_pattern
        self.mxf_server_path_to_storage = mxf_server_path_to_storage
        if atom_shapes is not None:
            self.atom_shapes = atom_shapes
        self.user_workspace_url = user_workspace_url
        self.storage_id = storage_id
        self.mxf_server_workspace_path = mxf_server_workspace_path
        if detect_atom is not None:
            self.detect_atom = detect_atom
        self.workspace_url = workspace_url
        if metadata is not None:
            self.metadata = metadata

    @property
    def import_shapes(self):
        """Gets the import_shapes of this MXFServerResourceType.  # noqa: E501


        :return: The import_shapes of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._import_shapes

    @import_shapes.setter
    def import_shapes(self, import_shapes):
        """Sets the import_shapes of this MXFServerResourceType.


        :param import_shapes: The import_shapes of this MXFServerResourceType.  # noqa: E501
        :type: str
        """

        self._import_shapes = import_shapes

    @property
    def database_name(self):
        """Gets the database_name of this MXFServerResourceType.  # noqa: E501


        :return: The database_name of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this MXFServerResourceType.


        :param database_name: The database_name of this MXFServerResourceType.  # noqa: E501
        :type: str
        """
        if database_name is None:
            raise ValueError("Invalid value for `database_name`, must not be `None`")  # noqa: E501

        self._database_name = database_name

    @property
    def url(self):
        """Gets the url of this MXFServerResourceType.  # noqa: E501


        :return: The url of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MXFServerResourceType.


        :param url: The url of this MXFServerResourceType.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def description(self):
        """Gets the description of this MXFServerResourceType.  # noqa: E501


        :return: The description of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MXFServerResourceType.


        :param description: The description of this MXFServerResourceType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def mxf_server_user_id(self):
        """Gets the mxf_server_user_id of this MXFServerResourceType.  # noqa: E501


        :return: The mxf_server_user_id of this MXFServerResourceType.  # noqa: E501
        :rtype: int
        """
        return self._mxf_server_user_id

    @mxf_server_user_id.setter
    def mxf_server_user_id(self, mxf_server_user_id):
        """Sets the mxf_server_user_id of this MXFServerResourceType.


        :param mxf_server_user_id: The mxf_server_user_id of this MXFServerResourceType.  # noqa: E501
        :type: int
        """
        if mxf_server_user_id is None:
            raise ValueError("Invalid value for `mxf_server_user_id`, must not be `None`")  # noqa: E501

        self._mxf_server_user_id = mxf_server_user_id

    @property
    def enforce_quota(self):
        """Gets the enforce_quota of this MXFServerResourceType.  # noqa: E501


        :return: The enforce_quota of this MXFServerResourceType.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_quota

    @enforce_quota.setter
    def enforce_quota(self, enforce_quota):
        """Sets the enforce_quota of this MXFServerResourceType.


        :param enforce_quota: The enforce_quota of this MXFServerResourceType.  # noqa: E501
        :type: bool
        """

        self._enforce_quota = enforce_quota

    @property
    def file_import_pattern(self):
        """Gets the file_import_pattern of this MXFServerResourceType.  # noqa: E501


        :return: The file_import_pattern of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._file_import_pattern

    @file_import_pattern.setter
    def file_import_pattern(self, file_import_pattern):
        """Sets the file_import_pattern of this MXFServerResourceType.


        :param file_import_pattern: The file_import_pattern of this MXFServerResourceType.  # noqa: E501
        :type: str
        """

        self._file_import_pattern = file_import_pattern

    @property
    def mxf_server_path_to_storage(self):
        """Gets the mxf_server_path_to_storage of this MXFServerResourceType.  # noqa: E501


        :return: The mxf_server_path_to_storage of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._mxf_server_path_to_storage

    @mxf_server_path_to_storage.setter
    def mxf_server_path_to_storage(self, mxf_server_path_to_storage):
        """Sets the mxf_server_path_to_storage of this MXFServerResourceType.


        :param mxf_server_path_to_storage: The mxf_server_path_to_storage of this MXFServerResourceType.  # noqa: E501
        :type: str
        """
        if mxf_server_path_to_storage is None:
            raise ValueError("Invalid value for `mxf_server_path_to_storage`, must not be `None`")  # noqa: E501

        self._mxf_server_path_to_storage = mxf_server_path_to_storage

    @property
    def atom_shapes(self):
        """Gets the atom_shapes of this MXFServerResourceType.  # noqa: E501


        :return: The atom_shapes of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._atom_shapes

    @atom_shapes.setter
    def atom_shapes(self, atom_shapes):
        """Sets the atom_shapes of this MXFServerResourceType.


        :param atom_shapes: The atom_shapes of this MXFServerResourceType.  # noqa: E501
        :type: str
        """

        self._atom_shapes = atom_shapes

    @property
    def user_workspace_url(self):
        """Gets the user_workspace_url of this MXFServerResourceType.  # noqa: E501


        :return: The user_workspace_url of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._user_workspace_url

    @user_workspace_url.setter
    def user_workspace_url(self, user_workspace_url):
        """Sets the user_workspace_url of this MXFServerResourceType.


        :param user_workspace_url: The user_workspace_url of this MXFServerResourceType.  # noqa: E501
        :type: str
        """
        if user_workspace_url is None:
            raise ValueError("Invalid value for `user_workspace_url`, must not be `None`")  # noqa: E501

        self._user_workspace_url = user_workspace_url

    @property
    def storage_id(self):
        """Gets the storage_id of this MXFServerResourceType.  # noqa: E501


        :return: The storage_id of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this MXFServerResourceType.


        :param storage_id: The storage_id of this MXFServerResourceType.  # noqa: E501
        :type: str
        """
        if storage_id is None:
            raise ValueError("Invalid value for `storage_id`, must not be `None`")  # noqa: E501
        if storage_id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', storage_id):  # noqa: E501
            raise ValueError(r"Invalid value for `storage_id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._storage_id = storage_id

    @property
    def mxf_server_workspace_path(self):
        """Gets the mxf_server_workspace_path of this MXFServerResourceType.  # noqa: E501


        :return: The mxf_server_workspace_path of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._mxf_server_workspace_path

    @mxf_server_workspace_path.setter
    def mxf_server_workspace_path(self, mxf_server_workspace_path):
        """Sets the mxf_server_workspace_path of this MXFServerResourceType.


        :param mxf_server_workspace_path: The mxf_server_workspace_path of this MXFServerResourceType.  # noqa: E501
        :type: str
        """
        if mxf_server_workspace_path is None:
            raise ValueError("Invalid value for `mxf_server_workspace_path`, must not be `None`")  # noqa: E501

        self._mxf_server_workspace_path = mxf_server_workspace_path

    @property
    def detect_atom(self):
        """Gets the detect_atom of this MXFServerResourceType.  # noqa: E501


        :return: The detect_atom of this MXFServerResourceType.  # noqa: E501
        :rtype: bool
        """
        return self._detect_atom

    @detect_atom.setter
    def detect_atom(self, detect_atom):
        """Sets the detect_atom of this MXFServerResourceType.


        :param detect_atom: The detect_atom of this MXFServerResourceType.  # noqa: E501
        :type: bool
        """

        self._detect_atom = detect_atom

    @property
    def workspace_url(self):
        """Gets the workspace_url of this MXFServerResourceType.  # noqa: E501


        :return: The workspace_url of this MXFServerResourceType.  # noqa: E501
        :rtype: str
        """
        return self._workspace_url

    @workspace_url.setter
    def workspace_url(self, workspace_url):
        """Sets the workspace_url of this MXFServerResourceType.


        :param workspace_url: The workspace_url of this MXFServerResourceType.  # noqa: E501
        :type: str
        """
        if workspace_url is None:
            raise ValueError("Invalid value for `workspace_url`, must not be `None`")  # noqa: E501

        self._workspace_url = workspace_url

    @property
    def metadata(self):
        """Gets the metadata of this MXFServerResourceType.  # noqa: E501


        :return: The metadata of this MXFServerResourceType.  # noqa: E501
        :rtype: SimpleMetadataType
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MXFServerResourceType.


        :param metadata: The metadata of this MXFServerResourceType.  # noqa: E501
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
        if not isinstance(other, MXFServerResourceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
