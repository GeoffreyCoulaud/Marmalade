from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_guid_pair import NameGuidPair


T = TypeVar("T", bound="QueryFilters")


@_attrs_define
class QueryFilters:
    """
    Attributes:
        genres (Union[Unset, None, List['NameGuidPair']]):
        tags (Union[Unset, None, List[str]]):
    """

    genres: Union[Unset, None, List["NameGuidPair"]] = UNSET
    tags: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        genres: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.genres, Unset):
            if self.genres is None:
                genres = None
            else:
                genres = []
                for genres_item_data in self.genres:
                    genres_item = genres_item_data.to_dict()

                    genres.append(genres_item)

        tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if tags is not UNSET:
            field_dict["Tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.name_guid_pair import NameGuidPair

        d = src_dict.copy()
        genres = []
        _genres = d.pop("Genres", UNSET)
        for genres_item_data in _genres or []:
            genres_item = NameGuidPair.from_dict(genres_item_data)

            genres.append(genres_item)

        tags = cast(List[str], d.pop("Tags", UNSET))

        query_filters = cls(
            genres=genres,
            tags=tags,
        )

        return query_filters
