import subprocess
from pathlib import Path


LANG_GLOB = "src/main/resources/assets/journeymap/lang/*.json"
EN_US_PATH = "src/main/resources/assets/journeymap/lang/en_us.json"


def build_commands(repo_root: Path) -> list[list[str]]:
    jar_path = repo_root / "tool" / "ForgeToolkit-1.1-all.jar"
    jar_arg = str(jar_path)
    return [
        ["java", "-jar", jar_arg, "update", EN_US_PATH, LANG_GLOB],
        ["java", "-jar", jar_arg, "flatten", LANG_GLOB],
        ["java", "-jar", jar_arg, "sort", LANG_GLOB],
    ]


def run_update(repo_root: Path) -> None:
    for command in build_commands(repo_root):
        subprocess.run(command, cwd=repo_root, check=True)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    run_update(repo_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
