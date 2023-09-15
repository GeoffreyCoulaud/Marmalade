from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserByName")


@_attrs_define
class CreateUserByName:
    """The create user by name request body.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the username.
        password (Union[Unset, None, str]): Gets or sets the password.
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

        create_user_by_name = cls(
            name=name,
            password=password,
        )

        return create_user_by_name
