# kernelm
Kernel Manager (kernelm) is an extension for Jupyter Notebook and Jupiter Lab. It allows you to manage different Python versions and environments in your computer to easily use on Jupyter environment.

## Installation

### Dependencies

### LINUX
- Pyenv
- C (sudo apt install build-essential)
- sudo apt install     build-essential     curl     libbz2-dev     libffi-dev     liblzma-dev     libncursesw5-dev     libreadline-dev     libsqlite3-dev     libssl-dev     libxml2-dev     libxmlsec1-dev     llvm     make     tk-dev     wget     xz-utils     zlib1g-dev


## Commands

- To install a new version of Python

```terminal
kerm newver <python version e.g. 3.9.6>
```
- To install a new environment of Python

```terminal
kerm newenv <python version e.g. 3.9.6> <environment name e.g. test>
```

### Examples

```terminal
kerm newver 3.9.6
kerm newenv 3.9.6 tester
```

more coming soon...

name: test1
channels:
  - conda-forge
  - defaults
  - https://repo.anaconda.com/pkgs/main
  - https://repo.anaconda.com/pkgs/r
dependencies:
  - appnope=0.1.4=pyhd8ed1ab_0
  - asttokens=2.4.1=pyhd8ed1ab_0
  - bzip2=1.0.8=h80987f9_6
  - ca-certificates=2024.9.24=hca03da5_0
  - comm=0.2.2=pyhd8ed1ab_0
  - debugpy=1.6.7=py311h313beb8_0
  - decorator=5.1.1=pyhd8ed1ab_0
  - exceptiongroup=1.2.2=pyhd8ed1ab_0
  - executing=2.1.0=pyhd8ed1ab_0
  - importlib-metadata=8.5.0=pyha770c72_0
  - ipykernel=6.29.5=pyh57ce528_0
  - ipython=8.29.0=pyh707e725_0
  - jedi=0.19.1=pyhd8ed1ab_0
  - jupyter_client=8.6.3=pyhd8ed1ab_0
  - jupyter_core=5.7.2=pyh31011fe_1
  - krb5=1.21.3=h237132a_0
  - libcxx=19.1.3=ha82da77_0
  - libedit=3.1.20191231=hc8eb9b7_2
  - libffi=3.4.4=hca03da5_1
  - libsodium=1.0.20=h99b78c6_0
  - matplotlib-inline=0.1.7=pyhd8ed1ab_0
  - ncurses=6.4=h313beb8_0
  - nest-asyncio=1.6.0=pyhd8ed1ab_0
  - openssl=3.3.2=h8359307_0
  - packaging=24.1=pyhd8ed1ab_0
  - parso=0.8.4=pyhd8ed1ab_0
  - pexpect=4.9.0=pyhd8ed1ab_0
  - pickleshare=0.7.5=py_1003
  - pip=24.2=py311hca03da5_0
  - platformdirs=4.3.6=pyhd8ed1ab_0
  - prompt-toolkit=3.0.48=pyha770c72_0
  - psutil=5.9.0=py311h80987f9_0
  - ptyprocess=0.7.0=pyhd3deb0d_0
  - pure_eval=0.2.3=pyhd8ed1ab_0
  - pygments=2.18.0=pyhd8ed1ab_0
  - python=3.11.10=hb885b13_0
  - python-dateutil=2.9.0=pyhd8ed1ab_0
  - pyzmq=25.1.2=py311h313beb8_0
  - readline=8.2=h1a28f6b_0
  - setuptools=75.1.0=py311hca03da5_0
  - six=1.16.0=pyh6c4a22f_0
  - sqlite=3.45.3=h80987f9_0
  - stack_data=0.6.2=pyhd8ed1ab_0
  - tk=8.6.14=h6ba3021_0
  - tornado=6.4.1=py311h80987f9_0
  - traitlets=5.14.3=pyhd8ed1ab_0
  - typing_extensions=4.12.2=pyha770c72_0
  - wcwidth=0.2.13=pyhd8ed1ab_0
  - wheel=0.44.0=py311hca03da5_0
  - xz=5.4.6=h80987f9_1
  - zeromq=4.3.5=h9f5b81c_6
  - zipp=3.20.2=pyhd8ed1ab_0
  - zlib=1.2.13=h18a0788_1
  - pip:
      - branca==0.8.0
      - certifi==2024.8.30
      - charset-normalizer==3.4.0
      - cloudpickle==3.1.0
      - contourpy==1.3.0
      - cycler==0.12.1
      - et-xmlfile==2.0.0
      - folium==0.18.0
      - fonttools==4.54.1
      - geopandas==1.0.1
      - idna==3.10
      - imageio==2.36.0
      - ipywidgets==8.1.5
      - jinja2==3.1.4
      - joblib==1.4.2
      - jupyterlab-widgets==3.0.13
      - kiwisolver==1.4.7
      - lazy-loader==0.4
      - lime==0.2.0.1
      - llvmlite==0.43.0
      - mapclassify==2.8.1
      - markupsafe==3.0.2
      - matplotlib==3.9.2
      - networkx==3.4.2
      - numba==0.60.0
      - numpy==2.0.2
      - openpyxl==3.1.5
      - pandas==2.2.3
      - pillow==11.0.0
      - pyogrio==0.10.0
      - pyparsing==3.2.0
      - pyproj==3.7.0
      - pytz==2024.2
      - requests==2.32.3
      - scikit-image==0.24.0
      - scikit-learn==1.5.2
      - scipy==1.14.1
      - seaborn==0.13.2
      - shap==0.46.0
      - shapely==2.0.6
      - slicer==0.0.8
      - threadpoolctl==3.5.0
      - tifffile==2024.9.20
      - tqdm==4.66.6
      - tzdata==2024.2
      - urllib3==2.2.3
      - widgetsnbextension==4.0.13
      - xyzservices==2024.9.0



