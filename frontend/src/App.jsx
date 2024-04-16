import React from 'react';
import Entertainment from  "./components/Entertainment"
import VenueList from './components/VenueList'
import './App.css'

function App() {
  return (
    <div className="App">
     <p>I-Do</p>
     <Entertainment />
     <VenueList/>

    </div>
  );
}

export default App;