from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_id_pair import NameIdPair
    from ..models.name_value_pair import NameValuePair
    from ..models.tuner_channel_mapping import TunerChannelMapping


T = TypeVar("T", bound="ChannelMappingOptionsDto")


@_attrs_define
class ChannelMappingOptionsDto:
    """Channel mapping options dto.

    Attributes:
        tuner_channels (Union[Unset, List['TunerChannelMapping']]): Gets or sets list of tuner channels.
        provider_channels (Union[Unset, List['NameIdPair']]): Gets or sets list of provider channels.
        mappings (Union[Unset, List['NameValuePair']]): Gets or sets list of mappings.
        provider_name (Union[Unset, None, str]): Gets or sets provider name.
    """

    tuner_channels: Union[Unset, List["TunerChannelMapping"]] = UNSET
    provider_channels: Union[Unset, List["NameIdPair"]] = UNSET
    mappings: Union[Unset, List["NameValuePair"]] = UNSET
    provider_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tuner_channels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tuner_channels, Unset):
            tuner_channels = []
            for tuner_channels_item_data in self.tuner_channels:
                tuner_channels_item = tuner_channels_item_data.to_dict()

                tuner_channels.append(tuner_channels_item)

        provider_channels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.provider_channels, Unset):
            provider_channels = []
            for provider_channels_item_data in self.provider_channels:
                provider_channels_item = provider_channels_item_data.to_dict()

                provider_channels.append(provider_channels_item)

        mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = []
            for mappings_item_data in self.mappings:
                mappings_item = mappings_item_data.to_dict()

                mappings.append(mappings_item)

        provider_name = self.provider_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tuner_channels is not UNSET:
            field_dict["TunerChannels"] = tuner_channels
        if provider_channels is not UNSET:
            field_dict["ProviderChannels"] = provider_channels
        if mappings is not UNSET:
            field_dict["Mappings"] = mappings
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.name_id_pair import NameIdPair
        from ..models.name_value_pair import NameValuePair
        from ..models.tuner_channel_mapping import TunerChannelMapping

        d = src_dict.copy()
        tuner_channels = []
        _tuner_channels = d.pop("TunerChannels", UNSET)
        for tuner_channels_item_data in _tuner_channels or []:
            tuner_channels_item = TunerChannelMapping.from_dict(tuner_channels_item_data)

            tuner_channels.append(tuner_channels_item)

        provider_channels = []
        _provider_channels = d.pop("ProviderChannels", UNSET)
        for provider_channels_item_data in _provider_channels or []:
            provider_channels_item = NameIdPair.from_dict(provider_channels_item_data)

            provider_channels.append(provider_channels_item)

        mappings = []
        _mappings = d.pop("Mappings", UNSET)
        for mappings_item_data in _mappings or []:
            mappings_item = NameValuePair.from_dict(mappings_item_data)

            mappings.append(mappings_item)

        provider_name = d.pop("ProviderName", UNSET)

        channel_mapping_options_dto = cls(
            tuner_channels=tuner_channels,
            provider_channels=provider_channels,
            mappings=mappings,
            provider_name=provider_name,
        )

        return channel_mapping_options_dto
