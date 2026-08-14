"""Shared API configuration for TeaCH inference models."""

import os
from dataclasses import dataclass

import config


@dataclass(frozen=True)
class ModelApiConfig:
    multimodal: bool
    api_base: str | None = None
    api_key_env: str | None = None
    api_model: str | None = None

    def to_legacy_dict(self) -> dict:
        """Return the dict shape consumed by existing inference scripts."""
        result = {
            "multimodal": self.multimodal,
            "api_base": self.api_base,
            "api_key_env": self.api_key_env,
        }
        if self.api_model is not None:
            result["api_model"] = self.api_model
        return result


def _proxy(multimodal: bool) -> ModelApiConfig:
    return ModelApiConfig(multimodal=multimodal)


MODEL_API_CONFIGS = {
    "mock": _proxy(multimodal=True),
    "claude-haiku-4-5": _proxy(multimodal=True),
    "claude-sonnet-4-5": _proxy(multimodal=True),
    "claude-sonnet-4-6": _proxy(multimodal=True),
    "claude-opus-4-5": _proxy(multimodal=True),
    "claude-opus-4-6": _proxy(multimodal=True),
    "gemini-2.0-flash": _proxy(multimodal=True),
    "gemini-2.5-flash": _proxy(multimodal=True),
    "gemini-2.5-pro": _proxy(multimodal=True),
    "gemini-3-flash-preview": _proxy(multimodal=True),
    "gemini-3-pro-preview": _proxy(multimodal=True),
    "gemini-3.1-pro-preview": _proxy(multimodal=True),
    "gpt-4o": _proxy(multimodal=True),
    "gpt-4.1": _proxy(multimodal=True),
    "gpt-5": _proxy(multimodal=True),
    "gpt-5.2": _proxy(multimodal=True),
    "doubao-seed-1-6-thinking-250715": _proxy(multimodal=False),
    "deepseek-chat": ModelApiConfig(
        multimodal=False,
        api_base="https://api.deepseek.com",
        api_key_env="DEEPSEEK_API_KEY",
    ),
    "deepseek-reasoner": ModelApiConfig(
        multimodal=False,
        api_base="https://api.deepseek.com",
        api_key_env="DEEPSEEK_API_KEY",
    ),
    "Kimi-K25": ModelApiConfig(
        multimodal=True,
        api_base=getattr(config, "KIMI_BASE", "https://api.agicto.cn/v1"),
        api_key_env="KIMI_KEY_PUBLIC",
        api_model=getattr(config, "KIMI_MODEL", "kimi-k2.5"),
    ),
    "MiniMax-M2.7": ModelApiConfig(
        multimodal=True,
        api_base="https://bcedpgqjghjpcjkjjchem5oaopkoqbba.openapi-qb-ai.sii.edu.cn/v1",
        api_key_env="KIMI_KEY_PUBLIC",
    ),
    "glm-5": ModelApiConfig(
        multimodal=True,
        api_base="https://5ach5c5dabhcceg5m8d8h5ahq9c8pmh5.openapi-qb-ai.sii.edu.cn/v1",
        api_key_env="KIMI_KEY_PUBLIC",
    ),
    "glm-4.6v": ModelApiConfig(
        multimodal=True,
        api_base="https://d9mppg5ga5gcc8jkj85h88g8mghpjkbd.openapi-qb-ai.sii.edu.cn/v1",
        api_key_env="GLM46V_KEY_PUBLIC",
    ),
    "qwen3.5-397b": ModelApiConfig(
        multimodal=True,
        api_base="https://cge8kkjh9jgqcmjqkgpdedqqaog8gbkb.openapi-qb-ai.sii.edu.cn/v1",
        api_key_env="QWEN_KEY_PUBLIC",
    ),
    "qwen3.6-35b": ModelApiConfig(
        multimodal=False,
        api_base="https://8cm59gempbddcop8m5pmjbmheohoaohj.openapi-qb-ai.sii.edu.cn/v1",
        api_key_env="QWEN_KEY_PUBLIC",
        api_model="qwen",
    ),
}


_CONFIG_KEY_NAMES = {
    "DEEPSEEK_API_KEY": "DEEPSEEK_API_KEY",
    "KIMI_API_KEY": "KIMI_API_KEY",
    "KIMI_KEY_PUBLIC": "KIMI_KEY",
    "GLM5_KEY_PUBLIC": "GLM5_KEY",
    "QWEN_KEY_PUBLIC": "QWEN_KEY",
    "GLM46V_KEY_PUBLIC": "GLM46V_KEY",
}


def resolve_api_key(key_env: str) -> str:
    """Resolve a model key from config.py first, then the environment."""
    config_name = _CONFIG_KEY_NAMES.get(key_env, key_env)
    return getattr(config, config_name, "") or os.environ.get(key_env, "")

