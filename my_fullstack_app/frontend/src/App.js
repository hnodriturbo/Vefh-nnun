import React, { useEffect } from 'react';





import { Route, Routes } from 'react-router-dom';


import Home from './components/Home';



import Navbar from './components/Navbar';
import Login from './components/Login';
import Register from './components/Register';

import { addGoogleTranslateScript, initGoogleTranslate } from './components/googleTranslateInit'; // Import the functions



import TopImage from './components/TopImage'; // Import the TopImage component


import LanguageSwitcher from './components/LanguageSwitcher';

const App = () => {

    useEffect(() => {
        addGoogleTranslateScript(); // Add the Google Translate script
      }, []);
    
      useEffect(() => {
        initGoogleTranslate(); // Initialize Google Translate
      }, []);




    return (
        <div className="App">

            
            <Navbar />

            <div className="d-flex justify-content-end p-3">
            <LanguageSwitcher />
            </div>


            <TopImage /> {/* Add the TopImage component */}

            <div className="container-fluid d-flex align-items-center justify-content-center mt-5">
                <Routes>
                <Route exact path="/" element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                {/* Add other routes here */}
                </Routes>
            </div>
            <div id="google_translate_element" style={{ display: 'none' }}></div>
        </div>
    );
};

export default App;
