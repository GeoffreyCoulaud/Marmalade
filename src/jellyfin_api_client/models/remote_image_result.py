from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remote_image_info import RemoteImageInfo


T = TypeVar("T", bound="RemoteImageResult")


@_attrs_define
class RemoteImageResult:
    """Class RemoteImageResult.

    Attributes:
        images (Union[Unset, None, List['RemoteImageInfo']]): Gets or sets the images.
        total_record_count (Union[Unset, int]): Gets or sets the total record count.
        providers (Union[Unset, None, List[str]]): Gets or sets the providers.
    """

    images: Union[Unset, None, List["RemoteImageInfo"]] = UNSET
    total_record_count: Union[Unset, int] = UNSET
    providers: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        images: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            if self.images is None:
                images = None
            else:
                images = []
                for images_item_data in self.images:
                    images_item = images_item_data.to_dict()

                    images.append(images_item)

        total_record_count = self.total_record_count
        providers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.providers, Unset):
            if self.providers is None:
                providers = None
            else:
                providers = self.providers

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if images is not UNSET:
            field_dict["Images"] = images
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count
        if providers is not UNSET:
            field_dict["Providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.remote_image_info import RemoteImageInfo

        d = src_dict.copy()
        images = []
        _images = d.pop("Images", UNSET)
        for images_item_data in _images or []:
            images_item = RemoteImageInfo.from_dict(images_item_data)

            images.append(images_item)

        total_record_count = d.pop("TotalRecordCount", UNSET)

        providers = cast(List[str], d.pop("Providers", UNSET))

        remote_image_result = cls(
            images=images,
            total_record_count=total_record_count,
            providers=providers,
        )

        return remote_image_result
