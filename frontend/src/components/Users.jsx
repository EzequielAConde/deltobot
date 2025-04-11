import React, { useEffect, useState } from 'react';
import { popularCountry } from '../logic/country';
import '../styles/Users.css';

function Users() {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/usuarios')
      .then(res => res.json())
      .then(data => setUsuarios(data.usuarios))
      .catch(err => console.error('Error al obtener usuarios:', err));
  }, []);

  const paisMasBuscado = popularCountry(usuarios);

  return (
    <div className="contenedor">
      <div className="ventana">
        <div className="encabezado">
          <div className="botones">
            <div className="boton boton-verde"></div>
            <div className="boton boton-amarillo"></div>
            <div className="boton boton-rojo"></div>
          </div>
          <div className="titulo-ventana">DELTOBOT</div>
        </div>

        <div className="contenido">
          <p className="subtitulo">Tu asistente virtual</p>

          <div className="secciones">
            <div className="usuarios">
              <h2>Contador de Usuarios</h2>
              <p>Total de usuarios: <strong>{usuarios.length}</strong></p>

              {/* Envoltura responsive */}
              <div className="table-container">
                <table>
                  <thead>
                    <tr>
                      <th>Usuario</th>
                      <th>Contador</th>
                      <th>Países buscados</th>
                    </tr>
                  </thead>
                  <tbody>
                    {usuarios.map((usuario, index) => (
                      <tr key={index}>
                        <td>{usuario.nombre || 'Sin nombre'}</td>
                        <td>{usuario.contador || 0}</td>
                        <td>
                          {Array.isArray(usuario.paises_buscados)
                            ? usuario.paises_buscados.join(', ')
                            : usuario.paises_buscados || 'Ninguno'}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            <div className="pais-mas-buscado">
              <h2>País más buscado</h2>
              <p>El país más buscado es:</p>
              <p className="pais">{paisMasBuscado}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Users;
