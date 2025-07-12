"""Utilities for configurations."""

import os


def get_bool_env(env_var_name: str, default: str = "False") -> bool:
    """Convert a 'string boolean' env variable into a true boolean.

    Args:
        env_var_name: Name of target environment variable.
        default: Default if said environment variable isn't defined.

    Returns:
        The env variable as a boolean.

    Raises:
        ValueError: If the env variable isn't a 'string boolean'.
    """
    env_var: str = os.getenv(env_var_name, default)

    # Normalize and check common boolean representations
    normalized = env_var.lower().strip()

    if normalized in ("true", "1", "yes", "on", "enabled"):
        return True
    elif normalized in ("false", "0", "no", "off", "disabled"):
        return False
    else:
        raise ValueError(f"Invalid boolean value: {env_var}")
