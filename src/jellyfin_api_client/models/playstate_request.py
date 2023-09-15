from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.playstate_command import PlaystateCommand
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaystateRequest")


@_attrs_define
class PlaystateRequest:
    """
    Attributes:
        command (Union[Unset, PlaystateCommand]): Enum PlaystateCommand.
        seek_position_ticks (Union[Unset, None, int]):
        controlling_user_id (Union[Unset, None, str]): Gets or sets the controlling user identifier.
    """

    command: Union[Unset, PlaystateCommand] = UNSET
    seek_position_ticks: Union[Unset, None, int] = UNSET
    controlling_user_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        command: Union[Unset, str] = UNSET
        if not isinstance(self.command, Unset):
            command = self.command.value

        seek_position_ticks = self.seek_position_ticks
        controlling_user_id = self.controlling_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if command is not UNSET:
            field_dict["Command"] = command
        if seek_position_ticks is not UNSET:
            field_dict["SeekPositionTicks"] = seek_position_ticks
        if controlling_user_id is not UNSET:
            field_dict["ControllingUserId"] = controlling_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _command = d.pop("Command", UNSET)
        command: Union[Unset, PlaystateCommand]
        if isinstance(_command, Unset):
            command = UNSET
        else:
            command = PlaystateCommand(_command)

        seek_position_ticks = d.pop("SeekPositionTicks", UNSET)

        controlling_user_id = d.pop("ControllingUserId", UNSET)

        playstate_request = cls(
            command=command,
            seek_position_ticks=seek_position_ticks,
            controlling_user_id=controlling_user_id,
        )

        return playstate_request
