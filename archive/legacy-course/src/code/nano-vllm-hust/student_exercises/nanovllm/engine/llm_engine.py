from dataclasses import fields
from transformers import AutoTokenizer
import torch.multiprocessing as mp

from nanovllm.config import Config
from nanovllm.sampling_params import SamplingParams
from nanovllm.engine.sequence import Sequence
from nanovllm.engine.scheduler import Scheduler
from nanovllm.engine.model_runner import ModelRunner


class LLMEngine:

    def __init__(self, model, **kwargs):
        config_fields = {field.name for field in fields(Config)}
        config_kwargs = {k: v for k, v in kwargs.items() if k in config_fields}
        config = Config(model, **config_kwargs)
        Sequence.block_size = config.kvcache_block_size
        self.ps = []
        self.events = []
        ctx = mp.get_context("spawn")
        for i in range(1, config.tensor_parallel_size):
            event = ctx.Event()
            process = ctx.Process(target=ModelRunner, args=(config, i, event))
            process.start()
            self.ps.append(process)
            self.events.append(event)
        self.model_runner = ModelRunner(config, 0, self.events)
        self.tokenizer = AutoTokenizer.from_pretrained(config.model, use_fast=True)
        config.eos = self.tokenizer.eos_token_id
        self.scheduler = Scheduler(config)

    def add_request(self, prompt: str | list[int], sampling_params: SamplingParams):
        """Tutorial 2 task.

        Goal:
        - accept either raw text or token ids
        - build a Sequence object
        - hand the sequence to the scheduler
        """
        raise NotImplementedError("TODO: implement request ingestion for Tutorial 2")

    def step(self):
        """Tutorial 2 task.

        Goal:
        - ask the scheduler for runnable sequences
        - decide the token count used for throughput accounting
        - call the model runner
        - hand model outputs back to the scheduler
        - collect finished sequence outputs
        """
        raise NotImplementedError("TODO: implement one engine step for Tutorial 2")

    def is_finished(self):
        return self.scheduler.is_finished()
