import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.forgot_password_action import ForgotPasswordAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="ForgotPasswordResult")


@_attrs_define
class ForgotPasswordResult:
    """
    Attributes:
        action (Union[Unset, ForgotPasswordAction]):
        pin_file (Union[Unset, None, str]): Gets or sets the pin file.
        pin_expiration_date (Union[Unset, None, datetime.datetime]): Gets or sets the pin expiration date.
    """

    action: Union[Unset, ForgotPasswordAction] = UNSET
    pin_file: Union[Unset, None, str] = UNSET
    pin_expiration_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        pin_file = self.pin_file
        pin_expiration_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.pin_expiration_date, Unset):
            pin_expiration_date = self.pin_expiration_date.isoformat() if self.pin_expiration_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if action is not UNSET:
            field_dict["Action"] = action
        if pin_file is not UNSET:
            field_dict["PinFile"] = pin_file
        if pin_expiration_date is not UNSET:
            field_dict["PinExpirationDate"] = pin_expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _action = d.pop("Action", UNSET)
        action: Union[Unset, ForgotPasswordAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ForgotPasswordAction(_action)

        pin_file = d.pop("PinFile", UNSET)

        _pin_expiration_date = d.pop("PinExpirationDate", UNSET)
        pin_expiration_date: Union[Unset, None, datetime.datetime]
        if _pin_expiration_date is None:
            pin_expiration_date = None
        elif isinstance(_pin_expiration_date, Unset):
            pin_expiration_date = UNSET
        else:
            pin_expiration_date = isoparse(_pin_expiration_date)

        forgot_password_result = cls(
            action=action,
            pin_file=pin_file,
            pin_expiration_date=pin_expiration_date,
        )

        return forgot_password_result
