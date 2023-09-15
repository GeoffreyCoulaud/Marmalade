from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.collection_type_options import CollectionTypeOptions
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_options import LibraryOptions


T = TypeVar("T", bound="VirtualFolderInfo")


@_attrs_define
class VirtualFolderInfo:
    """Used to hold information about a user's list of configured virtual folders.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        locations (Union[Unset, None, List[str]]): Gets or sets the locations.
        collection_type (Union[Unset, None, CollectionTypeOptions]):
        library_options (Union[Unset, None, LibraryOptions]):
        item_id (Union[Unset, None, str]): Gets or sets the item identifier.
        primary_image_item_id (Union[Unset, None, str]): Gets or sets the primary image item identifier.
        refresh_progress (Union[Unset, None, float]):
        refresh_status (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    locations: Union[Unset, None, List[str]] = UNSET
    collection_type: Union[Unset, None, CollectionTypeOptions] = UNSET
    library_options: Union[Unset, None, "LibraryOptions"] = UNSET
    item_id: Union[Unset, None, str] = UNSET
    primary_image_item_id: Union[Unset, None, str] = UNSET
    refresh_progress: Union[Unset, None, float] = UNSET
    refresh_status: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        locations: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.locations, Unset):
            if self.locations is None:
                locations = None
            else:
                locations = self.locations

        collection_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.collection_type, Unset):
            collection_type = self.collection_type.value if self.collection_type else None

        library_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.library_options, Unset):
            library_options = self.library_options.to_dict() if self.library_options else None

        item_id = self.item_id
        primary_image_item_id = self.primary_image_item_id
        refresh_progress = self.refresh_progress
        refresh_status = self.refresh_status

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if locations is not UNSET:
            field_dict["Locations"] = locations
        if collection_type is not UNSET:
            field_dict["CollectionType"] = collection_type
        if library_options is not UNSET:
            field_dict["LibraryOptions"] = library_options
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if primary_image_item_id is not UNSET:
            field_dict["PrimaryImageItemId"] = primary_image_item_id
        if refresh_progress is not UNSET:
            field_dict["RefreshProgress"] = refresh_progress
        if refresh_status is not UNSET:
            field_dict["RefreshStatus"] = refresh_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.library_options import LibraryOptions

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        locations = cast(List[str], d.pop("Locations", UNSET))

        _collection_type = d.pop("CollectionType", UNSET)
        collection_type: Union[Unset, None, CollectionTypeOptions]
        if _collection_type is None:
            collection_type = None
        elif isinstance(_collection_type, Unset):
            collection_type = UNSET
        else:
            collection_type = CollectionTypeOptions(_collection_type)

        _library_options = d.pop("LibraryOptions", UNSET)
        library_options: Union[Unset, None, LibraryOptions]
        if _library_options is None:
            library_options = None
        elif isinstance(_library_options, Unset):
            library_options = UNSET
        else:
            library_options = LibraryOptions.from_dict(_library_options)

        item_id = d.pop("ItemId", UNSET)

        primary_image_item_id = d.pop("PrimaryImageItemId", UNSET)

        refresh_progress = d.pop("RefreshProgress", UNSET)

        refresh_status = d.pop("RefreshStatus", UNSET)

        virtual_folder_info = cls(
            name=name,
            locations=locations,
            collection_type=collection_type,
            library_options=library_options,
            item_id=item_id,
            primary_image_item_id=primary_image_item_id,
            refresh_progress=refresh_progress,
            refresh_status=refresh_status,
        )

        return virtual_folder_info
