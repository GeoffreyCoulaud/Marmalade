from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="XbmcMetadataOptions")


@_attrs_define
class XbmcMetadataOptions:
    """
    Attributes:
        user_id (Union[Unset, None, str]):
        release_date_format (Union[Unset, str]):
        save_image_paths_in_nfo (Union[Unset, bool]):
        enable_path_substitution (Union[Unset, bool]):
        enable_extra_thumbs_duplication (Union[Unset, bool]):
    """

    user_id: Union[Unset, None, str] = UNSET
    release_date_format: Union[Unset, str] = UNSET
    save_image_paths_in_nfo: Union[Unset, bool] = UNSET
    enable_path_substitution: Union[Unset, bool] = UNSET
    enable_extra_thumbs_duplication: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        release_date_format = self.release_date_format
        save_image_paths_in_nfo = self.save_image_paths_in_nfo
        enable_path_substitution = self.enable_path_substitution
        enable_extra_thumbs_duplication = self.enable_extra_thumbs_duplication

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if release_date_format is not UNSET:
            field_dict["ReleaseDateFormat"] = release_date_format
        if save_image_paths_in_nfo is not UNSET:
            field_dict["SaveImagePathsInNfo"] = save_image_paths_in_nfo
        if enable_path_substitution is not UNSET:
            field_dict["EnablePathSubstitution"] = enable_path_substitution
        if enable_extra_thumbs_duplication is not UNSET:
            field_dict["EnableExtraThumbsDuplication"] = enable_extra_thumbs_duplication

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("UserId", UNSET)

        release_date_format = d.pop("ReleaseDateFormat", UNSET)

        save_image_paths_in_nfo = d.pop("SaveImagePathsInNfo", UNSET)

        enable_path_substitution = d.pop("EnablePathSubstitution", UNSET)

        enable_extra_thumbs_duplication = d.pop("EnableExtraThumbsDuplication", UNSET)

        xbmc_metadata_options = cls(
            user_id=user_id,
            release_date_format=release_date_format,
            save_image_paths_in_nfo=save_image_paths_in_nfo,
            enable_path_substitution=enable_path_substitution,
            enable_extra_thumbs_duplication=enable_extra_thumbs_duplication,
        )

        return xbmc_metadata_options
