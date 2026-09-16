from pathlib import Path
import re


SKILL = Path(__file__).parents[2] / "optional-skills" / "security" / "ndr-monitoring" / "SKILL.md"


def test_ndr_monitoring_skill_authoring_contract():
    text = SKILL.read_text(encoding="utf-8")
    description = re.search(r"^description: (.*)$", text, re.MULTILINE).group(1)
    assert len(description) <= 60
    assert description.endswith(".")
    for section in ("## When to Use", "## Prerequisites", "## How to Run", "## Procedure", "## Pitfalls", "## Verification"):
        assert section in text
    assert any(tool in text for tool in ("`read_file`", "`search_files`", "`terminal`"))
