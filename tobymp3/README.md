# 🐶 TOBYMP3

Conversor portable de audio y video a MP3 con opción de compresión.

**Uso:** descarga `TOBYMP3.html` y ábrelo con doble clic en Chrome, Edge, Firefox o Safari.
No necesita instalación ni internet, y tus archivos nunca salen de tu equipo.

## Qué hace

- Convierte audio (M4A, AAC, WAV, OGG, OPUS, FLAC, MP3…) a **MP3**.
- Extrae el sonido de **videos** (MP4, MOV, WEBM, MKV…) y lo guarda como MP3.
- Varios archivos a la vez (arrastrar y soltar o seleccionar).
- **Compresión** con presets (Máxima calidad, Estándar, Comprimido, Notas de voz, Mínimo tamaño)
  o ajuste manual de bitrate (32–320 kbps), canales (estéreo/mono) y frecuencia de muestreo.
- Estimación del tamaño final antes de convertir y % de ahorro al terminar.
- Normalización de volumen opcional, vista previa y descarga individual o de todos.

Los formatos que puede leer dependen del navegador (M4A/AAC funciona en Chrome, Edge, Safari y Firefox; MOV funciona mejor en Safari y Chrome; MKV en Chrome, Edge y Firefox).
Los videos se cargan completos en memoria, así que los muy grandes (varios GB) pueden fallar.

## Desarrollo

- `src/tobymp3.template.html` — interfaz y lógica.
- `vendor/lame.min.js` — codificador MP3 [lamejs](https://github.com/zhuker/lamejs) (LGPL, basado en [LAME](https://lame.sourceforge.io)).
- `python3 build.py` — genera `TOBYMP3.html` con lamejs incrustado en un solo archivo.
