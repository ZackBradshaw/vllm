from vllm import LLM, LoRARequest
from vllm.engine.llm_engine import forward

# Example of multimodal inference with a LoRA adapter
llm = LLM(model="your-model", enable_lora=True)
lora_request = LoRARequest("your_adapter_name", 1, "path/to/your/adapter", input_mode='multimodal')

# Assuming `input_embeddings` is your multimodal data
outputs = llm.generate(input_embeddings=input_embeddings, lora_request=lora_request)

print(outputs)
