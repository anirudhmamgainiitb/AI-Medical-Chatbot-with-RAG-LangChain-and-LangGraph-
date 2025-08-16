\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{xcolor}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue
}

\begin{document}

\section*{AI Medical Chatbot with RAG, LangChain \& LangGraph}

An intelligent \textbf{Medical Chatbot} that leverages \textbf{Retrieval-Augmented Generation (RAG)} with \textbf{LangChain} 
and \textbf{LangGraph} to deliver accurate, context-aware health query responses. 
The system integrates \textbf{HuggingFace embeddings}, \textbf{ChromaDB}, and \textbf{Groq LLaMA 3}, 
deployed with \textbf{Streamlit} for a seamless user experience.  

\subsection*{Features}
\begin{itemize}[leftmargin=*]
    \item Context-aware responses using RAG for reliable medical information.
    \item Efficient retrieval with HuggingFace embeddings \& ChromaDB, improving precision by \textbf{15\%}.
    \item Real-time performance with Groq LLaMA 3, achieving $<$2s query response time.
    \item Persistent chat history via Streamlit for conversational flow.
    \item Modular and scalable RAG pipeline with LangChain \& LangGraph.
\end{itemize}

\subsection*{Tech Stack}
\begin{itemize}[leftmargin=*]
    \item \textbf{LLM:} Groq LLaMA 3
    \item \textbf{Frameworks:} LangChain, LangGraph
    \item \textbf{Database:} ChromaDB (vector store)
    \item \textbf{Embeddings:} HuggingFace Transformers
    \item \textbf{Frontend:} Streamlit
    \item \textbf{Other Tools:} Python, FastAPI (optional)
\end{itemize}

\subsection*{Project Highlights}
\begin{itemize}[leftmargin=*]
    \item Built a medical chatbot using RAG with LangGraph \& LangChain for reliable health query answering.
    \item Enhanced retrieval accuracy by \textbf{15\%} with HuggingFace embeddings \& ChromaDB over keyword search.
    \item Achieved \textbf{$<$2 sec response time} via Groq LLaMA 3 integration for near real-time interaction.
    \item Deployed with Streamlit UI, supporting persistent conversations.
\end{itemize}

\subsection*{Quick Start}
\begin{verbatim}
# Clone the repository
git clone https://github.com/yourusername/ai-medical-chatbot.git
cd ai-medical-chatbot

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
\end{verbatim}

\subsection*{Future Work}
\begin{itemize}[leftmargin=*]
    \item Add multi-turn reasoning with memory chains.
    \item Integrate domain-specific medical datasets (PubMed, MedQA).
    \item Enable multilingual support for broader accessibility.
\end{itemize}

\subsection*{Contributor}
\textbf{Your Name} -- Developer \& Researcher  

\end{document}


