{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "17e8b970-fb70-48b8-8e68-17ecbb3dc68f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2f24e910b4494239b4e4a453eb583ee4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Loading weights:   0%|          | 0/103 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "==============================\n",
      "Q: What is the main topic of the document?\n",
      "A: The main topic of the document is academic and student-related matters.\n",
      "\n",
      "==============================\n",
      "Q: What are the key points discussed?\n",
      "A: I could not find this in the document.\n",
      "\n",
      "==============================\n",
      "Q: Summarize the document briefly.\n",
      "A: I could not find this in the document.\n",
      "\n",
      "==============================\n",
      "Q: Who is the president of the United States?\n",
      "A: I could not find this in the document.\n",
      "\n",
      "==============================\n",
      "Q: What is the capital of France?\n",
      "A: I could not find this in the document.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "\n",
    "os.environ[\"GROQ_API_KEY\"] = \"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\"\n",
    "\n",
    "\n",
    "from langchain_community.document_loaders import PyPDFLoader\n",
    "from langchain_text_splitters import RecursiveCharacterTextSplitter\n",
    "from langchain_community.vectorstores import FAISS\n",
    "from langchain_huggingface import HuggingFaceEmbeddings\n",
    "from langchain_groq import ChatGroq\n",
    "\n",
    "\n",
    "loader = PyPDFLoader(r\"C:\\Users\\LENOVO\\Downloads\\survey cdc.pdf\")  \n",
    "documents = loader.load()\n",
    "\n",
    "=\n",
    "splitter = RecursiveCharacterTextSplitter(\n",
    "    chunk_size=500,\n",
    "    chunk_overlap=50\n",
    ")\n",
    "docs = splitter.split_documents(documents)\n",
    "\n",
    "\n",
    "embeddings = HuggingFaceEmbeddings(\n",
    "    model_name=\"sentence-transformers/all-MiniLM-L6-v2\"\n",
    ")\n",
    "\n",
    "\n",
    "vectorstore = FAISS.from_documents(docs, embeddings)\n",
    "\n",
    "\n",
    "retriever = vectorstore.as_retriever(search_kwargs={\"k\": 3})\n",
    "\n",
    "\n",
    "llm = ChatGroq(\n",
    "    model=\"llama-3.1-8b-instant\",\n",
    "    temperature=0\n",
    ")\n",
    "\n",
    "\n",
    "questions = [\n",
    "    \n",
    "    \"What is the main topic of the document?\",\n",
    "    \"What are the key points discussed?\",\n",
    "    \"Summarize the document briefly.\",\n",
    "\n",
    "   \n",
    "    \"Who is the president of the United States?\",\n",
    "    \"What is the capital of France?\"\n",
    "]\n",
    "\n",
    "\n",
    "for q in questions:\n",
    "    retrieved_docs = retriever.invoke(q)\n",
    "\n",
    "    context = \"\\n\".join([d.page_content for d in retrieved_docs])\n",
    "\n",
    "    prompt = f\"\"\"\n",
    "You MUST follow these rules strictly:\n",
    "\n",
    "- Use ONLY the given context.\n",
    "- If the answer is not explicitly present, reply ONLY with:\n",
    "  \"I could not find this in the document.\"\n",
    "- Do NOT infer or use outside knowledge.\n",
    "\n",
    "Context:\n",
    "{context}\n",
    "\n",
    "Question: {q}\n",
    "\"\"\"\n",
    "\n",
    "    response = llm.invoke(prompt)\n",
    "\n",
    "    print(\"\\n==============================\")\n",
    "    print(\"Q:\", q)\n",
    "    print(\"A:\", response.content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67e42af6-dc5f-4365-b9ef-ed59b9d9baf8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
