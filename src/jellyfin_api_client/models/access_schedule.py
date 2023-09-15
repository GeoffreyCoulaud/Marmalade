from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.dynamic_day_of_week import DynamicDayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessSchedule")


@_attrs_define
class AccessSchedule:
    """An entity representing a user's access schedule.

    Attributes:
        id (Union[Unset, int]): Gets the id of this instance.
        user_id (Union[Unset, str]): Gets the id of the associated user.
        day_of_week (Union[Unset, DynamicDayOfWeek]): An enum that represents a day of the week, weekdays, weekends, or
            all days.
        start_hour (Union[Unset, float]): Gets or sets the start hour.
        end_hour (Union[Unset, float]): Gets or sets the end hour.
    """

    id: Union[Unset, int] = UNSET
    user_id: Union[Unset, str] = UNSET
    day_of_week: Union[Unset, DynamicDayOfWeek] = UNSET
    start_hour: Union[Unset, float] = UNSET
    end_hour: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        start_hour = self.start_hour
        end_hour = self.end_hour

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if day_of_week is not UNSET:
            field_dict["DayOfWeek"] = day_of_week
        if start_hour is not UNSET:
            field_dict["StartHour"] = start_hour
        if end_hour is not UNSET:
            field_dict["EndHour"] = end_hour

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        user_id = d.pop("UserId", UNSET)

        _day_of_week = d.pop("DayOfWeek", UNSET)
        day_of_week: Union[Unset, DynamicDayOfWeek]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = DynamicDayOfWeek(_day_of_week)

        start_hour = d.pop("StartHour", UNSET)

        end_hour = d.pop("EndHour", UNSET)

        access_schedule = cls(
            id=id,
            user_id=user_id,
            day_of_week=day_of_week,
            start_hour=start_hour,
            end_hour=end_hour,
        )

        return access_schedule
