from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from . import calculator


@dataclass
class QuickCalcSession:
    display: str = "0"
    _stored_value: Optional[float] = None
    _pending_op: Optional[str] = None
    _is_new_entry: bool = True
    _error: Optional[str] = None

    def press_digit(self, digit: str) -> None:
        if self._error:
            return
        if digit not in "0123456789":
            raise ValueError("digit must be 0-9")

        if self._is_new_entry:
            self.display = digit
            self._is_new_entry = False
        else:
            self.display = (self.display + digit) if self.display != "0" else digit

    def press_dot(self) -> None:
        if self._error:
            return
        if self._is_new_entry:
            self.display = "0."
            self._is_new_entry = False
            return
        if "." not in self.display:
            self.display += "."

    def press_operator(self, op: str) -> None:
        if self._error:
            return
        if op not in {"+", "-", "*", "/"}:
            raise ValueError("Unsupported operator")

        current = float(self.display)

        if self._pending_op is not None and self._stored_value is not None and not self._is_new_entry:
            self._apply_pending(current)
        else:
            self._stored_value = current

        self._pending_op = op
        self._is_new_entry = True

    def press_equals(self) -> None:
        if self._error:
            return
        if self._pending_op is None or self._stored_value is None:
            return

        current = float(self.display)
        self._apply_pending(current)

        self._pending_op = None
        self._is_new_entry = True

    def press_clear(self) -> None:
        self.display = "0"
        self._stored_value = None
        self._pending_op = None
        self._is_new_entry = True
        self._error = None

    def _apply_pending(self, current: float) -> None:
        assert self._pending_op is not None
        assert self._stored_value is not None

        try:
            if self._pending_op == "+":
                result = calculator.add(self._stored_value, current)
            elif self._pending_op == "-":
                result = calculator.subtract(self._stored_value, current)
            elif self._pending_op == "*":
                result = calculator.multiply(self._stored_value, current)
            elif self._pending_op == "/":
                result = calculator.divide(self._stored_value, current)
            else:
                raise ValueError("Unknown pending operation")

            self._stored_value = result
            self.display = str(int(result)) if result.is_integer() else str(result)

        except calculator.DivisionByZeroError:
            self._error = "DIV/0"
            self.display = "DIV/0"
            self._stored_value = None
            self._pending_op = None
            self._is_new_entry = True