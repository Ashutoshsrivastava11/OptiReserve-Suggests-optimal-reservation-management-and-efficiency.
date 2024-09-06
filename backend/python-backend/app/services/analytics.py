from datetime import datetime
from typing import Dict, List

# Dummy data for demonstration purposes
reservations = [
    {"id": 1, "customer_name": "Alice", "status": "confirmed", "date": datetime(2024, 9, 1)},
    {"id": 2, "customer_name": "Bob", "status": "canceled", "date": datetime(2024, 9, 2)},
    {"id": 3, "customer_name": "Charlie", "status": "confirmed", "date": datetime(2024, 9, 3)},
]

def get_reservation_statistics() -> Dict[str, int]:
    """
    Calculate and return statistics on reservations.

    Returns:
        Dict[str, int]: A dictionary containing reservation statistics.
    """
    total_reservations = len(reservations)
    canceled_reservations = sum(1 for res in reservations if res["status"] == "canceled")
    
    return {
        "total_reservations": total_reservations,
        "canceled_reservations": canceled_reservations
    }

def get_reservations_by_date(start_date: datetime, end_date: datetime) -> List[Dict]:
    """
    Retrieve reservations within a specific date range.

    Args:
        start_date (datetime): The start date for the query.
        end_date (datetime): The end date for the query.

    Returns:
        List[Dict]: A list of reservations within the specified date range.
    """
    return [
        res for res in reservations
        if start_date <= res["date"] <= end_date
    ]

def get_cancellation_rate() -> float:
    """
    Calculate and return the rate of cancellations as a percentage.

    Returns:
        float: The cancellation rate percentage.
    """
    total_reservations = len(reservations)
    if total_reservations == 0:
        return 0.0
    canceled_reservations = sum(1 for res in reservations if res["status"] == "canceled")
    return (canceled_reservations / total_reservations) * 100
