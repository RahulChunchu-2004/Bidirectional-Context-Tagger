import transformers

MAX_LEN = 128
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 8
EPOCHS = 10
BASE_MODEL_PATH = "../input/bert_base_uncased"
MODEL_PATH = "model.bin"
TRAINING_FILE = "../input/ner_dataset.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BASE_MODEL_PATH,
    do_lower_case=True,  use_auth_token="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"
)

# import transformers

# MAX_LEN = 128
# TRAIN_BATCH_SIZE = 32
# VALID_BATCH_SIZE = 8
# EPOCHS = 10
# BASE_MODEL_PATH = "../input/bert_base_uncased"
# MODEL_PATH = "model.bin"
# TRAINING_FILE = "../input/ner_dataset.csv"
# TOKENIZER = transformers.BertTokenizer.from_pretrained(
#     BASE_MODEL_PATH,
#     do_lower_case=True
# )

# import transformers

# MAX_LEN = 128
# TRAIN_BATCH_SIZE = 32
# VALID_BATCH_SIZE = 8
# EPOCHS = 10
# BASE_MODEL_PATH = "bert-base-uncased"  # Use Hugging Face model ID
# MODEL_PATH = "model.bin"
# TRAINING_FILE = "../input/ner_dataset.csv"
# TOKENIZER = transformers.BertTokenizer.from_pretrained(
#     BASE_MODEL_PATH,
#     do_lower_case=True
# )
# import transformers

# MAX_LEN = 128
# TRAIN_BATCH_SIZE = 32
# VALID_BATCH_SIZE = 8
# EPOCHS = 10
# BASE_MODEL_PATH = "../input/bert_base_uncased"
# MODEL_PATH = "model.bin"
# TRAINING_FILE = "../input/ner_dataset.csv"
# TOKENIZER = transformers.BertTokenizer.from_pretrained(
#     BASE_MODEL_PATH,
#     do_lower_case=True
# )

import transformers

MAX_LEN = 128
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 8
EPOCHS = 10
BASE_MODEL_PATH = "bert-base-uncased"  # Use Hugging Face model ID
MODEL_PATH = "model.bin"
TRAINING_FILE = "../input/ner_dataset.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BASE_MODEL_PATH,
    do_lower_case=True
)
