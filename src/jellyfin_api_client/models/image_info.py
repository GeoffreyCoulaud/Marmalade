from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageInfo")


@_attrs_define
class ImageInfo:
    """Class ImageInfo.

    Attributes:
        image_type (Union[Unset, ImageType]): Enum ImageType.
        image_index (Union[Unset, None, int]): Gets or sets the index of the image.
        image_tag (Union[Unset, None, str]): Gets or sets the image tag.
        path (Union[Unset, None, str]): Gets or sets the path.
        blur_hash (Union[Unset, None, str]): Gets or sets the blurhash.
        height (Union[Unset, None, int]): Gets or sets the height.
        width (Union[Unset, None, int]): Gets or sets the width.
        size (Union[Unset, int]): Gets or sets the size.
    """

    image_type: Union[Unset, ImageType] = UNSET
    image_index: Union[Unset, None, int] = UNSET
    image_tag: Union[Unset, None, str] = UNSET
    path: Union[Unset, None, str] = UNSET
    blur_hash: Union[Unset, None, str] = UNSET
    height: Union[Unset, None, int] = UNSET
    width: Union[Unset, None, int] = UNSET
    size: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        image_type: Union[Unset, str] = UNSET
        if not isinstance(self.image_type, Unset):
            image_type = self.image_type.value

        image_index = self.image_index
        image_tag = self.image_tag
        path = self.path
        blur_hash = self.blur_hash
        height = self.height
        width = self.width
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if image_type is not UNSET:
            field_dict["ImageType"] = image_type
        if image_index is not UNSET:
            field_dict["ImageIndex"] = image_index
        if image_tag is not UNSET:
            field_dict["ImageTag"] = image_tag
        if path is not UNSET:
            field_dict["Path"] = path
        if blur_hash is not UNSET:
            field_dict["BlurHash"] = blur_hash
        if height is not UNSET:
            field_dict["Height"] = height
        if width is not UNSET:
            field_dict["Width"] = width
        if size is not UNSET:
            field_dict["Size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _image_type = d.pop("ImageType", UNSET)
        image_type: Union[Unset, ImageType]
        if isinstance(_image_type, Unset):
            image_type = UNSET
        else:
            image_type = ImageType(_image_type)

        image_index = d.pop("ImageIndex", UNSET)

        image_tag = d.pop("ImageTag", UNSET)

        path = d.pop("Path", UNSET)

        blur_hash = d.pop("BlurHash", UNSET)

        height = d.pop("Height", UNSET)

        width = d.pop("Width", UNSET)

        size = d.pop("Size", UNSET)

        image_info = cls(
            image_type=image_type,
            image_index=image_index,
            image_tag=image_tag,
            path=path,
            blur_hash=blur_hash,
            height=height,
            width=width,
            size=size,
        )

        return image_info
