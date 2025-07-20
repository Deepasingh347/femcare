from datetime import datetime, timedelta

def predict_next_period(last_period_str, cycle_length):
    """
    Predicts the next period start date based on last period and average cycle.
    """
    try:
        last_date = datetime.strptime(last_period_str, '%Y-%m-%d')
        next_date = last_date + timedelta(days=cycle_length)
        return next_date.strftime('%Y-%m-%d')
    except ValueError:
        return "Invalid date format"
