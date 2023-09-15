from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserPassword")


@_attrs_define
class UpdateUserPassword:
    """The update user password request body.

    Attributes:
        current_password (Union[Unset, None, str]): Gets or sets the current sha1-hashed password.
        current_pw (Union[Unset, None, str]): Gets or sets the current plain text password.
        new_pw (Union[Unset, None, str]): Gets or sets the new plain text password.
        reset_password (Union[Unset, bool]): Gets or sets a value indicating whether to reset the password.
    """

    current_password: Union[Unset, None, str] = UNSET
    current_pw: Union[Unset, None, str] = UNSET
    new_pw: Union[Unset, None, str] = UNSET
    reset_password: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        current_password = self.current_password
        current_pw = self.current_pw
        new_pw = self.new_pw
        reset_password = self.reset_password

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if current_password is not UNSET:
            field_dict["CurrentPassword"] = current_password
        if current_pw is not UNSET:
            field_dict["CurrentPw"] = current_pw
        if new_pw is not UNSET:
            field_dict["NewPw"] = new_pw
        if reset_password is not UNSET:
            field_dict["ResetPassword"] = reset_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_password = d.pop("CurrentPassword", UNSET)

        current_pw = d.pop("CurrentPw", UNSET)

        new_pw = d.pop("NewPw", UNSET)

        reset_password = d.pop("ResetPassword", UNSET)

        update_user_password = cls(
            current_password=current_password,
            current_pw=current_pw,
            new_pw=new_pw,
            reset_password=reset_password,
        )

        return update_user_password
