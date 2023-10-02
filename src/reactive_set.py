from functools import wraps
from typing import Any, Callable, Iterable
from gi.repository import GObject


class ReactiveSetEmitter(GObject.Object):
    """
    Notifier object that emits signals when its associated set is updated

    Signals
    - changed
        - Emitted when an item is removed or added
    - item-added
        - Emitted when an item is added
        - Handlers receive the added item
    - item-removed
        - Emitted when an item is removed
        - Handlers receive the removed item
    """

    @GObject.Signal(name="changed")
    def changed(self):
        """Signal emitted when the set items change (added/removed)"""

    @GObject.Signal(name="item-added", arg_types=[object])
    def item_added(self, _item: Any):
        """Signal emitted when an item is added"""
        self.emit("changed")

    @GObject.Signal(name="item-removed", arg_types=[object])
    def item_removed(self, _item: Any):
        """Signal emitted when an item is removed"""
        self.emit("changed")


def with_update_signals(original_method: Callable) -> Callable:
    """Decorator that triggers added and removed signals after the original method"""

    @wraps(original_method)
    def new_method(self: "ReactiveSet", *args, **kwargs):
        before = self.copy()
        original_method(self, *args, **kwargs)
        for value in self - before:
            self.emitter.emit("item-added", value)
        for value in before - self:
            self.emitter.emit("item-removed", value)

    return new_method


class ReactiveSet(set):
    """
    Set that emits signals through its emitter when its contents changes
    """

    emitter: ReactiveSetEmitter

    def __init__(self, *items) -> None:
        super().__init__(*items)
        self.emitter = ReactiveSetEmitter()

    def add(self, value: Any) -> None:
        if value in self:
            return
        super().add(value)
        self.emitter.emit("item-added", value)

    def remove(self, value: Any) -> None:
        super().remove(value)
        self.emitter.emit("item-removed", value)

    def pop(self) -> Any:
        value = super().pop()
        self.emitter.emit("item-removed", value)
        return value

    def discard(self, value: Any) -> None:
        if value not in self:
            return
        self.remove(value)

    @with_update_signals
    def update(self, *others: Iterable) -> None:
        super().update(*others)

    @with_update_signals
    def intersection_update(self, *others: Iterable) -> None:
        super().intersection_update(*others)

    @with_update_signals
    def difference_update(self, *others: Iterable) -> None:
        super().difference_update(*others)

    @with_update_signals
    def symmetric_difference_update(self, *others: Iterable) -> None:
        super().symmetric_difference_update(*others)
