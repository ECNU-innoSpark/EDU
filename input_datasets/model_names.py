NO_THINK_SUFFIX = "_nothink"

def prettify_model_id(model_id: str) -> str:
    """Return a compact display name for generated model folder names."""
    suffix = ""
    base = model_id
    if base.endswith(NO_THINK_SUFFIX):
        base = base[:-len(NO_THINK_SUFFIX)]
        suffix = "-No Think"

    # Step3-VL 10B-No Think

    explicit = {
            "claude-opus-4-6"        : "Claude Opus 4.6",
            "gemma-4-12B-it"         : "Gemma 4 12B IT",
            "gemma-4-26B-A4B-it"     : "Gemma 4 26B-A4B IT",
            "gemma-4-31B-it"         : "Gemma 4 31B IT",
            "gemma-4-E2B-it"         : "Gemma 4 E2B IT",
            "InternVL3_5-14B"        : "InternVL3.5 14B",
            "InternVL3_5-2B"         : "InternVL3.5 2B",
            "InternVL3_5-4B"         : "InternVL3.5 4B",
            "InternVL3_5-8B"         : "InternVL3.5 8B",
            "Kimi-VL-A3B-Instruct"   : "Kimi-VL A3B Instruct",
            "MiMo-VL-7B-SFT"         : "MiMo-VL 7B SFT",
            "ministral-3-14b"        : "Ministral 3 14B",
            "ministral-3-3b"         : "Ministral 3 3B",
            "ministral-3-8b"         : "Ministral 3 8B",
            "Molmo2-8B"              : "Molmo2 8B",
            "Phi-3.5-vision-instruct": "Phi-3.5 Vision Instruct",
            "Qwen3.5-4B"             : "Qwen3.5 4B",
            "qwen3.5-9b"             : "Qwen3.5 9B",
            "qwen3.6-27b"            : "Qwen3.6 27B",
            "qwen3.6-35b"            : "Qwen3.5 35B",
            "qwen3.6-35b-latest"     : "Qwen3.6 35B",
            "qwen397"                : "Qwen3.5 397B",
            "Step3-VL-10B"           : "Step3-VL 10B",
    }
    return explicit.get(base, base.replace("_", " ").replace("-", " ")) + suffix

