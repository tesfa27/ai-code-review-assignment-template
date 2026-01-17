# AI Code Review Assignment (Python)

## Candidate
- Name:
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- **Division by zero/incorrect denominator**: Function divides total by `len(orders)` instead of count of non-cancelled orders, causing incorrect average calculation
- **Logic inconsistency**: Excludes cancelled orders from sum but includes them in count, leading to mathematically incorrect results

### Edge cases & risks
- **Empty orders list**: Will cause ZeroDivisionError when `len(orders)` is 0
- **All orders cancelled**: Will result in incorrect average (0 total / total count = 0) instead of undefined/no valid data
- **Missing required fields**: No validation for order structure (missing 'status' or 'amount' keys will cause KeyError)
- **Invalid data types**: No type checking for order amounts (non-numeric values will cause TypeError)
- **Case sensitivity**: Status comparison is not case-sensitive ("Cancelled" vs "cancelled")
- **Negative amounts**: No validation against negative values which could be refunds or corrupted data

### Code quality / design issues
- **No input validation**: Function assumes orders is a list of dictionaries with specific structure
- **Unclear variable naming**: `count` represents total orders, not valid orders count

## 2) Proposed Fixes / Improvements
### Summary of changes
- Fix denominator to use count of non-cancelled orders instead of total orders
- Add input validation for empty lists and data structure
- Add defensive programming for missing keys and invalid data types
- Improve variable naming for clarity
- Add case-insensitive status checking
- Reject negative amounts to prevent data corruption

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- **Empty input**: Test with empty list to ensure proper handling
- **All cancelled orders**: Verify behavior when no valid orders exist
- **Mixed order statuses**: Test with combination of cancelled and non-cancelled orders
- **Invalid data structures**: Test with malformed order dictionaries (missing keys, wrong types)
- **Edge case amounts**: Test with zero amounts, negative amounts, and non-numeric values
- **Large datasets**: Performance testing with many orders


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- **Factually incorrect**: Claims it "correctly excludes cancelled orders from the calculation" but the denominator still includes cancelled orders
- **Misleading**: Suggests the function works properly when it has a fundamental mathematical error
- **Incomplete**: Doesn't mention any edge cases or potential failure scenarios

### Rewritten explanation
- This function attempts to calculate average order value by summing amounts of non-cancelled orders, but contains a critical bug: it divides by the total number of orders instead of the count of valid (non-cancelled) orders. This results in incorrect average calculations. The function also lacks input validation and error handling for edge cases like empty lists or malformed data.

## 4) Final Judgment
- Decision: Reject
- Justification: Contains critical mathematical error that produces incorrect results. The function divides by total orders instead of valid orders, making the average calculation fundamentally wrong. Additionally lacks basic input validation and error handling.
- Confidence & unknowns: High confidence in the mathematical error identification. Function needs complete rewrite of the calculation logic and addition of proper error handling.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
