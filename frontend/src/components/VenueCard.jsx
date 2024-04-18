import React from "react";
import { useNavigate, useParams } from "react-router-dom";


function VenueCard({ venue }) {
    const navigate = useNavigate();

    function handleClick() {
        navigate("/venues/" + venue.id, {state: {venue: "venue"}})
    }

    return (
        <div onClick={handleClick}  className="venue-card">
          <img src={venue.venue_picture} alt={"venue"} />
          <div className="destination-card-details">
            <h3>{venue.name}</h3>
            <h4>{venue.address}</h4>
            <button className="favorites" > More Information</button>
          </div>
        </div>
      );
}
VenueCard()