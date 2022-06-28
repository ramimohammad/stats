To use this app please do the following:

1. python3.8 -m venv venv # you can choose 3.8+ versions too
2. source venv/bin/activate
3. git clone https://github.com/ramimohammad/stats.git
4. pip install -r requirements.txt
5. cd stats
6. python stats.py main_input.csv

Note : This script accept one csv file with main content and generates two csv files [ 0_output_file_name.csv : contains the product name with the avg of quantity ] [1_output_file_name.csv cotnains the product name with the brand names that have highest order frequency]
