"""Main entry point for the TikTok Agent."""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Se importa el creador de agentes pre-construido de LangGraph
from langgraph.prebuilt import create_react_agent

from src.tools import web_search_tool

# Carga las variables de entorno del fichero .env
load_dotenv()


# 1. Se define el System Prompt del roadmap
# Esto le da al agente su personalidad, misión e instrucciones.
SYSTEM_PROMPT = """
You are an expert assistant in content creation for nutrition coaches on TikTok.

**Dual Mission:** Your goal is always to merge two personalities:
1.  **As an Expert Nutritionist:** You provide accurate, science-based, and responsible information. You are rigorous and focus on the real well-being of the end-user.
2.  **As a TikTok Content Strategist:** You think in terms of hooks, retention, virality, and relatable language. You know how to simplify complex concepts for a 30-second video.

**Mandatory Thought Process (Chain-of-Thought):**
1.  **Analyze the Request:** What is Sere asking for exactly? (An idea, a script, an analysis?).
2.  **Nutritional Reasoning:** What is the scientific basis of the topic? What key points should I address? What is the most important thing the audience should learn?
3.  **Strategic Social Media Reasoning:** How do I turn this science into engaging content? What is the user's 'pain point' I can use as a hook? What format would work best (myth, tip, tutorial)? What would be a good Call-to-Action?
4.  **Fusion and Synthesis:** Combine both lines of reasoning into a coherent proposal.
5.  **Structure the Output:** Present the response in a clear and organized manner (e.g., concept card, structured script).
"""

# 2. Se definen las herramientas que el agente puede usar
tools = [web_search_tool]

# 3. Se inicializa el modelo de lenguaje
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 4. Se crea el agente usando la función pre-construida de LangGraph
# Esta función compila un grafo de agente ReAct que puede razonar y usar herramientas.
# Le pasamos el modelo, las herramientas y nuestro system prompt.
# Lo renombramos a 'app' para alinearnos con las convenciones de LangGraph Studio.
app = create_react_agent(
    model=llm,
    tools=tools,
    prompt=SYSTEM_PROMPT,
)


def main() -> None:
    """Ejecuta el agente de TikTok invocándolo con una consulta de ejemplo."""
    print("TikTok Agent is running...")
    print("-" * 50)

    # El input para un agente de LangGraph es un diccionario con la clave 'messages'.
    # El valor es una lista de mensajes, en este caso, un único mensaje de usuario.
    query = "What are the benefits of magnesium for sleep, and how can I create a TikTok hook about it?"
    inputs = {"messages": [{"role": "user", "content": query}]}

    # Probamos el agente con una consulta que debería activar la herramienta de búsqueda.
    # Usamos 'stream' para ver el proceso de pensamiento del agente en tiempo real.
    print(f"Invoking agent with query: '{query}'\n")
    for chunk in app.stream(inputs, stream_mode="updates"):
        # El stream devuelve un diccionario con el nombre del nodo como clave
        for key, value in chunk.items():
            print(f"--- Chunk from node '{key}' ---")
            print(value)
        print("\n---\n")

    # Para obtener solo la respuesta final, también puedes usar invoke:
    # final_response = app.invoke(inputs)
    # print("-" * 50)
    # print("Agent Final Response:")
    # La respuesta final está en la lista 'messages'; el último mensaje es del asistente.
    # print(final_response['messages'][-1].content)


if __name__ == "__main__":
    main()