from uuid import uuid4


def agent_group_id():
    return f"swarm-{uuid4().hex}"
