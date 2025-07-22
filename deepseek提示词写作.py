from agentscope.agents import DialogAgent,UserAgent
from agentscope.message import Msg
from agentscope.pipelines import sequential_pipeline
from agentscope import msghub
import agentscope
from agentscope.models import OpenAIChatWrapper
from openai import OpenAI
from docx import Document
from datetime import datetime
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import init_agents
# 加载模型配置

# 创建三个智能体

init_agents.init()

deepseek = DialogAgent(
    name="assistant1",
    model_config_name="deepseek_config",
    sys_prompt="""
    	
你是一位大模型提示词生成专家，请根据用户的需求为DeepSeek推理模型编写一个智能助手的提示词，来指导大模型进行内容生成，要求：
1. 以 Markdown 格式输出，使用中文
2. 贴合用户需求，描述智能助手的定位、能力、知识储备
3. 提示词应清晰、精确、易于理解，在保持质量的同时，尽可能简洁
4. 只输出提示词，不要输出多余解释
5. 保留一定的可拓展性即让大模型能够在一定限度内自由发挥
    """,

)

# 通过msghub创建一个聊天室，智能体的消息会广播给所有参与者
with agentscope.msghub(
    participants=[], 
) as hub:
    # 按顺序发言
    #sequential_pipeline([friday, saturday, judgement],x=None)
    hub.add(deepseek)
    while True:
        user_agent = UserAgent(name="用户")
        x=user_agent(x=None)
        x=deepseek(x)
    