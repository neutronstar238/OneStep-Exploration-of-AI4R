from agentscope.agents import ReActAgentV2, UserAgent
from agentscope.service import ServiceToolkit, execute_python_code
import agentscope
import requests
import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
import time
from agentscope.agents import DialogAgent
from agentscope.message import Msg
from agentscope.pipelines import sequential_pipeline
from agentscope import msghub
import agentscope
from docx import Document
from datetime import datetime
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from typing import Optional, Union, Sequence
import agentscope
from agentscope.agents import AgentBase, UserAgent
from agentscope.message import Msg

def init():
    agentscope.init(
    model_configs=[
        {
            "config_name": "deepseek_config",
            "model_type": "openai_chat",
            "model_name": "deepseek-reasoner", 
            "stream": True,
            "api_key": "",
            "client_args": {
                "base_url": "https://api.deepseek.com/v1"
            },
        }, 
        {
            "config_name": "deepseek1_config",
            "model_type": "openai_chat",
            "model_name": "deepseek-reasoner", 
            "stream": True,
            "api_key": "",
            "client_args": {
                "base_url": "https://api.deepseek.com/v1"
            },
        }, 
        {
            "config_name": "deepseek2_config",
            "model_type": "openai_chat",
            "model_name": "deepseek-reasoner", 
            "stream": True,
            "api_key": "",
            "client_args": {
                "base_url": "https://api.deepseek.com/v1"
            },
        }, 
        {
            "config_name": "deepseek3_config",
            "model_type": "openai_chat",
            "model_name": "deepseek-reasoner", 
            "stream": True,
            "api_key": "",
            "client_args": {
                "base_url": "https://api.deepseek.com/v1"
            },
        }, 
        {
            "config_name": "deepseek4_config",
            "model_type": "openai_chat",
            "model_name": "deepseek-reasoner", 
            "stream": True,
            "api_key": "",
            "client_args": {
                "base_url": "https://api.deepseek.com/v1"
            },
        }, 
        {
            "config_name": "deepseek5_config",
            "model_type": "openai_chat",
            "model_name": "deepseek-reasoner", 
            "stream": True,
            "api_key": "",
            "client_args": {
                "base_url": "https://api.deepseek.com/v1"
            },
        }, 
        {
            "config_name": "deepseek6_config",
            "model_type": "openai_chat",
            "model_name": "deepseek-reasoner", 
            "stream": True,
            "api_key": "",
            "client_args": {
                "base_url": "https://api.deepseek.com/v1"
            },
        },
        {
            "config_name": "score_config",
            "model_type": "openai_chat",
            "model_name": "deepseek-reasoner", 
            "stream": True,
            "api_key": "",
            "client_args": {
                "base_url": "https://api.deepseek.com/v1"
            },
        },
    ],
    project="科研小助手4.0",
    studio_url="http://localhost:3000",
    name="科研小助手1",
    )

