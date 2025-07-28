import os
import json
from datetime import datetime
import warnings
from utils import summarize_text

warnings.filterwarnings("ignore", category=FutureWarning)


def generate_json_output(documents, persona, job, ranked_sections):
    metadata = {
        "input_documents": documents,
        "persona": persona,
        "job_to_be_done": job,
        "processing_timestamp": datetime.now().isoformat(),
    }

    extracted_sections = []
    sub_section_analysis = []
    for idx, sec in enumerate(ranked_sections, 1):
        extracted_sections.append(
            {
                "document": sec.get("document", "unknown.pdf"),
                "page_number": sec["page"],
                "section_title": sec["title"],
                "importance_rank": idx,
            }
        )
        refined = summarize_text(sec["content"], top_n=2)
        sub_section_analysis.append(
            {
                "document": sec.get("document", "unknown.pdf"),
                "page_number": sec["page"],
                "refined_text": refined,
            }
        )

    result = {
        "metadata": metadata,
        "extracted_sections": extracted_sections,
        "sub_section_analysis": sub_section_analysis,
    }

    # ✅ Ensure output dir exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Write result.json even if it doesn’t exist
    result_path = os.path.join(output_dir, "result.json")
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print(f"✅ result.json created at {result_path}")
