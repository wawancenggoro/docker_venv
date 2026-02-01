# venv
sudo apt install python3.10-venv
python3 -m venv my_new_venv
source my_new_venv/bin/activate
pip install pandas
pip freeze
deactivate

# conda
# install miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install#linux-2
source ~/miniconda3/bin/activate
conda create -n myenv python=3.9
conda activate myenv
pip install pandas
pip freeze
conda deactivate