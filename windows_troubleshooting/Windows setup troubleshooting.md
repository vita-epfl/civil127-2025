# Windows setup troubleshooting

# Why is code not running python 3.12.9 in your terminal

- If you have downloaded python from the Microsoft Store : Windows uses a Python Launcher for every distribution and would preferably run python from it. This launcher would be installed from the store and would work like any windows app. However, this is not very practical for you as you would not be able to use this version to debug in your VS Code installation and it is general a hassle to use.
- If you have downloaded python from the link in the labs :
    - A version of python the 3.12.9 python interpreter is on your computer but it has not been added as a variable to you PATH variable. This means that your terminal does not know how to interpret the python file you are asking it to execute and will either try with another version or say it does not find python.
    - Currently, when you are running from VSCode the IDE is adding the interpreter path in your command automatically. It adds something like : `& <C:\Path\To\Python312\python.exe> <path_to_file>`. The first part works like an alias for the `python` command. Adding this command in any terminal will work fine, but might get a bit tricky when trying to run other commands.
        - Note : if you choose to simply paste this command before executing any lab file in your terminal and you find yourself wanting to install a python package the command would be : `& <C:\Path\To\Python312\python.exe> -m pip install SomePackage`

# Fixes

There are lots of ways to setup your computer and make it run python 3.12.9 from the terminal, here is a tree to help you choose :

```
Do you have another newer version you would like to be the default python version in your terminal ? /
├─ No /
│  ├─ Add python 3.12.9 to PATH/
├─ Yes /
│  ├─ Would you like a persistent change ?/
│  │  ├─ Yes/
│  │  │  ├─ Would you like to be able to run another version of python outside the specific class folder ? /
│  │  │  │  ├─ Yes/
│  │  │  │  │  ├─ Create virtual env/
│  │  │  │  ├─ No/
│  │  │  │  │  ├─ Create Bat file/
│  │  ├─ No/
│  │  │  ├─ Create alias /
```

## Creating an alias :

Note : This would have to be done at the start of every session 

1. Open PowerShell and run 
    
    ```powershell
    Set-Alias python312 "C:\Path\To\Python312\python.exe"
    
    ```
    
2. Now run 
    
    ```powershell
    python312
    ```
    
    If this opens a Python 3.12.9 REPL (cf. the image below) you have correctly created an alias for the path to your interpreter 
    
    ![image.png](image.png)
    
    - This means that you do not have to paste the `& <C:\Path\To\Python312\python.exe>`  command every time you want to run from the 3.12.9 interpreter. You simply can use your newly created command to for example run a file, open a terminal in the file location and type : `python312 file.py`

## Creating a .bat file :

- A bat file is a windows system file used by cmd and PowerShell to understand what to do when you type a command in the Terminal.

### Steps

1. To create a bat file you will have to go look at your  [Environment variables](#Environment-variables) and find a folder that is already in the PATH, like `“C:/User/username/source/”` 
2. Open this folder with VSCode.
3. Create a new bat file for example : `python312.bat`
4. Put this in your newly created file : 
    
    ```bash
    @echo off
    "C:\Path\To\Python312\python.exe" %*
    ```
    
5. Save the file, make sure it is the right folder 
6. Open a terminal either by pressing the windows key + X and choosing terminal or by searching terminal in the windows menu 
7. Run 
    
    ```powershell
    python312
    ```
    
    If this opens a Python 3.12.9 REPL (cf. the image below) you have correctly created an alias for the path to your interpreter 
    
    ![image.png](image.png)
    
    - This means that you do not have to paste the `& <C:\Path\To\Python312\python.exe>`  command every time you want to run from the 3.12.9 interpreter. You simply can use your newly created command to for example run a file, open a terminal in the file location and type : `python312 file.py`

## Virtual Environment :

- In your class folder you can define a virtual environment to make everything in this folder use the 3.12.9 version of python
- Note : you will have to activate the virtual environment before you run your code for the first time :  [activate virtual environment](#activate-the-virtual-environment)

### **Steps:**

1. Install `venv` if you haven't:
    
    ```powershell
    & <C:\Path\To\Python312\python.exe> -m pip install virtualenv
    ```
    
2. Create a virtual environment
    
    ```powershell
    & <C:\Path\To\Python312\python.exe> -m venv C:\path\to\new\virtual\environment 
    ```
    
3. Switch to command prompt 
    
    ```powershell
    cmd
    ```
    
4. #### Activate the virtual environment 
    
    ```powershell
    .\civil_env\Scripts\activate.bat
    ```
    

## Adding python 3.12.9 to path :

Note : this will work if you only have the 3.12.9 version of python installed on your machine. 

### Steps

1. Open the : 
    - ### Environment variables
        - to find environment variables on your computer search for it in your window menu’s search bar, on the `System Properties` window click on `Environment Variables` on the bottom right
            
            ![image.png](image%201.png)
            
        - look for the `Path` variable either in your system or in your user variables
            
            ![image.png](image%202.png)
            
        
        ---
        
2. Choose which type of `Path` variable you want to change 
    - **User Variable:** Only `<username>` can use Python from the command line.
    - **System Variable:** Every user on the system can use Python.
3. In your environment variables go to your chosen `Path` variable
4. Click on `Edit`, then on `New` 
5. add the `<C:\Path\To\Python312\python.exe>`  to the `Path` variable 
6. Click on `ok` and you have successfully added python 3.12.9 to your Path variable 
7. Now run
    
    ```powershell
    python 
    ```
    
    If this opens a Python 3.12.9 REPL (cf. the image below) you have correctly created an alias for the path to your interpreter
    
    ![image.png](image.png)
    
    - This means that you do not have to paste the `& <C:\\Path\\To\\Python312\\python.exe>` command every time you want to run from the 3.12.9 interpreter. You simply can use the normal python command to, for example, run a file, open a terminal in the file location and type : `python file.py`