import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_url import MediaUrl


T = TypeVar("T", bound="BaseItem")


@_attrs_define
class BaseItem:
    """Class BaseItem.

    Attributes:
        size (Union[Unset, None, int]):
        container (Union[Unset, None, str]):
        is_hd (Union[Unset, bool]):
        is_shortcut (Union[Unset, bool]):
        shortcut_path (Union[Unset, None, str]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        extra_ids (Union[Unset, None, List[str]]):
        date_last_saved (Union[Unset, datetime.datetime]):
        remote_trailers (Union[Unset, None, List['MediaUrl']]): Gets or sets the remote trailers.
        supports_external_transfer (Union[Unset, bool]):
    """

    size: Union[Unset, None, int] = UNSET
    container: Union[Unset, None, str] = UNSET
    is_hd: Union[Unset, bool] = UNSET
    is_shortcut: Union[Unset, bool] = UNSET
    shortcut_path: Union[Unset, None, str] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    extra_ids: Union[Unset, None, List[str]] = UNSET
    date_last_saved: Union[Unset, datetime.datetime] = UNSET
    remote_trailers: Union[Unset, None, List["MediaUrl"]] = UNSET
    supports_external_transfer: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        size = self.size
        container = self.container
        is_hd = self.is_hd
        is_shortcut = self.is_shortcut
        shortcut_path = self.shortcut_path
        width = self.width
        height = self.height
        extra_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.extra_ids, Unset):
            if self.extra_ids is None:
                extra_ids = None
            else:
                extra_ids = self.extra_ids

        date_last_saved: Union[Unset, str] = UNSET
        if not isinstance(self.date_last_saved, Unset):
            date_last_saved = self.date_last_saved.isoformat()

        remote_trailers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.remote_trailers, Unset):
            if self.remote_trailers is None:
                remote_trailers = None
            else:
                remote_trailers = []
                for remote_trailers_item_data in self.remote_trailers:
                    remote_trailers_item = remote_trailers_item_data.to_dict()

                    remote_trailers.append(remote_trailers_item)

        supports_external_transfer = self.supports_external_transfer

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if size is not UNSET:
            field_dict["Size"] = size
        if container is not UNSET:
            field_dict["Container"] = container
        if is_hd is not UNSET:
            field_dict["IsHD"] = is_hd
        if is_shortcut is not UNSET:
            field_dict["IsShortcut"] = is_shortcut
        if shortcut_path is not UNSET:
            field_dict["ShortcutPath"] = shortcut_path
        if width is not UNSET:
            field_dict["Width"] = width
        if height is not UNSET:
            field_dict["Height"] = height
        if extra_ids is not UNSET:
            field_dict["ExtraIds"] = extra_ids
        if date_last_saved is not UNSET:
            field_dict["DateLastSaved"] = date_last_saved
        if remote_trailers is not UNSET:
            field_dict["RemoteTrailers"] = remote_trailers
        if supports_external_transfer is not UNSET:
            field_dict["SupportsExternalTransfer"] = supports_external_transfer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_url import MediaUrl

        d = src_dict.copy()
        size = d.pop("Size", UNSET)

        container = d.pop("Container", UNSET)

        is_hd = d.pop("IsHD", UNSET)

        is_shortcut = d.pop("IsShortcut", UNSET)

        shortcut_path = d.pop("ShortcutPath", UNSET)

        width = d.pop("Width", UNSET)

        height = d.pop("Height", UNSET)

        extra_ids = cast(List[str], d.pop("ExtraIds", UNSET))

        _date_last_saved = d.pop("DateLastSaved", UNSET)
        date_last_saved: Union[Unset, datetime.datetime]
        if isinstance(_date_last_saved, Unset):
            date_last_saved = UNSET
        else:
            date_last_saved = isoparse(_date_last_saved)

        remote_trailers = []
        _remote_trailers = d.pop("RemoteTrailers", UNSET)
        for remote_trailers_item_data in _remote_trailers or []:
            remote_trailers_item = MediaUrl.from_dict(remote_trailers_item_data)

            remote_trailers.append(remote_trailers_item)

        supports_external_transfer = d.pop("SupportsExternalTransfer", UNSET)

        base_item = cls(
            size=size,
            container=container,
            is_hd=is_hd,
            is_shortcut=is_shortcut,
            shortcut_path=shortcut_path,
            width=width,
            height=height,
            extra_ids=extra_ids,
            date_last_saved=date_last_saved,
            remote_trailers=remote_trailers,
            supports_external_transfer=supports_external_transfer,
        )

        return base_item
