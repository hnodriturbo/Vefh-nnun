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
    <div className="d-flex">
      <i
        className="bi bi-translate"
        onClick={() => handleLanguageChange('en')}
        style={{ cursor: 'pointer', fontSize: '24px', margin: '0 5px' }}
        title="Switch to English"
      />
      <i
        className="bi bi-translate"
        onClick={() => handleLanguageChange('is')}
        style={{ cursor: 'pointer', fontSize: '24px', margin: '0 5px' }}
        title="Switch to Icelandic"
      />
    </div>
  );
};

export default LanguageSwitcher;
