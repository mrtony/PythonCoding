"""
如果一個函數是供Modulation 內部使用的，不應該從外部直接訪問，那麼在其名稱前加上下劃線( _ ) 。
例如，_calculate_internal_metrics。
對於傳回布林值（真/假）的函數，強烈建議使用is_ , has_或can_這樣的前綴，以即時提示其性質。這將大大提高程式碼的可讀性，因為僅從名稱就能看出函數的目的。讓我們來看幾個例子。
"""

def is_valid_email(email):
    # ... (Validation logic)
    return True  # Or False based on validation

def has_sufficient_balance(account):
    # ... (Balance check logic)
    return True  # Or False based on balance

def can_access_resource(user, resource):
    # ... (Permission check logic)
    return True  # 

# docstring範例
def calculate_monthly_payment(principal: float, interest_rate: float, loan_term_years: int) -> float:
    """
    Calculates the monthly payment for a fixed-rate loan.

    Args:
        principal: The total amount borrowed (float).
        interest_rate: The annual interest rate (as a decimal, float).
        loan_term_years: The loan term in years (int).

    Returns:
        The monthly payment amount (float).

    Raises:
        ValueError: If any of the inputs are negative or zero.

    Example:
        >>> calculate_monthly_payment(100000, 0.05, 30)
        536.82
    """
    if principal <= 0 or interest_rate <= 0 or loan_term_years <= 0:
        raise ValueError("All input values must be positive.")

    monthly_interest_rate = interest_rate / 12
    number_of_payments = loan_term_years * 12

    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / \
                      ((1 + monthly_interest_rate) ** number_of_payments - 1)

    return round(monthly_payment, 2)