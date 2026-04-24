from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, Dict, Any


class Component(BaseModel):
    name: str = Field(..., description="Full title of the component")
    category: str = Field(..., description="e.g., 'CPU', 'Motherboard', 'GPU'")
    url: HttpUrl = Field(..., description="Direct link to the product website")

    price_uah: float = Field(..., description="Current price in Ukrainian currency")
    is_available: bool = Field(default=True, description="Is it currently in stock?")

    specs: Dict[str, Any] = Field(
        default_factory=dict, description="Component-specific specifications"
    )


class Config:
    str_strip_whitespace = True
