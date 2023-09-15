import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.send_command_type import SendCommandType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendCommand")


@_attrs_define
class SendCommand:
    """Class SendCommand.

    Attributes:
        group_id (Union[Unset, str]): Gets the group identifier.
        playlist_item_id (Union[Unset, str]): Gets the playlist identifier of the playing item.
        when (Union[Unset, datetime.datetime]): Gets or sets the UTC time when to execute the command.
        position_ticks (Union[Unset, None, int]): Gets the position ticks.
        command (Union[Unset, SendCommandType]): Enum SendCommandType.
        emitted_at (Union[Unset, datetime.datetime]): Gets the UTC time when this command has been emitted.
    """

    group_id: Union[Unset, str] = UNSET
    playlist_item_id: Union[Unset, str] = UNSET
    when: Union[Unset, datetime.datetime] = UNSET
    position_ticks: Union[Unset, None, int] = UNSET
    command: Union[Unset, SendCommandType] = UNSET
    emitted_at: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id
        playlist_item_id = self.playlist_item_id
        when: Union[Unset, str] = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.isoformat()

        position_ticks = self.position_ticks
        command: Union[Unset, str] = UNSET
        if not isinstance(self.command, Unset):
            command = self.command.value

        emitted_at: Union[Unset, str] = UNSET
        if not isinstance(self.emitted_at, Unset):
            emitted_at = self.emitted_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["GroupId"] = group_id
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if when is not UNSET:
            field_dict["When"] = when
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks
        if command is not UNSET:
            field_dict["Command"] = command
        if emitted_at is not UNSET:
            field_dict["EmittedAt"] = emitted_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("GroupId", UNSET)

        playlist_item_id = d.pop("PlaylistItemId", UNSET)

        _when = d.pop("When", UNSET)
        when: Union[Unset, datetime.datetime]
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = isoparse(_when)

        position_ticks = d.pop("PositionTicks", UNSET)

        _command = d.pop("Command", UNSET)
        command: Union[Unset, SendCommandType]
        if isinstance(_command, Unset):
            command = UNSET
        else:
            command = SendCommandType(_command)

        _emitted_at = d.pop("EmittedAt", UNSET)
        emitted_at: Union[Unset, datetime.datetime]
        if isinstance(_emitted_at, Unset):
            emitted_at = UNSET
        else:
            emitted_at = isoparse(_emitted_at)

        send_command = cls(
            group_id=group_id,
            playlist_item_id=playlist_item_id,
            when=when,
            position_ticks=position_ticks,
            command=command,
            emitted_at=emitted_at,
        )

        return send_command
