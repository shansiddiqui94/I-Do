// import marriedcouple from '../photos/marriedcouple'
// This is where Venue and Entertainment live
import React from "react";
import { NavLink, useOutletContext } from "react-router-dom";
// import "./MainContent.css"; // Import your CSS file

// TODO:  Main needs <Outlet> (and probably <Nav>). It definitely
//        needs <Outlet> so that it knows to default to other child
//        components (like <VenueList>). Check out Sakib's <Root.jsx>
//        component for an example.

function Bullshit2() {
    const [currentPage, setCurrentPage] = useOutletContext();
    return (
        // <div className="main-content-container">
        //      <div className="overlay"></div>
        //         <div className="main-content">
         
        //     </div>
        // </div>
        <>
            <h1>this is some more bullshit!!!!</h1>
            <p>{currentPage}</p>
            <NavLink to="finalpage" replace onClick={() => {setCurrentPage("postcard")}}>
                Click Me!
            </NavLink>
        </>
    );
}
export default Bullshit2
