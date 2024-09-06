import React, { useState } from 'react';
import apiService from '../services/apiService';
import './BookingForm.css';

const BookingForm = () => {
    const [formData, setFormData] = useState({ name: '', date: '', time: '' });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await apiService.bookReservation(formData);
        alert("Reservation booked successfully!");
    };

    return (
        <div className="booking-form">
            <h2>Book a Reservation</h2>
            <form onSubmit={handleSubmit}>
                <input name="name" type="text" placeholder="Name" onChange={handleChange} />
                <input name="date" type="date" onChange={handleChange} />
                <input name="time" type="time" onChange={handleChange} />
                <button type="submit">Book</button>
            </form>
        </div>
    );
};

export default BookingForm;
