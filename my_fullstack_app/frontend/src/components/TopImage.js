import React from 'react';
import topImage from '../img/top_img.gif'; 

const TopImage = () => {
  return (
    <div className="container my-3">
      <img src={topImage} className="img-fluid" alt="Top" />
    </div>
  );
};

export default TopImage;
