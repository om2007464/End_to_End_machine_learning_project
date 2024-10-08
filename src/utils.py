import os
import pickle
from src.exception import CustomException
import sys

def save_object(file_path, obj):
    try:
        # Create the directory if it doesn't exist
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        # Save the object to a file using pickle
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)

                    

