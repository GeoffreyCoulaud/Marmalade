from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BasePluginConfiguration")


@_attrs_define
class BasePluginConfiguration:
    """Class BasePluginConfiguration."""

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        base_plugin_configuration = cls()

        return base_plugin_configuration
