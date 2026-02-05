# for our orchestrator the work is to initialize the state


def initial_state(goal: str) -> dict:
    """ 
        Create the initial agent state.
        State is owned ONLY by the controller.
    """
    return {
       "goal": goal,
       "status": "running",
       "history": [],         # reasoning + observations
       "result": []
    }
