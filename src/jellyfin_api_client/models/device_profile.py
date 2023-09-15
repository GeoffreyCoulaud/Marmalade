from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.codec_profile import CodecProfile
    from ..models.container_profile import ContainerProfile
    from ..models.device_identification import DeviceIdentification
    from ..models.direct_play_profile import DirectPlayProfile
    from ..models.response_profile import ResponseProfile
    from ..models.subtitle_profile import SubtitleProfile
    from ..models.transcoding_profile import TranscodingProfile
    from ..models.xml_attribute import XmlAttribute


T = TypeVar("T", bound="DeviceProfile")


@_attrs_define
class DeviceProfile:
    """A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata which determines which content a certain device
    is able to play.
    <br />
    Specifically, it defines the supported <see
    cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
    <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including codec
    profiles and levels)
    the device is able to direct play (without transcoding or remuxing),
    as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
    transcode to</see> in case it isn't.

        Attributes:
            name (Union[Unset, None, str]): Gets or sets the name of this device profile.
            id (Union[Unset, None, str]): Gets or sets the Id.
            identification (Union[Unset, None, DeviceIdentification]):
            friendly_name (Union[Unset, None, str]): Gets or sets the friendly name of the device profile, which can be
                shown to users.
            manufacturer (Union[Unset, None, str]): Gets or sets the manufacturer of the device which this profile
                represents.
            manufacturer_url (Union[Unset, None, str]): Gets or sets an url for the manufacturer of the device which this
                profile represents.
            model_name (Union[Unset, None, str]): Gets or sets the model name of the device which this profile represents.
            model_description (Union[Unset, None, str]): Gets or sets the model description of the device which this profile
                represents.
            model_number (Union[Unset, None, str]): Gets or sets the model number of the device which this profile
                represents.
            model_url (Union[Unset, None, str]): Gets or sets the ModelUrl.
            serial_number (Union[Unset, None, str]): Gets or sets the serial number of the device which this profile
                represents.
            enable_album_art_in_didl (Union[Unset, bool]): Gets or sets a value indicating whether EnableAlbumArtInDidl.
            enable_single_album_art_limit (Union[Unset, bool]): Gets or sets a value indicating whether
                EnableSingleAlbumArtLimit.
            enable_single_subtitle_limit (Union[Unset, bool]): Gets or sets a value indicating whether
                EnableSingleSubtitleLimit.
            supported_media_types (Union[Unset, str]): Gets or sets the SupportedMediaTypes.
            user_id (Union[Unset, None, str]): Gets or sets the UserId.
            album_art_pn (Union[Unset, None, str]): Gets or sets the AlbumArtPn.
            max_album_art_width (Union[Unset, None, int]): Gets or sets the MaxAlbumArtWidth.
            max_album_art_height (Union[Unset, None, int]): Gets or sets the MaxAlbumArtHeight.
            max_icon_width (Union[Unset, None, int]): Gets or sets the maximum allowed width of embedded icons.
            max_icon_height (Union[Unset, None, int]): Gets or sets the maximum allowed height of embedded icons.
            max_streaming_bitrate (Union[Unset, None, int]): Gets or sets the maximum allowed bitrate for all streamed
                content.
            max_static_bitrate (Union[Unset, None, int]): Gets or sets the maximum allowed bitrate for statically streamed
                content (= direct played files).
            music_streaming_transcoding_bitrate (Union[Unset, None, int]): Gets or sets the maximum allowed bitrate for
                transcoded music streams.
            max_static_music_bitrate (Union[Unset, None, int]): Gets or sets the maximum allowed bitrate for statically
                streamed (= direct played) music files.
            sony_aggregation_flags (Union[Unset, None, str]): Gets or sets the content of the aggregationFlags element in
                the urn:schemas-sonycom:av namespace.
            protocol_info (Union[Unset, None, str]): Gets or sets the ProtocolInfo.
            timeline_offset_seconds (Union[Unset, int]): Gets or sets the TimelineOffsetSeconds.
            requires_plain_video_items (Union[Unset, bool]): Gets or sets a value indicating whether
                RequiresPlainVideoItems.
            requires_plain_folders (Union[Unset, bool]): Gets or sets a value indicating whether RequiresPlainFolders.
            enable_ms_media_receiver_registrar (Union[Unset, bool]): Gets or sets a value indicating whether
                EnableMSMediaReceiverRegistrar.
            ignore_transcode_byte_range_requests (Union[Unset, bool]): Gets or sets a value indicating whether
                IgnoreTranscodeByteRangeRequests.
            xml_root_attributes (Union[Unset, List['XmlAttribute']]): Gets or sets the XmlRootAttributes.
            direct_play_profiles (Union[Unset, List['DirectPlayProfile']]): Gets or sets the direct play profiles.
            transcoding_profiles (Union[Unset, List['TranscodingProfile']]): Gets or sets the transcoding profiles.
            container_profiles (Union[Unset, List['ContainerProfile']]): Gets or sets the container profiles.
            codec_profiles (Union[Unset, List['CodecProfile']]): Gets or sets the codec profiles.
            response_profiles (Union[Unset, List['ResponseProfile']]): Gets or sets the ResponseProfiles.
            subtitle_profiles (Union[Unset, List['SubtitleProfile']]): Gets or sets the subtitle profiles.
    """

    name: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, str] = UNSET
    identification: Union[Unset, None, "DeviceIdentification"] = UNSET
    friendly_name: Union[Unset, None, str] = UNSET
    manufacturer: Union[Unset, None, str] = UNSET
    manufacturer_url: Union[Unset, None, str] = UNSET
    model_name: Union[Unset, None, str] = UNSET
    model_description: Union[Unset, None, str] = UNSET
    model_number: Union[Unset, None, str] = UNSET
    model_url: Union[Unset, None, str] = UNSET
    serial_number: Union[Unset, None, str] = UNSET
    enable_album_art_in_didl: Union[Unset, bool] = False
    enable_single_album_art_limit: Union[Unset, bool] = False
    enable_single_subtitle_limit: Union[Unset, bool] = False
    supported_media_types: Union[Unset, str] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    album_art_pn: Union[Unset, None, str] = UNSET
    max_album_art_width: Union[Unset, None, int] = UNSET
    max_album_art_height: Union[Unset, None, int] = UNSET
    max_icon_width: Union[Unset, None, int] = UNSET
    max_icon_height: Union[Unset, None, int] = UNSET
    max_streaming_bitrate: Union[Unset, None, int] = UNSET
    max_static_bitrate: Union[Unset, None, int] = UNSET
    music_streaming_transcoding_bitrate: Union[Unset, None, int] = UNSET
    max_static_music_bitrate: Union[Unset, None, int] = UNSET
    sony_aggregation_flags: Union[Unset, None, str] = UNSET
    protocol_info: Union[Unset, None, str] = UNSET
    timeline_offset_seconds: Union[Unset, int] = 0
    requires_plain_video_items: Union[Unset, bool] = False
    requires_plain_folders: Union[Unset, bool] = False
    enable_ms_media_receiver_registrar: Union[Unset, bool] = False
    ignore_transcode_byte_range_requests: Union[Unset, bool] = False
    xml_root_attributes: Union[Unset, List["XmlAttribute"]] = UNSET
    direct_play_profiles: Union[Unset, List["DirectPlayProfile"]] = UNSET
    transcoding_profiles: Union[Unset, List["TranscodingProfile"]] = UNSET
    container_profiles: Union[Unset, List["ContainerProfile"]] = UNSET
    codec_profiles: Union[Unset, List["CodecProfile"]] = UNSET
    response_profiles: Union[Unset, List["ResponseProfile"]] = UNSET
    subtitle_profiles: Union[Unset, List["SubtitleProfile"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        identification: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.identification, Unset):
            identification = self.identification.to_dict() if self.identification else None

        friendly_name = self.friendly_name
        manufacturer = self.manufacturer
        manufacturer_url = self.manufacturer_url
        model_name = self.model_name
        model_description = self.model_description
        model_number = self.model_number
        model_url = self.model_url
        serial_number = self.serial_number
        enable_album_art_in_didl = self.enable_album_art_in_didl
        enable_single_album_art_limit = self.enable_single_album_art_limit
        enable_single_subtitle_limit = self.enable_single_subtitle_limit
        supported_media_types = self.supported_media_types
        user_id = self.user_id
        album_art_pn = self.album_art_pn
        max_album_art_width = self.max_album_art_width
        max_album_art_height = self.max_album_art_height
        max_icon_width = self.max_icon_width
        max_icon_height = self.max_icon_height
        max_streaming_bitrate = self.max_streaming_bitrate
        max_static_bitrate = self.max_static_bitrate
        music_streaming_transcoding_bitrate = self.music_streaming_transcoding_bitrate
        max_static_music_bitrate = self.max_static_music_bitrate
        sony_aggregation_flags = self.sony_aggregation_flags
        protocol_info = self.protocol_info
        timeline_offset_seconds = self.timeline_offset_seconds
        requires_plain_video_items = self.requires_plain_video_items
        requires_plain_folders = self.requires_plain_folders
        enable_ms_media_receiver_registrar = self.enable_ms_media_receiver_registrar
        ignore_transcode_byte_range_requests = self.ignore_transcode_byte_range_requests
        xml_root_attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.xml_root_attributes, Unset):
            xml_root_attributes = []
            for xml_root_attributes_item_data in self.xml_root_attributes:
                xml_root_attributes_item = xml_root_attributes_item_data.to_dict()

                xml_root_attributes.append(xml_root_attributes_item)

        direct_play_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.direct_play_profiles, Unset):
            direct_play_profiles = []
            for direct_play_profiles_item_data in self.direct_play_profiles:
                direct_play_profiles_item = direct_play_profiles_item_data.to_dict()

                direct_play_profiles.append(direct_play_profiles_item)

        transcoding_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transcoding_profiles, Unset):
            transcoding_profiles = []
            for transcoding_profiles_item_data in self.transcoding_profiles:
                transcoding_profiles_item = transcoding_profiles_item_data.to_dict()

                transcoding_profiles.append(transcoding_profiles_item)

        container_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.container_profiles, Unset):
            container_profiles = []
            for container_profiles_item_data in self.container_profiles:
                container_profiles_item = container_profiles_item_data.to_dict()

                container_profiles.append(container_profiles_item)

        codec_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.codec_profiles, Unset):
            codec_profiles = []
            for codec_profiles_item_data in self.codec_profiles:
                codec_profiles_item = codec_profiles_item_data.to_dict()

                codec_profiles.append(codec_profiles_item)

        response_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.response_profiles, Unset):
            response_profiles = []
            for response_profiles_item_data in self.response_profiles:
                response_profiles_item = response_profiles_item_data.to_dict()

                response_profiles.append(response_profiles_item)

        subtitle_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subtitle_profiles, Unset):
            subtitle_profiles = []
            for subtitle_profiles_item_data in self.subtitle_profiles:
                subtitle_profiles_item = subtitle_profiles_item_data.to_dict()

                subtitle_profiles.append(subtitle_profiles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id
        if identification is not UNSET:
            field_dict["Identification"] = identification
        if friendly_name is not UNSET:
            field_dict["FriendlyName"] = friendly_name
        if manufacturer is not UNSET:
            field_dict["Manufacturer"] = manufacturer
        if manufacturer_url is not UNSET:
            field_dict["ManufacturerUrl"] = manufacturer_url
        if model_name is not UNSET:
            field_dict["ModelName"] = model_name
        if model_description is not UNSET:
            field_dict["ModelDescription"] = model_description
        if model_number is not UNSET:
            field_dict["ModelNumber"] = model_number
        if model_url is not UNSET:
            field_dict["ModelUrl"] = model_url
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if enable_album_art_in_didl is not UNSET:
            field_dict["EnableAlbumArtInDidl"] = enable_album_art_in_didl
        if enable_single_album_art_limit is not UNSET:
            field_dict["EnableSingleAlbumArtLimit"] = enable_single_album_art_limit
        if enable_single_subtitle_limit is not UNSET:
            field_dict["EnableSingleSubtitleLimit"] = enable_single_subtitle_limit
        if supported_media_types is not UNSET:
            field_dict["SupportedMediaTypes"] = supported_media_types
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if album_art_pn is not UNSET:
            field_dict["AlbumArtPn"] = album_art_pn
        if max_album_art_width is not UNSET:
            field_dict["MaxAlbumArtWidth"] = max_album_art_width
        if max_album_art_height is not UNSET:
            field_dict["MaxAlbumArtHeight"] = max_album_art_height
        if max_icon_width is not UNSET:
            field_dict["MaxIconWidth"] = max_icon_width
        if max_icon_height is not UNSET:
            field_dict["MaxIconHeight"] = max_icon_height
        if max_streaming_bitrate is not UNSET:
            field_dict["MaxStreamingBitrate"] = max_streaming_bitrate
        if max_static_bitrate is not UNSET:
            field_dict["MaxStaticBitrate"] = max_static_bitrate
        if music_streaming_transcoding_bitrate is not UNSET:
            field_dict["MusicStreamingTranscodingBitrate"] = music_streaming_transcoding_bitrate
        if max_static_music_bitrate is not UNSET:
            field_dict["MaxStaticMusicBitrate"] = max_static_music_bitrate
        if sony_aggregation_flags is not UNSET:
            field_dict["SonyAggregationFlags"] = sony_aggregation_flags
        if protocol_info is not UNSET:
            field_dict["ProtocolInfo"] = protocol_info
        if timeline_offset_seconds is not UNSET:
            field_dict["TimelineOffsetSeconds"] = timeline_offset_seconds
        if requires_plain_video_items is not UNSET:
            field_dict["RequiresPlainVideoItems"] = requires_plain_video_items
        if requires_plain_folders is not UNSET:
            field_dict["RequiresPlainFolders"] = requires_plain_folders
        if enable_ms_media_receiver_registrar is not UNSET:
            field_dict["EnableMSMediaReceiverRegistrar"] = enable_ms_media_receiver_registrar
        if ignore_transcode_byte_range_requests is not UNSET:
            field_dict["IgnoreTranscodeByteRangeRequests"] = ignore_transcode_byte_range_requests
        if xml_root_attributes is not UNSET:
            field_dict["XmlRootAttributes"] = xml_root_attributes
        if direct_play_profiles is not UNSET:
            field_dict["DirectPlayProfiles"] = direct_play_profiles
        if transcoding_profiles is not UNSET:
            field_dict["TranscodingProfiles"] = transcoding_profiles
        if container_profiles is not UNSET:
            field_dict["ContainerProfiles"] = container_profiles
        if codec_profiles is not UNSET:
            field_dict["CodecProfiles"] = codec_profiles
        if response_profiles is not UNSET:
            field_dict["ResponseProfiles"] = response_profiles
        if subtitle_profiles is not UNSET:
            field_dict["SubtitleProfiles"] = subtitle_profiles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.codec_profile import CodecProfile
        from ..models.container_profile import ContainerProfile
        from ..models.device_identification import DeviceIdentification
        from ..models.direct_play_profile import DirectPlayProfile
        from ..models.response_profile import ResponseProfile
        from ..models.subtitle_profile import SubtitleProfile
        from ..models.transcoding_profile import TranscodingProfile
        from ..models.xml_attribute import XmlAttribute

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        id = d.pop("Id", UNSET)

        _identification = d.pop("Identification", UNSET)
        identification: Union[Unset, None, DeviceIdentification]
        if _identification is None:
            identification = None
        elif isinstance(_identification, Unset):
            identification = UNSET
        else:
            identification = DeviceIdentification.from_dict(_identification)

        friendly_name = d.pop("FriendlyName", UNSET)

        manufacturer = d.pop("Manufacturer", UNSET)

        manufacturer_url = d.pop("ManufacturerUrl", UNSET)

        model_name = d.pop("ModelName", UNSET)

        model_description = d.pop("ModelDescription", UNSET)

        model_number = d.pop("ModelNumber", UNSET)

        model_url = d.pop("ModelUrl", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        enable_album_art_in_didl = d.pop("EnableAlbumArtInDidl", UNSET)

        enable_single_album_art_limit = d.pop("EnableSingleAlbumArtLimit", UNSET)

        enable_single_subtitle_limit = d.pop("EnableSingleSubtitleLimit", UNSET)

        supported_media_types = d.pop("SupportedMediaTypes", UNSET)

        user_id = d.pop("UserId", UNSET)

        album_art_pn = d.pop("AlbumArtPn", UNSET)

        max_album_art_width = d.pop("MaxAlbumArtWidth", UNSET)

        max_album_art_height = d.pop("MaxAlbumArtHeight", UNSET)

        max_icon_width = d.pop("MaxIconWidth", UNSET)

        max_icon_height = d.pop("MaxIconHeight", UNSET)

        max_streaming_bitrate = d.pop("MaxStreamingBitrate", UNSET)

        max_static_bitrate = d.pop("MaxStaticBitrate", UNSET)

        music_streaming_transcoding_bitrate = d.pop("MusicStreamingTranscodingBitrate", UNSET)

        max_static_music_bitrate = d.pop("MaxStaticMusicBitrate", UNSET)

        sony_aggregation_flags = d.pop("SonyAggregationFlags", UNSET)

        protocol_info = d.pop("ProtocolInfo", UNSET)

        timeline_offset_seconds = d.pop("TimelineOffsetSeconds", UNSET)

        requires_plain_video_items = d.pop("RequiresPlainVideoItems", UNSET)

        requires_plain_folders = d.pop("RequiresPlainFolders", UNSET)

        enable_ms_media_receiver_registrar = d.pop("EnableMSMediaReceiverRegistrar", UNSET)

        ignore_transcode_byte_range_requests = d.pop("IgnoreTranscodeByteRangeRequests", UNSET)

        xml_root_attributes = []
        _xml_root_attributes = d.pop("XmlRootAttributes", UNSET)
        for xml_root_attributes_item_data in _xml_root_attributes or []:
            xml_root_attributes_item = XmlAttribute.from_dict(xml_root_attributes_item_data)

            xml_root_attributes.append(xml_root_attributes_item)

        direct_play_profiles = []
        _direct_play_profiles = d.pop("DirectPlayProfiles", UNSET)
        for direct_play_profiles_item_data in _direct_play_profiles or []:
            direct_play_profiles_item = DirectPlayProfile.from_dict(direct_play_profiles_item_data)

            direct_play_profiles.append(direct_play_profiles_item)

        transcoding_profiles = []
        _transcoding_profiles = d.pop("TranscodingProfiles", UNSET)
        for transcoding_profiles_item_data in _transcoding_profiles or []:
            transcoding_profiles_item = TranscodingProfile.from_dict(transcoding_profiles_item_data)

            transcoding_profiles.append(transcoding_profiles_item)

        container_profiles = []
        _container_profiles = d.pop("ContainerProfiles", UNSET)
        for container_profiles_item_data in _container_profiles or []:
            container_profiles_item = ContainerProfile.from_dict(container_profiles_item_data)

            container_profiles.append(container_profiles_item)

        codec_profiles = []
        _codec_profiles = d.pop("CodecProfiles", UNSET)
        for codec_profiles_item_data in _codec_profiles or []:
            codec_profiles_item = CodecProfile.from_dict(codec_profiles_item_data)

            codec_profiles.append(codec_profiles_item)

        response_profiles = []
        _response_profiles = d.pop("ResponseProfiles", UNSET)
        for response_profiles_item_data in _response_profiles or []:
            response_profiles_item = ResponseProfile.from_dict(response_profiles_item_data)

            response_profiles.append(response_profiles_item)

        subtitle_profiles = []
        _subtitle_profiles = d.pop("SubtitleProfiles", UNSET)
        for subtitle_profiles_item_data in _subtitle_profiles or []:
            subtitle_profiles_item = SubtitleProfile.from_dict(subtitle_profiles_item_data)

            subtitle_profiles.append(subtitle_profiles_item)

        device_profile = cls(
            name=name,
            id=id,
            identification=identification,
            friendly_name=friendly_name,
            manufacturer=manufacturer,
            manufacturer_url=manufacturer_url,
            model_name=model_name,
            model_description=model_description,
            model_number=model_number,
            model_url=model_url,
            serial_number=serial_number,
            enable_album_art_in_didl=enable_album_art_in_didl,
            enable_single_album_art_limit=enable_single_album_art_limit,
            enable_single_subtitle_limit=enable_single_subtitle_limit,
            supported_media_types=supported_media_types,
            user_id=user_id,
            album_art_pn=album_art_pn,
            max_album_art_width=max_album_art_width,
            max_album_art_height=max_album_art_height,
            max_icon_width=max_icon_width,
            max_icon_height=max_icon_height,
            max_streaming_bitrate=max_streaming_bitrate,
            max_static_bitrate=max_static_bitrate,
            music_streaming_transcoding_bitrate=music_streaming_transcoding_bitrate,
            max_static_music_bitrate=max_static_music_bitrate,
            sony_aggregation_flags=sony_aggregation_flags,
            protocol_info=protocol_info,
            timeline_offset_seconds=timeline_offset_seconds,
            requires_plain_video_items=requires_plain_video_items,
            requires_plain_folders=requires_plain_folders,
            enable_ms_media_receiver_registrar=enable_ms_media_receiver_registrar,
            ignore_transcode_byte_range_requests=ignore_transcode_byte_range_requests,
            xml_root_attributes=xml_root_attributes,
            direct_play_profiles=direct_play_profiles,
            transcoding_profiles=transcoding_profiles,
            container_profiles=container_profiles,
            codec_profiles=codec_profiles,
            response_profiles=response_profiles,
            subtitle_profiles=subtitle_profiles,
        )

        return device_profile
