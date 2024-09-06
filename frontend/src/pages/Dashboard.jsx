import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line, Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend);

const Dashboard = () => {
    const [reservationData, setReservationData] = useState(null);
    const [recentActivities, setRecentActivities] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchDashboardData = async () => {
            try {
                const [reservationsResponse, activitiesResponse] = await Promise.all([
                    axios.get('/api/reports/statistics'),
                    axios.get('/api/activities/recent')
                ]);
                setReservationData(reservationsResponse.data);
                setRecentActivities(activitiesResponse.data);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };

        fetchDashboardData();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    const reservationChartData = {
        labels: reservationData.labels,
        datasets: [
            {
                label: 'Reservations',
                data: reservationData.data,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 1,
            },
        ],
    };

    const recentActivitiesData = {
        labels: recentActivities.map(activity => activity.date),
        datasets: [
            {
                label: 'Recent Activities',
                data: recentActivities.map(activity => activity.count),
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1,
            },
        ],
    };

    return (
        <div className="dashboard-container">
            <h1>Dashboard</h1>
            <section className="summary-section">
                <h2>Reservation Summary</h2>
                <div className="chart-container">
                    <Line data={reservationChartData} options={{ responsive: true }} />
                </div>
            </section>

            <section className="recent-activities-section">
                <h2>Recent Activities</h2>
                <div className="chart-container">
                    <Bar data={recentActivitiesData} options={{ responsive: true }} />
                </div>
            </section>

            <section className="quick-actions-section">
                <h2>Quick Actions</h2>
                <div className="quick-actions">
                    <button className="btn">Add Reservation</button>
                    <button className="btn">Manage Users</button>
                    <button className="btn">View Reports</button>
                </div>
            </section>
        </div>
    );
};

export default Dashboard;
