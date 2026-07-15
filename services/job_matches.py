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

    normalized_text = normalize_text(text)
    matching_terms = []

    for term in terms:
        normalized_term = normalize_text(term)
        pattern = rf"(?<!\w){re.escape(normalized_term)}(?!\w)"

        if re.search(pattern, normalized_text):
            matching_terms.append(term)

    return matching_terms

def calculate_match(job: Job, perfil: dict) -> dict:
    searchable_text = " ".join([
        job.title, job.description, job.location
        ])

    matching_title = find_matches_jobs(job.title, perfil["cargos"])

    matching_keywords = find_matches_jobs(searchable_text, perfil["palavras_chave"])

    matching_work_model = find_matches_jobs(searchable_text, perfil["modelo_trabalho"])

    matching_local = find_matches_jobs(job.location, perfil["localidades"])

    matching_skills = find_matches_jobs(searchable_text, perfil["skills"])
    
    matching_terms_found = find_matches_jobs(searchable_text, perfil["termos_ excluir"])

    score = 0

    score += len(matching_keywords)

    if matching_title: score += 4

    score += len(matching_skills) * 2

    if matching_local: score += 2

    if matching_work_model: score += 1

    score -= len(matching_terms_found) * 10

    is_compatible = (
        score >=perfil["score_minimo"]
        and not matching_terms_found
    )

    return {
        "score": score,
        "matching_titles": matching_title,
        "matching_keywords": matching_keywords,
        "matching_skills": matching_skills,
        "matching_locations": matching_local,
        "matching_work_models": matching_work_model,
        "excluded_terms_found": matching_terms_found,
        "is_compatible": is_compatible
    }

def filter_compatible_jobs(jobs: list[Job], perfil: dict) -> list[dict]:
    compatible_jobs = []

    for job in jobs:
        match_result = calculate_match(job, perfil)

        if match_result["is_compatible"]:
            match_result["job"] = job
            compatible_jobs.append(match_result)

        compatible_jobs.sort(
            key=lambda result: result["score"], #Função lambda para ordenar por score de cada resultado
            reverse=True #Ordenação do maior ao menor
        )
    return compatible_jobs