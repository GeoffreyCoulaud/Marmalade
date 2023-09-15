from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientLogDocumentResponseDto")


@_attrs_define
class ClientLogDocumentResponseDto:
    """Client log document response dto.

    Attributes:
        file_name (Union[Unset, str]): Gets the resulting filename.
    """

    file_name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["FileName"] = file_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_name = d.pop("FileName", UNSET)

        client_log_document_response_dto = cls(
            file_name=file_name,
        )

        return client_log_document_response_dto
