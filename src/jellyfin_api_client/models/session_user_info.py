from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionUserInfo")


@_attrs_define
class SessionUserInfo:
    """Class SessionUserInfo.

    Attributes:
        user_id (Union[Unset, str]): Gets or sets the user identifier.
        user_name (Union[Unset, None, str]): Gets or sets the name of the user.
    """

    user_id: Union[Unset, str] = UNSET
    user_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("UserId", UNSET)

        user_name = d.pop("UserName", UNSET)

        session_user_info = cls(
            user_id=user_id,
            user_name=user_name,
        )

        return session_user_info
