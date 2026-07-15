from models.job import Job

def get_sample_jobs() -> list[Job]:
    return [
        Job (
            title="Estágio em Desenvolvimento de Software",
            company="Tech Solutions",
            location="Remoto",
            description=("Vaga para estudantes com conhecimentos "
                "em Python, SQL, Git e APIs REST."),
            link="https://exemplo.com/vagas/estagio-python",
            source="Site de exemplo"
        ),
        Job(
            title="Desenvolvedor Java Sênior",
            company="Enterprise Systems",
            location="Remoto",
            description=(
                "Procuramos profissional com experiência "
                "em Java, Spring Boot e PostgreSQL."
            ),
            link="https://exemplo.com/vagas/java-senior",
            source="Site de exemplo"
        ),
        Job(
            title="Designer Gráfico",
            company="Creative Studio",
            location="São Paulo",
            description=(
                "Vaga para profissional com experiência "
                "em Photoshop, Illustrator e identidade visual."
            ),
            link="https://exemplo.com/vagas/designer",
            source="Site de exemplo"
        )
    ]