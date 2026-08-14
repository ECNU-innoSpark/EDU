"""
TeaCH 推理监控面板 (Web 版) - 实时显示各模型的推理进度

启动方式：
  python scripts/monitor/web_monitor.py

然后在浏览器打开：http://localhost:8000
"""

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime

# ── 路径配置 ──────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # scripts/monitor
SCRIPTS_DIR = os.path.dirname(SCRIPT_DIR)               # scripts
ROOT_DIR = os.path.dirname(SCRIPTS_DIR)                 # Jiaozikaoshi
sys.path.insert(0, SCRIPTS_DIR)

from config import DATASET_DIR
from inference.run import DATASET_GROUPS

try:
    from flask import Flask, render_template_string, jsonify
except ImportError:
    print("[ERROR] 需要安装 Flask: pip install flask")
    sys.exit(1)

app = Flask(__name__)

# 全局状态
monitor_state = {
    "models": {},
    "start_time": None,
    "total_questions": 0,
}

MODELS = [
    ("Claude Sonnet 4.6", "claude-sonnet-4-6"),
    ("Gemini 3.0-Flash", "gemini-3-flash-preview"),
    ("Gemini 3.1-Pro", "gemini-3.1-pro-preview"),
    ("GPT-5.2", "gpt-5.2"),
    ("Kimi K2.5", "Kimi-K25"),
    ("Qwen 3.5-397B", "qwen3.5-397b"),
    ("GLM-4.6V", "glm-4.6v"),
]

RESULTS_DIR = os.path.join(ROOT_DIR, "results")


def load_all_datasets_total_count():
    """扫描 dataset/ 计算真实题目总数"""
    import glob
    total_q = 0
    for group_name, pattern in DATASET_GROUPS.items():
        file_pattern = os.path.join(DATASET_DIR, pattern)
        for f in glob.glob(file_pattern):
            with open(f, "r", encoding="utf-8") as fh:
                total_q += sum(1 for _ in fh)
    return total_q


def count_completed_questions(model_id):
    """计算某个模型已完成的题目数"""
    model_results_dir = os.path.join(RESULTS_DIR, model_id)
    if not os.path.exists(model_results_dir):
        return 0
    completed = 0
    for jsonl_file in Path(model_results_dir).glob("*.jsonl"):
        if not jsonl_file.stem.endswith("_scored"):
            try:
                with open(jsonl_file, "r", encoding="utf-8") as f:
                    completed += sum(1 for _ in f)
            except:
                pass
    return completed


@app.route('/')
def index():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>TeaCH Monitor</title>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="10">
    <style>
        body { font-family: sans-serif; margin: 40px; background: #f4f4f9; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }
        h1 { color: #333; }
        table { width: 100%; border-collapse: collapse; }
        th, td { text-align: left; padding: 12px; border-bottom: 1px solid #ddd; }
        th { background: #eee; }
        .progress-bar { background: #eee; border-radius: 4px; width: 200px; height: 20px; display: inline-block; vertical-align: middle; }
        .progress-fill { background: #4caf50; height: 100%; border-radius: 4px; transition: width 0.5s; }
        .status-running { color: #2196f3; font-weight: bold; }
        .status-completed { color: #4caf50; font-weight: bold; }
        .status-pending { color: #999; }
    </style>
</head>
<body>
    <h1>TeaCH 推理实时监控</h1>
    <div class="card">
        <p>总题目数: {{ state.total_questions }} | 刷新时间: {{ now }}</p>
        <table>
            <thead>
                <tr>
                    <th>模型</th>
                    <th>完成度</th>
                    <th>百分比</th>
                    <th>进度条</th>
                </tr>
            </thead>
            <tbody>
                {% for model_id, m in state.models.items() %}
                <tr>
                    <td>{{ m.display_name }}</td>
                    <td>{{ m.completed }} / {{ state.total_questions }}</td>
                    <td>{{ (m.completed / state.total_questions * 100) | round(1) }}%</td>
                    <td>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: {{ (m.completed / state.total_questions * 100) }}%"></div>
                        </div>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
""", state=monitor_state, now=datetime.now().strftime("%H:%M:%S"))


def update_loop():
    """定期更新状态"""
    total_q = load_all_datasets_total_count()
    monitor_state["total_questions"] = total_q
    while True:
        for display_name, model_id in MODELS:
            completed = count_completed_questions(model_id)
            monitor_state["models"][model_id] = {
                "display_name": display_name,
                "completed": completed
            }
        time.sleep(10)


if __name__ == '__main__':
    import threading
    threading.Thread(target=update_loop, daemon=True).start()
    print("监控服务已启动: http://localhost:8000")
    app.run(port=8000)
