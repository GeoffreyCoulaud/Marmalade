from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.day_of_week import DayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskTriggerInfo")


@_attrs_define
class TaskTriggerInfo:
    """Class TaskTriggerInfo.

    Attributes:
        type (Union[Unset, None, str]): Gets or sets the type.
        time_of_day_ticks (Union[Unset, None, int]): Gets or sets the time of day.
        interval_ticks (Union[Unset, None, int]): Gets or sets the interval.
        day_of_week (Union[Unset, None, DayOfWeek]):
        max_runtime_ticks (Union[Unset, None, int]): Gets or sets the maximum runtime ticks.
    """

    type: Union[Unset, None, str] = UNSET
    time_of_day_ticks: Union[Unset, None, int] = UNSET
    interval_ticks: Union[Unset, None, int] = UNSET
    day_of_week: Union[Unset, None, DayOfWeek] = UNSET
    max_runtime_ticks: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        time_of_day_ticks = self.time_of_day_ticks
        interval_ticks = self.interval_ticks
        day_of_week: Union[Unset, None, str] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value if self.day_of_week else None

        max_runtime_ticks = self.max_runtime_ticks

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if time_of_day_ticks is not UNSET:
            field_dict["TimeOfDayTicks"] = time_of_day_ticks
        if interval_ticks is not UNSET:
            field_dict["IntervalTicks"] = interval_ticks
        if day_of_week is not UNSET:
            field_dict["DayOfWeek"] = day_of_week
        if max_runtime_ticks is not UNSET:
            field_dict["MaxRuntimeTicks"] = max_runtime_ticks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("Type", UNSET)

        time_of_day_ticks = d.pop("TimeOfDayTicks", UNSET)

        interval_ticks = d.pop("IntervalTicks", UNSET)

        _day_of_week = d.pop("DayOfWeek", UNSET)
        day_of_week: Union[Unset, None, DayOfWeek]
        if _day_of_week is None:
            day_of_week = None
        elif isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = DayOfWeek(_day_of_week)

        max_runtime_ticks = d.pop("MaxRuntimeTicks", UNSET)

        task_trigger_info = cls(
            type=type,
            time_of_day_ticks=time_of_day_ticks,
            interval_ticks=interval_ticks,
            day_of_week=day_of_week,
            max_runtime_ticks=max_runtime_ticks,
        )

        return task_trigger_info
