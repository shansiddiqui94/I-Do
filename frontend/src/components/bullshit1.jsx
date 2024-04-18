// import marriedcouple from '../photos/marriedcouple'
// This is where Venue and Entertainment live
import React from "react";
import { NavLink, useOutletContext } from "react-router-dom";
// import "./MainContent.css"; // Import your CSS file

// TODO:  Main needs <Outlet> (and probably <Nav>). It definitely
//        needs <Outlet> so that it knows to default to other child
//        components (like <VenueList>). Check out Sakib's <Root.jsx>
//        component for an example.

function Bullshit1() {
    const [currentPage, setCurrentPage] = useOutletContext();
    return (
        // <div className="main-content-container">
        //      <div className="overlay"></div>
        //         <div className="main-content">
         
        //     </div>
        // </div>
        <>
            <h1>Please Choose your desired venue</h1>
            <p>{currentPage}</p>
            <NavLink to="nextpage" onClick={() => {setCurrentPage("entertainment")}}>
                NEXT!
            </NavLink>
        </>
    );
}
export default Bullshit1
