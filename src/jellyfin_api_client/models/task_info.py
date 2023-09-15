from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.task_state import TaskState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_result import TaskResult
    from ..models.task_trigger_info import TaskTriggerInfo


T = TypeVar("T", bound="TaskInfo")


@_attrs_define
class TaskInfo:
    """Class TaskInfo.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        state (Union[Unset, TaskState]): Enum TaskState.
        current_progress_percentage (Union[Unset, None, float]): Gets or sets the progress.
        id (Union[Unset, None, str]): Gets or sets the id.
        last_execution_result (Union[Unset, None, TaskResult]): Class TaskExecutionInfo.
        triggers (Union[Unset, None, List['TaskTriggerInfo']]): Gets or sets the triggers.
        description (Union[Unset, None, str]): Gets or sets the description.
        category (Union[Unset, None, str]): Gets or sets the category.
        is_hidden (Union[Unset, bool]): Gets or sets a value indicating whether this instance is hidden.
        key (Union[Unset, None, str]): Gets or sets the key.
    """

    name: Union[Unset, None, str] = UNSET
    state: Union[Unset, TaskState] = UNSET
    current_progress_percentage: Union[Unset, None, float] = UNSET
    id: Union[Unset, None, str] = UNSET
    last_execution_result: Union[Unset, None, "TaskResult"] = UNSET
    triggers: Union[Unset, None, List["TaskTriggerInfo"]] = UNSET
    description: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, str] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    key: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        current_progress_percentage = self.current_progress_percentage
        id = self.id
        last_execution_result: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_execution_result, Unset):
            last_execution_result = self.last_execution_result.to_dict() if self.last_execution_result else None

        triggers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.triggers, Unset):
            if self.triggers is None:
                triggers = None
            else:
                triggers = []
                for triggers_item_data in self.triggers:
                    triggers_item = triggers_item_data.to_dict()

                    triggers.append(triggers_item)

        description = self.description
        category = self.category
        is_hidden = self.is_hidden
        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if state is not UNSET:
            field_dict["State"] = state
        if current_progress_percentage is not UNSET:
            field_dict["CurrentProgressPercentage"] = current_progress_percentage
        if id is not UNSET:
            field_dict["Id"] = id
        if last_execution_result is not UNSET:
            field_dict["LastExecutionResult"] = last_execution_result
        if triggers is not UNSET:
            field_dict["Triggers"] = triggers
        if description is not UNSET:
            field_dict["Description"] = description
        if category is not UNSET:
            field_dict["Category"] = category
        if is_hidden is not UNSET:
            field_dict["IsHidden"] = is_hidden
        if key is not UNSET:
            field_dict["Key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_result import TaskResult
        from ..models.task_trigger_info import TaskTriggerInfo

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        _state = d.pop("State", UNSET)
        state: Union[Unset, TaskState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = TaskState(_state)

        current_progress_percentage = d.pop("CurrentProgressPercentage", UNSET)

        id = d.pop("Id", UNSET)

        _last_execution_result = d.pop("LastExecutionResult", UNSET)
        last_execution_result: Union[Unset, None, TaskResult]
        if _last_execution_result is None:
            last_execution_result = None
        elif isinstance(_last_execution_result, Unset):
            last_execution_result = UNSET
        else:
            last_execution_result = TaskResult.from_dict(_last_execution_result)

        triggers = []
        _triggers = d.pop("Triggers", UNSET)
        for triggers_item_data in _triggers or []:
            triggers_item = TaskTriggerInfo.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        description = d.pop("Description", UNSET)

        category = d.pop("Category", UNSET)

        is_hidden = d.pop("IsHidden", UNSET)

        key = d.pop("Key", UNSET)

        task_info = cls(
            name=name,
            state=state,
            current_progress_percentage=current_progress_percentage,
            id=id,
            last_execution_result=last_execution_result,
            triggers=triggers,
            description=description,
            category=category,
            is_hidden=is_hidden,
            key=key,
        )

        return task_info
