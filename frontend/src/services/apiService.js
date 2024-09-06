const apiService = {
    getReservations: async () => {
        const response = await fetch('/api/reservations');
        return response.json();
    },

    bookReservation: async (data) => {
        const response = await fetch('/api/reservations/book', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        return response.json();
    }
};

export default apiService;
