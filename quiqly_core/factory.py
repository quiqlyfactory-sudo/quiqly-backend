import os
import shutil

class QuiqlyFactory:
    def __init__(self):
        # Changed to match your initial directory structure: Master_Library
        self.library_path = "./Master_Library"
        self.active_projects = ["WISeRly", "Quiqly"]
        
        # Create the library if it doesn't exist
        if not os.path.exists(self.library_path):
            os.makedirs(self.library_path)
    
    def harvest_module(self, module_name, source_code):
        """Saves a piece of code to the Master Library for reuse"""
        file_path = os.path.join(self.library_path, f"{module_name}.py")
        with open(file_path, "w") as f:
            f.write(source_code)
        print(f"📦 Module '{module_name}' harvested and stored for future apps.")
    
    def spawn_new_software(self, software_name):
        """Clones the core Quiqly engine into a new brand folder"""
        if not os.path.exists(software_name):
            os.makedirs(software_name)
            # Copy core logic from library to the new project
            # Ensure the destination is the new software_name directory
            for item in os.listdir(self.library_path):
                shutil.copy(
                    os.path.join(self.library_path, item),
                    os.path.join(software_name, item) # Corrected destination path
                )
            print(f"🚀 {software_name} has been initialized with all Master Modules.")
        else:
            print(f"⚠️ Project {software_name} already exists.")

# --- INITIALIZING THE FACTORY ---
factory = QuiqlyFactory()

# Example: You just finished the 'AskVault' for WISeRly. You harvest it:
vault_logic = """
class Vault:
    def scan(self):
        print('Scanning for Conservative Care...')
"""
factory.harvest_module("SecurityVault", vault_logic)

# Example: Next month, you start Software #3. You just run:
# factory.spawn_new_software("Software_Three")