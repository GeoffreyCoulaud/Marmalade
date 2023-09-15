from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_hint import SearchHint


T = TypeVar("T", bound="SearchHintResult")


@_attrs_define
class SearchHintResult:
    """Class SearchHintResult.

    Attributes:
        search_hints (Union[Unset, List['SearchHint']]): Gets the search hints.
        total_record_count (Union[Unset, int]): Gets the total record count.
    """

    search_hints: Union[Unset, List["SearchHint"]] = UNSET
    total_record_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        search_hints: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.search_hints, Unset):
            search_hints = []
            for search_hints_item_data in self.search_hints:
                search_hints_item = search_hints_item_data.to_dict()

                search_hints.append(search_hints_item)

        total_record_count = self.total_record_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if search_hints is not UNSET:
            field_dict["SearchHints"] = search_hints
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_hint import SearchHint

        d = src_dict.copy()
        search_hints = []
        _search_hints = d.pop("SearchHints", UNSET)
        for search_hints_item_data in _search_hints or []:
            search_hints_item = SearchHint.from_dict(search_hints_item_data)

            search_hints.append(search_hints_item)

        total_record_count = d.pop("TotalRecordCount", UNSET)

        search_hint_result = cls(
            search_hints=search_hints,
            total_record_count=total_record_count,
        )

        return search_hint_result
