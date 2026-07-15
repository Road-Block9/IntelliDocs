from app.config import Settings


def test_optional_service_credentials_are_not_required() -> None:
    settings = Settings(_env_file=None)

    assert settings.mongo_uri is None
    assert settings.llm_provider is None
    assert settings.llm_api_key is None
    assert settings.database_url == "sqlite:///./ct200.db"


def test_configuration_reads_environment_variables(monkeypatch) -> None:
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./test.db")
    monkeypatch.setenv("MONGO_DATABASE", "test_generations")

    settings = Settings(_env_file=None)

    assert settings.environment == "test"
    assert settings.database_url == "sqlite:///./test.db"
    assert settings.mongo_database == "test_generations"
