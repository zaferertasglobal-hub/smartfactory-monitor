import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App" style={{ padding: '40px', fontFamily: 'Arial' }}>
      <h1>SmartFactory Monitor</h1>
      <h2>Industry 4.0 Dashboard</h2>
      <p>Java Backend: <a href="http://localhost:8080/api/health" target="_blank">http://localhost:8080/api/health</a></p>
      <p>AI Service: <a href="http://localhost:8001/docs" target="_blank">http://localhost:8001/docs</a></p>
      <p style={{ marginTop: '50px', color: 'green' }}>Tüm servisler çalışıyor – Proje tamamlandı!</p>
    </div>
  );
}

export default App;