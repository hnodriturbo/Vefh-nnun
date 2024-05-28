
import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';


import './styles/bootstrap.css';
import './styles/custom.css';
import './styles/border-styles.css';
import './styles/extras.css';
import './styles/linear-gradient-styles.css';
import './styles/font-css.css';


import { BrowserRouter as Router } from 'react-router-dom';


const container = document.getElementById('root');
const root = createRoot(container); // CreateRoot is now the method used in React 18

root.render(
    <Router>
        <App />
    </Router>,
);