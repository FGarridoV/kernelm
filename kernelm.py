import os
import sys

ROOT_PATH = '/Users/francisco/Developer/Programs/kernelm'

image32 = 'logo-32x32.png'
image64 = 'logo-64x64.png'

json_template = lambda path, ver, env: """{
 "argv": [ "%s", "-m", "ipykernel",
          "-f", "{connection_file}"],
 "display_name": "Python%s%s",
 "language": "python"
}""" % (path, ver, env)

def get_kernels_path():
    paths = os.popen('jupyter --paths').readlines()
    paths = paths[8].strip()
    return f'{paths}/kernels' 

def create_kernel_env_folder_and_json(env_name, json_content, image32, image64, ver_name = None):
    global ROOT_PATH
    kernels_path = get_kernels_path()
    if ver_name is None:
        os.system(f'mkdir {kernels_path}/{env_name}')
        os.system(f'cp {ROOT_PATH}/{image32} {kernels_path}/{env_name}/{image32}')
        os.system(f'cp {ROOT_PATH}/{image64} {kernels_path}/{env_name}/{image64}')
        f = open(f'{kernels_path}/{env_name}/kernel.json', 'w')
    else:
        os.system(f'mkdir {kernels_path}/python{ver_name}')
        os.system(f'cp {ROOT_PATH}/{image32} {kernels_path}/python{ver_name}/{image32}')
        os.system(f'cp {ROOT_PATH}/{image64} {kernels_path}/python{ver_name}/{image64}')
        f = open(f'{kernels_path}/python{ver_name}/kernel.json', 'w')
    f.write(json_content)
    f.close()
     
def create_new_env_kernel(py_ver, env_name):
    global json_template, image32, image64
    
    # Creates python env
    os.system(f'pyenv virtualenv {py_ver} {env_name}')
    
    # Creates json content file
    python_env_folder = os.popen('pyenv root').read()[:-1] + f'/versions/{env_name}/bin'
    python_env_path = f'{python_env_folder}/python'
    ver_name = py_ver[:3]
    json_content = json_template(python_env_path, ver_name, f' ({env_name})')
    
    # Update pip and install ipykernel libs
    os.system(f'source {python_env_folder}/activate\n{python_env_path} -m pip install --upgrade pip')
    os.system(f'source {python_env_folder}/activate\npip3 install ipykernel')

    # Creates kernel folder and json
    create_kernel_env_folder_and_json(env_name, json_content, image32, image64)

def create_new_ver_kernel(py_ver):
    global json_template, image32, image64
    
    # Creates python env
    os.system(f'pyenv install {py_ver}')
    
    # Creates json content file
    python_folder = os.popen('pyenv root').read()[:-1] + f'/versions/{py_ver}/bin'
    python_path = f'{python_folder}/python'
    ver_name = py_ver[:3]
    json_content = json_template(python_path, ver_name, '')
    
    # Update pip and install ipykernel libs
    os.system(f'{python_path} -m pip install --upgrade pip')
    os.system(f'{python_path} -m pip install ipykernel')

    # Creates kernel folder and json
    create_kernel_env_folder_and_json('', json_content, image32, image64, ver_name = ver_name)
    
def delete_env_kernel(env_name):
    
    # Delete python env
    os.system(f'pyenv virtualenv-delete -f {env_name}')
    
    # Delete kernel folder
    kernel_path = get_kernels_path() + f'/{env_name}'
    os.system(f'rm -rf {kernel_path}')
    
def delete_ver_kernel(py_ver):
    
    # Delete python env
    os.system(f'pyenv uninstall -f {py_ver}')
    
    # Delete kernel folder
    ver_name = py_ver[:3]
    kernel_path = get_kernels_path() + f'/python{ver_name}/'
    os.system(f'rm -rf {kernel_path}')
    
if __name__ == '__main__':
    
    if sys.argv[1] == 'newenv' and len(sys.argv) == 4:
        py_ver = sys.argv[2]
        env_name = sys.argv[3]
        create_new_env_kernel(py_ver, env_name)
    
    elif sys.argv[1] == 'newver' and len(sys.argv) == 3:
        py_ver = sys.argv[2]
        create_new_ver_kernel(py_ver)
    
    elif sys.argv[1] == 'delenv' and len(sys.argv) == 3:
        env_name = sys.argv[2]
        delete_env_kernel(env_name)
    
    elif sys.argv[1] == 'delver' and len(sys.argv) == 3:
        py_ver = sys.argv[2]
        delete_ver_kernel(py_ver)
    
    else:
        print(f"kerm: no such command {sys.argv[0]}")