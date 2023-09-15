from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_options import LibraryOptions


T = TypeVar("T", bound="AddVirtualFolderDto")


@_attrs_define
class AddVirtualFolderDto:
    """Add virtual folder dto.

    Attributes:
        library_options (Union[Unset, None, LibraryOptions]):
    """

    library_options: Union[Unset, None, "LibraryOptions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        library_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.library_options, Unset):
            library_options = self.library_options.to_dict() if self.library_options else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if library_options is not UNSET:
            field_dict["LibraryOptions"] = library_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.library_options import LibraryOptions

        d = src_dict.copy()
        _library_options = d.pop("LibraryOptions", UNSET)
        library_options: Union[Unset, None, LibraryOptions]
        if _library_options is None:
            library_options = None
        elif isinstance(_library_options, Unset):
            library_options = UNSET
        else:
            library_options = LibraryOptions.from_dict(_library_options)

        add_virtual_folder_dto = cls(
            library_options=library_options,
        )

        return add_virtual_folder_dto
