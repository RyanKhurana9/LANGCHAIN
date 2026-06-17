
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
import os
#chathugging face provide chat interface to hugging face models
#HuggingFacePipeline allows us to use Hugging Face models as language models is Langchain.we specify the model id that we are going to use and the taks we want to perform and in this case we are using text genration task
# Optional: cache folder
os.environ['HF_HOME'] = '/Users/ryankhurana/huggingface_cache'
#sets the hugging face cache directory to the specified path
#Useful for managing storage or keeping models in a custom folder.

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',#model id of the hugging face model we want to use
    task='text-generation',#task we want to perform
    pipeline_kwargs={#additional parameters for the pipeline
        "temperature": 0.5,#randomness of the output
        "max_new_tokens": 100
    },
    model_kwargs={#automatically detects the best device (GPU or CPU) for running the model
        "device_map": "auto"  # Hugging Face detects 'mps' or 'cpu'
    }
)

model = ChatHuggingFace(llm=llm)

prompt = "What is the capital of India?"
result = model.invoke(prompt)
print(result.content)
del model
del llm
import gc; 
gc.collect()
