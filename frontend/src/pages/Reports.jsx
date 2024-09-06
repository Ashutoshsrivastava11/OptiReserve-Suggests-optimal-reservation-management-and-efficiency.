import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const Reports = () => {
    const [reportData, setReportData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchReportData = async () => {
            try {
                const response = await axios.get('/api/reports/statistics');
                setReportData(response.data);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };

        fetchReportData();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    const chartData = {
        labels: reportData.labels, // E.g., ['January', 'February', 'March']
        datasets: [
            {
                label: 'Reservations',
                data: reportData.data, // E.g., [10, 20, 30]
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 1,
            },
        ],
    };

    const chartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: (context) => `Reservations: ${context.raw}`,
                },
            },
        },
    };

    return (
        <div className="reports-container">
            <h2>Reservation Reports</h2>
            <div className="chart-container">
                <Line data={chartData} options={chartOptions} />
            </div>
        </div>
    );
};

export default Reports;
