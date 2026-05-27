{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f7153957-818e-4b71-8ff6-e193151cd18c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generated Poem:\n",
      "\n",
      "Softly falls the morning dew,\n",
      "On petals of flowers, both old and new.\n",
      "A gentle breeze whispers through the trees,\n",
      "A soothing melody that Nature brings to ease.\n",
      "\n",
      "--- Metrics ---\n",
      "Total tokens: 34\n",
      "Total time: 1.64 seconds\n",
      "Tokens per second: 20.73\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "from groq import Groq\n",
    "\n",
    "client = Groq(api_key=\"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\")\n",
    "\n",
    "\n",
    "start_time = time.time()\n",
    "\n",
    "tokens = []\n",
    "\n",
    "\n",
    "stream = client.chat.completions.create(\n",
    "    model=\"llama-3.1-8b-instant\",  \n",
    "    messages=[\n",
    "        {\"role\": \"user\", \"content\": \"Write a short 4-line poem about nature.\"}\n",
    "    ],\n",
    "    stream=True\n",
    ")\n",
    "\n",
    "print(\"Generated Poem:\\n\")\n",
    "\n",
    "\n",
    "for chunk in stream:\n",
    "    if chunk.choices[0].delta.content:\n",
    "        token = chunk.choices[0].delta.content\n",
    "        tokens.append(token)\n",
    "\n",
    "        print(token, end=\"\", flush=True)\n",
    "        time.sleep(0.02)\n",
    "\n",
    "\n",
    "end_time = time.time()\n",
    "\n",
    " \n",
    "total_time = end_time - start_time\n",
    "total_tokens = len(tokens)\n",
    "tokens_per_sec = total_tokens / total_time if total_time > 0 else 0\n",
    "\n",
    "print(\"\\n\\n--- Metrics ---\")\n",
    "print(f\"Total tokens: {total_tokens}\")\n",
    "print(f\"Total time: {total_time:.2f} seconds\")\n",
    "print(f\"Tokens per second: {tokens_per_sec:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e7cf089-2b3f-4d49-87d7-1cc3a19c7e56",
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
