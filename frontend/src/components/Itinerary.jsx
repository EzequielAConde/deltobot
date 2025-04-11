import React, { useEffect, useState } from 'react';
import "../styles/Itinerary.css";

const Itinerary = () => {
  const [datos, setDatos] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/planes')
      .then(res => res.json())
      .then(data => setDatos(data))
      .catch(err => console.error("Error al obtener planes:", err));
  }, []);

  if (!datos) return <div className="pixel-box">Cargando planes de viaje...</div>;

  return (
    <div className="pixel-box">
      <div className="seccion">
        <h3>Mira esta gran idea:</h3>
        <p>{datos.planes_ia}</p>
      </div>
    </div>
  );
};

export default Itinerary;
