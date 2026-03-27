import unittest
from pathlib import Path
from unittest.mock import patch

from tool.update_lang_files import build_commands, run_update


class UpdateLangFilesTest(unittest.TestCase):
    def test_build_commands_uses_expected_forge_toolkit_sequence(self):
        repo_root = Path("G:/MinecraftProjects/journeymap-lang")
        commands = build_commands(repo_root)

        self.assertEqual(3, len(commands))
        self.assertEqual(
            [
                "java",
                "-jar",
                str(repo_root / "tool" / "ForgeToolkit-1.1-all.jar"),
                "update",
                "src/main/resources/assets/journeymap/lang/en_us.json",
                "src/main/resources/assets/journeymap/lang/*.json",
            ],
            commands[0],
        )
        self.assertEqual("flatten", commands[1][3])
        self.assertEqual("sort", commands[2][3])

    @patch("tool.update_lang_files.subprocess.run")
    def test_run_update_executes_all_commands_in_repo_root(self, run_mock):
        repo_root = Path("G:/MinecraftProjects/journeymap-lang")

        run_update(repo_root)

        self.assertEqual(3, run_mock.call_count)
        first_call = run_mock.call_args_list[0]
        self.assertEqual(repo_root, first_call.kwargs["cwd"])
        self.assertTrue(first_call.kwargs["check"])


if __name__ == "__main__":
    unittest.main()
