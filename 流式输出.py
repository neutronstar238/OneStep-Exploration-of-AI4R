from typing import Optional, Union, Sequence
import agentscope
from agentscope.agents import AgentBase, UserAgent
from agentscope.message import Msg
# 加载模型配置

# 创建三个智能体
agentscope.init(
    model_configs=[
        {
            "config_name": "my_config",
            "model_type": "openai_chat",
            "model_name": "deepseek-chat",
            "api_key": "sk-XXXXX",
            "stream": True,
            "client_args": {
                "base_url": "https://api.deepseek.com/v1"
            },
        }, 
    ],
    save_api_invoke=True,
    # If AgentScope Studio is running locally
    # studio_url="http://127.0.0.1:5000",
    project="Conversation in Stream Mode",
    #studio_url="http://localhost:3001"
)

class StreamingAgent(AgentBase):
    """An agent that speaks streaming messages."""

    def __init__(
        self,
        name: str,
        sys_prompt: str,
        model_config_name: str,
    ) -> None:
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name,
        )

        self.memory.add(Msg(self.name, self.sys_prompt, "system"))

    def reply(self, x: Optional[Union[Msg, Sequence[Msg]]] = None) -> Msg:
        self.memory.add(x)

        prompt = self.model.format(self.memory.get_memory())

        res = self.model(prompt)


        if res.stream is not None:
            self.speak(res.stream)
        else:

            error_msg = "Received empty response from the model"
            self.speak(error_msg)
            msg_returned = Msg(self.name, error_msg, "assistant")
            self.memory.add(msg_returned)
            return msg_returned

        response_text = res.text.strip() if res.text else "No valid response generated"
        msg_returned = Msg(self.name, response_text, "assistant")

        self.memory.add(msg_returned)

        return msg_returned


agent = StreamingAgent(
    "assistant",
    sys_prompt="You're a helpful assistant",
    model_config_name="my_config",
)
user = UserAgent("user")

msg = None
while True:
    msg = user()

    msg = agent(msg)
