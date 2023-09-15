from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageProviderInfo")


@_attrs_define
class ImageProviderInfo:
    """Class ImageProviderInfo.

    Attributes:
        name (Union[Unset, str]): Gets the name.
        supported_images (Union[Unset, List[ImageType]]): Gets the supported image types.
    """

    name: Union[Unset, str] = UNSET
    supported_images: Union[Unset, List[ImageType]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        supported_images: Union[Unset, List[str]] = UNSET
        if not isinstance(self.supported_images, Unset):
            supported_images = []
            for supported_images_item_data in self.supported_images:
                supported_images_item = supported_images_item_data.value

                supported_images.append(supported_images_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if supported_images is not UNSET:
            field_dict["SupportedImages"] = supported_images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        supported_images = []
        _supported_images = d.pop("SupportedImages", UNSET)
        for supported_images_item_data in _supported_images or []:
            supported_images_item = ImageType(supported_images_item_data)

            supported_images.append(supported_images_item)

        image_provider_info = cls(
            name=name,
            supported_images=supported_images,
        )

        return image_provider_info
