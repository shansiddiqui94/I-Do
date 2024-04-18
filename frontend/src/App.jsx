import React from 'react';
import Entertainment from  "./components/Entertainment";
import VenueList from './components/VenueList';
import './App.css';
import FrontPage from './frontpage.jsx';
import './style.css'
import { Link, NavLink, RouterProvider, createBrowserRouter } from 'react-router-dom';
import MainContent from './components/MainContent.jsx';
import Bullshit1 from './components/bullshit1.jsx';
import Bullshit2 from './components/bullshit2.jsx';
import Bullshit3 from './components/bullshit3.jsx';
// import MainContent from './components/MainContent.jsx';

// TODO:  App needs to contain the browser-router with the
//        `router` variable (like how Sakib's `index.js`) looks.
//        The default parent component for the router should point to 
//        <Main>. The children of <Main> should start with the actual 
//        default content on page, which should be the venue data, or
//        <VenueList>. Other components can follow.

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <MainContent />,
      errorElement: <Bullshit3 />, // postcard
      children: [
        {
          // Default child (loads at home page)
          path: "/",
          element: <Bullshit1 /> // venue
        },
        {
          // Second child (triggered by button click)
          path: "/nextpage",
          element: <Bullshit2 /> // entertainment
        },
        {
          // Third child (final page triggered by button click from second page)
          path: "/finalpage",
          element: <Bullshit3 /> // postcard
        }
      ]
    }
  ]);

  return (
    <div className="App">
      <h1>Ben please pass us</h1>
     <RouterProvider router={router}/>
    </div>
  );
}

export default App;