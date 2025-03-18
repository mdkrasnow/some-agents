def get_models_by_company():
    models_list = [
        "cohere/command-r-08-2024", "cohere/command-r-plus-08-2024", "sao10k/l3.1-euryale-70b", "google/gemini-flash-1.5-8b-exp",
        "qwen/qwen-2.5-vl-7b-instruct", "ai21/jamba-1-5-large", "ai21/jamba-1-5-mini", "microsoft/phi-3.5-mini-128k-instruct",
        "nousresearch/hermes-3-llama-3.1-70b", "nousresearch/hermes-3-llama-3.1-405b", "openai/chatgpt-4o-latest", "sao10k/l3-lunaris-8b",
        "aetherwiing/mn-starcannon-12b", "openai/gpt-4o-2024-08-06", "meta-llama/llama-3.1-405b", "nothingiisreal/mn-celeste-12b",
        "perplexity/llama-3.1-sonar-small-128k-chat", "perplexity/llama-3.1-sonar-large-128k-chat", "perplexity/llama-3.1-sonar-large-128k-online",
        "perplexity/llama-3.1-sonar-small-128k-online", "meta-llama/llama-3.1-405b-instruct", "meta-llama/llama-3.1-8b-instruct:free",
        "meta-llama/llama-3.1-8b-instruct", "meta-llama/llama-3.1-70b-instruct", "mistralai/mistral-nemo:free", "mistralai/mistral-nemo",
        "mistralai/codestral-mamba", "openai/gpt-4o-mini", "openai/gpt-4o-mini-2024-07-18", "qwen/qwen-2-7b-instruct:free",
        "qwen/qwen-2-7b-instruct", "google/gemma-2-27b-it", "alpindale/magnum-72b", "google/gemma-2-9b-it:free", "google/gemma-2-9b-it",
        "01-ai/yi-large", "ai21/jamba-instruct", "anthropic/claude-3.5-sonnet-20240620:beta", "anthropic/claude-3.5-sonnet-20240620",
        "sao10k/l3-euryale-70b", "cognitivecomputations/dolphin-mixtral-8x22b", "qwen/qwen-2-72b-instruct", "mistralai/mistral-7b-instruct:free",
        "mistralai/mistral-7b-instruct", "mistralai/mistral-7b-instruct-v0.3", "nousresearch/hermes-2-pro-llama-3-8b",
        "microsoft/phi-3-mini-128k-instruct:free", "microsoft/phi-3-mini-128k-instruct", "microsoft/phi-3-medium-128k-instruct:free",
        "microsoft/phi-3-medium-128k-instruct", "neversleep/llama-3-lumimaid-70b", "google/gemini-flash-1.5", "openai/gpt-4o-2024-05-13",
        "meta-llama/llama-guard-2-8b", "openai/gpt-4o", "openai/gpt-4o:extended", "neversleep/llama-3-lumimaid-8b:extended",
        "neversleep/llama-3-lumimaid-8b", "sao10k/fimbulvetr-11b-v2", "meta-llama/llama-3-8b-instruct:free", "meta-llama/llama-3-8b-instruct",
        "meta-llama/llama-3-70b-instruct", "mistralai/mistral-large", "google/gemma-7b-it", "openai/gpt-3.5-turbo-0613",
        "openai/gpt-4-turbo-preview", "nousresearch/nous-hermes-2-mixtral-8x7b-dpo", "mistralai/mistral-small", "mistralai/mistral-tiny",
        "mistralai/mistral-medium", "mistralai/mistral-7b-instruct-v0.2", "cognitivecomputations/dolphin-mixtral-8x7b", "google/gemini-pro-vision",
        "google/gemini-pro", "mistralai/mixtral-8x7b", "mistralai/mixtral-8x7b-instruct", "openchat/openchat-7b:free", "openchat/openchat-7b",
        "neversleep/noromaid-20b", "anthropic/claude-2:beta", "anthropic/claude-2", "anthropic/claude-2.1:beta", "anthropic/claude-2.1",
        "teknium/openhermes-2.5-mistral-7b", "undi95/toppy-m-7b:free", "undi95/toppy-m-7b", "alpindale/goliath-120b", "openrouter/auto",
        "openai/gpt-3.5-turbo-1106", "openai/gpt-4-1106-preview", "google/palm-2-chat-bison-32k", "google/palm-2-codechat-bison-32k",
        "jondurbin/airoboros-l2-70b", "xwin-lm/xwin-lm-70b", "openai/gpt-3.5-turbo-instruct", "mistralai/mistral-7b-instruct-v0.1",
        "pygmalionai/mythalion-13b", "openai/gpt-3.5-turbo-16k", "openai/gpt-4-32k", "openai/gpt-4-32k-0314", "nousresearch/nous-hermes-llama2-13b",
        "mancer/weaver", "huggingfaceh4/zephyr-7b-beta:free", "anthropic/claude-2.0:beta", "anthropic/claude-2.0", "undi95/remm-slerp-l2-13b",
        "google/palm-2-chat-bison", "google/palm-2-codechat-bison", "gryphe/mythomax-l2-13b:free", "gryphe/mythomax-l2-13b",
        "meta-llama/llama-2-13b-chat", "meta-llama/llama-2-70b-chat", "openai/gpt-3.5-turbo", "openai/gpt-3.5-turbo-0125", "openai/gpt-4",
        "openai/gpt-4-0314"
    ]
    
    # Group models by company
    models_by_company = defaultdict(list)
    for model in models_list:
        company = model.split('/')[0]
        models_by_company[company].append(model)
    
    return models_by_company