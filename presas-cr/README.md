# PRESAS CR

Arcade de tráfico costarricense visto desde arriba. Estás atrapado en una presa: avanzá, esquivá motos, pasá carros por un pelo para subir el combo y sobreviví lo más que podás.

## Cómo jugar

Abrí `index.html` en cualquier navegador moderno. No necesita servidor ni instalar nada; es HTML + CSS + JavaScript (Canvas 2D y WebAudio), sin dependencias.

| Acción | Teclado | Táctil |
|---|---|---|
| Cambiar de carril | ← → / A D | botones ◀ ▶, deslizar o tocar mitad izq/der |
| Meterle | ↑ / W | ▲ (mantener) |
| Frenar | ↓ / S | ▼ (mantener) |
| Pausa | P / Esc | botón II |
| Sonido | M | — |
| Música | N | botón en la pausa |

## Música

Composición original generada en vivo con WebAudio (no hay archivos de audio, suma unos 5 KB). Está inspirada en el punto guanacasteco: marimba en 6/8 alternando 3+3 y 2+2+2 (sesquiáltera) sobre I–IV–V7 en sol mayor, con una base de beat que se va armando por fase: marimba y bajo, luego maraca y acordes, después bombo y palmas, hi-hat, y en el Infierno de Presa más rápido y con el bajo saltando de octava.

## Puntuación

- Puntos por distancia × multiplicador.
- **Pasar vehículos** y **casi-choques** (pasar a menos de 15 px) suben el combo; cada 8 de combo sube el multiplicador (hasta x10).
- El combo se pierde si pasan 3,5 s sin acción, si caés en un hueco o si le estorbás a la ambulancia.
- Poderes: **₡** monedas, **cafecito** (cámara lenta 5 s), **Pura Vida** (escudo de un golpe).

## Fases (por distancia)

1. **Todavía se puede** (0 m): pocos carros, alguna moto, buses ocasionales.
2. **Ya empezó la vara** (300 m): taxis, camiones, más cambios de carril y frenazos, motos filtradoras y zigzag.
3. **San José** (700 m): muchas más motos; aparecen la rápida y la oportunista.
4. **Mae...** (1150 m): caos, motos kamikaze, eventos más seguidos.
5. **Infierno de Presa** (1650 m): sigue subiendo la densidad.

La velocidad base sube muy poco (245 → 278). Lo que crece es la cantidad y la complejidad del tráfico. Una regla de justicia impide generar obstáculos o cambios de carril que tapen los tres carriles a la vez, y lo que viene por detrás se anuncia con una flecha y nunca te choca por detrás.

## Motos (color del casco)

- ⚪ **Normal**: mantiene su trayectoria.
- 🟡 **Filtradora**: va por la línea entre carriles y se cambia de rendija.
- 🟣 **Zigzag**: cambia de posición todo el tiempo.
- 🔵 **Rápida**: aparece por detrás a toda velocidad y te esquiva.
- 🟠 **Oportunista**: cuando cambiás de carril, se mete en el carril a donde ibas (muestra "!").
- 🔴 **Kamikaze**: arrancones, frenazos y cruces bruscos; parpadea y marca la trayectoria antes de hacerlo.

## Vehículos

Carro (predecible), SUV, taxi rojo (cambia de carril de repente), bus (largo y lento, se detiene en "paradas"), camión (puede ir montado entre dos carriles), carreta con bueyes (lentísima), tuneado (viene por detrás y pita), ambulancia.

## Eventos aleatorios

Huecos (frenan y quitan el combo), zaguate cruzando, "¡Milagro! se abrió la presa" (menos tráfico y monedas), aguacero (el carro patina), ambulancia, trabajos del MOPT (carril cerrado con conos), vendedor de mamones entre carriles, enjambre de motos, choque adelante (con mirones que frenan), frenazo general y hora pico de buses.

## Pruebas

`index.html?m=1200` arranca la partida con 1200 m recorridos para probar fases avanzadas. `window.__presas` expone ganchos de depuración (`step`, `event(id)`, etc.).

## Compartir

- **En línea (GitHub Pages):** https://estebanperez4.github.io/Proyectos/presas-cr/ (cuando Pages esté activado en la rama `main`).
- **Un solo archivo:** `presas-cr-un-archivo.html` trae todo el juego adentro (unos 100 KB). Se puede mandar por correo o WhatsApp y abrir en cualquier navegador sin internet.
