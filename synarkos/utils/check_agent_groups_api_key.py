import os


def check_synarkos_api_key():
    """
    Check if the SynarkOS API key is set.

    Returns:
        str: The value of the SYNARKOS_API_KEY environment variable.

    Raises:
        ValueError: If the SYNARKOS_API_KEY environment variable is not set.
    """
    if os.getenv("SYNARKOS_API_KEY") is None:
        raise ValueError(
            "SynarkOS API key is not set. Please set the SYNARKOS_API_KEY environment variable. "
            "You can get your key here: https://synarkos.world/platform/api-keys"
        )
    return os.getenv("SYNARKOS_API_KEY")
