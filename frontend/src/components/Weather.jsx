import { useEffect, useState } from "react";
import "../styles/Weather.css";

{/*
  const capitalizar = (texto) => {
  return texto
    .split(" ")
    .map(palabra => palabra.charAt(0).toUpperCase() + palabra.slice(1))
    .join(" ");
};*/}

const weather = () => {
  const [clima, setClima] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/clima")
      .then((res) => res.json())
      .then((data) => {
        if (data.error) {
          setError(data.error);
        } else {
          setClima(data);
        }
      })
      .catch(() => setError("No se pudo conectar al servidor."));
  }, []);

  if (error) {
    return <div className="error">{error}</div>;
  }

  if (!clima) {
    return <div className="loading">Cargando clima...</div>;
  }

  const getImagen = (maxTemp) => {
    if (maxTemp >= 25) return "./assets/sunny.png";
    if (maxTemp >= 20) return "./assets/evening.png";
    if (maxTemp >= 15) return "./assets/rain.png";
    return "./assets/storm.png";
  };

  return (
    <div className="clima-contenedor">
      <div className="clima-info">
        <h2 className="clima-titulo">Pronóstico para:</h2>
        <h3 className="clima-pais">{clima.pais && clima.pais[0].toUpperCase() + clima.pais.slice(1)}</h3>
      </div>
      <div className="clima-tarjetas">
        {clima.pronostico.map((dia, i) => (
          <div
            key={i}
            className="tarjeta-clima"
            style={{ backgroundImage: `url(${getImagen(dia.max)})` }}
          >
            <div className="nombre-dia">{dia.dia}</div>
            <div className="temperatura">{dia.min}° / <strong>{dia.max}°</strong></div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default weather;
