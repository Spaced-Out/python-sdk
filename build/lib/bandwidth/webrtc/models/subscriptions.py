# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from bandwidth.webrtc.models.participant_subscription import ParticipantSubscription


class Subscriptions(object):

    """Implementation of the 'Subscriptions' model.

    TODO: type model description here.

    Attributes:
        session_id (string): Session the subscriptions are associated with  If
            this is the only field, the subscriber will be subscribed to all
            participants in the session (including any participants that are
            later added to the session)
        participants (list of ParticipantSubscription): Subset of participants
            to subscribe to in the session. Optional.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "session_id": 'sessionId',
        "participants": 'participants'
    }

    def __init__(self,
                 session_id=None,
                 participants=None):
        """Constructor for the Subscriptions class"""

        # Initialize members of the class
        self.session_id = session_id
        self.participants = participants

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
        session_id = dictionary.get('sessionId')
        participants = None
        if dictionary.get('participants') is not None:
            participants = [ParticipantSubscription.from_dictionary(x) for x in dictionary.get('participants')]

        # Return an object of this model
        return cls(session_id,
                   participants)