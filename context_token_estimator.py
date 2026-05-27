{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "18b9b935-f7f4-4d93-b923-5bfd8f921b1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total tokens: 16308\n",
      "Usage: 199.07% of 8192 token limit\n",
      "WARNING: Context usage exceeds 80% of the model limit!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "16308"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import tiktoken\n",
    "\n",
    "def estimate_context_usage(messages_list, limit=8192):\n",
    "    enc = tiktoken.get_encoding(\"cl100k_base\")\n",
    "    \n",
    "    total_tokens = 0\n",
    "    \n",
    "    for msg in messages_list:\n",
    "       \n",
    "        text = msg[\"role\"] + \": \" + msg[\"content\"]\n",
    "        tokens = enc.encode(text)\n",
    "        total_tokens += len(tokens)\n",
    "    \n",
    "    usage_percent = (total_tokens / limit) * 100\n",
    "    \n",
    "    print(f\"Total tokens: {total_tokens}\")\n",
    "    print(f\"Usage: {usage_percent:.2f}% of {limit} token limit\")\n",
    "    \n",
    "    if usage_percent > 80:\n",
    "        print(\"WARNING: Context usage exceeds 80% of the model limit!\")\n",
    "    \n",
    "    return total_tokens\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "messages = [\n",
    "    {\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}\n",
    "]\n",
    "\n",
    "\n",
    "for i in range(50):\n",
    "    messages.append({\n",
    "        \"role\": \"user\",\n",
    "        \"content\": \"Explain recursion in Python with examples. \" * 20\n",
    "    })\n",
    "    messages.append({\n",
    "        \"role\": \"assistant\",\n",
    "        \"content\": \"Recursion is when a function calls itself. \" * 20\n",
    "    })\n",
    "\n",
    "\n",
    "estimate_context_usage(messages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6b6be20-f6d8-4497-a77c-888d4834a82b",
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
