import { useSate, useEffect } from 'react'
import { Outlet } from 'react-router-dom'
import './App.css'


function Venue() {

    const [venues, setVenues] = useSate([])

    useEffect(() => {
        fetch('http://127.0.0.1:5555/venues')
        .then((resp) => resp.json())
        .then((data) => setVenues(data))
    }, [])

    return (
        <div className='container'>
            <Outlet context={{venues, setVenues}} />
        </div>
    )
}

export default Venue