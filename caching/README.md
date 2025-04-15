<h1 align="center">Caching</h1>

## 📚 Description

This project explores the concept of **caching systems** and implements several **cache replacement policies** using Python.  
You will build different caching strategies by inheriting from a base class and implementing custom `put` and `get` methods for each policy.

The goal is to understand how different algorithms handle cache eviction and data retrieval under memory constraints.

---

## 🎯 Objectives

- Understand what a **caching system** is and how it works  
- Implement the following **cache replacement policies**:
  - FIFO: First-In, First-Out  
  - LIFO: Last-In, First-Out  
  - LRU: Least Recently Used  
  - MRU: Most Recently Used  
  - LFU: Least Frequently Used  
- Understand the **advantages and limitations** of each policy  
- Write clean, modular, and well-documented Python code  

---

## 📁 Project Structure

Each caching algorithm is implemented in its own Python file.  
All classes inherit from the base class: `BaseCaching`.

```
.
├── base_caching.py        # Base class with shared logic
├── 0-fifo_cache.py        # FIFO implementation
├── 1-lifo_cache.py        # LIFO implementation
├── 2-lru_cache.py         # LRU implementation
├── 3-mru_cache.py         # MRU implementation
├── 4-lfu_cache.py         # LFU implementation
├── main.py (optional)     # For testing your classes
└── README.md              # Project documentation
```

---

## ✅ Requirements

- All scripts must be written in **Python 3.9**
- Files will be interpreted/compiled on **Ubuntu 20.04 LTS**
- Use **pycodestyle** (version 2.5) for code style  
- All files must:
  - End with a **new line**
  - Be **executable**
  - Contain a valid shebang `#!/usr/bin/env python3`
- All modules, classes, and functions must include **full docstrings**
- A `README.md` file is required (✔️ you're reading it!)

---

## 📘 Resources

You may find the following resources helpful:

- [FIFO - First In First Out](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_in_first_out_(FIFO))
- [LIFO - Last In First Out](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_in_first_out_(LIFO))
- [LRU - Least Recently Used](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU))
- [MRU - Most Recently Used](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_recently_used_(MRU))
- [LFU - Least Frequently Used](https://en.wikipedia.org/wiki/Least_frequently_used)

---

## 🚀 Clone the Repository

To get a local copy of the project, run the following commands in your terminal:

```bash
git clone https://github.com/harishammache/holbertonschool-web_back_end.git
cd holbertonschool-web_back_end
```

## 👨‍💻 Author

**Haris** – Full-Stack Web Developer  
GitHub: [@harishammache](https://github.com/harishammache)

---
