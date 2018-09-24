# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Tags(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'application_tags': 'dict(str, str)',
        'user_defined_tags': 'dict(str, str)',
        'default_tags': 'dict(str, str)'
    }

    attribute_map = {
        'application_tags': 'applicationTags',
        'user_defined_tags': 'userDefinedTags',
        'default_tags': 'defaultTags'
    }

    def __init__(self, application_tags=None, user_defined_tags=None, default_tags=None):
        """
        Tags - a model defined in Swagger
        """

        self._application_tags = None
        self._user_defined_tags = None
        self._default_tags = None

        if application_tags is not None:
          self.application_tags = application_tags
        if user_defined_tags is not None:
          self.user_defined_tags = user_defined_tags
        if default_tags is not None:
          self.default_tags = default_tags

    @property
    def application_tags(self):
        """
        Gets the application_tags of this Tags.
        stack related application tags

        :return: The application_tags of this Tags.
        :rtype: dict(str, str)
        """
        return self._application_tags

    @application_tags.setter
    def application_tags(self, application_tags):
        """
        Sets the application_tags of this Tags.
        stack related application tags

        :param application_tags: The application_tags of this Tags.
        :type: dict(str, str)
        """

        self._application_tags = application_tags

    @property
    def user_defined_tags(self):
        """
        Gets the user_defined_tags of this Tags.
        stack related userdefined tags

        :return: The user_defined_tags of this Tags.
        :rtype: dict(str, str)
        """
        return self._user_defined_tags

    @user_defined_tags.setter
    def user_defined_tags(self, user_defined_tags):
        """
        Sets the user_defined_tags of this Tags.
        stack related userdefined tags

        :param user_defined_tags: The user_defined_tags of this Tags.
        :type: dict(str, str)
        """

        self._user_defined_tags = user_defined_tags

    @property
    def default_tags(self):
        """
        Gets the default_tags of this Tags.
        stack related default tags

        :return: The default_tags of this Tags.
        :rtype: dict(str, str)
        """
        return self._default_tags

    @default_tags.setter
    def default_tags(self, default_tags):
        """
        Sets the default_tags of this Tags.
        stack related default tags

        :param default_tags: The default_tags of this Tags.
        :type: dict(str, str)
        """

        self._default_tags = default_tags

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Tags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
