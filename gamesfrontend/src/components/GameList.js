import React, { useEffect, useState } from 'react';
import axios from 'axios';

function GameList() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/games/')
      .then(response => {
        setGames(response.data);
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  }, []);

  return (
    <div>
      {games.map(game => (
        <div key={game.id}>
          <h3>{game.title}</h3>
          {/* Otros detalles del juego */}
        </div>
      ))}
    </div>
  );
}
export default GameList;