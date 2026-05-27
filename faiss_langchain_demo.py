{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "224ee7ef-3f62-4797-bc66-f1717c7749e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: langchain in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (1.3.2)\n",
      "Requirement already satisfied: faiss-cpu in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (1.14.2)\n",
      "Requirement already satisfied: sentence-transformers in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (5.5.1)\n",
      "Requirement already satisfied: langchain-core<2.0.0,>=1.4.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain) (1.4.0)\n",
      "Requirement already satisfied: langgraph<1.3.0,>=1.2.2 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain) (1.2.2)\n",
      "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain) (2.12.4)\n",
      "Requirement already satisfied: jsonpatch<2.0.0,>=1.33.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain-core<2.0.0,>=1.4.0->langchain) (1.33)\n",
      "Requirement already satisfied: langchain-protocol>=0.0.14 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain-core<2.0.0,>=1.4.0->langchain) (0.0.15)\n",
      "Requirement already satisfied: langsmith<1.0.0,>=0.3.45 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain-core<2.0.0,>=1.4.0->langchain) (0.8.5)\n",
      "Requirement already satisfied: packaging>=23.2.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain-core<2.0.0,>=1.4.0->langchain) (25.0)\n",
      "Requirement already satisfied: pyyaml<7.0.0,>=5.3.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain-core<2.0.0,>=1.4.0->langchain) (6.0.3)\n",
      "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain-core<2.0.0,>=1.4.0->langchain) (9.1.2)\n",
      "Requirement already satisfied: typing-extensions<5.0.0,>=4.7.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain-core<2.0.0,>=1.4.0->langchain) (4.15.0)\n",
      "Requirement already satisfied: uuid-utils<1.0,>=0.12.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langchain-core<2.0.0,>=1.4.0->langchain) (0.16.0)\n",
      "Requirement already satisfied: jsonpointer>=1.9 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from jsonpatch<2.0.0,>=1.33.0->langchain-core<2.0.0,>=1.4.0->langchain) (3.0.0)\n",
      "Requirement already satisfied: langgraph-checkpoint<5.0.0,>=4.1.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langgraph<1.3.0,>=1.2.2->langchain) (4.1.1)\n",
      "Requirement already satisfied: langgraph-prebuilt<1.2.0,>=1.1.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langgraph<1.3.0,>=1.2.2->langchain) (1.1.0)\n",
      "Requirement already satisfied: langgraph-sdk<0.4.0,>=0.3.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langgraph<1.3.0,>=1.2.2->langchain) (0.3.15)\n",
      "Requirement already satisfied: xxhash>=3.5.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langgraph<1.3.0,>=1.2.2->langchain) (3.7.0)\n",
      "Requirement already satisfied: ormsgpack>=1.12.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langgraph-checkpoint<5.0.0,>=4.1.0->langgraph<1.3.0,>=1.2.2->langchain) (1.12.2)\n",
      "Requirement already satisfied: httpx>=0.25.2 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langgraph-sdk<0.4.0,>=0.3.0->langgraph<1.3.0,>=1.2.2->langchain) (0.28.1)\n",
      "Requirement already satisfied: orjson>=3.11.5 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langgraph-sdk<0.4.0,>=0.3.0->langgraph<1.3.0,>=1.2.2->langchain) (3.11.9)\n",
      "Requirement already satisfied: requests-toolbelt>=1.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.4.0->langchain) (1.0.0)\n",
      "Requirement already satisfied: requests>=2.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.4.0->langchain) (2.32.5)\n",
      "Requirement already satisfied: zstandard>=0.23.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.4.0->langchain) (0.24.0)\n",
      "Requirement already satisfied: anyio in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph<1.3.0,>=1.2.2->langchain) (4.10.0)\n",
      "Requirement already satisfied: certifi in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph<1.3.0,>=1.2.2->langchain) (2026.4.22)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph<1.3.0,>=1.2.2->langchain) (1.0.9)\n",
      "Requirement already satisfied: idna in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph<1.3.0,>=1.2.2->langchain) (3.11)\n",
      "Requirement already satisfied: h11>=0.16 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph<1.3.0,>=1.2.2->langchain) (0.16.0)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.41.5 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from pydantic<3.0.0,>=2.7.4->langchain) (2.41.5)\n",
      "Requirement already satisfied: typing-inspection>=0.4.2 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.4.2)\n",
      "Requirement already satisfied: numpy>=1.25 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from faiss-cpu) (2.3.5)\n",
      "Requirement already satisfied: transformers<6.0.0,>=4.41.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from sentence-transformers) (5.9.0)\n",
      "Requirement already satisfied: huggingface-hub>=0.23.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from sentence-transformers) (1.16.4)\n",
      "Requirement already satisfied: torch>=1.11.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from sentence-transformers) (2.12.0)\n",
      "Requirement already satisfied: scikit-learn>=0.22.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from sentence-transformers) (1.7.2)\n",
      "Requirement already satisfied: scipy>=1.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from sentence-transformers) (1.16.3)\n",
      "Requirement already satisfied: tqdm>=4.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from sentence-transformers) (4.67.1)\n",
      "Requirement already satisfied: regex>=2025.10.22 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from transformers<6.0.0,>=4.41.0->sentence-transformers) (2026.5.9)\n",
      "Requirement already satisfied: tokenizers<=0.23.0,>=0.22.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from transformers<6.0.0,>=4.41.0->sentence-transformers) (0.22.2)\n",
      "Requirement already satisfied: typer in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from transformers<6.0.0,>=4.41.0->sentence-transformers) (0.20.0)\n",
      "Requirement already satisfied: safetensors>=0.4.3 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from transformers<6.0.0,>=4.41.0->sentence-transformers) (0.7.0)\n",
      "Requirement already satisfied: click>=8.4.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.23.0->sentence-transformers) (8.4.1)\n",
      "Requirement already satisfied: filelock>=3.10.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.23.0->sentence-transformers) (3.20.0)\n",
      "Requirement already satisfied: fsspec>=2023.5.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.23.0->sentence-transformers) (2025.10.0)\n",
      "Requirement already satisfied: hf-xet<2.0.0,>=1.4.3 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from huggingface-hub>=0.23.0->sentence-transformers) (1.5.0)\n",
      "Requirement already satisfied: shellingham>=1.3.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from typer->transformers<6.0.0,>=4.41.0->sentence-transformers) (1.5.4)\n",
      "Requirement already satisfied: rich>=10.11.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from typer->transformers<6.0.0,>=4.41.0->sentence-transformers) (14.2.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from click>=8.4.0->huggingface-hub>=0.23.0->sentence-transformers) (0.4.6)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from requests>=2.0.0->langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.4.0->langchain) (3.4.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from requests>=2.0.0->langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.4.0->langchain) (2.5.0)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from rich>=10.11.0->typer->transformers<6.0.0,>=4.41.0->sentence-transformers) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from rich>=10.11.0->typer->transformers<6.0.0,>=4.41.0->sentence-transformers) (2.19.2)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer->transformers<6.0.0,>=4.41.0->sentence-transformers) (0.1.2)\n",
      "Requirement already satisfied: joblib>=1.2.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from scikit-learn>=0.22.0->sentence-transformers) (1.5.2)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from scikit-learn>=0.22.0->sentence-transformers) (3.5.0)\n",
      "Requirement already satisfied: setuptools<82 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (80.9.0)\n",
      "Requirement already satisfied: sympy>=1.13.3 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (1.14.0)\n",
      "Requirement already satisfied: networkx>=2.5.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (3.5)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from torch>=1.11.0->sentence-transformers) (3.1.6)\n",
      "Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from sympy>=1.13.3->torch>=1.11.0->sentence-transformers) (1.3.0)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from anyio->httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph<1.3.0,>=1.2.2->langchain) (1.3.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from jinja2->torch>=1.11.0->sentence-transformers) (3.0.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install langchain faiss-cpu sentence-transformers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "47674613-03b3-4364-8e58-a61d79a8f3ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\LENOVO\\AppData\\Local\\Temp\\ipykernel_6308\\850162986.py:1: DeprecationWarning: `langchain-community` is being sunset and is no longer actively maintained. See https://github.com/langchain-ai/langchain-community/issues/674 for details and migration guidance toward standalone integration packages.\n",
      "  from langchain_community.vectorstores import FAISS\n"
     ]
    },
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'HuggingFaceEmbeddings' from 'langchain.embeddings' (C:\\Users\\LENOVO\\anaconda3\\Lib\\site-packages\\langchain\\embeddings\\__init__.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mImportError\u001b[39m                               Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mlangchain_community\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mvectorstores\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m FAISS\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mlangchain\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01membeddings\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m HuggingFaceEmbeddings\n\u001b[32m      4\u001b[39m \u001b[38;5;66;03m# Same 10 sentences\u001b[39;00m\n\u001b[32m      5\u001b[39m sentences = [\n\u001b[32m      6\u001b[39m     \u001b[38;5;66;03m# Cricket\u001b[39;00m\n\u001b[32m      7\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mVirat Kohli scored a century in the match\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m   (...)\u001b[39m\u001b[32m     20\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mDebugging code can be challenging\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m     21\u001b[39m ]\n",
      "\u001b[31mImportError\u001b[39m: cannot import name 'HuggingFaceEmbeddings' from 'langchain.embeddings' (C:\\Users\\LENOVO\\anaconda3\\Lib\\site-packages\\langchain\\embeddings\\__init__.py)"
     ]
    }
   ],
   "source": [
    "from langchain_community.vectorstores import FAISS\n",
    "from langchain.embeddings import HuggingFaceEmbeddings\n",
    "\n",
    "# Same 10 sentences\n",
    "sentences = [\n",
    "    # Cricket\n",
    "    \"Virat Kohli scored a century in the match\",\n",
    "    \"The bowler delivered a fast yorker\",\n",
    "    \"India won the cricket match by 5 wickets\",\n",
    "    \"The batsman hit a six over long-on\",\n",
    "\n",
    "    # Cooking\n",
    "    \"I added salt and spices to the curry\",\n",
    "    \"The chef cooked a delicious pasta\",\n",
    "    \"Baking requires precise measurements\",\n",
    "\n",
    "    # Programming\n",
    "    \"Python is a popular programming language\",\n",
    "    \"I wrote a function to sort a list\",\n",
    "    \"Debugging code can be challenging\"\n",
    "]\n",
    "\n",
    "# 1. Load embeddings (same model as before)\n",
    "embedding_model = HuggingFaceEmbeddings(\n",
    "    model_name=\"sentence-transformers/all-MiniLM-L6-v2\"\n",
    ")\n",
    "\n",
    "# 2. Build FAISS index using LangChain\n",
    "vectorstore = FAISS.from_texts(sentences, embedding_model)\n",
    "\n",
    "# 3. Create retriever\n",
    "retriever = vectorstore.as_retriever(search_kwargs={\"k\": 3})\n",
    "\n",
    "# 4. Queries\n",
    "queries = [\n",
    "    \"cricket match performance\",\n",
    "    \"how to cook pasta\",\n",
    "    \"python coding errors\"\n",
    "]\n",
    "\n",
    "# 5. Run queries\n",
    "print(\"🔍 LangChain FAISS Results:\\n\")\n",
    "\n",
    "for q in queries:\n",
    "    docs = retriever.get_relevant_documents(q)\n",
    "\n",
    "    print(f\"Query: {q}\")\n",
    "    for d in docs:\n",
    "        print(f\"  -> {d.page_content}\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5cc07dee-a360-4c24-9f9e-1e0ae4aff0bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "acbcd5354e2b427c880b49c40e88c559",
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
      "Query: cricket match performance\n",
      " -> India won the cricket match by 5 wickets\n",
      " -> Virat Kohli scored a century in the match\n",
      " -> The batsman hit a six over long-on\n",
      "\n",
      "Query: how to cook pasta\n",
      " -> The chef cooked a delicious pasta\n",
      " -> I added salt and spices to the curry\n",
      " -> Baking requires precise measurements\n",
      "\n",
      "Query: python coding errors\n",
      " -> Python is a popular programming language\n",
      " -> Debugging code can be challenging\n",
      " -> I wrote a function to sort a list\n"
     ]
    }
   ],
   "source": [
    "from langchain_community.vectorstores import FAISS\n",
    "from langchain_community.embeddings import HuggingFaceEmbeddings\n",
    "\n",
    "\n",
    "sentences = [\n",
    "    \"Virat Kohli scored a century in the match\",\n",
    "    \"The bowler delivered a fast yorker\",\n",
    "    \"India won the cricket match by 5 wickets\",\n",
    "    \"The batsman hit a six over long-on\",\n",
    "    \"I added salt and spices to the curry\",\n",
    "    \"The chef cooked a delicious pasta\",\n",
    "    \"Baking requires precise measurements\",\n",
    "    \"Python is a popular programming language\",\n",
    "    \"I wrote a function to sort a list\",\n",
    "    \"Debugging code can be challenging\"\n",
    "]\n",
    "\n",
    "l\n",
    "embedding_model = HuggingFaceEmbeddings(\n",
    "    model_name=\"sentence-transformers/all-MiniLM-L6-v2\"\n",
    ")\n",
    "\n",
    "\n",
    "vectorstore = FAISS.from_texts(sentences, embedding_model)\n",
    "\n",
    "\n",
    "retriever = vectorstore.as_retriever(search_kwargs={\"k\": 3})\n",
    "\n",
    "queries = [\n",
    "    \"cricket match performance\",\n",
    "    \"how to cook pasta\",\n",
    "    \"python coding errors\"\n",
    "]\n",
    "\n",
    "for q in queries:\n",
    "    docs = retriever.invoke(q)\n",
    "    print(f\"\\nQuery: {q}\")\n",
    "    for d in docs:\n",
    "        print(\" ->\", d.page_content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f163cbd1-d158-4dbc-af1a-62b14d7acd34",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5d4f1fc-17e7-48a0-b478-ffde98af1153",
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
