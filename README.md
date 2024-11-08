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

yaml file 
```
name: tpm034a
channels:
  - conda-forge
  - defaults
  - https://repo.anaconda.com/pkgs/main
  - https://repo.anaconda.com/pkgs/r
dependencies:
  - aom=3.6.0=h313beb8_0
  - appnope=0.1.4=pyhd8ed1ab_0
  - asttokens=2.4.1=pyhd8ed1ab_0
  - attrs=24.2.0=py311hca03da5_0
  - blas=1.0=openblas
  - blosc=1.21.3=h313beb8_0
  - boost-cpp=1.82.0=h48ca7d4_2
  - bottleneck=1.3.7=py311hb9f6ed7_0
  - branca=0.6.0=py311hca03da5_0
  - brotli=1.0.9=h80987f9_8
  - brotli-bin=1.0.9=h80987f9_8
  - brotli-python=1.0.9=py311h313beb8_8
  - brunsli=0.1=hc377ac9_1
  - bzip2=1.0.8=h80987f9_6
  - c-ares=1.19.1=h80987f9_0
  - ca-certificates=2024.9.24=hca03da5_0
  - cairo=1.16.0=h302bd0f_5
  - certifi=2024.8.30=py311hca03da5_0
  - cfitsio=3.470=h7f6438f_7
  - charls=2.2.0=hc377ac9_0
  - charset-normalizer=3.3.2=pyhd3eb1b0_0
  - click=8.1.7=py311hca03da5_0
  - click-plugins=1.1.1=pyhd3eb1b0_0
  - cligj=0.7.2=pyhd3eb1b0_0
  - cloudpickle=3.0.0=py311hca03da5_0
  - comm=0.2.2=pyhd8ed1ab_0
  - contourpy=1.2.0=py311h48ca7d4_0
  - cycler=0.11.0=pyhd3eb1b0_0
  - dav1d=1.2.1=h80987f9_0
  - debugpy=1.6.7=py311h313beb8_0
  - decorator=5.1.1=pyhd8ed1ab_0
  - et_xmlfile=1.1.0=py311hca03da5_0
  - exceptiongroup=1.2.2=pyhd8ed1ab_0
  - executing=2.1.0=pyhd8ed1ab_0
  - expat=2.6.3=h313beb8_0
  - fiona=1.9.5=py311h7aedaa7_0
  - folium=0.14.0=py311hca03da5_0
  - fontconfig=2.14.1=h6402c1e_3
  - fonttools=4.51.0=py311h80987f9_0
  - freetype=2.12.1=h1192e45_0
  - freexl=2.0.0=ha3de405_0
  - gdal=3.6.2=py311h950983f_6
  - geopandas=0.14.2=py311hca03da5_0
  - geopandas-base=0.14.2=py311hca03da5_0
  - geos=3.9.1=hc377ac9_1
  - geotiff=1.7.0=h41f0982_3
  - gettext=0.21.0=hbdbcc25_2
  - giflib=5.2.2=h80987f9_0
  - glib=2.78.4=h313beb8_0
  - glib-tools=2.78.4=h313beb8_0
  - hdf4=4.2.13=h5e329fb_3
  - hdf5=1.12.1=h05c076b_3
  - icu=73.1=h313beb8_0
  - idna=3.7=py311hca03da5_0
  - imagecodecs=2023.1.23=py311h5e7c512_0
  - imageio=2.33.1=py311hca03da5_0
  - importlib-metadata=8.5.0=pyha770c72_0
  - ipykernel=6.29.5=pyh57ce528_0
  - ipython=8.29.0=pyh707e725_0
  - ipywidgets=8.1.2=py311hca03da5_0
  - jedi=0.19.1=pyhd8ed1ab_0
  - jinja2=3.1.4=py311hca03da5_1
  - joblib=1.4.2=py311hca03da5_0
  - jpeg=9e=h80987f9_3
  - json-c=0.16=h1a28f6b_0
  - jupyter_client=8.6.3=pyhd8ed1ab_0
  - jupyter_core=5.7.2=pyh31011fe_1
  - jupyterlab_widgets=3.0.10=py311hca03da5_0
  - jxrlib=1.1=h1a28f6b_2
  - kealib=1.5.0=hba2eb73_1
  - kiwisolver=1.4.4=py311h313beb8_0
  - krb5=1.20.1=hf3e1bf2_1
  - lazy_loader=0.4=py311hca03da5_0
  - lcms2=2.12=hba8e193_0
  - lerc=3.0=hc377ac9_0
  - libaec=1.0.4=hc377ac9_1
  - libavif=0.11.1=h80987f9_0
  - libboost=1.82.0=h0bc93f9_2
  - libbrotlicommon=1.0.9=h80987f9_8
  - libbrotlidec=1.0.9=h80987f9_8
  - libbrotlienc=1.0.9=h80987f9_8
  - libcurl=8.9.1=h3e2b118_0
  - libcxx=14.0.6=h848a8c0_0
  - libdeflate=1.17=h80987f9_1
  - libedit=3.1.20230828=h80987f9_0
  - libev=4.33=h1a28f6b_1
  - libffi=3.4.4=hca03da5_1
  - libgdal=3.6.2=h51eea9d_6
  - libgfortran=5.0.0=11_3_0_hca03da5_28
  - libgfortran5=11.3.0=h009349e_28
  - libglib=2.78.4=h0a96307_0
  - libiconv=1.16=h80987f9_3
  - libkml=1.3.0=hc4d7c42_7
  - libllvm14=14.0.6=h19fdd8a_4
  - libnetcdf=4.8.1=h0fce390_4
  - libnghttp2=1.57.0=h62f6fdd_0
  - libopenblas=0.3.21=h269037a_0
  - libpng=1.6.39=h80987f9_0
  - libpq=12.20=h02f6b3c_0
  - libsodium=1.0.18=h27ca646_1
  - libspatialindex=1.9.3=hc377ac9_0
  - libspatialite=5.1.0=h3e2df84_1
  - libssh2=1.11.0=h3e2b118_0
  - libtiff=4.5.1=h313beb8_0
  - libwebp-base=1.3.2=h80987f9_1
  - libxml2=2.13.1=h0b34f26_2
  - libzip=1.8.0=h62fee54_1
  - libzopfli=1.0.3=hc377ac9_0
  - lime=0.2.0.1=py311hca03da5_0
  - llvm-openmp=14.0.6=hc6e5704_0
  - llvmlite=0.43.0=py311h313beb8_0
  - lz4-c=1.9.4=h313beb8_1
  - mapclassify=2.5.0=py311hca03da5_0
  - markupsafe=2.1.3=py311h80987f9_0
  - matplotlib=3.9.2=py311hca03da5_0
  - matplotlib-base=3.9.2=py311hecf7826_0
  - matplotlib-inline=0.1.7=pyhd8ed1ab_0
  - minizip=4.0.3=ha89c15f_0
  - ncurses=6.4=h313beb8_0
  - nest-asyncio=1.6.0=pyhd8ed1ab_0
  - networkx=3.3=py311hca03da5_0
  - nspr=4.35=h313beb8_0
  - nss=3.89.1=h313beb8_0
  - numba=0.60.0=py311h7aedaa7_0
  - numexpr=2.10.1=py311h5d9532f_0
  - numpy=1.26.4=py311he598dae_0
  - numpy-base=1.26.4=py311hfbfe69c_0
  - openjpeg=2.5.2=h54b8e55_0
  - openpyxl=3.1.5=py311h80987f9_0
  - openssl=3.3.2=h8359307_0
  - packaging=24.1=py311hca03da5_0
  - pandas=2.2.2=py311h7aedaa7_0
  - parso=0.8.4=pyhd8ed1ab_0
  - pcre2=10.42=hb066dcc_1
  - pexpect=4.9.0=pyhd8ed1ab_0
  - pickleshare=0.7.5=py_1003
  - pillow=10.4.0=py311h80987f9_0
  - pip=24.2=py311hca03da5_0
  - pixman=0.40.0=h1a28f6b_0
  - platformdirs=4.3.6=pyhd8ed1ab_0
  - poppler=22.12.0=h52f4003_3
  - poppler-data=0.4.11=hca03da5_1
  - proj=9.3.1=h805f6d4_0
  - prompt-toolkit=3.0.48=pyha770c72_0
  - psutil=5.9.0=py311h80987f9_0
  - ptyprocess=0.7.0=pyhd3deb0d_0
  - pure_eval=0.2.3=pyhd8ed1ab_0
  - pybind11-abi=4=hd3eb1b0_1
  - pygments=2.18.0=pyhd8ed1ab_0
  - pyparsing=3.1.2=py311hca03da5_0
  - pyproj=3.6.1=py311h041c639_0
  - pysocks=1.7.1=py311hca03da5_0
  - python=3.11.10=hb885b13_0
  - python-dateutil=2.9.0post0=py311hca03da5_2
  - python-tzdata=2023.3=pyhd3eb1b0_0
  - pytz=2024.1=py311hca03da5_0
  - pyzmq=25.1.2=py311h313beb8_0
  - qhull=2020.2=h48ca7d4_2
  - readline=8.2=h1a28f6b_0
  - requests=2.32.3=py311hca03da5_0
  - rtree=1.0.1=py311hca03da5_0
  - scikit-image=0.24.0=py311h7aedaa7_0
  - scikit-learn=1.5.1=py311h7aedaa7_0
  - scipy=1.13.1=py311hac8794a_0
  - seaborn=0.13.2=py311hca03da5_0
  - setuptools=75.1.0=py311hca03da5_0
  - shap=0.46.0=py311h7aedaa7_0
  - shapely=2.0.5=py311h3713c0e_0
  - six=1.16.0=pyhd3eb1b0_1
  - slicer=0.0.8=py311hb6e6a13_0
  - snappy=1.2.1=h313beb8_0
  - sqlite=3.45.3=h80987f9_0
  - stack_data=0.6.2=pyhd8ed1ab_0
  - tbb=2021.8.0=h48ca7d4_0
  - threadpoolctl=3.5.0=py311hb6e6a13_0
  - tifffile=2023.4.12=py311hca03da5_0
  - tiledb=2.3.3=hb4a6b97_3
  - tk=8.6.14=h6ba3021_0
  - tornado=6.4.1=py311h80987f9_0
  - tqdm=4.66.5=py311hb6e6a13_0
  - traitlets=5.14.3=pyhd8ed1ab_0
  - typing_extensions=4.12.2=pyha770c72_0
  - tzdata=2024b=h04d1e81_0
  - unicodedata2=15.1.0=py311h80987f9_0
  - uriparser=0.9.7=h80987f9_0
  - urllib3=2.2.3=py311hca03da5_0
  - wcwidth=0.2.13=pyhd8ed1ab_0
  - wheel=0.44.0=py311hca03da5_0
  - widgetsnbextension=4.0.10=py311hca03da5_0
  - xerces-c=3.2.4=h313beb8_1
  - xyzservices=2022.9.0=py311hca03da5_1
  - xz=5.4.6=h80987f9_1
  - zeromq=4.3.5=h313beb8_0
  - zfp=1.0.0=h313beb8_0
  - zipp=3.20.2=pyhd8ed1ab_0
  - zlib=1.2.13=h18a0788_1
  - zstd=1.5.6=hfb09047_0
  - pip:
      - affine==2.4.0
      - contextily==1.6.2
      - geographiclib==2.0
      - geopy==2.4.1
      - mercantile==1.2.1
      - rasterio==1.4.2
```
