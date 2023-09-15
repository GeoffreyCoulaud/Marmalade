from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PinRedeemResult")


@_attrs_define
class PinRedeemResult:
    """
    Attributes:
        success (Union[Unset, bool]): Gets or sets a value indicating whether this
            MediaBrowser.Model.Users.PinRedeemResult is success.
        users_reset (Union[Unset, List[str]]): Gets or sets the users reset.
    """

    success: Union[Unset, bool] = UNSET
    users_reset: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        success = self.success
        users_reset: Union[Unset, List[str]] = UNSET
        if not isinstance(self.users_reset, Unset):
            users_reset = self.users_reset

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if success is not UNSET:
            field_dict["Success"] = success
        if users_reset is not UNSET:
            field_dict["UsersReset"] = users_reset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        success = d.pop("Success", UNSET)

        users_reset = cast(List[str], d.pop("UsersReset", UNSET))

        pin_redeem_result = cls(
            success=success,
            users_reset=users_reset,
        )

        return pin_redeem_result
