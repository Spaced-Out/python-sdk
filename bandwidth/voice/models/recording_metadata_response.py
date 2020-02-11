# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
import bandwidth.voice.models.transcription


class RecordingMetadataResponse(object):

    """Implementation of the 'RecordingMetadataResponse' model.

    TODO: type model description here.

    Attributes:
        application_id (string): TODO: type description here.
        account_id (string): TODO: type description here.
        call_id (string): TODO: type description here.
        recording_id (string): TODO: type description here.
        to (string): TODO: type description here.
        mfrom (string): TODO: type description here.
        duration (string): Format is ISO-8601
        direction (DirectionEnum): TODO: type description here.
        channels (int): TODO: type description here.
        start_time (long|int): TODO: type description here.
        end_time (long|int): TODO: type description here.
        file_format (FileFormatEnum): TODO: type description here.
        status (StatusEnum): TODO: type description here.
        media_url (string): TODO: type description here.
        transcription (Transcription): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_id": 'applicationId',
        "account_id": 'accountId',
        "call_id": 'callId',
        "recording_id": 'recordingId',
        "to": 'to',
        "mfrom": 'from',
        "duration": 'duration',
        "direction": 'direction',
        "channels": 'channels',
        "start_time": 'startTime',
        "end_time": 'endTime',
        "file_format": 'fileFormat',
        "status": 'status',
        "media_url": 'mediaUrl',
        "transcription": 'transcription'
    }

    def __init__(self,
                 application_id=None,
                 account_id=None,
                 call_id=None,
                 recording_id=None,
                 to=None,
                 mfrom=None,
                 duration=None,
                 direction=None,
                 channels=None,
                 start_time=None,
                 end_time=None,
                 file_format=None,
                 status=None,
                 media_url=None,
                 transcription=None):
        """Constructor for the RecordingMetadataResponse class"""

        # Initialize members of the class
        self.application_id = application_id
        self.account_id = account_id
        self.call_id = call_id
        self.recording_id = recording_id
        self.to = to
        self.mfrom = mfrom
        self.duration = duration
        self.direction = direction
        self.channels = channels
        self.start_time = start_time
        self.end_time = end_time
        self.file_format = file_format
        self.status = status
        self.media_url = media_url
        self.transcription = transcription

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
        application_id = dictionary.get('applicationId')
        account_id = dictionary.get('accountId')
        call_id = dictionary.get('callId')
        recording_id = dictionary.get('recordingId')
        to = dictionary.get('to')
        mfrom = dictionary.get('from')
        duration = dictionary.get('duration')
        direction = dictionary.get('direction')
        channels = dictionary.get('channels')
        start_time = dictionary.get('startTime')
        end_time = dictionary.get('endTime')
        file_format = dictionary.get('fileFormat')
        status = dictionary.get('status')
        media_url = dictionary.get('mediaUrl')
        transcription = bandwidth.voice.models.transcription.Transcription.from_dictionary(dictionary.get('transcription')) if dictionary.get('transcription') else None

        # Return an object of this model
        return cls(application_id,
                   account_id,
                   call_id,
                   recording_id,
                   to,
                   mfrom,
                   duration,
                   direction,
                   channels,
                   start_time,
                   end_time,
                   file_format,
                   status,
                   media_url,
                   transcription)