from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_person_image_blur_hashes_art import BaseItemPersonImageBlurHashesArt
    from ..models.base_item_person_image_blur_hashes_backdrop import BaseItemPersonImageBlurHashesBackdrop
    from ..models.base_item_person_image_blur_hashes_banner import BaseItemPersonImageBlurHashesBanner
    from ..models.base_item_person_image_blur_hashes_box import BaseItemPersonImageBlurHashesBox
    from ..models.base_item_person_image_blur_hashes_box_rear import BaseItemPersonImageBlurHashesBoxRear
    from ..models.base_item_person_image_blur_hashes_chapter import BaseItemPersonImageBlurHashesChapter
    from ..models.base_item_person_image_blur_hashes_disc import BaseItemPersonImageBlurHashesDisc
    from ..models.base_item_person_image_blur_hashes_logo import BaseItemPersonImageBlurHashesLogo
    from ..models.base_item_person_image_blur_hashes_menu import BaseItemPersonImageBlurHashesMenu
    from ..models.base_item_person_image_blur_hashes_primary import BaseItemPersonImageBlurHashesPrimary
    from ..models.base_item_person_image_blur_hashes_profile import BaseItemPersonImageBlurHashesProfile
    from ..models.base_item_person_image_blur_hashes_screenshot import BaseItemPersonImageBlurHashesScreenshot
    from ..models.base_item_person_image_blur_hashes_thumb import BaseItemPersonImageBlurHashesThumb


T = TypeVar("T", bound="BaseItemPersonImageBlurHashes")


@_attrs_define
class BaseItemPersonImageBlurHashes:
    """Gets or sets the primary image blurhash.

    Attributes:
        primary (Union[Unset, BaseItemPersonImageBlurHashesPrimary]):
        art (Union[Unset, BaseItemPersonImageBlurHashesArt]):
        backdrop (Union[Unset, BaseItemPersonImageBlurHashesBackdrop]):
        banner (Union[Unset, BaseItemPersonImageBlurHashesBanner]):
        logo (Union[Unset, BaseItemPersonImageBlurHashesLogo]):
        thumb (Union[Unset, BaseItemPersonImageBlurHashesThumb]):
        disc (Union[Unset, BaseItemPersonImageBlurHashesDisc]):
        box (Union[Unset, BaseItemPersonImageBlurHashesBox]):
        screenshot (Union[Unset, BaseItemPersonImageBlurHashesScreenshot]):
        menu (Union[Unset, BaseItemPersonImageBlurHashesMenu]):
        chapter (Union[Unset, BaseItemPersonImageBlurHashesChapter]):
        box_rear (Union[Unset, BaseItemPersonImageBlurHashesBoxRear]):
        profile (Union[Unset, BaseItemPersonImageBlurHashesProfile]):
    """

    primary: Union[Unset, "BaseItemPersonImageBlurHashesPrimary"] = UNSET
    art: Union[Unset, "BaseItemPersonImageBlurHashesArt"] = UNSET
    backdrop: Union[Unset, "BaseItemPersonImageBlurHashesBackdrop"] = UNSET
    banner: Union[Unset, "BaseItemPersonImageBlurHashesBanner"] = UNSET
    logo: Union[Unset, "BaseItemPersonImageBlurHashesLogo"] = UNSET
    thumb: Union[Unset, "BaseItemPersonImageBlurHashesThumb"] = UNSET
    disc: Union[Unset, "BaseItemPersonImageBlurHashesDisc"] = UNSET
    box: Union[Unset, "BaseItemPersonImageBlurHashesBox"] = UNSET
    screenshot: Union[Unset, "BaseItemPersonImageBlurHashesScreenshot"] = UNSET
    menu: Union[Unset, "BaseItemPersonImageBlurHashesMenu"] = UNSET
    chapter: Union[Unset, "BaseItemPersonImageBlurHashesChapter"] = UNSET
    box_rear: Union[Unset, "BaseItemPersonImageBlurHashesBoxRear"] = UNSET
    profile: Union[Unset, "BaseItemPersonImageBlurHashesProfile"] = UNSET
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
        from ..models.base_item_person_image_blur_hashes_art import BaseItemPersonImageBlurHashesArt
        from ..models.base_item_person_image_blur_hashes_backdrop import BaseItemPersonImageBlurHashesBackdrop
        from ..models.base_item_person_image_blur_hashes_banner import BaseItemPersonImageBlurHashesBanner
        from ..models.base_item_person_image_blur_hashes_box import BaseItemPersonImageBlurHashesBox
        from ..models.base_item_person_image_blur_hashes_box_rear import BaseItemPersonImageBlurHashesBoxRear
        from ..models.base_item_person_image_blur_hashes_chapter import BaseItemPersonImageBlurHashesChapter
        from ..models.base_item_person_image_blur_hashes_disc import BaseItemPersonImageBlurHashesDisc
        from ..models.base_item_person_image_blur_hashes_logo import BaseItemPersonImageBlurHashesLogo
        from ..models.base_item_person_image_blur_hashes_menu import BaseItemPersonImageBlurHashesMenu
        from ..models.base_item_person_image_blur_hashes_primary import BaseItemPersonImageBlurHashesPrimary
        from ..models.base_item_person_image_blur_hashes_profile import BaseItemPersonImageBlurHashesProfile
        from ..models.base_item_person_image_blur_hashes_screenshot import BaseItemPersonImageBlurHashesScreenshot
        from ..models.base_item_person_image_blur_hashes_thumb import BaseItemPersonImageBlurHashesThumb

        d = src_dict.copy()
        _primary = d.pop("Primary", UNSET)
        primary: Union[Unset, BaseItemPersonImageBlurHashesPrimary]
        if isinstance(_primary, Unset):
            primary = UNSET
        else:
            primary = BaseItemPersonImageBlurHashesPrimary.from_dict(_primary)

        _art = d.pop("Art", UNSET)
        art: Union[Unset, BaseItemPersonImageBlurHashesArt]
        if isinstance(_art, Unset):
            art = UNSET
        else:
            art = BaseItemPersonImageBlurHashesArt.from_dict(_art)

        _backdrop = d.pop("Backdrop", UNSET)
        backdrop: Union[Unset, BaseItemPersonImageBlurHashesBackdrop]
        if isinstance(_backdrop, Unset):
            backdrop = UNSET
        else:
            backdrop = BaseItemPersonImageBlurHashesBackdrop.from_dict(_backdrop)

        _banner = d.pop("Banner", UNSET)
        banner: Union[Unset, BaseItemPersonImageBlurHashesBanner]
        if isinstance(_banner, Unset):
            banner = UNSET
        else:
            banner = BaseItemPersonImageBlurHashesBanner.from_dict(_banner)

        _logo = d.pop("Logo", UNSET)
        logo: Union[Unset, BaseItemPersonImageBlurHashesLogo]
        if isinstance(_logo, Unset):
            logo = UNSET
        else:
            logo = BaseItemPersonImageBlurHashesLogo.from_dict(_logo)

        _thumb = d.pop("Thumb", UNSET)
        thumb: Union[Unset, BaseItemPersonImageBlurHashesThumb]
        if isinstance(_thumb, Unset):
            thumb = UNSET
        else:
            thumb = BaseItemPersonImageBlurHashesThumb.from_dict(_thumb)

        _disc = d.pop("Disc", UNSET)
        disc: Union[Unset, BaseItemPersonImageBlurHashesDisc]
        if isinstance(_disc, Unset):
            disc = UNSET
        else:
            disc = BaseItemPersonImageBlurHashesDisc.from_dict(_disc)

        _box = d.pop("Box", UNSET)
        box: Union[Unset, BaseItemPersonImageBlurHashesBox]
        if isinstance(_box, Unset):
            box = UNSET
        else:
            box = BaseItemPersonImageBlurHashesBox.from_dict(_box)

        _screenshot = d.pop("Screenshot", UNSET)
        screenshot: Union[Unset, BaseItemPersonImageBlurHashesScreenshot]
        if isinstance(_screenshot, Unset):
            screenshot = UNSET
        else:
            screenshot = BaseItemPersonImageBlurHashesScreenshot.from_dict(_screenshot)

        _menu = d.pop("Menu", UNSET)
        menu: Union[Unset, BaseItemPersonImageBlurHashesMenu]
        if isinstance(_menu, Unset):
            menu = UNSET
        else:
            menu = BaseItemPersonImageBlurHashesMenu.from_dict(_menu)

        _chapter = d.pop("Chapter", UNSET)
        chapter: Union[Unset, BaseItemPersonImageBlurHashesChapter]
        if isinstance(_chapter, Unset):
            chapter = UNSET
        else:
            chapter = BaseItemPersonImageBlurHashesChapter.from_dict(_chapter)

        _box_rear = d.pop("BoxRear", UNSET)
        box_rear: Union[Unset, BaseItemPersonImageBlurHashesBoxRear]
        if isinstance(_box_rear, Unset):
            box_rear = UNSET
        else:
            box_rear = BaseItemPersonImageBlurHashesBoxRear.from_dict(_box_rear)

        _profile = d.pop("Profile", UNSET)
        profile: Union[Unset, BaseItemPersonImageBlurHashesProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = BaseItemPersonImageBlurHashesProfile.from_dict(_profile)

        base_item_person_image_blur_hashes = cls(
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

        base_item_person_image_blur_hashes.additional_properties = d
        return base_item_person_image_blur_hashes

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
