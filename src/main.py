import os
import argparse
from extract_pdf import extract_text_from_pdf
from segment_sections import segment_into_sections
from embed_and_rank import rank_sections
from generate_output import generate_json_output
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--persona", type=str, required=True, help="Persona description")
    parser.add_argument("--job", type=str, required=True, help="Job to be done")
    parser.add_argument("--pdf_dir", type=str, default="data", help="Path to input PDFs")
    parser.add_argument("--top_n", type=int, default=5, help="Top N sections to extract")
    args = parser.parse_args()

    documents = [f for f in os.listdir(args.pdf_dir) if f.endswith(".pdf")]
    all_sections = []

    for doc in documents:
        full_path = os.path.join(args.pdf_dir, doc)
        pages = extract_text_from_pdf(full_path)
        sections = segment_into_sections(pages)
        for sec in sections:
            sec["document"] = doc
        all_sections.extend(sections)

    ranked = rank_sections(all_sections, args.persona, args.job, args.top_n)
    generate_json_output(documents, args.persona, args.job, ranked)
    print("✅ Output saved to output/result.json")



if __name__ == "__main__":
    persona = os.getenv("PERSONA", "Default Persona")
    job = os.getenv("JOB", "Default Job")
    data_dir = "data"
    output_path = "output/result.json"

    generate_json_output(persona, job, data_dir, output_path)
