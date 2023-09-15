from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.music_video_info import MusicVideoInfo


T = TypeVar("T", bound="MusicVideoInfoRemoteSearchQuery")


@_attrs_define
class MusicVideoInfoRemoteSearchQuery:
    """
    Attributes:
        search_info (Union[Unset, None, MusicVideoInfo]):
        item_id (Union[Unset, str]):
        search_provider_name (Union[Unset, None, str]): Gets or sets the provider name to search within if set.
        include_disabled_providers (Union[Unset, bool]): Gets or sets a value indicating whether disabled providers
            should be included.
    """

    search_info: Union[Unset, None, "MusicVideoInfo"] = UNSET
    item_id: Union[Unset, str] = UNSET
    search_provider_name: Union[Unset, None, str] = UNSET
    include_disabled_providers: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        search_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.search_info, Unset):
            search_info = self.search_info.to_dict() if self.search_info else None

        item_id = self.item_id
        search_provider_name = self.search_provider_name
        include_disabled_providers = self.include_disabled_providers

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if search_info is not UNSET:
            field_dict["SearchInfo"] = search_info
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if search_provider_name is not UNSET:
            field_dict["SearchProviderName"] = search_provider_name
        if include_disabled_providers is not UNSET:
            field_dict["IncludeDisabledProviders"] = include_disabled_providers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.music_video_info import MusicVideoInfo

        d = src_dict.copy()
        _search_info = d.pop("SearchInfo", UNSET)
        search_info: Union[Unset, None, MusicVideoInfo]
        if _search_info is None:
            search_info = None
        elif isinstance(_search_info, Unset):
            search_info = UNSET
        else:
            search_info = MusicVideoInfo.from_dict(_search_info)

        item_id = d.pop("ItemId", UNSET)

        search_provider_name = d.pop("SearchProviderName", UNSET)

        include_disabled_providers = d.pop("IncludeDisabledProviders", UNSET)

        music_video_info_remote_search_query = cls(
            search_info=search_info,
            item_id=item_id,
            search_provider_name=search_provider_name,
            include_disabled_providers=include_disabled_providers,
        )

        return music_video_info_remote_search_query
