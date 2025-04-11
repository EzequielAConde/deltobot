
export function popularCountry(usuarios) {
    const paises = usuarios.flatMap(u =>
      Array.isArray(u.paises_buscados) ? u.paises_buscados : []
    ).filter(pais =>
      typeof pais === 'string' &&
      /^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]+$/.test(pais) &&
      pais.length > 2
    ).map(p => p.trim().toLowerCase());
  
    if (paises.length === 0) return 'Ninguno';
  
    const conteo = paises.reduce((acc, pais) => {
      acc[pais] = (acc[pais] || 0) + 1;
      return acc;
    }, {});
  
    const [paisMasBuscado] = Object.entries(conteo).sort((a, b) => b[1] - a[1])[0];
  
    return capitalizar(paisMasBuscado);
  }
  
  function capitalizar(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }
  