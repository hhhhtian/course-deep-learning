import itertools, os

# ✅ grid 不变
grid = {
    "block_size": [64, 128],
    "n_layer": [4, 6],
    "n_head": [4, 8],
    "n_embd": [128, 256],
    "batch_size": [8, 16],
    "max_iters": [1000, 2000],
    "dropout": [0.1, 0.2],
}

out_dir = "config/train_shakespeare"
os.makedirs(out_dir, exist_ok=True)

# 所有组合
keys = list(grid.keys())
values = [grid[k] for k in keys]
combos = list(itertools.product(*values))
print(f"Total configs: {len(combos)}")

for idx, combo in enumerate(combos):
    cfg = dict(zip(keys, combo))
    path = os.path.join(out_dir, f"train_shakespeare_{idx:03d}.py")
    with open(path, "w") as f:
        f.write("# Auto-generated config file\n\n")

        # 固定部分（不变）
        f.write("# train a miniature character-level shakespeare model\n")
        f.write("# good for debugging and playing on macbooks and such\n\n")

        f.write("out_dir = 'out-shakespeare'\n")
        f.write("eval_interval = 250\n")
        f.write("eval_iters = 200\n")
        f.write("log_interval = 10\n\n")

        f.write("always_save_checkpoint = False\n\n")

        f.write("wandb_log = True\n")
        f.write("wandb_project = 'shakespeare'\n")
        f.write(f"wandb_run_name = 'shakespeare_{idx:03d}'\n\n")

        f.write("dataset = 'shakespeare'\n")
        f.write("gradient_accumulation_steps = 1\n")

      
        f.write(f"batch_size = {cfg['batch_size']}\n")
        f.write(f"block_size = {cfg['block_size']}\n\n")

        f.write("# baby GPT model :)\n")
        f.write(f"n_layer = {cfg['n_layer']}\n")
        f.write(f"n_head = {cfg['n_head']}\n")
        f.write(f"n_embd = {cfg['n_embd']}\n")
        f.write(f"dropout = {cfg['dropout']}\n\n")

       
        f.write("learning_rate = 1e-3\n")
        f.write(f"max_iters = {cfg['max_iters']}\n")
        f.write(f"lr_decay_iters = {cfg['max_iters']}\n")
        f.write("min_lr = 1e-4\n")
        f.write("beta2 = 0.99\n\n")
        f.write("warmup_iters = 100\n")

    print(f"Wrote {path}")
