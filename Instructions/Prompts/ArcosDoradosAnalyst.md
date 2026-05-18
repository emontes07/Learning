---
layout: none
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Agente Analyst — Arcos Dorados | Learning</title>
<link rel="stylesheet" href="../../Allfiles/demo-style.css">
<style>:root { --hero-from: #B71C1C; --hero-via: #D32F2F; --hero-to: #FFC107; }</style>
</head>
<body>

<div class="back-bar">
  <a href="https://emontes07.github.io/Learning/">← Back to Index</a>
</div>

<button class="sidebar-toggle" onclick="openSidebar()" aria-label="Open menu">☰ Menu</button>

<div class="hero">
  <div class="hero-inner">
    <h1>📊 Agente Analyst — Arcos Dorados</h1>
    <p class="subtitle">Análisis avanzado de datos con el agente Analyst.</p>
    <div class="hero-meta">
      <span>📊 Analyst</span>
      <span>🍔 Arcos Dorados</span>
      <span>💬 Copilot</span>
    </div>
  </div>
</div>

<div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

<div class="layout">

<nav class="sidebar" id="sidebar">
  <a class="sb-home" href="https://emontes07.github.io/Learning/">← Back to Index</a>
  <div class="sb-title">Arcos Dorados</div>

  <a href="#sec-intro" class="section-link">Overview</a>
  <a href="#part1-analyst-construye-un-plan-de-marketing" class="part-link">Analyst: Construye un Plan de Marketing</a>
  <a href="#part2-analyst-segmentación-de-clientes-y-modelado-financiero" class="part-link">Analyst: Segmentación de Clientes y Modelado Financiero</a>
  <a href="#part3-preguntas-de-seguimiento-para-el-analyst-agent" class="part-link">Preguntas de Seguimiento para el Analyst Agent</a>
  <a href="#part4-escenarios-adicionales-para-analyst" class="part-link">Escenarios adicionales para Analyst</a>
</nav>

<div class="main-content">

<div class="section" id="sec-intro">
<div markdown="1">

Esta demostración destaca cómo usar el agente **Analyst**, piensa como un científico de datos experto, capaz de realizar análisis avanzados de datos y ejecutar Python, incluso si no sabes programar.


**Tarea 1: Realizar análisis de resultados de campañas de Marketing**

Para completar estas demostraciones, deberás descargar lo siguientes archivos que contiene todos los archivos y recursos necesarios.

- [Arcos Dorados Datos Campaña Marketing](https://github.com/emontes07/Learning/blob/main/ResourceFiles/ArcosDorados_Marketing_Campaign_Results.xlsx)


> **💡 Tip: :** Antes de realizar la demostración, puedes almacenar los archivos en un sitio de SharePoint de tu entorno de pruebas para facilitar el acceso. Alternativamente, puedes guardar los archivos localmente y hacer referencia a ellos directamente en tus indicaciones usando **/**.



Para acceder a estos agentes:  

- Abre la **aplicación Copilot** desde [m365.cloud.microsoft](https://m365.cloud.microsoft).  
- Usa la **navegación del panel izquierdo** para seleccionar  **Analyst**.  

> **Nota:** Deberás vincular Analyst y Analyst a archivos internos (SharePoint/OneDrive) para obtener información fundamentada en datos confiables.

---

## Escenario
- El departamento de Marketing de Arcos Dorados está planificando la Campaña Familiar de octubre 2025 en Ciudad de México, aprovechando datos históricos de campañas como Cajita Feliz: Aventuras CDMX, McFlurry Edición Pan de Muerto y Monopoly McDonald’s 2025.

- Para esta planeación utilizarán el agente Analyst en Copilot junto con el nuevo archivo de resultados de campañas de marketing que incluye datos por canal, ROI y desempeño de promociones.

El agente ayudará a:
- Investigar tendencias y comportamientos de consumo en familias urbanas y su afinidad con licencias de entretenimiento.
- Proponer alianzas estratégicas para la Cajita Feliz (p. ej., películas de estreno o colecciones coleccionables).
- Recomendar el tipo de juguetes más relevantes para la audiencia infantil de 4–10 años.

¿Por qué usar Analyst?
- Analiza datos de mercado y de campañas pasadas de forma rápida y confiable.
- Detecta oportunidades y brechas en la estrategia actual (por ejemplo, baja inversión en canales digitales o poca activación en eventos locales).
- Visualiza el impacto estimado de cada recomendación en KPIs como ventas, tráfico a restaurantes y awareness.
- Reduce riesgos al evitar decisiones basadas solo en intuición y ayuda a optimizar presupuesto por canal.

---

</div>
</div>

<div class="part-card" id="part1-analyst-construye-un-plan-de-marketing">
  <div class="part-header-bar blue"></div>
  <div class="part-header" onclick="togglePart('body1', this)">
    <h2>Analyst: Construye un Plan de Marketing</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body1">
<div markdown="1">

1. Abre **Analyst** desde la navegación izquierda en la aplicación de Copilot.  

    ![Captura de pantalla mostrando Analyst seleccionado en el menú de M365 Copilot.](../Prompts/Media/Analyst.png)  

2. Ingresa el siguiente prompt:

</div>

<div class="prompt-box">    Genera una tabla que muestre Gasto Total, Impresiones, Clics, Conversiones, CTR,<br>    Tasa de Conversión y ROAS, desglosada primero por Campaña y luego por Canal.<br><br>    Proporciona una narrativa breve que resuma las principales tendencias observadas<br>    (por ejemplo, qué campaña tuvo el ROI más alto en general, qué canal generó la mayor cantidad de impresiones y cuál tuvo mejor desempeño en conversiones).<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

1. Adjunta los archivos de referencia usando `/` (apuntando a SharePoint/OneDrive):  

- [Arcos Dorados Datos Campaña Marketing](https://github.com/emontes07/Learning/blob/main/ResourceFiles/ArcosDorados_Marketing_Campaign_Results.xlsx)

    ![Screenshot showing attach files in Analyst.](../Prompts/Media/ArcosAnalyst10.png)  

2. Haz clic en **Enviar**.  

Analyst hará lo siguiente:  

- Analizará los datos de los archivos internos para identificar patrones, segmentos clave y oportunidades.  
- Generará visualizaciones y modelos simples que respalden decisiones (segmentación, proyecciones)  
- Explicará su metodología y supuestos utilizados, para facilitar la validación.

> **Nota:** Analyst muestra su ruta de razonamiento (“chain of thought”) y puede invocar otros agentes si es necesario.

</div>
  </div>
</div>

<div class="part-card" id="part2-analyst-segmentación-de-clientes-y-modelado-financiero">
  <div class="part-header-bar green"></div>
  <div class="part-header" onclick="togglePart('body2', this)">
    <h2>Analyst: Segmentación de Clientes y Modelado Financiero</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body2">
<div markdown="1">

1. Abre **Analyst** desde la navegación izquierda en la aplicación de Copilot. 

   ![Captura de pantalla mostrando Analyst seleccionado en el menú de M365 Copilot.](../Prompts/Media/Analyst.png)


1. Ingresa el siguiente prompt:

</div>

<div class="prompt-box">    Calcula una matriz de correlación entre: Gasto, Impresiones, Clics, Conversiones, CTR,<br>    Tasa de Conversión y ROAS.<br>    Visualiza las correlaciones más fuertes (positivas y negativas) como mapa de calor  y/o scatterplots.<br><br>    Destaca patrones inesperados (p. ej., canales donde mayor inversión no genera<br>    más conversiones) y sugiere hipótesis y próximos pasos de validación.<br><button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

1. Click **Submit**. 

Analyst hará lo siguiente:  

- Analizará el conjunto de datos.  
- Identificará los segmentos de clientes de mayor valor.  
- Proporcionará visualizaciones que respalden las recomendaciones.

  ![Captura de pantalla resultados del agente Analyst.](../Prompts/Media/ArcosAnalyst02.png)

</div>
  </div>
</div>

<div class="part-card" id="part3-preguntas-de-seguimiento-para-el-analyst-agent">
  <div class="part-header-bar purple"></div>
  <div class="part-header" onclick="togglePart('body3', this)">
    <h2>Preguntas de Seguimiento para el Analyst Agent</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body3">
<div markdown="1">

Después de recibir el primer análisis, puedes hacer estas dos preguntas para profundizar en el escenario:

**Pregunta 1: Análisis de Segmentos de Audiencia**

</div>

<div class="prompt-box">        Segmenta los datos por grupo de edad y género. Para cada segmento, calcula Tasa de Conversión, Costo por Conversión y ROI general.Ordena los segmentos por ROI y recomienda los 5 segmentos con mejor desempeño en los que deberíamos invertir más, y los 5 con peor desempeño para despriorizar. Incluye gráficos de barras que muestren el ROI por segmento.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

**Pregunta 2:Escenario de Reasignación Presupuestaria y Proyección**

</div>

<div class="prompt-box">  Basado en el ROI histórico por canal y segmento demográfico, simula una reasignación presupuestaria:<br>  transfiere el 20% del presupuesto desde los canales de peor desempeño hacia los de mejor desempeño, manteniendo el presupuesto total constante. <br>  Proyecta el cambio estimado en conversiones totales y ROAS bajo esta nueva asignación, y presenta gráficos comparativos de “Antes vs. Después”.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>
  </div>
</div>

<div class="part-card" id="part4-escenarios-adicionales-para-analyst">
  <div class="part-header-bar orange"></div>
  <div class="part-header" onclick="togglePart('body4', this)">
    <h2>Escenarios adicionales para Analyst</h2>
    <span class="toggle-icon open">▾</span>
  </div>
  <div class="part-body" id="body4">
<div markdown="1">

Puedes ejecutar estos mensajes adicionales para variar. Cada uno sigue el mismo patrón: **Mensaje → Adjuntar archivo → Enviar → Revisar resultados.**

- **Escenario: Reasignación de Presupuesto**

</div>

<div class="prompt-box">    Con base en el ROI histórico por canal y segmento demográfico, simula una reasignación de presupuesto: mueve el 20% del gasto de los canales de menor desempeño hacia los     de mayor desempeño, manteniendo el presupuesto total constante. Proyecta el cambio estimado en conversiones totales y en ROAS general e incluye gráficos comparativos de     “Antes vs. Después”.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

- **Análisis de Series Temporales y Pronóstico**

</div>

<div class="prompt-box">    Agrupa inversión, impresiones, clics y conversiones por mes para cada campaña principal.<br>    Traza las tendencias mensuales para identificar estacionalidad (por ejemplo, picos durante promociones navideñas). <br>    Luego construye un modelo de pronóstico simple (por ejemplo, Holt-Winters o ARIMA) para predecir estos indicadores para el Q1 de 2025, <br>    y muestra los datos históricos vs. proyectados, junto con recomendaciones puntuales para la planificación presupuestaria del próximo trimestre.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

- **Rendimiento de campaña**

</div>

<div class="prompt-box">    Analiza y visualiza cómo se desempeñó la campaña de marketing en cada segmento objetivo <br>    y ayúdame a decidir dónde reorientar nuestra próxima campaña.<button class="copy-btn" onclick="copyPrompt(this)">Copy</button></div>

<div markdown="1">

**💡 Tips útiles:** 
- Asegúrate de citar fuentes confiables y recientes (ej. datos 2024-2025 de INEGI, Euromonitor, Kantar).
- Usa los datos internos de Arcos Dorados como punto de partida: ventas pasadas, desempeño de Cajita Feliz, estudios previos, para calibrar recomendaciones.
- Al adjuntar archivos, nómbralos de forma clara para referirse fácilmente en análisis (“Planificación Familiar 2024”, “Resumen Visual Campaña 2024”).
- Pide gráficos comparativos año vs año (2024 vs 2025) para observar tendencias crecientes o decrecientes.
- Itera: luego de ver los resultados iniciales, usa preguntas de seguimiento para ajustar supuestos, explorar escenarios alternativos o validar hipótesis inesperadas.

## Resultados de aprendizaje esperados

- Capacidad para detectar y priorizar tendencias emergentes en el mercado infantil, particularmente en juguetes/licencias, digitales/AR, y comportamientos de consumo de familias.

- Destreza para combinar datos internos (ventas previas, desempeño de campañas) con datos de mercado externos para identificar brechas estratégicas.

- Habilidad para traducir esas tendencias y brechas en recomendaciones prácticas, incluyendo KPIs SMART, estimaciones de impacto, y mapas de canal.

- Experiencia en generación de visualizaciones de datos (gráficos, comparaciones, proyecciones) para respaldar decisiones de campaña.

- Mejora en eficiencia en el proceso de investigación de campañas: desde archivo + prompt → análisis → seguimiento → resultados accionables, ahorrando tiempo y reduciendo riesgos.


Juntos, Researcher y Analyst acortan el camino de la **pregunta al conocimiento**, convirtiendo semanas de trabajo en minutos.

</div>
  </div>
</div>


</div><!-- /main-content -->
</div><!-- /layout -->

<script src="../../Allfiles/demo-script.js"></script>
</body>
</html>
