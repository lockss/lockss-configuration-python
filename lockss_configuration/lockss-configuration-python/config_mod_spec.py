# coding: utf-8

"""
    LOCKSS Configuration Service REST API

    API of the LOCKSS Configuration REST Service  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: lockss-support@lockss.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ConfigModSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'header': 'str',
        'updates': 'dict(str, str)',
        'deletes': 'list[str]'
    }

    attribute_map = {
        'header': 'header',
        'updates': 'updates',
        'deletes': 'deletes'
    }

    def __init__(self, header=None, updates=None, deletes=None):  # noqa: E501
        """ConfigModSpec - a model defined in Swagger"""  # noqa: E501

        self._header = None
        self._updates = None
        self._deletes = None
        self.discriminator = None

        self.header = header
        self.updates = updates
        self.deletes = deletes

    @property
    def header(self):
        """Gets the header of this ConfigModSpec.  # noqa: E501

        A file header string  # noqa: E501

        :return: The header of this ConfigModSpec.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this ConfigModSpec.

        A file header string  # noqa: E501

        :param header: The header of this ConfigModSpec.  # noqa: E501
        :type: str
        """
        if header is None:
            raise ValueError("Invalid value for `header`, must not be `None`")  # noqa: E501

        self._header = header

    @property
    def updates(self):
        """Gets the updates of this ConfigModSpec.  # noqa: E501

        The map of configuration items that are modified  # noqa: E501

        :return: The updates of this ConfigModSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._updates

    @updates.setter
    def updates(self, updates):
        """Sets the updates of this ConfigModSpec.

        The map of configuration items that are modified  # noqa: E501

        :param updates: The updates of this ConfigModSpec.  # noqa: E501
        :type: dict(str, str)
        """
        if updates is None:
            raise ValueError("Invalid value for `updates`, must not be `None`")  # noqa: E501

        self._updates = updates

    @property
    def deletes(self):
        """Gets the deletes of this ConfigModSpec.  # noqa: E501

        The set of configuration keys to be deleted  # noqa: E501

        :return: The deletes of this ConfigModSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._deletes

    @deletes.setter
    def deletes(self, deletes):
        """Sets the deletes of this ConfigModSpec.

        The set of configuration keys to be deleted  # noqa: E501

        :param deletes: The deletes of this ConfigModSpec.  # noqa: E501
        :type: list[str]
        """
        if deletes is None:
            raise ValueError("Invalid value for `deletes`, must not be `None`")  # noqa: E501

        self._deletes = deletes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ConfigModSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigModSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
