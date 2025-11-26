# CharBPE
Character level Byte-Pair Encoding. 
---

# **BPETokenizer**

A minimal **Byte-Pair Encoding (BPE)** tokenizer implemented in Python.



# **Example**

```python
import BPETokenizer

tokenizer = BPETokenizer(vocab_size=400)

tokenizer.train("hello world hello world")

ids = tokenizer.tokenize("hello world")
print("Tokens:", ids)

decoded = tokenizer.decode(ids)
print("Decoded:", decoded)

```

---

# **Stuff to do**

* Have to get EOS done
* Word boundaries to be taken care of 
* Vocabulary values are raw strings right now


---

