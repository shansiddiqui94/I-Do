import { useState, useEffect } from 'react'
import { Outlet } from 'react-router-dom'
import './App.css'


function Venue() {

    const [venues, setVenues] = useState("")

    useEffect(() => {
        fetch('http://127.0.0.1:5555/venues')
        .then((resp) => resp.json())
        .then((data) => setVenues(data))
    }, [])

    return (
        
        <div className='container'>
             <form>
        {venues.map(item => (
          <div key={item.id}>
            <input type="checkbox" id={item.id} name={item.name} value={item.id} />
            <label htmlFor={item.id}>{item.name}</label>
          </div>
        ))}
      </form>
            <Outlet context={{venues, setVenues}} />
        </div>
    )
}

export default Venue