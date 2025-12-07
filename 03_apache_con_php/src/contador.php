<?php
// contador.php
$archivo = "/tmp/contador.txt";

if (!file_exists($archivo)) {
    file_put_contents($archivo, 0);
}

$contador = (int) file_get_contents($archivo);
$contador++;
file_put_contents($archivo, $contador);

echo "<h1>👋 Has visitado esta página $contador veces.</h1>";
echo "<p><a href='index.php'>Volver al inicio</a></p>";
?>