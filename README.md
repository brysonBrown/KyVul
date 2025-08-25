# KyVul: A Balanced C/C++ Vulnerability Dataset

🚀 **Welcome to KyVul** — the first large-scale, balanced dataset of C/C++ vulnerabilities created by an LLM, designed for training, evaluating, and benchmarking Large Language Models (LLMs), static analyzers, and program analysis tools in software security.

---

## 📌 Overview

KyVul contains **20,000 code samples** (10,000 vulnerable + 10,000 fixed non-vulnerable pairs) all created and fixed by ChatGPT 4.1-nano.
Each vulnerable sample is immediately followed by its **corresponding patched version**, making it easy to train or evaluate models on **vulnerability detection, localization, and repair tasks**.

All samples are stored in **`KyVul.json`**, where each entry provides:

* **`code`** → The code snippet (C/C++), formatted as JSON
* **`category`** → One of 9 vulnerability categories
* **`vulnerable`** → `1` for vulnerable code, `0` for non-vulnerable code

---

## 🛠 Vulnerability Coverage

KyVul spans **9 major vulnerability categories**, mapped to **13 common CWEs**:

* **Buffer Overflows**

  * Stack-based (CWE-121)
  * Heap-based (CWE-122)
* **Use-After-Free** (CWE-416)
* **Integer Overflow** (CWE-190)
* **Race Conditions** (CWE-362)
* **Command Injection** (CWE-78, CWE-20)
* **Out-of-Bounds Access** (CWE-125, CWE-129, CWE-787)
* **Memory Leaks** (CWE-401)
* **Double Free** (CWE-415)

👉 This diversity ensures that KyVul can be applied to both **memory safety** and **software security research** across a wide range of real-world bug classes.

---

## ⚙️ Dataset Creation

KyVul was built using a two-step process:

1. **Code Generation**

   * `vulnDataCreator.py` → generates vulnerable examples.
   * `nvDataCreator.py` → produces patched versions of those samples.

2. **Preprocessing & Cleaning**

   * Removal of comments & JSON formatting errors.
   * Removal of stray `global` keywords sometimes introduced by LLMs.
   * Replacement of trivially unsafe calls (`scanf → fgets`, `sprintf → snprintf`, `strcpy → strncpy`) to avoid low-value trivial vulnerabilities.

---

## 📂 Repository Structure

```
KyVul/
│── KyVul.json            # Full dataset (20K entries)
│
├── README/               # Documentation
│   └── CODE_CREATION_README
│   └── CLEAN_README
│
├── Code Creation/        # vulnDataCreator.py + nvDataCreator.py
│
├── Code Cleaners/        # Preprocessing utilities
```

---

## 🎯 Why KyVul?

🔹 **Balanced** → Every vulnerable snippet has a 1:1 paired fixed version.
🔹 **Diverse** → Covers 9 vulnerability categories across 13 CWEs.
🔹 **Cleaned** → Preprocessed for consistency, correctness, and reduced noise.
🔹 **LLM-Ready** → JSON-structured data, easy to integrate into model training.
🔹 **Research-Oriented** → Supports detection, repair, and explainability tasks.

---

## 🚀 Getting Started

1. Download or clone the repository.
2. Load the dataset:

```python
import json  

with open("KyVul.json", "r") as f:  
    dataset = json.load(f)  

print(dataset[0]["code"])  
print(dataset[0]["category"])  
print(dataset[0]["vulnerable"])  
```

3. Explore paired samples (vulnerable → fixed) for your task.

---

## 📊 Results Summary

KyVul was evaluated by fine-tuning **CodeBertGraph** using NVIDIA RTX A6000 GPUs. Two models were trained:

1. **PrimeVul-only model** → trained exclusively on PrimeVul.
2. **Combined model** → trained on PrimeVul + KyVul.

Both were tested on the official PrimeVul validation and test sets.

* **PrimeVul-only model**:

  * AUPRC = **0.098** (variance: 2.3e-5)
  * AUROC = **0.832** (variance: 5e-5)

* **PrimeVul + KyVul model**:

  * AUPRC = **0.145** (variance: 1.33e-4)
  * AUROC = **0.842** (variance: 2.8e-5)

📈 **Impact of Adding KyVul**

* **AUPRC improved by 47.5%** (p < 0.0001, extremely significant).
* **AUROC improved by 1.3%** (p = 0.006, highly significant).

✅ In all 5 trials, the combined model achieved higher AUPRC, and in 4 of 5 trials, it achieved higher AUROC.

These results demonstrate that **KyVul significantly improves vulnerability detection performance** when augmenting an existing, human-curated dataset.

---

## 🔬 Applications

* Training LLMs for **vulnerability detection & repair**
* Benchmarking **static/dynamic analysis tools**
* Building **secure code assistants**
* Academic research in **software security, ML for code, and program repair**

---

## 📢 Citation

If you use **KyVul** in your research, please cite this project (citation details will be added upon paper release).

---

## 🐍 Example

A quick look at a vulnerable → fixed pair:

```json
{
  "code": "char buf[10]; gets(buf);",
  "category": "stack-based buffer overflow",
  "vulnerable": 1
},
{
  "code": "char buf[10]; fgets(buf, sizeof(buf), stdin);",
  "category": "stack-based buffer overflow",
  "vulnerable": 0
}
```



🔥 With **20K high-quality paired samples**, **KyVul** is your go-to dataset for **secure AI coding research**.
