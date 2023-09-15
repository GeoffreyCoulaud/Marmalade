from enum import Enum


class TranscodeReason(str, Enum):
    ANAMORPHICVIDEONOTSUPPORTED = "AnamorphicVideoNotSupported"
    AUDIOBITDEPTHNOTSUPPORTED = "AudioBitDepthNotSupported"
    AUDIOBITRATENOTSUPPORTED = "AudioBitrateNotSupported"
    AUDIOCHANNELSNOTSUPPORTED = "AudioChannelsNotSupported"
    AUDIOCODECNOTSUPPORTED = "AudioCodecNotSupported"
    AUDIOISEXTERNAL = "AudioIsExternal"
    AUDIOPROFILENOTSUPPORTED = "AudioProfileNotSupported"
    AUDIOSAMPLERATENOTSUPPORTED = "AudioSampleRateNotSupported"
    CONTAINERBITRATEEXCEEDSLIMIT = "ContainerBitrateExceedsLimit"
    CONTAINERNOTSUPPORTED = "ContainerNotSupported"
    DIRECTPLAYERROR = "DirectPlayError"
    INTERLACEDVIDEONOTSUPPORTED = "InterlacedVideoNotSupported"
    REFFRAMESNOTSUPPORTED = "RefFramesNotSupported"
    SECONDARYAUDIONOTSUPPORTED = "SecondaryAudioNotSupported"
    SUBTITLECODECNOTSUPPORTED = "SubtitleCodecNotSupported"
    UNKNOWNAUDIOSTREAMINFO = "UnknownAudioStreamInfo"
    UNKNOWNVIDEOSTREAMINFO = "UnknownVideoStreamInfo"
    VIDEOBITDEPTHNOTSUPPORTED = "VideoBitDepthNotSupported"
    VIDEOBITRATENOTSUPPORTED = "VideoBitrateNotSupported"
    VIDEOCODECNOTSUPPORTED = "VideoCodecNotSupported"
    VIDEOFRAMERATENOTSUPPORTED = "VideoFramerateNotSupported"
    VIDEOLEVELNOTSUPPORTED = "VideoLevelNotSupported"
    VIDEOPROFILENOTSUPPORTED = "VideoProfileNotSupported"
    VIDEORANGETYPENOTSUPPORTED = "VideoRangeTypeNotSupported"
    VIDEORESOLUTIONNOTSUPPORTED = "VideoResolutionNotSupported"

    def __str__(self) -> str:
        return str(self.value)
