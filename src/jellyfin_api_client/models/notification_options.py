from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_option import NotificationOption


T = TypeVar("T", bound="NotificationOptions")


@_attrs_define
class NotificationOptions:
    """
    Attributes:
        options (Union[Unset, None, List['NotificationOption']]):
    """

    options: Union[Unset, None, List["NotificationOption"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        options: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            if self.options is None:
                options = None
            else:
                options = []
                for options_item_data in self.options:
                    options_item = options_item_data.to_dict()

                    options.append(options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if options is not UNSET:
            field_dict["Options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_option import NotificationOption

        d = src_dict.copy()
        options = []
        _options = d.pop("Options", UNSET)
        for options_item_data in _options or []:
            options_item = NotificationOption.from_dict(options_item_data)

            options.append(options_item)

        notification_options = cls(
            options=options,
        )

        return notification_options
