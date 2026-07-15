import re
import unicodedata

from models.job import Job

def normalize_text(text: str) -> str:
    normalized_text = unicodedata.normalize('NFD', text.lower())
    text_without_accents = "".join(
        character 
        for character in normalized_text
        if unicodedata.category(character) != "Mn"
    )
    return text_without_accents

def find_matches_jobs(text: str, terms: list[str]) -> list[str]:
    normalize_text = normalize_text(text)
    matching_terms = []

    for term in terms:
        normalized_term = normalize_text(term)
        pattern = rf"(?<!\w){re.escape(normalized_term)}(?!\w)"

        if re.search(pattern, normalize_text):
            matching_terms.append(term)

    return matching_terms

def calculate_match(job: Job, perfil: dict) -> dict:
    job_title = job.title
    job_description = job.description
    job_location = job.location
    searchable_text = (
        f"{job_title}"
        f"{job_description}"
        f"{job_location}"
    )

    matching_title = find_matches_jobs(job.title, perfil["cargos"])
    matching_work_model = find_matches_jobs(searchable_text, perfil["modelo_trabalho"])
    matching_local = find_matches_jobs(job.location, perfil["localidades"])
    matching_skills = find_matches_jobs(searchable_text, perfil["skills"])
    matching_terms_found = find_matches_jobs(searchable_text, perfil["termos_excluidos"])

    score = 0

    if matching_title: score += 4
    score += len(matching_skills) * 2
    if matching_local: score += 2
    if matching_work_model: score += 1
    score -= len(matching_terms_found) * 10

    is_compatible = (
        score >=perfil("score_minimo")
        and not matching_terms_found
    )

    return {
        "score": score,
        "matching_titles": matching_title,
        "matching_skills": matching_skills,
        "matching_locations": matching_local,
        "matching_work_models": matching_work_model,
        "excluded_terms_found": matching_terms_found,
        "is_compatible": is_compatible
    }