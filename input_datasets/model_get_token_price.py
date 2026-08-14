from input_datasets.load import BASE_MODEL_SHORT_V1

# make sure to save screenshots and source pages in /Users/l/other_git_repos/TeaCH-main/scripts/input_datasets/model_pages
# 每百万 output token 的美元单价。
# 口径 = OpenRouter 模型页正文标称价（"<model> costs $X per million input tokens and
# $Y per million output tokens"），与下方 Kimi-K25 那条原始记录一致；注意它与
# /api/v1/models 的 pricing.completion 并不总是相等（后者是默认 provider 路由价，
# 例如 Kimi K2.5 页面 2.025 而接口 2.85），本表一律以页面标称价为准。
# 行尾注释是该模型在 https://openrouter.ai/<slug> 的 slug，对应存档见同目录
# model_pages/<slug 中 / 换成 _>.html（另有 openrouter_api_v1_models__<date>.json 全量快照）。
# 值为 None 的是开源权重、本项目自行部署推理的模型：OpenRouter 上没有对应条目，
# 也就没有按 token 计费的官方单价（成本取决于自己的 GPU 时长，不可比）。
model2usd_per_moutput_token = {
        # ── 闭源 / 托管 API ─────────────────────────────────────────
        "claude-opus-4-6"        : 25.0,   # anthropic/claude-opus-4.6
        "claude-sonnet-4-6"      : 15.0,   # anthropic/claude-sonnet-4.6
        "gemini-3.1-pro-preview" : 12.0,   # google/gemini-3.1-pro-preview
        "gemini-3-flash-preview" : 3.0,    # google/gemini-3-flash-preview
        "gpt-5.2"                : 14.0,   # openai/gpt-5.2
        # source: 'https://openrouter.ai/moonshotai/kimi-k2.5',
        "Kimi-K25":2.025,
        "qwen3.5-397b"           : 2.45,   # qwen/qwen3.5-397b-a17b
        "glm-4.6v"               : 0.90,   # z-ai/glm-4.6v
        "qwen3.5-9b"             : 0.15,   # qwen/qwen3.5-9b
        "qwen3.6-27b"            : 2.40,   # qwen/qwen3.6-27b
        # 这两条 key 名都带 3.6，但按 load.py 里的显示名，无后缀的那条其实是 Qwen3.5-35B-A3B、
        # -latest 才是 Qwen3.6 35B A3B；两个模型页标价恰好都是 $0.14 / $1 per 1M，故同值。
        "qwen3.6-35b"            : 1.0,    # qwen/qwen3.5-35b-a3b
        "qwen3.6-35b-latest"     : 1.0,    # qwen/qwen3.6-35b-a3b
        "gemma-4-26B-A4B-it"     : 0.34,   # google/gemma-4-26b-a4b-it
        "gemma-4-31B-it"         : 0.34,   # google/gemma-4-31b-it
        "ministral-3-14b"        : 0.2,    # mistralai/ministral-14b-2512
        "ministral-3-8b"         : 0.15,   # mistralai/ministral-8b-2512
        "ministral-3-3b"         : 0.1,    # mistralai/ministral-3b-2512

        # ── 开源权重、自行部署（OpenRouter 无对应条目，无 per-token 单价） ──
        "gemma-4-12B-it"         : None,
        "gemma-4-E2B-it"         : None,
        "InternVL3_5-2B"         : None,
        "InternVL3_5-4B"         : None,
        "InternVL3_5-8B"         : None,
        "InternVL3_5-14B"        : None,
        "Kimi-VL-A3B-Instruct"   : None,
        "MiMo-VL-7B-SFT"         : None,
        "Molmo2-8B"              : None,
        "Phi-3.5-vision-instruct": None,
        # 不在 BASE_MODEL_SHORT_V1 里，但出现在 cross_national CSV 里；
        # OpenRouter 只剩 llama-3.2-1b/3b，11B-Vision 已下架，故同样无标价。
        "Llama-3.2-11B-Vision-Instruct": None,
        "Qwen3.5-4B"             : None,
        "Step3-VL-10B"           : None,
}

# 放进 main guard：本模块会被 generate_latex.py 等 import，
# 裸的 print 循环会污染那边的 stdout。
if __name__ == "__main__":
    for m in BASE_MODEL_SHORT_V1:
        print(model2usd_per_moutput_token[m])
