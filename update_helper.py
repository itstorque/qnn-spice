import sys
import os
import shutil

# Move to using similar to any(ext in name for ext in [".asy", ".lib"])
# for all types of lib and asy..

is_file = lambda name: any(ext in name for ext in [".asy", ".lib", ".asc"])

if __name__=="__main__":
    
    if sys.argv[1] == "--update-symlinks":
        
        LTSPICE_LIB_PATH = sys.argv[2]
        
        os.makedirs(LTSPICE_LIB_PATH+"/sym/qnn-spice", exist_ok=True)
        os.makedirs(LTSPICE_LIB_PATH+"/sub/qnn-spice", exist_ok=True)
        
        files_asy = []
        files_lib = []
        
        models = open("models.md", "r").read()
        
        last_dir = []
        dest_dir = []
        last_dir_size = [-1]

        for line in models.split("\n"):
            
            indents = (len(line) - len(line.lstrip()))
            
            loc = line.split("- ")[1].split(":")[0]
            
            if ":" in line:
                name = line.split("- ")[1].split(":")[1].lstrip().rstrip()
                path = line.split("- ")[1].split(":")[0].lstrip().rstrip()
            elif is_file(line):
                
                if ":" in line:
                    name = line.split("- ")[1].split(":")[1].rstrip().lstrip()
                    path = line.split("- ")[1].split(":")[0].rstrip().lstrip()
                else:
                    name = line.split("- ")[1].rstrip().lstrip()
                    path = name
            else:
                name = "."
                path = line.split("- ")[1].lstrip().rstrip()
            
            if not is_file(name): 
                
                while indents < last_dir_size[-1]:
                    
                    last_dir = last_dir[:-1]
                    dest_dir = dest_dir[:-1]
                    last_dir_size = last_dir_size[:-1]
                
                if indents == last_dir_size[-1]:
                    
                    last_dir[-1] = path+"/"
                    dest_dir[-1] = name+"/"
                    
                else: # indents > prev_indents
                    
                    last_dir.append(path+"/")
                    dest_dir.append(name+"/")
                    last_dir_size.append(indents)
                
            if ".asy" in name: files_asy.append((''.join(last_dir) + path, 
                                                 (''.join(dest_dir)).replace("./", ""),
                                                 name
                                                 ))
            if (".lib" in name or ".asc" in name): files_lib.append((''.join(last_dir) + path, 
                                                                    (''.join(dest_dir)).replace("./", ""),
                                                                    name
                                                                    ))
        
        for src, dest, dest_filename in files_asy:
            
            os.makedirs(LTSPICE_LIB_PATH + "/sym/qnn-spice/" + dest, exist_ok=True)

            os.symlink(os.getcwd() + "/" + src, LTSPICE_LIB_PATH + "/sym/qnn-spice/" + dest + dest_filename)
            
            print("    ADDED:", dest_filename)
        
        for src, dest, dest_filename in files_lib:
            
            os.makedirs(LTSPICE_LIB_PATH + "/sub/qnn-spice/" + dest, exist_ok=True)

            os.symlink(os.getcwd() + "/" + src, LTSPICE_LIB_PATH + "/sub/qnn-spice/" + dest + dest_filename)
            
            print(os.getcwd() + "/" + src, LTSPICE_LIB_PATH + "/sub/qnn-spice/" + dest + dest_filename)
            
            print("    ADDED:", dest_filename)