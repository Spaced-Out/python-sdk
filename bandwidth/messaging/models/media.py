# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
import bandwidth.messaging.models.tag


class Media(object):

    """Implementation of the 'Media' model.

    TODO: type model description here.

    Attributes:
        input_stream (object): TODO: type description here.
        content (string): TODO: type description here.
        url (string): TODO: type description here.
        content_length (string): TODO: type description here.
        content_type (string): TODO: type description here.
        tags (list of Tag): TODO: type description here.
        user_id (string): TODO: type description here.
        media_name (string): TODO: type description here.
        media_id (string): TODO: type description here.
        cache_control (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "input_stream": 'inputStream',
        "content": 'content',
        "url": 'url',
        "content_length": 'contentLength',
        "content_type": 'contentType',
        "tags": 'tags',
        "user_id": 'userId',
        "media_name": 'mediaName',
        "media_id": 'mediaId',
        "cache_control": 'cacheControl'
    }

    def __init__(self,
                 input_stream=None,
                 content=None,
                 url=None,
                 content_length=None,
                 content_type=None,
                 tags=None,
                 user_id=None,
                 media_name=None,
                 media_id=None,
                 cache_control=None):
        """Constructor for the Media class"""

        # Initialize members of the class
        self.input_stream = input_stream
        self.content = content
        self.url = url
        self.content_length = content_length
        self.content_type = content_type
        self.tags = tags
        self.user_id = user_id
        self.media_name = media_name
        self.media_id = media_id
        self.cache_control = cache_control

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        input_stream = dictionary.get('inputStream')
        content = dictionary.get('content')
        url = dictionary.get('url')
        content_length = dictionary.get('contentLength')
        content_type = dictionary.get('contentType')
        tags = None
        if dictionary.get('tags') is not None:
            tags = [bandwidth.messaging.models.tag.Tag.from_dictionary(x) for x in dictionary.get('tags')]
        user_id = dictionary.get('userId')
        media_name = dictionary.get('mediaName')
        media_id = dictionary.get('mediaId')
        cache_control = dictionary.get('cacheControl')

        # Return an object of this model
        return cls(input_stream,
                   content,
                   url,
                   content_length,
                   content_type,
                   tags,
                   user_id,
                   media_name,
                   media_id,
                   cache_control)
