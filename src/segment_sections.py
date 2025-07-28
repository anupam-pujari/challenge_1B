import re
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

def segment_into_sections(pages_data):
    sections = []
    for page in pages_data:
        lines = page["text"].split('\n')
        current_section = {"title": None, "content": "", "page": page["page_num"]}
        for line in lines:
            if re.match(r'^[0-9. ]{0,5}[A-Z].{3,}', line):  # crude heading detector
                if current_section["title"]:
                    sections.append(current_section)
                current_section = {
                    "title": line.strip(),
                    "content": "",
                    "page": page["page_num"]
                }
            else:
                current_section["content"] += line.strip() + " "
        if current_section["title"]:
            sections.append(current_section)
    return sections
