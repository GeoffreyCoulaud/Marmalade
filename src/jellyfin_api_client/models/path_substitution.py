from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PathSubstitution")


@_attrs_define
class PathSubstitution:
    """Defines the MediaBrowser.Model.Configuration.PathSubstitution.

    Attributes:
        from_ (Union[Unset, str]): Gets or sets the value to substitute.
        to (Union[Unset, str]): Gets or sets the value to substitution with.
    """

    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_
        to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["From"] = from_
        if to is not UNSET:
            field_dict["To"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("From", UNSET)

        to = d.pop("To", UNSET)

        path_substitution = cls(
            from_=from_,
            to=to,
        )

        return path_substitution
