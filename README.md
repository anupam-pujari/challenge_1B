# 📄 Persona-Driven Document Intelligence

A system that extracts and ranks the most relevant sections from a set of documents (PDFs) based on a **persona** and their **job-to-be-done**. The goal is to quickly highlight parts of reports or documents that matter most to a specific role — such as an Investment Analyst reviewing annual reports.

---

## 💡 Approach

The system works in the following stages:

1. **PDF Parsing**  
   - Uses `pdfplumber` to extract text blocks (paragraphs, headings) from each page, along with metadata (font size, bold/italic info, position, etc.).

2. **Section Segmentation**  
   - Text blocks are grouped into logical sections using heuristics like font size, position, and heading patterns.

3. **Semantic Embedding & Ranking**  
   - Each section is embedded into a vector space using `sentence-transformers`.
   - The **persona + job description** is also embedded.
   - Relevance is computed via **cosine similarity** between persona embedding and section embeddings.

4. **Output Generation**  
   - The most relevant sections are saved in a structured JSON format (`output/result.json`) with page numbers and section titles.

---

## 🧠 Models & Libraries Used

| Library / Model             | Purpose                                          |
|----------------------------|--------------------------------------------------|
| `pdfplumber`               | Extract text, font info, and layout from PDFs    |
| `sentence-transformers`    | Convert persona/job and sections into embeddings |
| `scikit-learn`             | Calculate cosine similarity for ranking          |
| `nltk`                     | Tokenization and preprocessing support           |

---

## 🐳 How to Build and Run (Docker-Based)

### 🔧 1. Build Docker Image (One-Time)
```bash
docker build -t persona-doc-intel .
```
🚀 Step 2: Run with Your PDFs and Persona Inputs
Make sure to:

Place your PDFs inside the data/ folder.

Output will be saved inside the output/ folder.

Pass the persona and job-to-be-done using environment variables.

▶ On Windows (PowerShell)
```
docker run --rm -v "${PWD}\output:/app/output" `
  -v "${PWD}\data:/app/data" `
  -e PERSONA="Investment Analyst" `
  -e JOB="Analyze revenue trends, R&D investments, and market positioning strategies" `
  persona-doc-intel
```
▶ On Linux/macOS
```
docker run --rm \
  -v "$(pwd)/data:/app/data" \
  -v "$(pwd)/output:/app/output" \
  -e PERSONA="Investment Analyst" \
  -e JOB="Analyze revenue trends, R&D investments, and market positioning strategies" \
  persona-doc-intel
```
📤 Output
The extracted, ranked, and structured sections will be available at:
output/result.json

📁 Directory Structure
```
persona_doc_intelligence/
├── data/                   # Input PDFs
│   └── *.pdf
├── output/                 # Output JSON results
│   └── result.json
├── src/                    # Source Code
│   ├── extract_pdf.py
│   ├── segment_sections.py
│   ├── embed_and_rank.py
│   ├── generate_output.py
│   └── main.py
├── Dockerfile              # Docker environment config
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
✅ Offline & Efficient
🧠 Model size: < 1GB

🛜 Fully offline: No internet access required

⚡ Fast: Processes 3–5 PDF reports in < 60 seconds

🖥️ CPU-only (amd64): Designed for 8-core / 16 GB RAM environments

🔄 Modify Persona Without Rebuilding
You do not need to rebuild the Docker image to change persona or job descriptions — just provide new values using -e PERSONA="..." -e JOB="..." flags during runtime.
