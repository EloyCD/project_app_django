import React, { useState } from 'react';
import axios from 'axios';

function GameForm({ game, setGames }) {
  const [title, setTitle] = useState(game ? game.title : '');

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = { title };
    if (game) {
      axios.put(`http://localhost:8000/api/games/${game.id}/`, data)
        .then(response => {
          // Actualizar lista de juegos
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    } else {
      axios.post('http://localhost:8000/api/games/', data)
        .then(response => {
          // Actualizar lista de juegos
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={title} 
        onChange={(e) => setTitle(e.target.value)} 
        placeholder="Nombre del juego" 
      />
      <button type="submit">Guardar</button>
    </form>
  );
}
export default GameForm;
