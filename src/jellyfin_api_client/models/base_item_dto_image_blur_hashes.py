from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_dto_image_blur_hashes_art import BaseItemDtoImageBlurHashesArt
    from ..models.base_item_dto_image_blur_hashes_backdrop import BaseItemDtoImageBlurHashesBackdrop
    from ..models.base_item_dto_image_blur_hashes_banner import BaseItemDtoImageBlurHashesBanner
    from ..models.base_item_dto_image_blur_hashes_box import BaseItemDtoImageBlurHashesBox
    from ..models.base_item_dto_image_blur_hashes_box_rear import BaseItemDtoImageBlurHashesBoxRear
    from ..models.base_item_dto_image_blur_hashes_chapter import BaseItemDtoImageBlurHashesChapter
    from ..models.base_item_dto_image_blur_hashes_disc import BaseItemDtoImageBlurHashesDisc
    from ..models.base_item_dto_image_blur_hashes_logo import BaseItemDtoImageBlurHashesLogo
    from ..models.base_item_dto_image_blur_hashes_menu import BaseItemDtoImageBlurHashesMenu
    from ..models.base_item_dto_image_blur_hashes_primary import BaseItemDtoImageBlurHashesPrimary
    from ..models.base_item_dto_image_blur_hashes_profile import BaseItemDtoImageBlurHashesProfile
    from ..models.base_item_dto_image_blur_hashes_screenshot import BaseItemDtoImageBlurHashesScreenshot
    from ..models.base_item_dto_image_blur_hashes_thumb import BaseItemDtoImageBlurHashesThumb


T = TypeVar("T", bound="BaseItemDtoImageBlurHashes")


@_attrs_define
class BaseItemDtoImageBlurHashes:
    """Gets or sets the blurhashes for the image tags.
    Maps image type to dictionary mapping image tag to blurhash value.

        Attributes:
            primary (Union[Unset, BaseItemDtoImageBlurHashesPrimary]):
            art (Union[Unset, BaseItemDtoImageBlurHashesArt]):
            backdrop (Union[Unset, BaseItemDtoImageBlurHashesBackdrop]):
            banner (Union[Unset, BaseItemDtoImageBlurHashesBanner]):
            logo (Union[Unset, BaseItemDtoImageBlurHashesLogo]):
            thumb (Union[Unset, BaseItemDtoImageBlurHashesThumb]):
            disc (Union[Unset, BaseItemDtoImageBlurHashesDisc]):
            box (Union[Unset, BaseItemDtoImageBlurHashesBox]):
            screenshot (Union[Unset, BaseItemDtoImageBlurHashesScreenshot]):
            menu (Union[Unset, BaseItemDtoImageBlurHashesMenu]):
            chapter (Union[Unset, BaseItemDtoImageBlurHashesChapter]):
            box_rear (Union[Unset, BaseItemDtoImageBlurHashesBoxRear]):
            profile (Union[Unset, BaseItemDtoImageBlurHashesProfile]):
    """

    primary: Union[Unset, "BaseItemDtoImageBlurHashesPrimary"] = UNSET
    art: Union[Unset, "BaseItemDtoImageBlurHashesArt"] = UNSET
    backdrop: Union[Unset, "BaseItemDtoImageBlurHashesBackdrop"] = UNSET
    banner: Union[Unset, "BaseItemDtoImageBlurHashesBanner"] = UNSET
    logo: Union[Unset, "BaseItemDtoImageBlurHashesLogo"] = UNSET
    thumb: Union[Unset, "BaseItemDtoImageBlurHashesThumb"] = UNSET
    disc: Union[Unset, "BaseItemDtoImageBlurHashesDisc"] = UNSET
    box: Union[Unset, "BaseItemDtoImageBlurHashesBox"] = UNSET
    screenshot: Union[Unset, "BaseItemDtoImageBlurHashesScreenshot"] = UNSET
    menu: Union[Unset, "BaseItemDtoImageBlurHashesMenu"] = UNSET
    chapter: Union[Unset, "BaseItemDtoImageBlurHashesChapter"] = UNSET
    box_rear: Union[Unset, "BaseItemDtoImageBlurHashesBoxRear"] = UNSET
    profile: Union[Unset, "BaseItemDtoImageBlurHashesProfile"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        primary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.primary, Unset):
            primary = self.primary.to_dict()

        art: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.art, Unset):
            art = self.art.to_dict()

        backdrop: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.backdrop, Unset):
            backdrop = self.backdrop.to_dict()

        banner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.banner, Unset):
            banner = self.banner.to_dict()

        logo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.logo, Unset):
            logo = self.logo.to_dict()

        thumb: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.thumb, Unset):
            thumb = self.thumb.to_dict()

        disc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disc, Unset):
            disc = self.disc.to_dict()

        box: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.box, Unset):
            box = self.box.to_dict()

        screenshot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.screenshot, Unset):
            screenshot = self.screenshot.to_dict()

        menu: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.menu, Unset):
            menu = self.menu.to_dict()

        chapter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chapter, Unset):
            chapter = self.chapter.to_dict()

        box_rear: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.box_rear, Unset):
            box_rear = self.box_rear.to_dict()

        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary is not UNSET:
            field_dict["Primary"] = primary
        if art is not UNSET:
            field_dict["Art"] = art
        if backdrop is not UNSET:
            field_dict["Backdrop"] = backdrop
        if banner is not UNSET:
            field_dict["Banner"] = banner
        if logo is not UNSET:
            field_dict["Logo"] = logo
        if thumb is not UNSET:
            field_dict["Thumb"] = thumb
        if disc is not UNSET:
            field_dict["Disc"] = disc
        if box is not UNSET:
            field_dict["Box"] = box
        if screenshot is not UNSET:
            field_dict["Screenshot"] = screenshot
        if menu is not UNSET:
            field_dict["Menu"] = menu
        if chapter is not UNSET:
            field_dict["Chapter"] = chapter
        if box_rear is not UNSET:
            field_dict["BoxRear"] = box_rear
        if profile is not UNSET:
            field_dict["Profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_dto_image_blur_hashes_art import BaseItemDtoImageBlurHashesArt
        from ..models.base_item_dto_image_blur_hashes_backdrop import BaseItemDtoImageBlurHashesBackdrop
        from ..models.base_item_dto_image_blur_hashes_banner import BaseItemDtoImageBlurHashesBanner
        from ..models.base_item_dto_image_blur_hashes_box import BaseItemDtoImageBlurHashesBox
        from ..models.base_item_dto_image_blur_hashes_box_rear import BaseItemDtoImageBlurHashesBoxRear
        from ..models.base_item_dto_image_blur_hashes_chapter import BaseItemDtoImageBlurHashesChapter
        from ..models.base_item_dto_image_blur_hashes_disc import BaseItemDtoImageBlurHashesDisc
        from ..models.base_item_dto_image_blur_hashes_logo import BaseItemDtoImageBlurHashesLogo
        from ..models.base_item_dto_image_blur_hashes_menu import BaseItemDtoImageBlurHashesMenu
        from ..models.base_item_dto_image_blur_hashes_primary import BaseItemDtoImageBlurHashesPrimary
        from ..models.base_item_dto_image_blur_hashes_profile import BaseItemDtoImageBlurHashesProfile
        from ..models.base_item_dto_image_blur_hashes_screenshot import BaseItemDtoImageBlurHashesScreenshot
        from ..models.base_item_dto_image_blur_hashes_thumb import BaseItemDtoImageBlurHashesThumb

        d = src_dict.copy()
        _primary = d.pop("Primary", UNSET)
        primary: Union[Unset, BaseItemDtoImageBlurHashesPrimary]
        if isinstance(_primary, Unset):
            primary = UNSET
        else:
            primary = BaseItemDtoImageBlurHashesPrimary.from_dict(_primary)

        _art = d.pop("Art", UNSET)
        art: Union[Unset, BaseItemDtoImageBlurHashesArt]
        if isinstance(_art, Unset):
            art = UNSET
        else:
            art = BaseItemDtoImageBlurHashesArt.from_dict(_art)

        _backdrop = d.pop("Backdrop", UNSET)
        backdrop: Union[Unset, BaseItemDtoImageBlurHashesBackdrop]
        if isinstance(_backdrop, Unset):
            backdrop = UNSET
        else:
            backdrop = BaseItemDtoImageBlurHashesBackdrop.from_dict(_backdrop)

        _banner = d.pop("Banner", UNSET)
        banner: Union[Unset, BaseItemDtoImageBlurHashesBanner]
        if isinstance(_banner, Unset):
            banner = UNSET
        else:
            banner = BaseItemDtoImageBlurHashesBanner.from_dict(_banner)

        _logo = d.pop("Logo", UNSET)
        logo: Union[Unset, BaseItemDtoImageBlurHashesLogo]
        if isinstance(_logo, Unset):
            logo = UNSET
        else:
            logo = BaseItemDtoImageBlurHashesLogo.from_dict(_logo)

        _thumb = d.pop("Thumb", UNSET)
        thumb: Union[Unset, BaseItemDtoImageBlurHashesThumb]
        if isinstance(_thumb, Unset):
            thumb = UNSET
        else:
            thumb = BaseItemDtoImageBlurHashesThumb.from_dict(_thumb)

        _disc = d.pop("Disc", UNSET)
        disc: Union[Unset, BaseItemDtoImageBlurHashesDisc]
        if isinstance(_disc, Unset):
            disc = UNSET
        else:
            disc = BaseItemDtoImageBlurHashesDisc.from_dict(_disc)

        _box = d.pop("Box", UNSET)
        box: Union[Unset, BaseItemDtoImageBlurHashesBox]
        if isinstance(_box, Unset):
            box = UNSET
        else:
            box = BaseItemDtoImageBlurHashesBox.from_dict(_box)

        _screenshot = d.pop("Screenshot", UNSET)
        screenshot: Union[Unset, BaseItemDtoImageBlurHashesScreenshot]
        if isinstance(_screenshot, Unset):
            screenshot = UNSET
        else:
            screenshot = BaseItemDtoImageBlurHashesScreenshot.from_dict(_screenshot)

        _menu = d.pop("Menu", UNSET)
        menu: Union[Unset, BaseItemDtoImageBlurHashesMenu]
        if isinstance(_menu, Unset):
            menu = UNSET
        else:
            menu = BaseItemDtoImageBlurHashesMenu.from_dict(_menu)

        _chapter = d.pop("Chapter", UNSET)
        chapter: Union[Unset, BaseItemDtoImageBlurHashesChapter]
        if isinstance(_chapter, Unset):
            chapter = UNSET
        else:
            chapter = BaseItemDtoImageBlurHashesChapter.from_dict(_chapter)

        _box_rear = d.pop("BoxRear", UNSET)
        box_rear: Union[Unset, BaseItemDtoImageBlurHashesBoxRear]
        if isinstance(_box_rear, Unset):
            box_rear = UNSET
        else:
            box_rear = BaseItemDtoImageBlurHashesBoxRear.from_dict(_box_rear)

        _profile = d.pop("Profile", UNSET)
        profile: Union[Unset, BaseItemDtoImageBlurHashesProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = BaseItemDtoImageBlurHashesProfile.from_dict(_profile)

        base_item_dto_image_blur_hashes = cls(
            primary=primary,
            art=art,
            backdrop=backdrop,
            banner=banner,
            logo=logo,
            thumb=thumb,
            disc=disc,
            box=box,
            screenshot=screenshot,
            menu=menu,
            chapter=chapter,
            box_rear=box_rear,
            profile=profile,
        )

        base_item_dto_image_blur_hashes.additional_properties = d
        return base_item_dto_image_blur_hashes

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
