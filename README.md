
## Installation

### Prerequisites

- **Node.js**: For running the frontend.
- **Java JDK**: For the backend.
- **Python**: For analytics services.
- **PostgreSQL**: For the database.

### Frontend Setup

1. **Navigate to the frontend directory:**

    ```bash
    cd frontend
    ```

2. **Install dependencies:**

    ```bash
    npm install
    ```

3. **Start the development server:**

    ```bash
    npm start
    ```

### Backend Setup

1. **Navigate to the backend directory:**

    ```bash
    cd backend
    ```

2. **Configure your database connection in `src/main/resources/application.properties`.**

3. **Build and run the application:**

    ```bash
    ./mvnw spring-boot:run
    ```

### Python Analytics Setup

1. **Navigate to the python-backend directory:**

    ```bash
    cd python-backend
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the analytics service:**

    ```bash
    python analytics/analysis.py
    ```

## Usage

1. **Access the Application**: 
   - Frontend: Open your web browser and go to `http://localhost:3000`.
   - Backend API: Navigate to `http://localhost:8080`.

2. **Create a Reservation**: Use the ReservationForm component in the frontend to create a new reservation.

3. **View Reports**: Go to the Reports section to view reservation analytics and trends.

## Contributing

We welcome contributions to improve OptiReserve. To contribute:

1. **Fork the Repository**: Click on "Fork" at the top-right of this page.

2. **Clone Your Fork**:

    ```bash
    git clone https://github.com/your-username/optitreserve.git
    ```

3. **Create a Branch**:

    ```bash
    git checkout -b feature/your-feature
    ```

4. **Make Your Changes** and commit them:

    ```bash
    git add .
    git commit -m "Add a descriptive commit message"
    ```

5. **Push to Your Fork**:

    ```bash
    git push origin feature/your-feature
    ```

6. **Open a Pull Request**: Go to the original repository and click on "New Pull Request".

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact:

- **Email**: support@optitreserve.com
- **Phone**: +1 234 567 890
