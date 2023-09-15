from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_person_image_blur_hashes import BaseItemPersonImageBlurHashes


T = TypeVar("T", bound="BaseItemPerson")


@_attrs_define
class BaseItemPerson:
    """This is used by the api to get information about a Person within a BaseItem.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        id (Union[Unset, str]): Gets or sets the identifier.
        role (Union[Unset, None, str]): Gets or sets the role.
        type (Union[Unset, None, str]): Gets or sets the type.
        primary_image_tag (Union[Unset, None, str]): Gets or sets the primary image tag.
        image_blur_hashes (Union[Unset, None, BaseItemPersonImageBlurHashes]): Gets or sets the primary image blurhash.
    """

    name: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    role: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    primary_image_tag: Union[Unset, None, str] = UNSET
    image_blur_hashes: Union[Unset, None, "BaseItemPersonImageBlurHashes"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        role = self.role
        type = self.type
        primary_image_tag = self.primary_image_tag
        image_blur_hashes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.image_blur_hashes, Unset):
            image_blur_hashes = self.image_blur_hashes.to_dict() if self.image_blur_hashes else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id
        if role is not UNSET:
            field_dict["Role"] = role
        if type is not UNSET:
            field_dict["Type"] = type
        if primary_image_tag is not UNSET:
            field_dict["PrimaryImageTag"] = primary_image_tag
        if image_blur_hashes is not UNSET:
            field_dict["ImageBlurHashes"] = image_blur_hashes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_person_image_blur_hashes import BaseItemPersonImageBlurHashes

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        id = d.pop("Id", UNSET)

        role = d.pop("Role", UNSET)

        type = d.pop("Type", UNSET)

        primary_image_tag = d.pop("PrimaryImageTag", UNSET)

        _image_blur_hashes = d.pop("ImageBlurHashes", UNSET)
        image_blur_hashes: Union[Unset, None, BaseItemPersonImageBlurHashes]
        if _image_blur_hashes is None:
            image_blur_hashes = None
        elif isinstance(_image_blur_hashes, Unset):
            image_blur_hashes = UNSET
        else:
            image_blur_hashes = BaseItemPersonImageBlurHashes.from_dict(_image_blur_hashes)

        base_item_person = cls(
            name=name,
            id=id,
            role=role,
            type=type,
            primary_image_tag=primary_image_tag,
            image_blur_hashes=image_blur_hashes,
        )

        return base_item_person
