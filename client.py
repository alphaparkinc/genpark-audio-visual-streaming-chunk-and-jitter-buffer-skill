"""Audio-Visual Streaming Chunk & Jitter Buffer.
100% Python Standard Library.
"""

class StreamingJitterBuffer:
    """Buffers, reorders, and deduplicates fragmented real-time audio/video chunks with sequence tracking."""

    @staticmethod
    def process_chunks(chunks: list, expected_total: int) -> dict:
        seen_seqs = set()
        unique_chunks = []
        for ch in chunks:
            seq = int(ch.get("seq", 0))
            if seq not in seen_seqs:
                seen_seqs.add(seq)
                unique_chunks.append(ch)

        sorted_chunks = sorted(unique_chunks, key=lambda x: int(x.get("seq", 0)))
        missing_seqs = [s for s in range(1, expected_total + 1) if s not in seen_seqs]
        is_complete = len(missing_seqs) == 0

        total_bytes = sum(len(c.get("payload_b64", "")) for c in sorted_chunks)
        return {
            "received_chunks": len(chunks),
            "unique_ordered_count": len(sorted_chunks),
            "missing_sequences": missing_seqs,
            "buffer_complete": is_complete,
            "total_payload_bytes": total_bytes
        }
