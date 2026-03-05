# TESTING STRATEGY — Quick-Calc

## 1. What I Tested (and Why)
This project is split into two layers:
1) **Core calculation logic** (`quick_calc/calculator.py`) tested with **unit tests** to validate each operation in isolation.
2) **Input/controller session layer** (`quick_calc/session.py`) tested with **integration tests** to verify button-press interactions produce correct results.

### Tested
- Addition, subtraction, multiplication, division
- Edge cases:
  - Division by zero (handled gracefully)
  - Negative numbers
  - Decimal arithmetic (checked using approximate comparison)

### Not Tested
- Real GUI rendering (Tkinter/React/etc.)
  - Reason: the focus is testing strategy and code quality, not UI complexity.
- Non-functional concerns (performance, security, accessibility)
  - Reason: outside scope for v1.0.0 of a small calculator.

## 2. Lecture Concepts Applied

### Testing Pyramid
The suite reflects the Testing Pyramid:
- **Many unit tests** (fast, isolated)
- **Few integration tests** (broader behavior across components)

### Black-box vs White-box Testing
- **Unit tests:** mostly **white-box** (testing specific functions and known edge cases).
- **Integration tests:** closer to **black-box** (simulate user actions and assert observable outputs).

### Functional vs Non-Functional Testing
- **Functional:** covered (correct results, clear reset, error handling).
- **Non-functional:** intentionally not covered (performance, security, etc.).

### Regression Testing
Running `pytest` after changes helps catch regressions. If a future update breaks division-by-zero handling or user interaction flow, tests fail and signal the regression quickly.

## 3. Test Results Summary

| Test Name                                   | Type         | Status |
|--------------------------------------------|--------------|--------|
| test_add_integers                           | Unit         | Pass   |
| test_subtract_integers                      | Unit         | Pass   |
| test_multiply_integers                      | Unit         | Pass   |
| test_divide_integers                        | Unit         | Pass   |
| test_divide_by_zero_raises                  | Unit         | Pass   |
| test_negative_numbers_subtraction           | Unit         | Pass   |
| test_decimal_addition                       | Unit         | Pass   |
| test_large_number_multiplication            | Unit         | Pass   |
| test_full_user_interaction_addition         | Integration  | Pass   |
| test_clear_resets_after_calculation         | Integration  | Pass   |