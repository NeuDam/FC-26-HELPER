# FC 26 HELPER

**FC 26 Helper** es un script en Python diseñado para ayudar a solucionar el problema de rendimiento en _FC 26_, como bajos FPS, stuttering y uso constante de la GPU al 99 %, incluso en equipos con buenas especificaciones.

## ¿Qué hace este script?

El script elimina la **caché de shaders** del juego.  
En algunos casos, FC 26 mantiene shaders corruptos u obsoletos que generan problemas de rendimiento persistentes.

Al borrar estos archivos, se fuerza al juego a **reconstruir los shaders desde cero**, lo que suele mejorar la estabilidad y el rendimiento.## Uso inicial (importante)

Si es la primera vez que usas el script y estás experimentando problemas de rendimiento, debes ejecutar:

    python restore.py

Este script:

- Elimina la caché de shaders de FC 26
- Obliga al juego a reconstruirlos en el próximo inicio

---

## Requisitos antes de ejecutar el script

Antes de ejecutar `restore.py`, asegúrate de que todas estas aplicaciones estén completamente cerradas:

- FC 26
- EA App / EA Play
- La tienda desde la que ejecutas el juego:
  - Steam
  - Epic Games Store

Si alguna de estas aplicaciones está abierta, el script puede no funcionar correctamente.

---

## Notas importantes

- La primera vez que abras FC 26 después de ejecutar el script, el juego puede tardar más en cargar o presentar pequeños tirones iniciales. Esto es normal mientras se reconstruyen los shaders.
- No es necesario ejecutar el script cada vez que juegas; solo cuando reaparezcan los problemas de rendimiento constantemente.

---

## Requisitos

- Python 3.x
- Windows

---

## Advertencia

Este script no modifica archivos del juego ni proporciona ventajas competitivas.  
Únicamente elimina archivos temporales generados por el propio juego.

## Authors

- [@Alex V](https://www.github.com/neudam)
