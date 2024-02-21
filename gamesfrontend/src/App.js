import React from 'react';
import Navbar from './components/Navbar';
import GameList from './components/GameList';
// Importar BrowserRouter, Route, etc., si usas enrutamiento

function App() {
  return (
    <div>
      <Navbar />
      <GameList />
      {/* Rutas para otros componentes como GameForm */}
    </div>
  );
}

export default App;
