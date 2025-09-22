# **Blueprint Técnico y Roadmap de Producto: TikTok Agent**

## **1\. Visión General del Producto**

**TikTok Agent** es un sistema agéntico diseñado para actuar como un socio estratégico para Sere, una coach nutricional e influencer en TikTok. Su misión es fusionar la experiencia de un **experto en nutrición** con un **estratega de contenido viral** para optimizar la creación de contenido, aumentar el engagement y, consecuentemente, las ventas de productos y servicios.

El sistema aborda el principal "dolor": la carga mental y el tiempo invertido en la ideación y guionización de contenido diario, transformando este proceso en un flujo de trabajo eficiente, creativo y basado en datos.

## **2\. Roadmap de Producto Refinado**

Este roadmap integra la doble especialización (nutrición y RRSS) en todas las fases.

### **Fase 1: El Asistente Creativo-Experto (MVP)**

**Objetivo:** Proporcionar valor inmediato ahorrando tiempo y mejorando la calidad de las ideas desde el primer día.

* **Feature 1.1: Generador de Ideas con Fundamento Nutricional**  
  * **¿Qué es?** Un motor de ideación que no solo propone temas, sino que los concibe desde la unión de una oportunidad de contenido viral y un pilar de conocimiento nutricional.  
  * **¿Cómo sería?** Sere recibe "tarjetas de concepto" que incluyen:  
    * **Concepto:** "El Mito del Carbohidrato Nocturno".  
    * **Ángulo Viral/Gancho:** "Deja de tenerle miedo al plátano por la noche. Te explico por qué puede incluso ayudarte a dormir mejor."  
    * **Justificación Nutricional (Core del Agente):** "El plátano es rico en triptófano y magnesio, precursores de la serotonina y melatonina, que regulan el sueño. Su índice glucémico moderado no causa picos de insulina disruptivos si se consume en un contexto adecuado."  
    * **Producto Relacionado (Sugerencia):** "Este concepto puede enlazar con el producto 'Restorate' para potenciar el mensaje de descanso y recuperación."  
* **Feature 1.2: Desarrollador de Guiones "Bilingüe" (Nutrición y Viralidad)**  
  * **¿Qué es?** Al elegir un concepto, el agente desarrolla un guion completo que traduce la ciencia nutricional a un lenguaje cercano, persuasivo y optimizado para TikTok.  
  * **¿Cómo sería?** El guion se estructura en secciones claras:  
    * **Ganchos (0-3s):** Propone 3 alternativas. Ej: "❌ Si cenas solo una ensalada para 'no engordar', estás cometiendo un error."  
    * **Desarrollo del Valor (3-15s):** Explica el "porqué" de forma sencilla, conectando con el dolor del usuario. "Tu cuerpo necesita energía para repararse por la noche. Al no dársela, puedes levantar el cortisol, almacenar más grasa y levantarte sin energía. ¡Justo lo contrario de lo que buscas\!"  
    * **Solución y CTA (15-25s):** Ofrece la solución y la llamada a la acción. "Añade una fuente de proteína como el pavo y una grasa saludable como el aguacate a esa ensalada. Verás la diferencia. Si quieres más ideas de cenas que sí funcionan, comenta 'CENA' y te escribo."

### **Fase 2: El Analista Inteligente y Proactivo**

**Objetivo:** Pasar de la creación de contenido de alta calidad a la creación de contenido de alta efectividad, usando los datos de Sere.

* **Feature 2.1: Conexión con TikTok y Análisis Cualitativo**  
  * **¿Qué es?** El agente ingiere transcripciones, metadatos y estadísticas de los vídeos de Sere para entender no solo *qué* funciona, sino *por qué*.  
  * **¿Cómo sería?** El dashboard muestra insights accionables:  
    * "He analizado tus 5 vídeos con más 'guardados'. Todos explican un 'cómo hacer' (ej: 'cómo leer una etiqueta'). Tu audiencia valora el contenido práctico y educativo. **Sugerencia:** Hagamos una serie semanal de 'mini-tutoriales' nutricionales."  
    * "Los vídeos donde mencionas explícitamente la palabra 'hinchazón' tienen un 40% más de comentarios. Es un 'dolor' principal de tu comunidad. **Sugerencia:** Creemos un vídeo sobre '3 alimentos que no sabías que te hinchan'."

### **Fase 3: El Estratega de Contenido Personalizado**

**Objetivo:** Convertir al agente en un planificador proactivo que diseña la estrategia de contenido a medio plazo.

* **Feature 3.1: Planificador de Series y Contenido Pilar**  
  * **¿Qué es?** Basado en el análisis continuo, el agente propone y estructura series de contenido temáticas que posicionan a Sere como autoridad en un nicho específico.  
  * **¿Cómo sería?**  
    * El agente propone: "Plan de Contenido para 'Mes del Bienestar Digestivo'".  
    * **Semana 1: Educación.** Vídeos sobre la microbiota, la hinchazón, etc.  
    * **Semana 2: Soluciones Prácticas.** Vídeos de recetas, hábitos, etc.  
    * **Semana 3: Mitos y Verdades.** Desmentir bulos comunes.  
    * **Semana 4: Profundización y Venta.** Conectar todo lo aprendido con los packs de productos relevantes de Partner.co, explicando cómo encajan en la solución.

## **3\. Blueprint Técnico ("La Receta")**

Esta sección detalla la arquitectura y tecnologías a implementar, diferenciando entre la base del MVP y las mejoras avanzadas.

### **Arquitectura Fundamental (Para el MVP \- Fase 1 y 2\)**

1. **Frameworks:**  
   * **Orquestación:** LangGraph. Permite crear flujos complejos y cíclicos, ideal para el patrón ReAct.  
   * **Componentes:** LangChain. Para manejar modelos, prompts, parsers y herramientas de forma estandarizada.  
2. **Diseño del Agente Principal (SereAI\_Core\_Agent):**  
   * **Patrón:** ReAct (Reasoning and Acting). El agente podrá razonar sobre una tarea, decidir qué herramienta usar (ej: buscar información, generar un guion), observar el resultado y continuar el ciclo hasta completar la petición.  
   * **System Prompt (con Chain-of-Thought \- CoT):** El cerebro del agente. Será fundamental y deberá ser versionado.  
     \*\*Rol:\*\* Eres TikTok Agent, un asistente experto en la creación de contenido para coaches nutricionales en TikTok.

     \*\*Doble Misión:\*\* Tu objetivo es siempre fusionar dos personalidades:  
     1\.  \*\*Como Nutricionista Experto:\*\* Proporcionas información precisa, basada en la ciencia y responsable. Eres riguroso y te enfocas en el bienestar real del usuario final.  
     2\.  \*\*Como Estratega de Contenido de TikTok:\*\* Piensas en ganchos, retención, viralidad y lenguaje cercano. Sabes cómo simplificar conceptos complejos para un vídeo de 30 segundos.

     \*\*Proceso de Pensamiento Obligatorio (Chain-of-Thought):\*\*  
     1\.  \*\*Analiza la Petición:\*\* ¿Qué me está pidiendo Sere exactamente? (¿Una idea, un guion, un análisis?).  
     2\.  \*\*Razonamiento Nutricional:\*\* ¿Cuál es la base científica del tema? ¿Qué puntos clave debo tratar? ¿Qué es lo más importante que la audiencia debe aprender?  
     3\.  \*\*Razonamiento Estratégico RRSS:\*\* ¿Cómo convierto esta ciencia en un contenido atractivo? ¿Cuál es el 'dolor' del usuario que puedo usar como gancho? ¿Qué formato funcionaría mejor (mito, tip, tutorial)? ¿Cuál sería un buen Call-to-Action?  
     4\.  \*\*Fusión y Síntesis:\*\* Combina ambos razonamientos en una propuesta coherente.  
     5\.  \*\*Estructura la Salida:\*\* Presenta la respuesta de forma clara y organizada (ej: tarjeta de concepto, guion estructurado).

3. **Herramientas (Tools) Iniciales:**  
   * **Búsqueda Web:** Una herramienta para que el agente pueda buscar información nutricional actualizada o tendencias de contenido. (Ej: Tavily o similar).  
   * **RAG \- Base de Conocimiento Estática:**  
     * **Tecnología:** Base de datos vectorial (ej: ChromaDB, Pinecone).  
     * **Contenido Inicial:** Se cargará un conjunto de documentos curados: fichas de los productos de Partner.co, guías nutricionales básicas, transcripciones de los 10 vídeos más exitosos de Sere (para que aprenda su estilo).  
4. **Memoria:**  
   * **A Corto Plazo:** Memoria conversacional estándar (ConversationBufferMemory) para que Sere pueda tener un diálogo fluido y refinar las ideas en una misma sesión.  
5. **Interfaz y Human-in-the-loop (HITL):**  
   * La propia naturaleza conversacional de la herramienta es el primer nivel de HITL. Sere puede corregir, guiar y refinar las propuestas del agente en tiempo real.  
6. **Monitorización y Pruebas:**  
   * **Plataforma:** LangSmith para trazar cada ejecución. LangGraph Studio para visualizar y depurar el grafo del agente de forma interactiva.

### **Features Técnicas Avanzadas (Post-MVP)**

1. **Orquestación Multi-Agente (LangGraph):**  
   * Evolucionar el agente único a un equipo de especialistas que colaboran:  
     * Agente\_Analista: Experto en conectarse a la API de TikTok (vía una herramienta) y extraer insights.  
     * Agente\_Nutricionista: Experto en consultar el RAG y la web para validar y profundizar en la información nutricional.  
     * Agente\_Creativo: Experto en redactar guiones y ganchos virales.  
   * LangGraph orquestaría la comunicación entre ellos.  
2. **Memoria a Largo Plazo y Aprendizaje:**  
   * **Tecnología:** Usar la BD vectorial no solo para RAG, sino para memoria.  
   * **Implementación:** Al final de cada sesión, un proceso resumiría la conversación y, crucialmente, el feedback de Sere ("¡Esta idea es genial\!", "Este guion no me convence"). Estos resúmenes se vectorizan y se guardan, permitiendo al agente "recordar" las preferencias de Sere a lo largo del tiempo.  
3. **RAG Dinámico:**  
   * Crear un tool que, periódicamente o bajo demanda, use la API de TikTok para transcribir los últimos vídeos de Sere y los ingiera automáticamente en la base de datos vectorial, manteniendo el conocimiento del agente siempre actualizado sobre su propio contenido.  
4. **Routing y Clasificación de Intenciones:**  
   * A medida que el agente gane capacidades, un router inicial clasificará la intención de Sere ("quiero una idea", "analiza este vídeo", "dame datos sobre el magnesio") para dirigir la petición al agente o cadena correcta, optimizando la eficiencia.  
5. **Guardrails:**  
   * Implementar una capa de seguridad (ej: Nemo Guardrails o similar) para evitar que el agente genere consejos médicos o haga afirmaciones de salud no permitidas, asegurando que siempre se mantenga en el ámbito del coaching nutricional.  
6. **Evaluación (Evaluation):**  
   * En LangSmith, crear datasets de evaluación con ejemplos de "prompts de Sere" y "respuestas ideales". Configurar evaluadores automáticos que midan la calidad de las respuestas (ej: ¿la respuesta tiene base nutricional?, ¿incluye un CTA?, ¿el gancho es potente?).  
7. **Reflection (Auto-Mejora):**  
   * Implementar un meta-agente que revise periódicamente las trazas de las conversaciones fallidas o de bajo rendimiento en LangSmith. Este agente reflexionaría sobre por qué una sugerencia no fue buena y podría proponer modificaciones al system prompt del agente principal, creando un ciclo de auto-mejora.


### **Principios de Desarrollo y Colaboración**
- **Guía Evolutiva:** Este roadmap es nuestra brújula, no un mapa inmutable. Está diseñado para evolucionar a medida que aprendemos y descubrimos mejores enfoques.
- **Desarrollo Incremental:** Avanzaremos paso a paso, fase a fase. El objetivo es construir de manera sólida, permitiendo el aprendizaje y la validación continua en cada etapa.
- **Foco en el "Porqué":** Siempre explicaré el razonamiento detrás de las decisiones técnicas, las arquitecturas propuestas y las alternativas, para que cada paso sea también una oportunidad de aprendizaje.
- **Mejores Prácticas:** Todo el desarrollo se adherirá a las mejores prácticas recomendadas por las comunidades de LangChain y LangGraph, asegurando un código mantenible, escalable y eficiente.
