// import marriedcouple from '../photos/marriedcouple'
// This is where Venue and Entertainment live
import React, { useState } from "react";
// import "./MainContent.css"; // Import your CSS file
import { Outlet } from "react-router";
import GoHome from "./gohome";

// TODO:  Main needs <Outlet> (and probably <Nav>). It definitely
//        needs <Outlet> so that it knows to default to other child
//        components (like <VenueList>). Check out Sakib's <Root.jsx>
//        component for an example.

function MainContent() {
    const [currentPage, setCurrentPage] = useState("venues");
    return (
        // <div className="main-content-container">
        //      <div className="overlay"></div>
        //         <div className="main-content">
         
        //     </div>
        // </div>
        <div>
            <Outlet context={[currentPage, setCurrentPage]} />
        </div>
    );
}
export default MainContent
