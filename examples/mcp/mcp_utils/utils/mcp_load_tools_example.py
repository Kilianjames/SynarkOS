import json

from synarkos.schemas.mcp_schemas import MCPConnection
from synarkos.tools.mcp_client_tools import (
    get_mcp_tools_sync,
)

if __name__ == "__main__":
    tools = get_mcp_tools_sync(
        server_path="http://0.0.0.0:8000/mcp",
        format="openai",
        connection=MCPConnection(
            url="http://0.0.0.0:8000/mcp",
            headers={"Authorization": "Bearer 1234567890"},
            timeout=10,
        ),
    )
    print(json.dumps(tools, indent=4))
