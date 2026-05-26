{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d24ee569-34f5-4325-bf3a-1b4a2f66a32e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "English sentence\n",
      "Input: This is a simple English sentence.\n",
      "Tokens: ['This', ' is', ' a', ' simple', ' English', ' sentence', '.']\n",
      "Token count: 7\n",
      "\n",
      "Python function\n",
      "Input: def add(a, b): return a + b\n",
      "Tokens: ['def', ' add', '(a', ',', ' b', '):', ' return', ' a', ' +', ' b']\n",
      "Token count: 10\n",
      "\n",
      "Native language\n",
      "Input: എനിക്ക് പൈതൺ പഠിക്കാൻ ഇഷ്ടമാണ്\n",
      "Tokens: ['�', '�', '�', '�', '�', '�', '�', '�', '്�', '�', '്', ' �', '�', '�', '�', '�', '�', '�', '�', '�', ' �', '�', '�', '�', '�', '�', '�', '�', '�', '്�', '�', '�', '�', '�', '�', ' �', '�', '�', '�', '�', '്�', '�', '�', '�', '�', '�', '�', '�', '്']\n",
      "Token count: 49\n",
      "\n",
      "Number\n",
      "Input: 1234567\n",
      "Tokens: ['123', '456', '7']\n",
      "Token count: 3\n",
      "\n",
      "Email\n",
      "Input: example123@gmail.com\n",
      "Tokens: ['example', '123', '@gmail', '.com']\n",
      "Token count: 4\n",
      "\n",
      "Math notation\n",
      "Input: f(x) = x^2 + 2x + 1\n",
      "Tokens: ['f', '(x', ')', ' =', ' x', '^', '2', ' +', ' ', '2', 'x', ' +', ' ', '1']\n",
      "Token count: 14\n",
      "\n",
      "Explanation:\n",
      "I was surprised that numbers like 1234567 are often split into multiple tokens instead of one.\n",
      "Email addresses are also broken into smaller meaningful parts like words, symbols, and domains.\n",
      "Non-English text is tokenized differently, often into smaller pieces because of Unicode encoding.\n"
     ]
    }
   ],
   "source": [
    "import subprocess\n",
    "import sys\n",
    "\n",
    "try:\n",
    "    import tiktoken\n",
    "except ImportError:\n",
    "    subprocess.check_call([sys.executable, \"-m\", \"pip\", \"install\", \"tiktoken\"])\n",
    "    import tiktoken\n",
    "\n",
    "enc = tiktoken.get_encoding(\"cl100k_base\")\n",
    "\n",
    "inputs = {\n",
    "    \"English sentence\": \"This is a simple English sentence.\",\n",
    "    \"Python function\": \"def add(a, b): return a + b\",\n",
    "    \"Native language\": \"എനിക്ക് പൈതൺ പഠിക്കാൻ ഇഷ്ടമാണ്\",\n",
    "    \"Number\": \"1234567\",\n",
    "    \"Email\": \"example123@gmail.com\",\n",
    "    \"Math notation\": \"f(x) = x^2 + 2x + 1\"\n",
    "}\n",
    "\n",
    "for name, text in inputs.items():\n",
    "    tokens = enc.encode(text)\n",
    "    token_strings = [enc.decode([t]) for t in tokens]\n",
    "    \n",
    "    print(\"\\n\" + name)\n",
    "    print(\"Input:\", text)\n",
    "    print(\"Tokens:\", token_strings)\n",
    "    print(\"Token count:\", len(tokens))\n",
    "\n",
    "print(\"\\nExplanation:\")\n",
    "print(\"I was surprised that numbers like 1234567 are often split into multiple tokens instead of one.\")\n",
    "print(\"Email addresses are also broken into smaller meaningful parts like words, symbols, and domains.\")\n",
    "print(\"Non-English text is tokenized differently, often into smaller pieces because of Unicode encoding.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a2f141e-806a-4686-b721-266bf5fb6d0e",
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
