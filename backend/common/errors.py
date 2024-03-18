from typing import Tuple, Dict


def wrap_error(message: str, status: int) -> Tuple[Dict[str, str], int]:
    return {'error': message}, status
