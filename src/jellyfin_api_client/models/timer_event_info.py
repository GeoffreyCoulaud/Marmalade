from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimerEventInfo")


@_attrs_define
class TimerEventInfo:
    """
    Attributes:
        id (Union[Unset, str]):
        program_id (Union[Unset, None, str]):
    """

    id: Union[Unset, str] = UNSET
    program_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        program_id = self.program_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if program_id is not UNSET:
            field_dict["ProgramId"] = program_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        program_id = d.pop("ProgramId", UNSET)

        timer_event_info = cls(
            id=id,
            program_id=program_id,
        )

        return timer_event_info
