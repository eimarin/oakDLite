# Install native M1 version of brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# Install conda to create virtual environments for Python
brew install --cask miniconda
conda init zsh

# Close and re-open a Terminal window

# Install DepthAI by building a M1 wheel (inside ~/DepthAI/)
conda create --name DepthAIEnv39 python=3.9
conda activate DepthAIEnv39
python3 -m pip install -U pip
brew update
brew install cmake libusb
cd ~; mkdir DepthAI; cd DepthAI
git clone --recursive  https://github.com/luxonis/depthai-python.git
cd depthai-python
mkdir build && cd build
# Build depthai-python
cmake ..
cmake --build . --parallel
cd ..
python3 -m pip wheel . -w wheelhouse
pip install wheelhouse/depthai-*

# Test DepthAI with a OAK plugged to your new M1 Mac
cd examples
nano install_requirements.py
#   Remove code of block (3 lines) starting with: if thisPlatform == "arm64" and platform.system() == "Darwin":
#   Remove code of block (48 lines) starting with: if not args.skip_depthai:
python3 install_requirements.py
python3 ColorCamera/rgb_preview.py
