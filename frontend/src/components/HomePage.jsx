import React, { useState, useEffect } from 'react';
import apiService from '../services/apiService';
import './HomePage.css';

const HomePage = () => {
    const [reservations, setReservations] = useState([]);

    useEffect(() => {
        apiService.getReservations().then(setReservations);
    }, []);

    return (
        <div className="home-page">
            <h1>Available Reservations</h1>
            <ul>
                {reservations.map(res => (
                    <li key={res.id}>{res.customerName} - {res.reservationDate}</li>
                ))}
            </ul>
        </div>
    );
};

export default HomePage;
