from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="ContainerProfile")


@_attrs_define
class ContainerProfile:
    """
    Attributes:
        type (Union[Unset, DlnaProfileType]):
        conditions (Union[Unset, None, List['ProfileCondition']]):
        container (Union[Unset, str]):
    """

    type: Union[Unset, DlnaProfileType] = UNSET
    conditions: Union[Unset, None, List["ProfileCondition"]] = UNSET
    container: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        conditions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            if self.conditions is None:
                conditions = None
            else:
                conditions = []
                for conditions_item_data in self.conditions:
                    conditions_item = conditions_item_data.to_dict()

                    conditions.append(conditions_item)

        container = self.container

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions
        if container is not UNSET:
            field_dict["Container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.profile_condition import ProfileCondition

        d = src_dict.copy()
        _type = d.pop("Type", UNSET)
        type: Union[Unset, DlnaProfileType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DlnaProfileType(_type)

        conditions = []
        _conditions = d.pop("Conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ProfileCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        container = d.pop("Container", UNSET)

        container_profile = cls(
            type=type,
            conditions=conditions,
            container=container,
        )

        return container_profile
