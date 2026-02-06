def build_prompt(state: dict, tool_descriptions: str) -> str:
    history = "\n".join(state["history"])
    print(history)
    return f"""
        You are an AI agent.

        Goal:
        {state['goal']}

        Available tools:
        {tool_descriptions}

        History:
        {history}

        Respond strictly in ReAct format:
        Thought:
        Action:
        Action Input:
        """
