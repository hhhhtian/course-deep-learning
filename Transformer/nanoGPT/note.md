# Workflow
## 1. Tokenizer (分词器)

### 步骤 1: Tokenization (切分)
把文本切分成更小的单位（tokens）。这些单位可以是：
* **词 (Word)**：例如英文的 “I”、“love”、“you”
* **子词 (Subword)**：例如 “play”, “##ing”
* **字符或字节 (Character/Byte)**：例如 GPT 使用的 byte pair encoding (BPE)

### 步骤 2: 查词汇表 (Vocabulary Lookup)
* 每个 token 在词汇表 (vocab) 中有唯一的编号 (token ID)。

### 步骤 3: 输出 Token IDs
* 把 tokens 转换成数字序列。

---

## 2. 组建 Batch (构建批次)
* 将 token IDs 组建成 **Batch Size** (B, 批次大小) 和 **Block Size** (T, 序列长度或上下文窗口大小)。
* *此阶段的输出张量 (tensor) 形状通常为 `(B, T)`*

---

## 3. Embedding Table (词嵌入表)
* 创建一个 Embedding Table（词嵌入表）。
* **标准尺寸 (Standard Size)**: `(vocab_size, embedding_dim)`
    * *注：一开始AK采用 `(vocab_size * vocab_size)` 是最简易的将输入和输出合二为一*
* *此阶段的输出张量 (tensor) 形状通常为 `(B, T, C)`*
---

## 4. Self-Attention (自注意力机制)
* (这是模型的核心计算层Block之一)
---


