import React from 'react';


const LanguageSwitcher = () => {
  const handleLanguageChange = (lang) => {
    const googleTranslateElement = document.querySelector('.goog-te-combo');
    if (googleTranslateElement) {
      googleTranslateElement.value = lang;
      googleTranslateElement.dispatchEvent(new Event('change'));
    }
  };

  return (
    <div className="container-fluid d-flex align-items-center justify-content-center">
        <div className="col-auto">
            <i
                className="bi bi-translate"
                onClick={() => handleLanguageChange('en')}
                style={{ cursor: 'pointer', fontSize: '12px', margin: '0 5px' }}
                title="Switch to English"
            /> 
            Switch to English  
        </div>
        
        <div className="col-auto">

                    
        </div>

        <i
            className="bi bi-translate"
            onClick={() => handleLanguageChange('is')}
            style={{ cursor: 'pointer', fontSize: '12px', margin: '0 5px' }}
            title="Switch to Icelandic"
        /> Switch to Icelandic
    </div>
  );
};

export default LanguageSwitcher;
