import React from "react";
import { useState, useEffect } from "react";




function Entertainment(){
const [ent, setEnt] = useState([])
useEffect(() => {
    fetch('http://127.0.0.1:5555/venues')
      .then(response => response.json())
      .then(data => {
        setEnt(data);
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []) 
  
  return (
    <div>
      <h2>Entertainment Choices</h2>
      <form>
        {ent.map(item => (
          <div key={item.id}>
            <input type="checkbox" id={item.id} name={item.name} value={item.id} />
            <label htmlFor={item.id}>{item.name}</label>
          </div>
        ))}
      </form>
    </div>
  );
}
export default Entertainment