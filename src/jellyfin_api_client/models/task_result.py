import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.task_completion_status import TaskCompletionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskResult")


@_attrs_define
class TaskResult:
    """Class TaskExecutionInfo.

    Attributes:
        start_time_utc (Union[Unset, datetime.datetime]): Gets or sets the start time UTC.
        end_time_utc (Union[Unset, datetime.datetime]): Gets or sets the end time UTC.
        status (Union[Unset, TaskCompletionStatus]): Enum TaskCompletionStatus.
        name (Union[Unset, None, str]): Gets or sets the name.
        key (Union[Unset, None, str]): Gets or sets the key.
        id (Union[Unset, None, str]): Gets or sets the id.
        error_message (Union[Unset, None, str]): Gets or sets the error message.
        long_error_message (Union[Unset, None, str]): Gets or sets the long error message.
    """

    start_time_utc: Union[Unset, datetime.datetime] = UNSET
    end_time_utc: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, TaskCompletionStatus] = UNSET
    name: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    long_error_message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start_time_utc: Union[Unset, str] = UNSET
        if not isinstance(self.start_time_utc, Unset):
            start_time_utc = self.start_time_utc.isoformat()

        end_time_utc: Union[Unset, str] = UNSET
        if not isinstance(self.end_time_utc, Unset):
            end_time_utc = self.end_time_utc.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name = self.name
        key = self.key
        id = self.id
        error_message = self.error_message
        long_error_message = self.long_error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if start_time_utc is not UNSET:
            field_dict["StartTimeUtc"] = start_time_utc
        if end_time_utc is not UNSET:
            field_dict["EndTimeUtc"] = end_time_utc
        if status is not UNSET:
            field_dict["Status"] = status
        if name is not UNSET:
            field_dict["Name"] = name
        if key is not UNSET:
            field_dict["Key"] = key
        if id is not UNSET:
            field_dict["Id"] = id
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message
        if long_error_message is not UNSET:
            field_dict["LongErrorMessage"] = long_error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _start_time_utc = d.pop("StartTimeUtc", UNSET)
        start_time_utc: Union[Unset, datetime.datetime]
        if isinstance(_start_time_utc, Unset):
            start_time_utc = UNSET
        else:
            start_time_utc = isoparse(_start_time_utc)

        _end_time_utc = d.pop("EndTimeUtc", UNSET)
        end_time_utc: Union[Unset, datetime.datetime]
        if isinstance(_end_time_utc, Unset):
            end_time_utc = UNSET
        else:
            end_time_utc = isoparse(_end_time_utc)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, TaskCompletionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskCompletionStatus(_status)

        name = d.pop("Name", UNSET)

        key = d.pop("Key", UNSET)

        id = d.pop("Id", UNSET)

        error_message = d.pop("ErrorMessage", UNSET)

        long_error_message = d.pop("LongErrorMessage", UNSET)

        task_result = cls(
            start_time_utc=start_time_utc,
            end_time_utc=end_time_utc,
            status=status,
            name=name,
            key=key,
            id=id,
            error_message=error_message,
            long_error_message=long_error_message,
        )

        return task_result
