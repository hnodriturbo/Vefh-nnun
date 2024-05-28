import React from 'react';
import { Link } from 'react-router-dom';

import LanguageSwitcher from './LanguageSwitcher';



const Navbar = () => {


/*     useEffect(() => {
      const handleResize = () => {
        const brand = document.querySelector('.navbar-brand');
        if (window.innerWidth >= 768) {
          brand.classList.add('ms-auto');
        } else {
          brand.classList.remove('ms-auto');
        }
      };
      
      window.addEventListener('resize', handleResize);
      handleResize(); // Initial check
  
      return () => {
        window.removeEventListener('resize', handleResize);
      };
    }, []); */




  return (
    <nav className="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
        <div className="container-fluid no-wrap">
            <div className="container-fluid">
                
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#navbarNav"
                        aria-controls="navbarNav"
                        aria-expanded="false"
                        aria-label="Toggle navigation"
                    >

                        <span className="navbar-toggler-icon"></span>

                    </button>
                
                    <Link className="navbar-brand me-auto ms-md-auto my-navbar-brand-styles" to="/">
                        The Best IPTV Service You Can Get
                    </Link>
                    <LanguageSwitcher /> {/* Add the LanguageSwitcher component here */}
                    
            </div>

            <div className="collapse navbar-collapse mt-2" id="navbarNav">

                    <ul className="navbar-nav me-auto">
                        <li className="nav-item">
                            <Link className="nav-pill btn btn-outline-secondary my-navbar-btn-styles" to="/">Home</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-pill btn btn-outline-light my-navbar-btn-styles" to="/login">Login</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-pill btn btn-outline-info my-navbar-btn-styles bold-underlined" to="/register">Get Your Free Trial !!!</Link>
                        </li>
                    </ul>
                    
            </div>

        </div>
        <div id="google_translate_element" style={{ display: 'none' }}></div>
    </nav>
  );
};

export default Navbar;
