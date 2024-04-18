// import marriedcouple from '../photos/marriedcouple'
// This is where Venue and Entertainment live
import React from "react";
import { NavLink } from "react-router-dom";
// import "./MainContent.css"; // Import your CSS file

// TODO:  Main needs <Outlet> (and probably <Nav>). It definitely
//        needs <Outlet> so that it knows to default to other child
//        components (like <VenueList>). Check out Sakib's <Root.jsx>
//        component for an example.

function GoHome() {
    return (
        // <div className="main-content-container">
        //      <div className="overlay"></div>
        //         <div className="main-content">
         
        //     </div>
        // </div>
        <>
            <h1>This is a header.</h1>
            <NavLink to="/">
                Go Home
            </NavLink>
        </>
    );
}
export default GoHome