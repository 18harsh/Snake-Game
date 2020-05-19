import cx_Freeze 

executables = [
                      
        cx_Freeze.Executable("main.py") 
] 
cx_Freeze.setup( 
        name = "", 
        options = {"build_exe": {"packages":["pygame"],"include_files":["apple2.png","snakehead.png","background.jpg"]}},
        description = "The classic snake game", 
        executables = executables)
