from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.external_id_media_type import ExternalIdMediaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalIdInfo")


@_attrs_define
class ExternalIdInfo:
    """Represents the external id information for serialization to the client.

    Attributes:
        name (Union[Unset, str]): Gets or sets the display name of the external id provider (IE: IMDB, MusicBrainz,
            etc).
        key (Union[Unset, str]): Gets or sets the unique key for this id. This key should be unique across all
            providers.
        type (Union[Unset, None, ExternalIdMediaType]): The specific media type of an
            MediaBrowser.Model.Providers.ExternalIdInfo.
        url_format_string (Union[Unset, None, str]): Gets or sets the URL format string.
    """

    name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    type: Union[Unset, None, ExternalIdMediaType] = UNSET
    url_format_string: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        key = self.key
        type: Union[Unset, None, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value if self.type else None

        url_format_string = self.url_format_string

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if key is not UNSET:
            field_dict["Key"] = key
        if type is not UNSET:
            field_dict["Type"] = type
        if url_format_string is not UNSET:
            field_dict["UrlFormatString"] = url_format_string

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        key = d.pop("Key", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, None, ExternalIdMediaType]
        if _type is None:
            type = None
        elif isinstance(_type, Unset):
            type = UNSET
        else:
            type = ExternalIdMediaType(_type)

        url_format_string = d.pop("UrlFormatString", UNSET)

        external_id_info = cls(
            name=name,
            key=key,
            type=type,
            url_format_string=url_format_string,
        )

        return external_id_info
