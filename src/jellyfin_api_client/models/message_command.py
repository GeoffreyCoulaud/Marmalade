from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageCommand")


@_attrs_define
class MessageCommand:
    """
    Attributes:
        text (str):
        header (Union[Unset, None, str]):
        timeout_ms (Union[Unset, None, int]):
    """

    text: str
    header: Union[Unset, None, str] = UNSET
    timeout_ms: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        header = self.header
        timeout_ms = self.timeout_ms

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Text": text,
            }
        )
        if header is not UNSET:
            field_dict["Header"] = header
        if timeout_ms is not UNSET:
            field_dict["TimeoutMs"] = timeout_ms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("Text")

        header = d.pop("Header", UNSET)

        timeout_ms = d.pop("TimeoutMs", UNSET)

        message_command = cls(
            text=text,
            header=header,
            timeout_ms=timeout_ms,
        )

        return message_command
