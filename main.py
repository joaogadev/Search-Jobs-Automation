from models.job import Job
from pathlib import Path
from services.profile_loader import load_profile

def main():
    project_directory = Path(__file__).resolve().parent
    profile_path = project_directory / "config" / "perfil.json"

    profile = load_profile(profile_path)

    job = Job(
        title="Software Engineer",
        company="Tech Company",
        location="San Francisco, CA",
        description="Develop and maintain software applications.",
        link="https://www.techcompany.com/jobs/software-engineer",
        source="Tech Company Careers"
    )
    print("Vaga Carregada: ")
    print(job)

    print("\nPerfil Carregado: ")
    print(profile)


    for skill in profile["skills"]:
        print(f"- {skill}")

if __name__ == "__main__":
    main()