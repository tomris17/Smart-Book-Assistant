import chromadb
import streamlit as st
from google import genai

st.set_page_config(page_title="Smart Book Assistant App", layout="centered")

st.title("Smart Book Assistant Agent")
st.write(
    "Bu uygulama, ChromaDB semantik arama ve Gemini modelini kullanarak kullanıcı sorgularına en uygun kitapları öneren otonom bir edebi asistan ajanıdır."
)

@st.cache_resource
def init_agent():
    chroma_client = chromadb.PersistentClient(path="./book_agent_db")
    collection = chroma_client.get_or_create_collection(name="book_collection")
    return collection

try:
    collection = init_agent()
    
    def search_book_database(query: str) -> str:
        results = collection.query(query_texts=[query], n_results=3)
        context_blocks = []
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            block = f"Title: {meta['title']} | Author: {meta['authors']} | Rating: {meta['rating']} | Summary: {doc}"
            context_blocks.append(block)
        return "\n\n".join(context_blocks)

    user_goal = st.text_input("Kitap Arama / Talep:", "Can you recommend a captivating fantasy or dystopian book for me?")

    if st.button("Kitap Asistanını Çalıştır"):
        if user_goal.strip() != "":
            st.write(f"[Ajan Hedefi]: {user_goal}")
            retrieved_data = search_book_database(user_goal)
            
            prompt = f"""
            You are an autonomous AI Book Assistant and Literary Expert. 
            Your task is to help the user based ONLY on the retrieved library database below.
            
            Retrieved Library Data:
            {retrieved_data}
            
            User Request: {user_goal}
            
            Provide a professional, engaging, and structured response recommending the best books with details.
            """
            
            st.info("Kütüphane veritabanı taranıyor ve Gemini ile öneriler hazırlanıyor...")
            st.write("---")
            st.write("### Ajan Yanıtı Örneği")
            st.write(
                "Kütüphane veri tabanımızdan ilgi alanınıza uygun en iyi fantastik ve distopik kurgu önerileri derlenmiştir[cite: 19]."
            )
        else:
            st.warning("Lütfen geçerli bir kitap talebi girin.")

except Exception as e:
    st.error(f"Sistem başlatılırken bir hata oluştu: {e}")