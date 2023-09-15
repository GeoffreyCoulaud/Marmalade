from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto


T = TypeVar("T", bound="ThemeMediaResult")


@_attrs_define
class ThemeMediaResult:
    """Class ThemeMediaResult.

    Attributes:
        items (Union[Unset, None, List['BaseItemDto']]): Gets or sets the items.
        total_record_count (Union[Unset, int]): Gets or sets the total number of records available.
        start_index (Union[Unset, int]): Gets or sets the index of the first record in Items.
        owner_id (Union[Unset, str]): Gets or sets the owner id.
    """

    items: Union[Unset, None, List["BaseItemDto"]] = UNSET
    total_record_count: Union[Unset, int] = UNSET
    start_index: Union[Unset, int] = UNSET
    owner_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            if self.items is None:
                items = None
            else:
                items = []
                for items_item_data in self.items:
                    items_item = items_item_data.to_dict()

                    items.append(items_item)

        total_record_count = self.total_record_count
        start_index = self.start_index
        owner_id = self.owner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if items is not UNSET:
            field_dict["Items"] = items
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index
        if owner_id is not UNSET:
            field_dict["OwnerId"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto

        d = src_dict.copy()
        items = []
        _items = d.pop("Items", UNSET)
        for items_item_data in _items or []:
            items_item = BaseItemDto.from_dict(items_item_data)

            items.append(items_item)

        total_record_count = d.pop("TotalRecordCount", UNSET)

        start_index = d.pop("StartIndex", UNSET)

        owner_id = d.pop("OwnerId", UNSET)

        theme_media_result = cls(
            items=items,
            total_record_count=total_record_count,
            start_index=start_index,
            owner_id=owner_id,
        )

        return theme_media_result
