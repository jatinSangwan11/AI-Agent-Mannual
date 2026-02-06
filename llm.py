# here we are mocking the LLM and want to test the agent loop
"""
A real LLM:

Reads the goal

Decides what to do next

Our mock:

Pattern-matches the goal

Returns the “correct” next step

We are not testing intelligence.
We are testing control flow. """

class MockLLM:
    """
        mock LLM that returns ReAct-style outputs.
    """

    def generate(self, prompt: str)-> str:

        if "Action:" not in prompt:
            return ""

        if "Observation:" in prompt:
            print("\ngot the obeservation")
            return (
                "Thought: I have the papers. I should summarize them and finish.\n"
                "Action: Finish\n"
                "Action Input: summarize"
            )

        if "Find 3 recent AI agent research papers" in prompt:
            return (
                "Thought: I should search for recent AI agent research papers.\n"
                "Action: search_papers\n"
                "Action Input: AI agent research"                
            )

        # After receiving search results
        print


        return ""
