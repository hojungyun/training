```
git clone https://github.com/hojungyun/training
cd training
poetry install
poetry shell

python gil/1_single_process_single_thread.py
python gil/2_single_process_multi_thread.py
python gil/3_multi_process_single_thread_per_proc.py

or

cd gil
python 1_single_process_single_thread.py
python 2_single_process_multi_thread.py
python 3_multi_process_single_thread_per_proc.py
```