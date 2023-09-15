from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticateUserByName")


@_attrs_define
class AuthenticateUserByName:
    """The authenticate user by name request body.

    Attributes:
        username (Union[Unset, None, str]): Gets or sets the username.
        pw (Union[Unset, None, str]): Gets or sets the plain text password.
        password (Union[Unset, None, str]): Gets or sets the sha1-hashed password.
    """

    username: Union[Unset, None, str] = UNSET
    pw: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        pw = self.pw
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if username is not UNSET:
            field_dict["Username"] = username
        if pw is not UNSET:
            field_dict["Pw"] = pw
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("Username", UNSET)

        pw = d.pop("Pw", UNSET)

        password = d.pop("Password", UNSET)

        authenticate_user_by_name = cls(
            username=username,
            pw=pw,
            password=password,
        )

        return authenticate_user_by_name
