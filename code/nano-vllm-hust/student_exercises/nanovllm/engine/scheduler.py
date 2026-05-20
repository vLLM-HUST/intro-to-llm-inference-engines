from collections import deque

from nanovllm.config import Config
from nanovllm.engine.sequence import Sequence, SequenceStatus
from nanovllm.engine.block_manager import BlockManager


class Scheduler:

    def __init__(self, config: Config):
        self.max_num_seqs = config.max_num_seqs
        self.max_num_batched_tokens = config.max_num_batched_tokens
        self.eos = config.eos
        self.block_size = config.kvcache_block_size
        self.block_manager = BlockManager(config.num_kvcache_blocks, config.kvcache_block_size)
        self.waiting: deque[Sequence] = deque()
        self.running: deque[Sequence] = deque()

    def is_finished(self):
        return not self.waiting and not self.running

    def add(self, seq: Sequence):
        self.waiting.append(seq)

    def schedule(self) -> tuple[list[Sequence], bool]:
        """Tutorial 3 task.

        Required behavior:
        - prefer prefill if any request can be prefilling
        - respect `max_num_seqs` and `max_num_batched_tokens`
        - move fully prefetched requests from waiting to running
        - fall back to decode when no prefill work is scheduled
        - preempt when decode cannot append because KV space is exhausted
        """
        raise NotImplementedError("TODO: implement prefill/decode scheduling for Tutorial 3")

    def preempt(self, seq: Sequence):
        """Tutorial 3 task.

        Goal:
        - move the sequence back to waiting state
        - mark it as prefill again
        - release its current KV residency
        """
        raise NotImplementedError("TODO: implement sequence preemption for Tutorial 3")

    def postprocess(self, seqs: list[Sequence], token_ids: list[int], is_prefill: bool):
        """Tutorial 3 task.

        Goal:
        - update cached-token accounting
        - finalize prefill-only chunks without sampling when prompt is incomplete
        - append sampled token after a finished prefill or a decode step
        - detect EOS or max_tokens completion
        - free KV state for finished requests
        """
        raise NotImplementedError("TODO: implement scheduler postprocess for Tutorial 3")
