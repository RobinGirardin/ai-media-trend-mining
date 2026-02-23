import numpy as np
import pytest

from lib import parse_string_into_list


def test_parsing():
    """Test the parsing of `tags` and `content`."""

    trial = "['The Digit humanoid could work in distribution, retail and 'e-commerce', manufacturing, and third-party logistics. | Source: Agility Robotics', 'Agility Robotics Inc. this week announced a partnership with Ricoh USA Inc., a global service delivery organization. The company said Ricoh will help it expand its customer-support capabilities throughout North America, better preparing it for larger deployments of its bipedal mobile manipulation robot, Digit.']"

    parsed_string = parse_string_into_list(trial)

    hint = f"The parsed string should have length 2, not '{len(parsed_string)}'"
    assert len(parsed_string) == 2, hint

    correct_parsing = [
        "The Digit humanoid could work in distribution, retail and 'e-commerce', manufacturing, and third-party logistics. | Source: Agility Robotics",
        (
            "Agility Robotics Inc. this week announced a partnership with Ricoh USA Inc., a global service delivery organization. "
            "The company said Ricoh will help it expand its customer-support capabilities throughout North America, "
            "better preparing it for larger deployments of its bipedal mobile manipulation robot, Digit."
        )
    ]
    hint = f"The correct parsed string should be instead: \n '{correct_parsing}'"
    assert parsed_string == correct_parsing
