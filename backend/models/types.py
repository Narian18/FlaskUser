from dataclasses import dataclass
from uuid import UUID


@dataclass
class ModelID:
    id: int | UUID
