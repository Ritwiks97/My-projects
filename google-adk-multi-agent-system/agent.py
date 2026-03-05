from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool

maths_agent = Agent(
    model='gemini-2.5-flash',
    name='maths_agent',
    description='A helpful maths assistant for user questions.',
    instruction='You are a math expert and you help only with math queries. Do not answer non-math queries',
)

computer_agent = Agent(
    model='gemini-2.5-flash',
    name='computer_agent',
    description='A helpful computer assistant for user questions.',
    instruction='You are a computer expert and you help only with computer queries. Do not answer non-computer queries',
)

orchestrator_agent = Agent(
    model='gemini-2.5-flash',
    name='orchestrator_agent',
    description='The main entry point for user queries. It routes tasks to the correct expert agent.',
    instruction="""You are an intelligent orchestrator. Your job is to analyze the user's request and delegate it to the appropriate sub-agent:
- If the request is about Mathematics, use the maths_agent.
- If the request is about Computer, use the computer_agent.
- If the request is not related to these two subjects, inform the user that you only specialize in Mathematics and Computer.

IMPORTANT: Once you receive the response from a sub-agent tool, you MUST provide that response back to the user. Do not just call the tool and stop. Your goal is to be the bridge between the experts and the user.""",
    tools=[
        AgentTool(maths_agent),
        AgentTool(computer_agent),
    ],
)
root_agent = orchestrator_agent

