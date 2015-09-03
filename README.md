README
==============

Setting up project
--------------

```bash
# Create working directory
mkdir workspace
cd workspace
# Checkout source code from github
git clone https://github.com/pchaivong/wippie.git

# Create virtual environment
# Highly recommended using name 'env' because it's has been added to .gitignore file already
# If you use another name, ensure that you add that name to .gitignore as well.
virtualenv env

# Activate using virtual environment (Windows)
.\env\Scripts\activate

# For Mac or Linux
source env/bin/activate

# download all mandatory library
pip install -r requirements.txt


