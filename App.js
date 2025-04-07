import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import ListerDashboard from './pages/ListerDashboard';
import CollectorDashboard from './pages/CollectorDashboard';
import Login from './components/LoginForm';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route exact path="/" component={Login} />
          <Route path="/lister-dashboard" component={ListerDashboard} />
          <Route path="/collector-dashboard" component={CollectorDashboard} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
