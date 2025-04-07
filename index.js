import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';  // Optional: global CSS file for the entire app
import App from './App'; // Main React app component
import { BrowserRouter as Router } from 'react-router-dom'; // For routing

// Rendering the React app and wrapping it with Router to enable routing
ReactDOM.render(
  <React.StrictMode>
    <Router>  {/* Enables routing functionality in the app */}
      <App />  {/* Main application component */}
    </Router>
  </React.StrictMode>,
  document.getElementById('root')  // This attaches the app to the HTML element with id 'root'
);
