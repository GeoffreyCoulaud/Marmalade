import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.group_state_type import GroupStateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupInfoDto")


@_attrs_define
class GroupInfoDto:
    """Class GroupInfoDto.

    Attributes:
        group_id (Union[Unset, str]): Gets the group identifier.
        group_name (Union[Unset, str]): Gets the group name.
        state (Union[Unset, GroupStateType]): Enum GroupState.
        participants (Union[Unset, List[str]]): Gets the participants.
        last_updated_at (Union[Unset, datetime.datetime]): Gets the date when this DTO has been created.
    """

    group_id: Union[Unset, str] = UNSET
    group_name: Union[Unset, str] = UNSET
    state: Union[Unset, GroupStateType] = UNSET
    participants: Union[Unset, List[str]] = UNSET
    last_updated_at: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id
        group_name = self.group_name
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        participants: Union[Unset, List[str]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = self.participants

        last_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_at, Unset):
            last_updated_at = self.last_updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["GroupId"] = group_id
        if group_name is not UNSET:
            field_dict["GroupName"] = group_name
        if state is not UNSET:
            field_dict["State"] = state
        if participants is not UNSET:
            field_dict["Participants"] = participants
        if last_updated_at is not UNSET:
            field_dict["LastUpdatedAt"] = last_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("GroupId", UNSET)

        group_name = d.pop("GroupName", UNSET)

        _state = d.pop("State", UNSET)
        state: Union[Unset, GroupStateType]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = GroupStateType(_state)

        participants = cast(List[str], d.pop("Participants", UNSET))

        _last_updated_at = d.pop("LastUpdatedAt", UNSET)
        last_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_at, Unset):
            last_updated_at = UNSET
        else:
            last_updated_at = isoparse(_last_updated_at)

        group_info_dto = cls(
            group_id=group_id,
            group_name=group_name,
            state=state,
            participants=participants,
            last_updated_at=last_updated_at,
        )

        return group_info_dto
