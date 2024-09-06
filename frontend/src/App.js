import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import LoginPage from './components/LoginPage';
import HomePage from './components/HomePage';
import BookingForm from './components/BookingForm';
import UserProfile from './components/UserProfile';
import './styles/App.css';

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route exact path="/" component={LoginPage} />
                    <Route path="/home" component={HomePage} />
                    <Route path="/book" component={BookingForm} />
                    <Route path="/profile" component={UserProfile} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;
