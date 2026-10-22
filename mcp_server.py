"""MCP server for Audio-Visual Streaming Chunk & Jitter Buffer."""
import sys
import json
from client import StreamingJitterBuffer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "process_streaming_jitter_buffer",
                "description": "Reorders and deduplicates fragmented real-time audio/video chunks",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "chunks": {"type": "array"},
                        "expected_total": {"type": "integer"}
                    },
                    "required": ["chunks", "expected_total"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "process_streaming_jitter_buffer":
            args = params.get("arguments", {})
            res = StreamingJitterBuffer.process_chunks(
                args.get("chunks", []),
                int(args.get("expected_total", 1))
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
