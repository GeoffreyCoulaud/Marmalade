from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_option import ImageOption
    from ..models.library_option_info_dto import LibraryOptionInfoDto


T = TypeVar("T", bound="LibraryTypeOptionsDto")


@_attrs_define
class LibraryTypeOptionsDto:
    """Library type options dto.

    Attributes:
        type (Union[Unset, None, str]): Gets or sets the type.
        metadata_fetchers (Union[Unset, List['LibraryOptionInfoDto']]): Gets or sets the metadata fetchers.
        image_fetchers (Union[Unset, List['LibraryOptionInfoDto']]): Gets or sets the image fetchers.
        supported_image_types (Union[Unset, List[ImageType]]): Gets or sets the supported image types.
        default_image_options (Union[Unset, List['ImageOption']]): Gets or sets the default image options.
    """

    type: Union[Unset, None, str] = UNSET
    metadata_fetchers: Union[Unset, List["LibraryOptionInfoDto"]] = UNSET
    image_fetchers: Union[Unset, List["LibraryOptionInfoDto"]] = UNSET
    supported_image_types: Union[Unset, List[ImageType]] = UNSET
    default_image_options: Union[Unset, List["ImageOption"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        metadata_fetchers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata_fetchers, Unset):
            metadata_fetchers = []
            for metadata_fetchers_item_data in self.metadata_fetchers:
                metadata_fetchers_item = metadata_fetchers_item_data.to_dict()

                metadata_fetchers.append(metadata_fetchers_item)

        image_fetchers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.image_fetchers, Unset):
            image_fetchers = []
            for image_fetchers_item_data in self.image_fetchers:
                image_fetchers_item = image_fetchers_item_data.to_dict()

                image_fetchers.append(image_fetchers_item)

        supported_image_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.supported_image_types, Unset):
            supported_image_types = []
            for supported_image_types_item_data in self.supported_image_types:
                supported_image_types_item = supported_image_types_item_data.value

                supported_image_types.append(supported_image_types_item)

        default_image_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.default_image_options, Unset):
            default_image_options = []
            for default_image_options_item_data in self.default_image_options:
                default_image_options_item = default_image_options_item_data.to_dict()

                default_image_options.append(default_image_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if metadata_fetchers is not UNSET:
            field_dict["MetadataFetchers"] = metadata_fetchers
        if image_fetchers is not UNSET:
            field_dict["ImageFetchers"] = image_fetchers
        if supported_image_types is not UNSET:
            field_dict["SupportedImageTypes"] = supported_image_types
        if default_image_options is not UNSET:
            field_dict["DefaultImageOptions"] = default_image_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_option import ImageOption
        from ..models.library_option_info_dto import LibraryOptionInfoDto

        d = src_dict.copy()
        type = d.pop("Type", UNSET)

        metadata_fetchers = []
        _metadata_fetchers = d.pop("MetadataFetchers", UNSET)
        for metadata_fetchers_item_data in _metadata_fetchers or []:
            metadata_fetchers_item = LibraryOptionInfoDto.from_dict(metadata_fetchers_item_data)

            metadata_fetchers.append(metadata_fetchers_item)

        image_fetchers = []
        _image_fetchers = d.pop("ImageFetchers", UNSET)
        for image_fetchers_item_data in _image_fetchers or []:
            image_fetchers_item = LibraryOptionInfoDto.from_dict(image_fetchers_item_data)

            image_fetchers.append(image_fetchers_item)

        supported_image_types = []
        _supported_image_types = d.pop("SupportedImageTypes", UNSET)
        for supported_image_types_item_data in _supported_image_types or []:
            supported_image_types_item = ImageType(supported_image_types_item_data)

            supported_image_types.append(supported_image_types_item)

        default_image_options = []
        _default_image_options = d.pop("DefaultImageOptions", UNSET)
        for default_image_options_item_data in _default_image_options or []:
            default_image_options_item = ImageOption.from_dict(default_image_options_item_data)

            default_image_options.append(default_image_options_item)

        library_type_options_dto = cls(
            type=type,
            metadata_fetchers=metadata_fetchers,
            image_fetchers=image_fetchers,
            supported_image_types=supported_image_types,
            default_image_options=default_image_options,
        )

        return library_type_options_dto
