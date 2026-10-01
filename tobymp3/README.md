# 🐶 TOBYMP3

Conversor portable de audio a MP3 con opción de compresión.

**Uso:** descarga `TOBYMP3.html` y ábrelo con doble clic en Chrome, Edge, Firefox o Safari.
No necesita instalación ni internet, y los audios nunca salen de tu equipo.

## Qué hace

- Convierte M4A, AAC, WAV, OGG, OPUS, FLAC, WEBM, MP4 (pista de audio) y MP3 a **MP3**.
- Varios archivos a la vez (arrastrar y soltar o seleccionar).
- **Compresión** con presets (Máxima calidad, Estándar, Comprimido, Notas de voz, Mínimo tamaño)
  o ajuste manual de bitrate (32–320 kbps), canales (estéreo/mono) y frecuencia de muestreo.
- Estimación del tamaño final antes de convertir y % de ahorro al terminar.
- Normalización de volumen opcional, vista previa y descarga individual o de todos.

Los formatos que puede leer dependen del navegador (M4A/AAC funciona en Chrome, Edge, Safari y Firefox).

## Desarrollo

- `src/tobymp3.template.html` — interfaz y lógica.
- `vendor/lame.min.js` — codificador MP3 [lamejs](https://github.com/zhuker/lamejs) (LGPL, basado en [LAME](https://lame.sourceforge.io)).
- `python3 build.py` — genera `TOBYMP3.html` con lamejs incrustado en un solo archivo.
