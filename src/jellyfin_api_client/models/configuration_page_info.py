from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationPageInfo")


@_attrs_define
class ConfigurationPageInfo:
    """The configuration page info.

    Attributes:
        name (Union[Unset, str]): Gets or sets the name.
        enable_in_main_menu (Union[Unset, bool]): Gets or sets a value indicating whether the configurations page is
            enabled in the main menu.
        menu_section (Union[Unset, None, str]): Gets or sets the menu section.
        menu_icon (Union[Unset, None, str]): Gets or sets the menu icon.
        display_name (Union[Unset, None, str]): Gets or sets the display name.
        plugin_id (Union[Unset, None, str]): Gets or sets the plugin id.
    """

    name: Union[Unset, str] = UNSET
    enable_in_main_menu: Union[Unset, bool] = UNSET
    menu_section: Union[Unset, None, str] = UNSET
    menu_icon: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    plugin_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        enable_in_main_menu = self.enable_in_main_menu
        menu_section = self.menu_section
        menu_icon = self.menu_icon
        display_name = self.display_name
        plugin_id = self.plugin_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if enable_in_main_menu is not UNSET:
            field_dict["EnableInMainMenu"] = enable_in_main_menu
        if menu_section is not UNSET:
            field_dict["MenuSection"] = menu_section
        if menu_icon is not UNSET:
            field_dict["MenuIcon"] = menu_icon
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if plugin_id is not UNSET:
            field_dict["PluginId"] = plugin_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        enable_in_main_menu = d.pop("EnableInMainMenu", UNSET)

        menu_section = d.pop("MenuSection", UNSET)

        menu_icon = d.pop("MenuIcon", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        plugin_id = d.pop("PluginId", UNSET)

        configuration_page_info = cls(
            name=name,
            enable_in_main_menu=enable_in_main_menu,
            menu_section=menu_section,
            menu_icon=menu_icon,
            display_name=display_name,
            plugin_id=plugin_id,
        )

        return configuration_page_info
