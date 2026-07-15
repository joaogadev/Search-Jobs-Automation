from models.job import Job
from pathlib import Path
from services.profile_loader import load_profile
from services.job_matches import filter_compatible_jobs, calculate_match, normalize_text, find_matches_jobs
from data.sample_jobs import get_sample_jobs

def main():
    project_directory = Path(__file__).resolve().parent
    profile_path = project_directory / "config" / "perfil.json"

    profile = load_profile(profile_path)
    jobs = get_sample_jobs()

    for job in jobs:
        result2 = calculate_match(job, profile)

        print("\nDEBUG:")
        print(f"Vaga: {job.title}")
        print(f"Pontuação: {result2['score']}")
        print(
            "Termos excluídos encontrados: "
            f"{result2['excluded_terms_found']}"
        )
        print(f"É compatível: {result2['is_compatible']}")

    compatible_jobs = filter_compatible_jobs(jobs, profile)

    print(f"vagas analisadas: ", {len(jobs)})
    print(f"vagas compativeis: ", {len(compatible_jobs)})

    for result in compatible_jobs:
        job = result["job"]
        print("\n------------------------------")
        print(f"Vaga: {job.title}")
        print(f"Empresa: {job.company}")
        print(f"Localização: {job.location}")
        print(f"Pontuação: {result['score']}")
        print(
            "Tecnologias encontradas: "
            f"{', '.join(result['matching_skills'])}"
        )
        print(f"Link: {job.link}")

    test_text = "Desenvolvedor Java Sênior"

    print("\nTESTE DE NORMALIZAÇÃO:")
    print(normalize_text(test_text))

    print("\nTESTE DE TERMO EXCLUÍDO:")
    print(
        find_matches_jobs(
            test_text,
            profile["termos_ excluir"]
        )
    )

if __name__ == "__main__":
    main()