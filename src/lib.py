import re
from typing import List


def parse_string_into_list(
        string: str,
        parsing_pattern: re.Pattern = re.compile(r"(?<=\')[^,].*?(?=\', '|'])", flags=re.MULTILINE)
) -> List[str]:
    """Parse `tags` and `content` features into list of string"""
    parsed_string = parsing_pattern.findall(string)

    return parsed_string
