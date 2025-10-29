# Auto-generated config file

# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out-shakespeare'
eval_interval = 250
eval_iters = 200
log_interval = 10

always_save_checkpoint = False

wandb_log = True
wandb_project = 'shakespeare'
wandb_run_name = 'shakespeare_115'

dataset = 'shakespeare'
gradient_accumulation_steps = 1
batch_size = 8
block_size = 128

# baby GPT model :)
n_layer = 6
n_head = 8
n_embd = 128
dropout = 0.2

learning_rate = 1e-3
max_iters = 2000
lr_decay_iters = 2000
min_lr = 1e-4
beta2 = 0.99

warmup_iters = 100
