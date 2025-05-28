import os
import shutil

# Source and destination paths
src_root = r"c:/Users/SURYA/Desktop/Surya/code_raja_code/Visual Navigation/river1"
dst_root = r"c:/Users/SURYA/Desktop/Surya/code_raja_code/Visual Navigation/visualnav-transformer/train/vint_train/data/river1"

# Create the destination directory if it doesn't exist
os.makedirs(dst_root, exist_ok=True)

# Loop through each trajectory folder in river1
for traj_folder in os.listdir(src_root):
    src_traj_path = os.path.join(src_root, traj_folder)
    dst_traj_path = os.path.join(dst_root, traj_folder)
    if os.path.isdir(src_traj_path):
        print(f"Copying {src_traj_path} -> {dst_traj_path}")
        # Remove destination if it exists to ensure a clean copy
        if os.path.exists(dst_traj_path):
            shutil.rmtree(dst_traj_path)
        shutil.copytree(src_traj_path, dst_traj_path)

print("Copy complete.")
