from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.scroll_direction import ScrollDirection
from ..models.sort_order import SortOrder
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.display_preferences_dto_custom_prefs import DisplayPreferencesDtoCustomPrefs


T = TypeVar("T", bound="DisplayPreferencesDto")


@_attrs_define
class DisplayPreferencesDto:
    """Defines the display preferences for any item that supports them (usually Folders).

    Attributes:
        id (Union[Unset, None, str]): Gets or sets the user id.
        view_type (Union[Unset, None, str]): Gets or sets the type of the view.
        sort_by (Union[Unset, None, str]): Gets or sets the sort by.
        index_by (Union[Unset, None, str]): Gets or sets the index by.
        remember_indexing (Union[Unset, bool]): Gets or sets a value indicating whether [remember indexing].
        primary_image_height (Union[Unset, int]): Gets or sets the height of the primary image.
        primary_image_width (Union[Unset, int]): Gets or sets the width of the primary image.
        custom_prefs (Union[Unset, DisplayPreferencesDtoCustomPrefs]): Gets or sets the custom prefs.
        scroll_direction (Union[Unset, ScrollDirection]): An enum representing the axis that should be scrolled.
        show_backdrop (Union[Unset, bool]): Gets or sets a value indicating whether to show backdrops on this item.
        remember_sorting (Union[Unset, bool]): Gets or sets a value indicating whether [remember sorting].
        sort_order (Union[Unset, SortOrder]): An enum representing the sorting order.
        show_sidebar (Union[Unset, bool]): Gets or sets a value indicating whether [show sidebar].
        client (Union[Unset, None, str]): Gets or sets the client.
    """

    id: Union[Unset, None, str] = UNSET
    view_type: Union[Unset, None, str] = UNSET
    sort_by: Union[Unset, None, str] = UNSET
    index_by: Union[Unset, None, str] = UNSET
    remember_indexing: Union[Unset, bool] = UNSET
    primary_image_height: Union[Unset, int] = UNSET
    primary_image_width: Union[Unset, int] = UNSET
    custom_prefs: Union[Unset, "DisplayPreferencesDtoCustomPrefs"] = UNSET
    scroll_direction: Union[Unset, ScrollDirection] = UNSET
    show_backdrop: Union[Unset, bool] = UNSET
    remember_sorting: Union[Unset, bool] = UNSET
    sort_order: Union[Unset, SortOrder] = UNSET
    show_sidebar: Union[Unset, bool] = UNSET
    client: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        view_type = self.view_type
        sort_by = self.sort_by
        index_by = self.index_by
        remember_indexing = self.remember_indexing
        primary_image_height = self.primary_image_height
        primary_image_width = self.primary_image_width
        custom_prefs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_prefs, Unset):
            custom_prefs = self.custom_prefs.to_dict()

        scroll_direction: Union[Unset, str] = UNSET
        if not isinstance(self.scroll_direction, Unset):
            scroll_direction = self.scroll_direction.value

        show_backdrop = self.show_backdrop
        remember_sorting = self.remember_sorting
        sort_order: Union[Unset, str] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        show_sidebar = self.show_sidebar
        client = self.client

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if view_type is not UNSET:
            field_dict["ViewType"] = view_type
        if sort_by is not UNSET:
            field_dict["SortBy"] = sort_by
        if index_by is not UNSET:
            field_dict["IndexBy"] = index_by
        if remember_indexing is not UNSET:
            field_dict["RememberIndexing"] = remember_indexing
        if primary_image_height is not UNSET:
            field_dict["PrimaryImageHeight"] = primary_image_height
        if primary_image_width is not UNSET:
            field_dict["PrimaryImageWidth"] = primary_image_width
        if custom_prefs is not UNSET:
            field_dict["CustomPrefs"] = custom_prefs
        if scroll_direction is not UNSET:
            field_dict["ScrollDirection"] = scroll_direction
        if show_backdrop is not UNSET:
            field_dict["ShowBackdrop"] = show_backdrop
        if remember_sorting is not UNSET:
            field_dict["RememberSorting"] = remember_sorting
        if sort_order is not UNSET:
            field_dict["SortOrder"] = sort_order
        if show_sidebar is not UNSET:
            field_dict["ShowSidebar"] = show_sidebar
        if client is not UNSET:
            field_dict["Client"] = client

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.display_preferences_dto_custom_prefs import DisplayPreferencesDtoCustomPrefs

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        view_type = d.pop("ViewType", UNSET)

        sort_by = d.pop("SortBy", UNSET)

        index_by = d.pop("IndexBy", UNSET)

        remember_indexing = d.pop("RememberIndexing", UNSET)

        primary_image_height = d.pop("PrimaryImageHeight", UNSET)

        primary_image_width = d.pop("PrimaryImageWidth", UNSET)

        _custom_prefs = d.pop("CustomPrefs", UNSET)
        custom_prefs: Union[Unset, DisplayPreferencesDtoCustomPrefs]
        if isinstance(_custom_prefs, Unset):
            custom_prefs = UNSET
        else:
            custom_prefs = DisplayPreferencesDtoCustomPrefs.from_dict(_custom_prefs)

        _scroll_direction = d.pop("ScrollDirection", UNSET)
        scroll_direction: Union[Unset, ScrollDirection]
        if isinstance(_scroll_direction, Unset):
            scroll_direction = UNSET
        else:
            scroll_direction = ScrollDirection(_scroll_direction)

        show_backdrop = d.pop("ShowBackdrop", UNSET)

        remember_sorting = d.pop("RememberSorting", UNSET)

        _sort_order = d.pop("SortOrder", UNSET)
        sort_order: Union[Unset, SortOrder]
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = SortOrder(_sort_order)

        show_sidebar = d.pop("ShowSidebar", UNSET)

        client = d.pop("Client", UNSET)

        display_preferences_dto = cls(
            id=id,
            view_type=view_type,
            sort_by=sort_by,
            index_by=index_by,
            remember_indexing=remember_indexing,
            primary_image_height=primary_image_height,
            primary_image_width=primary_image_width,
            custom_prefs=custom_prefs,
            scroll_direction=scroll_direction,
            show_backdrop=show_backdrop,
            remember_sorting=remember_sorting,
            sort_order=sort_order,
            show_sidebar=show_sidebar,
            client=client,
        )

        return display_preferences_dto
