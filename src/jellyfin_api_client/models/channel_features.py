from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.channel_item_sort_field import ChannelItemSortField
from ..models.channel_media_content_type import ChannelMediaContentType
from ..models.channel_media_type import ChannelMediaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelFeatures")


@_attrs_define
class ChannelFeatures:
    """
    Attributes:
        name (Union[Unset, str]): Gets or sets the name.
        id (Union[Unset, str]): Gets or sets the identifier.
        can_search (Union[Unset, bool]): Gets or sets a value indicating whether this instance can search.
        media_types (Union[Unset, List[ChannelMediaType]]): Gets or sets the media types.
        content_types (Union[Unset, List[ChannelMediaContentType]]): Gets or sets the content types.
        max_page_size (Union[Unset, None, int]): Gets or sets the maximum number of records the channel allows
            retrieving at a time.
        auto_refresh_levels (Union[Unset, None, int]): Gets or sets the automatic refresh levels.
        default_sort_fields (Union[Unset, List[ChannelItemSortField]]): Gets or sets the default sort orders.
        supports_sort_order_toggle (Union[Unset, bool]): Gets or sets a value indicating whether a sort
            ascending/descending toggle is supported.
        supports_latest_media (Union[Unset, bool]): Gets or sets a value indicating whether [supports latest media].
        can_filter (Union[Unset, bool]): Gets or sets a value indicating whether this instance can filter.
        supports_content_downloading (Union[Unset, bool]): Gets or sets a value indicating whether [supports content
            downloading].
    """

    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    can_search: Union[Unset, bool] = UNSET
    media_types: Union[Unset, List[ChannelMediaType]] = UNSET
    content_types: Union[Unset, List[ChannelMediaContentType]] = UNSET
    max_page_size: Union[Unset, None, int] = UNSET
    auto_refresh_levels: Union[Unset, None, int] = UNSET
    default_sort_fields: Union[Unset, List[ChannelItemSortField]] = UNSET
    supports_sort_order_toggle: Union[Unset, bool] = UNSET
    supports_latest_media: Union[Unset, bool] = UNSET
    can_filter: Union[Unset, bool] = UNSET
    supports_content_downloading: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        can_search = self.can_search
        media_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.media_types, Unset):
            media_types = []
            for media_types_item_data in self.media_types:
                media_types_item = media_types_item_data.value

                media_types.append(media_types_item)

        content_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.content_types, Unset):
            content_types = []
            for content_types_item_data in self.content_types:
                content_types_item = content_types_item_data.value

                content_types.append(content_types_item)

        max_page_size = self.max_page_size
        auto_refresh_levels = self.auto_refresh_levels
        default_sort_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.default_sort_fields, Unset):
            default_sort_fields = []
            for default_sort_fields_item_data in self.default_sort_fields:
                default_sort_fields_item = default_sort_fields_item_data.value

                default_sort_fields.append(default_sort_fields_item)

        supports_sort_order_toggle = self.supports_sort_order_toggle
        supports_latest_media = self.supports_latest_media
        can_filter = self.can_filter
        supports_content_downloading = self.supports_content_downloading

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id
        if can_search is not UNSET:
            field_dict["CanSearch"] = can_search
        if media_types is not UNSET:
            field_dict["MediaTypes"] = media_types
        if content_types is not UNSET:
            field_dict["ContentTypes"] = content_types
        if max_page_size is not UNSET:
            field_dict["MaxPageSize"] = max_page_size
        if auto_refresh_levels is not UNSET:
            field_dict["AutoRefreshLevels"] = auto_refresh_levels
        if default_sort_fields is not UNSET:
            field_dict["DefaultSortFields"] = default_sort_fields
        if supports_sort_order_toggle is not UNSET:
            field_dict["SupportsSortOrderToggle"] = supports_sort_order_toggle
        if supports_latest_media is not UNSET:
            field_dict["SupportsLatestMedia"] = supports_latest_media
        if can_filter is not UNSET:
            field_dict["CanFilter"] = can_filter
        if supports_content_downloading is not UNSET:
            field_dict["SupportsContentDownloading"] = supports_content_downloading

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        id = d.pop("Id", UNSET)

        can_search = d.pop("CanSearch", UNSET)

        media_types = []
        _media_types = d.pop("MediaTypes", UNSET)
        for media_types_item_data in _media_types or []:
            media_types_item = ChannelMediaType(media_types_item_data)

            media_types.append(media_types_item)

        content_types = []
        _content_types = d.pop("ContentTypes", UNSET)
        for content_types_item_data in _content_types or []:
            content_types_item = ChannelMediaContentType(content_types_item_data)

            content_types.append(content_types_item)

        max_page_size = d.pop("MaxPageSize", UNSET)

        auto_refresh_levels = d.pop("AutoRefreshLevels", UNSET)

        default_sort_fields = []
        _default_sort_fields = d.pop("DefaultSortFields", UNSET)
        for default_sort_fields_item_data in _default_sort_fields or []:
            default_sort_fields_item = ChannelItemSortField(default_sort_fields_item_data)

            default_sort_fields.append(default_sort_fields_item)

        supports_sort_order_toggle = d.pop("SupportsSortOrderToggle", UNSET)

        supports_latest_media = d.pop("SupportsLatestMedia", UNSET)

        can_filter = d.pop("CanFilter", UNSET)

        supports_content_downloading = d.pop("SupportsContentDownloading", UNSET)

        channel_features = cls(
            name=name,
            id=id,
            can_search=can_search,
            media_types=media_types,
            content_types=content_types,
            max_page_size=max_page_size,
            auto_refresh_levels=auto_refresh_levels,
            default_sort_fields=default_sort_fields,
            supports_sort_order_toggle=supports_sort_order_toggle,
            supports_latest_media=supports_latest_media,
            can_filter=can_filter,
            supports_content_downloading=supports_content_downloading,
        )

        return channel_features
