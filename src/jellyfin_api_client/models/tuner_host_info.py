from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TunerHostInfo")


@_attrs_define
class TunerHostInfo:
    """
    Attributes:
        id (Union[Unset, None, str]):
        url (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        device_id (Union[Unset, None, str]):
        friendly_name (Union[Unset, None, str]):
        import_favorites_only (Union[Unset, bool]):
        allow_hw_transcoding (Union[Unset, bool]):
        enable_stream_looping (Union[Unset, bool]):
        source (Union[Unset, None, str]):
        tuner_count (Union[Unset, int]):
        user_agent (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    device_id: Union[Unset, None, str] = UNSET
    friendly_name: Union[Unset, None, str] = UNSET
    import_favorites_only: Union[Unset, bool] = UNSET
    allow_hw_transcoding: Union[Unset, bool] = UNSET
    enable_stream_looping: Union[Unset, bool] = UNSET
    source: Union[Unset, None, str] = UNSET
    tuner_count: Union[Unset, int] = UNSET
    user_agent: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        type = self.type
        device_id = self.device_id
        friendly_name = self.friendly_name
        import_favorites_only = self.import_favorites_only
        allow_hw_transcoding = self.allow_hw_transcoding
        enable_stream_looping = self.enable_stream_looping
        source = self.source
        tuner_count = self.tuner_count
        user_agent = self.user_agent

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if url is not UNSET:
            field_dict["Url"] = url
        if type is not UNSET:
            field_dict["Type"] = type
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if friendly_name is not UNSET:
            field_dict["FriendlyName"] = friendly_name
        if import_favorites_only is not UNSET:
            field_dict["ImportFavoritesOnly"] = import_favorites_only
        if allow_hw_transcoding is not UNSET:
            field_dict["AllowHWTranscoding"] = allow_hw_transcoding
        if enable_stream_looping is not UNSET:
            field_dict["EnableStreamLooping"] = enable_stream_looping
        if source is not UNSET:
            field_dict["Source"] = source
        if tuner_count is not UNSET:
            field_dict["TunerCount"] = tuner_count
        if user_agent is not UNSET:
            field_dict["UserAgent"] = user_agent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        url = d.pop("Url", UNSET)

        type = d.pop("Type", UNSET)

        device_id = d.pop("DeviceId", UNSET)

        friendly_name = d.pop("FriendlyName", UNSET)

        import_favorites_only = d.pop("ImportFavoritesOnly", UNSET)

        allow_hw_transcoding = d.pop("AllowHWTranscoding", UNSET)

        enable_stream_looping = d.pop("EnableStreamLooping", UNSET)

        source = d.pop("Source", UNSET)

        tuner_count = d.pop("TunerCount", UNSET)

        user_agent = d.pop("UserAgent", UNSET)

        tuner_host_info = cls(
            id=id,
            url=url,
            type=type,
            device_id=device_id,
            friendly_name=friendly_name,
            import_favorites_only=import_favorites_only,
            allow_hw_transcoding=allow_hw_transcoding,
            enable_stream_looping=enable_stream_looping,
            source=source,
            tuner_count=tuner_count,
            user_agent=user_agent,
        )

        return tuner_host_info
