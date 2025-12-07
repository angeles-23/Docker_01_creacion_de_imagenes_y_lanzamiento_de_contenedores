// app.js
const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('<h1>🚀 Hola Docker desde Node.js y Express</h1><p>Tu contenedor está funcionando correctamente.</p>');
});

app.listen(PORT, () => {
  console.log(`Servidor escuchando en http://localhost:${PORT}`);
});