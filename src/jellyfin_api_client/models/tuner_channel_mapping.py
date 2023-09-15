from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TunerChannelMapping")


@_attrs_define
class TunerChannelMapping:
    """
    Attributes:
        name (Union[Unset, None, str]):
        provider_channel_name (Union[Unset, None, str]):
        provider_channel_id (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    provider_channel_name: Union[Unset, None, str] = UNSET
    provider_channel_id: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        provider_channel_name = self.provider_channel_name
        provider_channel_id = self.provider_channel_id
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if provider_channel_name is not UNSET:
            field_dict["ProviderChannelName"] = provider_channel_name
        if provider_channel_id is not UNSET:
            field_dict["ProviderChannelId"] = provider_channel_id
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        provider_channel_name = d.pop("ProviderChannelName", UNSET)

        provider_channel_id = d.pop("ProviderChannelId", UNSET)

        id = d.pop("Id", UNSET)

        tuner_channel_mapping = cls(
            name=name,
            provider_channel_name=provider_channel_name,
            provider_channel_id=provider_channel_id,
            id=id,
        )

        return tuner_channel_mapping
