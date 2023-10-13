"""Volt/Generic/GetterSetter"""


from typing import Any, Callable


SET = 0
GET = 1

class GetterSetter:
    """Getter/Setter. Implements new syntax so you can implement getter and setter in one line."""

    value: Any = None

    on_upd: Callable = None

    def __init__(self, value: Any=None, on_upd: Callable=None) -> None:
        """
        Initialize GetterSetter.

        `value` - Value.
        """
        self.value = value

        self.on_update(on_upd)

    def on_update(self, on_upd: Callable) -> None:
        """Set on update."""
        self.on_upd = on_upd

    def __getitem__(self, _) -> Any:
        """Get/Set item."""
        if isinstance(_, tuple):
            if _[0] == SET:
                self.value = _[1]

                if self.on_upd:
                    self.on_upd(_[1])

                return _[1]

        else:
            if _ == GET:
                return self.value
