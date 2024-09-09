import os

def get_model_path():
    file_name = 'model.pkl'
    my_path=__file__
    dir_name = os.path.dirname(my_path)
    model_path = os.path.join(dir_name, file_name)
    return model_path
