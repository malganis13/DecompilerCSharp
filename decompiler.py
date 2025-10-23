import clr
import sys
import os

# Add references to necessary .NET libraries (adjust paths if needed)
sys.path.append(os.path.dirname(os.path.abspath(__file__))) # Add current directory
sys.path.append(r"C:\Users\SeregaSGD\AppData\Local\JetBrains\Installations\dotPeek252_000") # Adjust this path
try:
    clr.AddReference("System")
    clr.AddReference("System.Core")
    clr.AddReference("dnlib")
    clr.AddReference("ICSharpCode.Decompiler")
    clr.AddReference("dotPeek.Engine")
except Exception as e:
    print(f"Error loading references: {e}")
    print("Make sure dotPeek is installed or the paths are correct.")
    exit()

from System import *
from System.IO import *
from dnlib.DotNet import *
from dnlib.DotNet.Emit import *
from ICSharpCode.Decompiler import *
from ICSharpCode.Decompiler.CSharp import *
from ICSharpCode.Decompiler.TypeSystem import *
from dotPeek.Engine import *



def decompile_dll(dll_path, output_path):
    """
    Decompiles a .NET DLL using dnSpy/dotPeek libraries.
    """

    try:
        # Load the module using dnlib
        module = ModuleDefMD.Load(dll_path)

        # Initialize decompiler settings
        settings = DecompilerSettings()
        decompiler = CSharpDecompiler(module, settings)

        # Decompile the entire assembly
        full_code = decompiler.DecompileWholeModuleAsString()

        # Save the decompiled code to a file
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(full_code)

        print(f"Successfully decompiled {dll_path} to {output_path}")

    except Exception as e:
        print(f"Error decompiling {dll_path}: {e}")


# Example Usage:
dll_file1 = "Guna.UI2.dll"
dll_file2 = "Newtonsoft.Json.dll"

output_file1 = "Guna.UI2_decompiled.cs"
output_file2 = "Newtonsoft.Json_decompiled.cs"

decompile_dll(dll_file1, output_file1)
decompile_dll(dll_file2, output_file2)

print("Decompilation process completed.")