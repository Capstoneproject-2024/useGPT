from typing import Dict, Any


def inject_variables(prompt: str, variables: Dict[str, Any]) -> str:
    for key, value in variables.items():
        placeholder = f"{{{{{key}}}}}"
        prompt = prompt.replace(placeholder, str(value))
    return prompt
