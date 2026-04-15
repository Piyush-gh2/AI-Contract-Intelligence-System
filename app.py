import streamlit as st
from src.agents import analyze_contract
from src.rag import load_knowledge, build_index, retrieve

st.title("⚖️ AI Contract Intelligence System")

if st.button("Analyze Contract"):
    
    results = analyze_contract()
    
    st.subheader("📄 Contract Analysis")
    
    for line, risk in results:
        st.write(f"{line} → {risk}")
    
    # RAG Insights
    docs = load_knowledge()
    index = build_index(docs)
    
    st.subheader("🔎 Legal Insights")
    
    insights = retrieve("contract risk", docs, index)
    
    for i in insights:
        st.write(i)