{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bdf4917b-9553-49fb-870f-cf1242612526",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python Doubt Chatbot (type 'exit' to stop)\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  exit\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Full Conversation History:\n",
      "\n",
      "SYSTEM: You are a helpful assistant that solves Python programming doubts clearly with examples.\n"
     ]
    }
   ],
   "source": [
    "from groq import Groq\n",
    "\n",
    "\n",
    "client = Groq(api_key=\"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\")\n",
    "\n",
    "\n",
    "messages = [\n",
    "    {\n",
    "        \"role\": \"system\",\n",
    "        \"content\": \"You are a helpful assistant that solves Python programming doubts clearly with examples.\"\n",
    "    }\n",
    "]\n",
    "\n",
    "print(\"Python Doubt Chatbot (type 'exit' to stop)\\n\")\n",
    "\n",
    "turn = 0\n",
    "\n",
    "while True:\n",
    "    user_input = input(\"You: \")\n",
    "    \n",
    "    if user_input.lower() == \"exit\":\n",
    "        break\n",
    "\n",
    "  \n",
    "    messages.append({\"role\": \"user\", \"content\": user_input})\n",
    "\n",
    "    \n",
    "    response = client.chat.completions.create(\n",
    "        model=\"llama-3.1-8b-instant\",\n",
    "        messages=messages\n",
    "    )\n",
    "\n",
    "    reply = response.choices[0].message.content\n",
    "\n",
    "\n",
    "    messages.append({\"role\": \"assistant\", \"content\": reply})\n",
    "\n",
    "    print(\"Bot:\", reply)\n",
    "    \n",
    "    turn += 1\n",
    "\n",
    "   \n",
    "    if turn == 4:\n",
    "        break\n",
    "\n",
    "\n",
    "\n",
    "print(\"\\nFull Conversation History:\\n\")\n",
    "for msg in messages:\n",
    "    print(f\"{msg['role'].upper()}: {msg['content']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8507f11-6c37-4dbe-9faf-b5835ba408b6",
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
