from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPlugin")


@_attrs_define
class IPlugin:
    """Defines the MediaBrowser.Common.Plugins.IPlugin.

    Attributes:
        name (Union[Unset, None, str]): Gets the name of the plugin.
        description (Union[Unset, None, str]): Gets the Description.
        id (Union[Unset, str]): Gets the unique id.
        version (Union[Unset, None, str]): Gets the plugin version.
        assembly_file_path (Union[Unset, None, str]): Gets the path to the assembly file.
        can_uninstall (Union[Unset, bool]): Gets a value indicating whether the plugin can be uninstalled.
        data_folder_path (Union[Unset, None, str]): Gets the full path to the data folder, where the plugin can store
            any miscellaneous files needed.
    """

    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    assembly_file_path: Union[Unset, None, str] = UNSET
    can_uninstall: Union[Unset, bool] = UNSET
    data_folder_path: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        id = self.id
        version = self.version
        assembly_file_path = self.assembly_file_path
        can_uninstall = self.can_uninstall
        data_folder_path = self.data_folder_path

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if id is not UNSET:
            field_dict["Id"] = id
        if version is not UNSET:
            field_dict["Version"] = version
        if assembly_file_path is not UNSET:
            field_dict["AssemblyFilePath"] = assembly_file_path
        if can_uninstall is not UNSET:
            field_dict["CanUninstall"] = can_uninstall
        if data_folder_path is not UNSET:
            field_dict["DataFolderPath"] = data_folder_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        id = d.pop("Id", UNSET)

        version = d.pop("Version", UNSET)

        assembly_file_path = d.pop("AssemblyFilePath", UNSET)

        can_uninstall = d.pop("CanUninstall", UNSET)

        data_folder_path = d.pop("DataFolderPath", UNSET)

        i_plugin = cls(
            name=name,
            description=description,
            id=id,
            version=version,
            assembly_file_path=assembly_file_path,
            can_uninstall=can_uninstall,
            data_folder_path=data_folder_path,
        )

        return i_plugin
