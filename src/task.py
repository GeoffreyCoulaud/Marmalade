from functools import partial
from typing import Any, Callable, Iterable, Mapping, Optional

from gi.repository import Gio


def nop(*_args, **_kwargs):
    """A function that does nothing"""


class Task:
    """
    Wrapper around async Gio Tasks.

    - `error_callback` must accept `error` as a keyword argument.
    - `callback` must accept `result` as a keyword argument.
    - If `main` raises an exception, `error_callback` will receive it in `error`.
    - Else, `callback` will receive the return value in `result`.
    - If `callback` or `error_callback` are not passed, they will be NOP.
    - The task is assigned a Gio.Cancellable, unless one is passed.
    - By setting `return_on_cancel` to `True`, cancelling will exit `main` immediately.
    """

    __gio_task: Gio.Task
    __main: Callable
    __callback: Callable
    __error_callback: Callable
    __cancellable: Gio.Cancellable

    # Set at run time
    __result: Optional[Any] = None
    __error: Optional[Exception] = None

    @property
    def return_on_cancel(self) -> bool:
        return self.__gio_task.get_return_on_cancel()

    @return_on_cancel.setter
    def return_on_cancel(self, value: bool) -> None:
        self.__gio_task.set_return_on_cancel(value)

    # pylint: disable=dangerous-default-value
    # Using single-use empty dicts, it doesn't matter.
    def __init__(
        self,
        main: Callable,
        main_args: Iterable = (),
        main_kwargs: Mapping[str, Any] = {},
        callback: Callable = nop,
        callback_args: Iterable = (),
        callback_kwargs: Mapping[str, Any] = {},
        error_callback: Callable = nop,
        error_callback_args: Iterable = (),
        error_callback_kwargs: Mapping[str, Any] = {},
        cancellable: Optional[Gio.Cancellable] = None,
        return_on_cancel: bool = True,
    ) -> None:
        # Create or pass the cancellable
        if cancellable is None:
            self.__cancellable = Gio.Cancellable()
        else:
            self.__cancellable = cancellable
        # Bind the functions
        self.__main = partial(main, *main_args, **main_kwargs)
        self.__callback = partial(callback, *callback_args, **callback_kwargs)
        self.__error_callback = partial(
            error_callback, *error_callback_args, **error_callback_kwargs
        )
        # Create the task
        self.__gio_task = Gio.Task.new(
            None, self.__cancellable, self.__gio_callback, None
        )
        # Configure the task
        self.return_on_cancel = return_on_cancel

    def __gio_callback(self, _source_object, _result, _data) -> None:
        if self.__error is not None:
            self.__error_callback(error=self.__error)
        else:
            self.__callback(result=self.__result)

    def __gio_main(self, _task, _source_object, _task_data, _cancellable) -> None:
        try:
            result: object = self.__main()
        except Exception as error:  # pylint: disable=broad-exception-caught
            self.__error = error
        else:
            self.__result = result

    def run(self) -> None:
        """Run the task's main function in a separate thread"""
        self.__gio_task.run_in_thread(self.__gio_main)

    def cancel(self) -> None:
        """Cancel the task"""
        self.__cancellable.cancel()
