from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_option import ImageOption


T = TypeVar("T", bound="TypeOptions")


@_attrs_define
class TypeOptions:
    """
    Attributes:
        type (Union[Unset, None, str]):
        metadata_fetchers (Union[Unset, None, List[str]]):
        metadata_fetcher_order (Union[Unset, None, List[str]]):
        image_fetchers (Union[Unset, None, List[str]]):
        image_fetcher_order (Union[Unset, None, List[str]]):
        image_options (Union[Unset, None, List['ImageOption']]):
    """

    type: Union[Unset, None, str] = UNSET
    metadata_fetchers: Union[Unset, None, List[str]] = UNSET
    metadata_fetcher_order: Union[Unset, None, List[str]] = UNSET
    image_fetchers: Union[Unset, None, List[str]] = UNSET
    image_fetcher_order: Union[Unset, None, List[str]] = UNSET
    image_options: Union[Unset, None, List["ImageOption"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        metadata_fetchers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.metadata_fetchers, Unset):
            if self.metadata_fetchers is None:
                metadata_fetchers = None
            else:
                metadata_fetchers = self.metadata_fetchers

        metadata_fetcher_order: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.metadata_fetcher_order, Unset):
            if self.metadata_fetcher_order is None:
                metadata_fetcher_order = None
            else:
                metadata_fetcher_order = self.metadata_fetcher_order

        image_fetchers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.image_fetchers, Unset):
            if self.image_fetchers is None:
                image_fetchers = None
            else:
                image_fetchers = self.image_fetchers

        image_fetcher_order: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.image_fetcher_order, Unset):
            if self.image_fetcher_order is None:
                image_fetcher_order = None
            else:
                image_fetcher_order = self.image_fetcher_order

        image_options: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.image_options, Unset):
            if self.image_options is None:
                image_options = None
            else:
                image_options = []
                for image_options_item_data in self.image_options:
                    image_options_item = image_options_item_data.to_dict()

                    image_options.append(image_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if metadata_fetchers is not UNSET:
            field_dict["MetadataFetchers"] = metadata_fetchers
        if metadata_fetcher_order is not UNSET:
            field_dict["MetadataFetcherOrder"] = metadata_fetcher_order
        if image_fetchers is not UNSET:
            field_dict["ImageFetchers"] = image_fetchers
        if image_fetcher_order is not UNSET:
            field_dict["ImageFetcherOrder"] = image_fetcher_order
        if image_options is not UNSET:
            field_dict["ImageOptions"] = image_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_option import ImageOption

        d = src_dict.copy()
        type = d.pop("Type", UNSET)

        metadata_fetchers = cast(List[str], d.pop("MetadataFetchers", UNSET))

        metadata_fetcher_order = cast(List[str], d.pop("MetadataFetcherOrder", UNSET))

        image_fetchers = cast(List[str], d.pop("ImageFetchers", UNSET))

        image_fetcher_order = cast(List[str], d.pop("ImageFetcherOrder", UNSET))

        image_options = []
        _image_options = d.pop("ImageOptions", UNSET)
        for image_options_item_data in _image_options or []:
            image_options_item = ImageOption.from_dict(image_options_item_data)

            image_options.append(image_options_item)

        type_options = cls(
            type=type,
            metadata_fetchers=metadata_fetchers,
            metadata_fetcher_order=metadata_fetcher_order,
            image_fetchers=image_fetchers,
            image_fetcher_order=image_fetcher_order,
            image_options=image_options,
        )

        return type_options
