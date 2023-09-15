from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartupUserDto")


@_attrs_define
class StartupUserDto:
    """The startup user DTO.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the username.
        password (Union[Unset, None, str]): Gets or sets the user's password.
    """

    name: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        password = d.pop("Password", UNSET)

        startup_user_dto = cls(
            name=name,
            password=password,
        )

        return startup_user_dto
