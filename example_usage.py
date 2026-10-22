"""Example usage for Audio-Visual Streaming Chunk & Jitter Buffer."""
from client import StreamingJitterBuffer

if __name__ == "__main__":
    chunks = [
        {"seq": 3, "payload_b64": "AAA="},
        {"seq": 1, "payload_b64": "BBB="},
        {"seq": 2, "payload_b64": "CCC="}
    ]
    res = StreamingJitterBuffer.process_chunks(chunks, expected_total=3)
    print("Buffer Complete:", res["buffer_complete"], "Ordered Count:", res["unique_ordered_count"])
