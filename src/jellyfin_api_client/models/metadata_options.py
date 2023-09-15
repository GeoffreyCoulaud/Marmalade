from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataOptions")


@_attrs_define
class MetadataOptions:
    """Class MetadataOptions.

    Attributes:
        item_type (Union[Unset, None, str]):
        disabled_metadata_savers (Union[Unset, None, List[str]]):
        local_metadata_reader_order (Union[Unset, None, List[str]]):
        disabled_metadata_fetchers (Union[Unset, None, List[str]]):
        metadata_fetcher_order (Union[Unset, None, List[str]]):
        disabled_image_fetchers (Union[Unset, None, List[str]]):
        image_fetcher_order (Union[Unset, None, List[str]]):
    """

    item_type: Union[Unset, None, str] = UNSET
    disabled_metadata_savers: Union[Unset, None, List[str]] = UNSET
    local_metadata_reader_order: Union[Unset, None, List[str]] = UNSET
    disabled_metadata_fetchers: Union[Unset, None, List[str]] = UNSET
    metadata_fetcher_order: Union[Unset, None, List[str]] = UNSET
    disabled_image_fetchers: Union[Unset, None, List[str]] = UNSET
    image_fetcher_order: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type = self.item_type
        disabled_metadata_savers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.disabled_metadata_savers, Unset):
            if self.disabled_metadata_savers is None:
                disabled_metadata_savers = None
            else:
                disabled_metadata_savers = self.disabled_metadata_savers

        local_metadata_reader_order: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.local_metadata_reader_order, Unset):
            if self.local_metadata_reader_order is None:
                local_metadata_reader_order = None
            else:
                local_metadata_reader_order = self.local_metadata_reader_order

        disabled_metadata_fetchers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.disabled_metadata_fetchers, Unset):
            if self.disabled_metadata_fetchers is None:
                disabled_metadata_fetchers = None
            else:
                disabled_metadata_fetchers = self.disabled_metadata_fetchers

        metadata_fetcher_order: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.metadata_fetcher_order, Unset):
            if self.metadata_fetcher_order is None:
                metadata_fetcher_order = None
            else:
                metadata_fetcher_order = self.metadata_fetcher_order

        disabled_image_fetchers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.disabled_image_fetchers, Unset):
            if self.disabled_image_fetchers is None:
                disabled_image_fetchers = None
            else:
                disabled_image_fetchers = self.disabled_image_fetchers

        image_fetcher_order: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.image_fetcher_order, Unset):
            if self.image_fetcher_order is None:
                image_fetcher_order = None
            else:
                image_fetcher_order = self.image_fetcher_order

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type
        if disabled_metadata_savers is not UNSET:
            field_dict["DisabledMetadataSavers"] = disabled_metadata_savers
        if local_metadata_reader_order is not UNSET:
            field_dict["LocalMetadataReaderOrder"] = local_metadata_reader_order
        if disabled_metadata_fetchers is not UNSET:
            field_dict["DisabledMetadataFetchers"] = disabled_metadata_fetchers
        if metadata_fetcher_order is not UNSET:
            field_dict["MetadataFetcherOrder"] = metadata_fetcher_order
        if disabled_image_fetchers is not UNSET:
            field_dict["DisabledImageFetchers"] = disabled_image_fetchers
        if image_fetcher_order is not UNSET:
            field_dict["ImageFetcherOrder"] = image_fetcher_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_type = d.pop("ItemType", UNSET)

        disabled_metadata_savers = cast(List[str], d.pop("DisabledMetadataSavers", UNSET))

        local_metadata_reader_order = cast(List[str], d.pop("LocalMetadataReaderOrder", UNSET))

        disabled_metadata_fetchers = cast(List[str], d.pop("DisabledMetadataFetchers", UNSET))

        metadata_fetcher_order = cast(List[str], d.pop("MetadataFetcherOrder", UNSET))

        disabled_image_fetchers = cast(List[str], d.pop("DisabledImageFetchers", UNSET))

        image_fetcher_order = cast(List[str], d.pop("ImageFetcherOrder", UNSET))

        metadata_options = cls(
            item_type=item_type,
            disabled_metadata_savers=disabled_metadata_savers,
            local_metadata_reader_order=local_metadata_reader_order,
            disabled_metadata_fetchers=disabled_metadata_fetchers,
            metadata_fetcher_order=metadata_fetcher_order,
            disabled_image_fetchers=disabled_image_fetchers,
            image_fetcher_order=image_fetcher_order,
        )

        return metadata_options
