import React from "react";
import './style.css'
import marriedcouple from './photos/marriedcouple.jpg'
import MainContent from "./components/MainContent";
function FrontPage() {
  return (
    <div className="w-64 h-64 bg-gray-200 flex justify-center items-center">
      {/* Add your content here */}
      <img src={marriedcouple} alt="Your Photo" className="w-32 h-32 rounded-full" />
      <MainContent/>
    </div>
  );
}
 export default FrontPage;

 