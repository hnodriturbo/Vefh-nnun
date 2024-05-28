import React from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

const Home = () => {
  return (
    <div className="container-fluid mt-2 light-italic drop-shadow responsive-font text-white">
      <div className="text-center mb-4">
      <hr></hr>
        <h1>Welcome to our IPTV Subscription home page !</h1>
        <hr></hr>
        <p>Note that this page is still in production and more features will be added.</p>
        <hr></hr>
      </div>
      <div className="row">
        <div className="col-md-6 mb-4">
          <div className="card my-card-styles">
            <div className="card-body">
              <h5 className="card-title">Best IPTV Apps</h5>
              <ul className="list-group list-group-flush">
                <li className="list-group-item">
                  <Link to="/apps/app1" className="card-link">IPTV Smarters</Link>: <br></br>
                  A user-friendly app designed for IPTV service providers.
                </li>
                <li className="list-group-item">
                  <Link to="/apps/app2" className="card-link">MaxPlayer</Link>: <br></br>
                  MaxPlayer is easy in the styles and let's you navigate easily through your channel list. Easily keep favourites and lot's of good features.
                </li>
                <li className="list-group-item">
                  <Link to="/apps/app3" className="card-link">App 3</Link>: Description of App 3
                </li>
                <li className="list-group-item">
                  <Link to="/apps/app4" className="card-link">App 4</Link>: Description of App 4
                </li>
                <li className="list-group-item">
                  <Link to="/apps/app5" className="card-link">App 5</Link>: Description of App 5
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div className="col-md-6 mb-4">

          <div className="card">
            <div className="card-header">
                <h5 className="card-title text-center">Advertisement</h5>
            </div>

            <div className="card-body">

              <p>
                Get the best IPTV subscription package now! Enjoy unlimited access to hundreds of channels with high-quality streaming.
                Sign up today and get a special discount on your first month.
              </p>
              </div>
              <div className="card-footer">
                <Link className="btn btn-lg btn-info my-navbar-btn-styles ms-auto" to="/learn-more" >Skoða Betur</Link>
                <Link className="btn btn-info my-navbar-btn-styles me-auto" to="/register">Fáðu Fría Prufu</Link>
              </div>
            </div>
          </div>
        </div>
      </div>

  );
};

export default Home;

