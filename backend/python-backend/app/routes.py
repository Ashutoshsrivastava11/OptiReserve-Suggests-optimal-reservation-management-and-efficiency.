from fastapi import APIRouter, HTTPException, Depends
from typing import List
from datetime import datetime
from .models import Reservation, User, ReservationCreate, ReservationUpdate
from .analytics import get_reservation_statistics, get_reservations_by_date, get_cancellation_rate
from .helper import validate_date, format_date, get_current_timestamp

router = APIRouter()

@router.post("/reservations/", response_model=Reservation)
async def create_reservation(reservation: ReservationCreate) -> Reservation:
    """
    Create a new reservation.

    Args:
        reservation (ReservationCreate): The reservation data.

    Returns:
        Reservation: The created reservation.
    """
    # Here you would typically add logic to save the reservation to a database
    reservation_id = 1  # Dummy ID for demonstration
    return {**reservation.dict(), "id": reservation_id}

@router.get("/reservations/", response_model=List[Reservation])
async def read_reservations(start_date: str, end_date: str) -> List[Reservation]:
    """
    Retrieve reservations within a specific date range.

    Args:
        start_date (str): The start date for filtering reservations (YYYY-MM-DD).
        end_date (str): The end date for filtering reservations (YYYY-MM-DD).

    Returns:
        List[Reservation]: A list of reservations within the specified date range.
    """
    valid, error = validate_date(start_date)
    if not valid:
        raise HTTPException(status_code=400, detail=error)

    valid, error = validate_date(end_date)
    if not valid:
        raise HTTPException(status_code=400, detail=error)

    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    reservations = get_reservations_by_date(start, end)
    return reservations

@router.get("/reservations/stats/")
async def read_reservation_statistics() -> dict:
    """
    Retrieve reservation statistics.

    Returns:
        dict: A dictionary containing reservation statistics.
    """
    stats = get_reservation_statistics()
    return stats

@router.get("/reservations/cancellation-rate/")
async def read_cancellation_rate() -> dict:
    """
    Retrieve the cancellation rate.

    Returns:
        dict: A dictionary containing the cancellation rate.
    """
    rate = get_cancellation_rate()
    return {"cancellation_rate": rate}

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int) -> User:
    """
    Retrieve a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        User: The user with the specified ID.
    """
    # Here you would typically add logic to retrieve the user from a database
    user = {"id": user_id, "name": "John Doe", "email": "john.doe@example.com"}
    return user

@router.put("/reservations/{reservation_id}", response_model=Reservation)
async def update_reservation(reservation_id: int, reservation: ReservationUpdate) -> Reservation:
    """
    Update an existing reservation.

    Args:
        reservation_id (int): The ID of the reservation to update.
        reservation (ReservationUpdate): The updated reservation data.

    Returns:
        Reservation: The updated reservation.
    """
    # Here you would typically add logic to update the reservation in a database
    updated_reservation = {**reservation.dict(), "id": reservation_id}
    return updated_reservation

@router.delete("/reservations/{reservation_id}")
async def delete_reservation(reservation_id: int) -> dict:
    """
    Delete a reservation by its ID.

    Args:
        reservation_id (int): The ID of the reservation to delete.

    Returns:
        dict: A confirmation message.
    """
    # Here you would typically add logic to delete the reservation from a database
    return {"message": f"Reservation with ID {reservation_id} deleted successfully."}
