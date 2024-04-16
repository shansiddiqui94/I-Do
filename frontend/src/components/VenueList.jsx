import { useState, useEffect } from 'react';

function VenueList() {
    const [venues, setVenues] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5555/venues')
            .then(resp => resp.json())
            .then(data => setVenues(data))
            .catch(error => console.error('Error fetching venues:', error));
    }, []);

    return (
        <div className="container mx-auto px-4">
            <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
                {venues.map(item => (
                    <div className="bg-white rounded-lg shadow-lg p-4" key={item.id}>
                        {/* Venue Name */}
                        <h2 className="text-xl font-semibold mb-2">{item.name}</h2>
                        {/* Address */}
                        <p className="text-gray-600">{item.address}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default VenueList;
