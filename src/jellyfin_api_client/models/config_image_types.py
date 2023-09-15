from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigImageTypes")


@_attrs_define
class ConfigImageTypes:
    """
    Attributes:
        backdrop_sizes (Union[Unset, None, List[str]]):
        base_url (Union[Unset, None, str]):
        logo_sizes (Union[Unset, None, List[str]]):
        poster_sizes (Union[Unset, None, List[str]]):
        profile_sizes (Union[Unset, None, List[str]]):
        secure_base_url (Union[Unset, None, str]):
        still_sizes (Union[Unset, None, List[str]]):
    """

    backdrop_sizes: Union[Unset, None, List[str]] = UNSET
    base_url: Union[Unset, None, str] = UNSET
    logo_sizes: Union[Unset, None, List[str]] = UNSET
    poster_sizes: Union[Unset, None, List[str]] = UNSET
    profile_sizes: Union[Unset, None, List[str]] = UNSET
    secure_base_url: Union[Unset, None, str] = UNSET
    still_sizes: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        backdrop_sizes: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.backdrop_sizes, Unset):
            if self.backdrop_sizes is None:
                backdrop_sizes = None
            else:
                backdrop_sizes = self.backdrop_sizes

        base_url = self.base_url
        logo_sizes: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.logo_sizes, Unset):
            if self.logo_sizes is None:
                logo_sizes = None
            else:
                logo_sizes = self.logo_sizes

        poster_sizes: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.poster_sizes, Unset):
            if self.poster_sizes is None:
                poster_sizes = None
            else:
                poster_sizes = self.poster_sizes

        profile_sizes: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.profile_sizes, Unset):
            if self.profile_sizes is None:
                profile_sizes = None
            else:
                profile_sizes = self.profile_sizes

        secure_base_url = self.secure_base_url
        still_sizes: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.still_sizes, Unset):
            if self.still_sizes is None:
                still_sizes = None
            else:
                still_sizes = self.still_sizes

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if backdrop_sizes is not UNSET:
            field_dict["BackdropSizes"] = backdrop_sizes
        if base_url is not UNSET:
            field_dict["BaseUrl"] = base_url
        if logo_sizes is not UNSET:
            field_dict["LogoSizes"] = logo_sizes
        if poster_sizes is not UNSET:
            field_dict["PosterSizes"] = poster_sizes
        if profile_sizes is not UNSET:
            field_dict["ProfileSizes"] = profile_sizes
        if secure_base_url is not UNSET:
            field_dict["SecureBaseUrl"] = secure_base_url
        if still_sizes is not UNSET:
            field_dict["StillSizes"] = still_sizes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        backdrop_sizes = cast(List[str], d.pop("BackdropSizes", UNSET))

        base_url = d.pop("BaseUrl", UNSET)

        logo_sizes = cast(List[str], d.pop("LogoSizes", UNSET))

        poster_sizes = cast(List[str], d.pop("PosterSizes", UNSET))

        profile_sizes = cast(List[str], d.pop("ProfileSizes", UNSET))

        secure_base_url = d.pop("SecureBaseUrl", UNSET)

        still_sizes = cast(List[str], d.pop("StillSizes", UNSET))

        config_image_types = cls(
            backdrop_sizes=backdrop_sizes,
            base_url=base_url,
            logo_sizes=logo_sizes,
            poster_sizes=poster_sizes,
            profile_sizes=profile_sizes,
            secure_base_url=secure_base_url,
            still_sizes=still_sizes,
        )

        return config_image_types
