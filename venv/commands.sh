# venv
python -m venv my_new_venv
./my_new_venv/Scripts/activate
pip install pandas
pip freeze

# conda
# install miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install#linux-2
source ~/miniconda3/bin/activate
conda create -n myenv python=3.9
conda activate myenv
pip install pandas
pip freeze
conda deactivate