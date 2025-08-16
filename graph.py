# graph.py
from langgraph.graph import StateGraph
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

def make_llm(api_key):
    return ChatGroq(
        groq_api_key=api_key,
        model_name="llama3-8b-8192"
    )

def build_graph():
    def retrieve(state):
        retriever = state["vectorstore"].as_retriever(search_kwargs={"k": 3})
        docs = retriever.get_relevant_documents(state["query"])
        state["docs"] = docs
        return state

    def generate(state):
        llm = state["llm"]
        context = "\n\n".join(doc.page_content for doc in state["docs"])
        prompt = ChatPromptTemplate.from_template(
            "You are a medical assistant. Use the context to answer.\n\nContext:\n{context}\n\nQuestion: {question}"
        )
        answer = llm.invoke(prompt.format(context=context, question=state["query"]))
        state["final"] = answer.content if hasattr(answer, "content") else str(answer)
        return state

    # Create graph
    g = StateGraph(dict)
    g.add_node("retrieve", retrieve)
    g.add_node("generate", generate)
    g.add_edge("retrieve", "generate")
    g.set_entry_point("retrieve")
    g.set_finish_point("generate")

    compiled_graph = g.compile()  # ✅ compile before returning
    return compiled_graph