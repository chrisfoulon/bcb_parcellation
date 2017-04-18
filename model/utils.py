# -*- coding: utf-8 -*-

import os
import glob


def parent_dir(path):
    """ Return the path to the parent directory of the given path, even if the
    path designates a folder (with or without "\\" at the end)
    Parameters
    ----------
    path : str
        The path to the file/folder you want to know the parent folder

    Returns
    -------
    parent : str
        the path to the parent folder
    """
    parent = os.path.dirname(os.path.dirname(os.path.join(path, "")))
    return parent

def split_ext(path):
    """ Split the file extension from the path even in case of double extension.
    (like .nii.gz)
    Parameters
    ----------
    path : Full path or just file name
    Returns
    -------
    couple of file name(or path) and the extension(s)
    """
    if len(path.split('.')) > 2:
        return path.split('.')[0],'.'.join(path.split('.')[-2:])
    return splitext(path)

def find_in_filename(path, string):
    """ Find string in the filename of path (only in the basename).
        Note that the filename is splitted by underscores.
    Parameters
    ----------
    path : str
        the path of the filename you want to parse
    string : str
        the string you want to find in path
    Returns
    -------
    file_path : str
        the path to the file if ONE filename contains string
        empty str if not
        Throw an error if several files contain string
    """
    # join is here to handle folder paths with or without '/' at the end
    arr = glob.glob(os.path.join(path, "") + '*' + string + '*')
    if len(arr) == 0:
        return ""
    elif len(arr) == 1:
        return arr[0]
    else:
        raise Exception("I found several files corresponding to this pattern")

def save_dict(d, path):
    """ Save a dictionary in a file
    Parameters
    ----------
    d : dict
        A dictionary with data
    path : str
        The path to the file you want to create
        Note that the folder which will contain the file have to exist
    """
    with open(path, "w") as input_file:
        for k, v in d.items():
            line = '{} {}'.format(k, v)
            print(line, file=input_file)

def read_dict_from_file(path, sep=None):
    """ Read a dictionnary from a file. The file have to composed of pairs
    key[separator]value
    Parameters
    ----------
    path : str
        path to the file to be read
    sep : str[default None]
        the separator between key and value. The default None value will
        use spaces
    Returns
    -------
    d : dict
        The dictionnary contained in the file
    """
    d={}
    with open(path) as f:
        for line in f:
            (key, val) = line.split(sep)
            d[key] = val
    return d

def read_ROIs_from_nifti(path):
    ROIs = nib.load(path).get_data()
    # Create an index to the xyz coordinates of the voxels in each ROIs
    ind_xyz_ROIs = np.where(ROIs)
    # Create an index of the ROI associated with each row of the
    # (subsequently) created 2D_connectivity_matrix
    ind_2Drows_to_ROIs_label = ROIs[ind_xyz_ROIs]

    return ind_xyz_ROIs, ind_2Drows_to_ROIs_label

# tt = find_in_filename("/data", 'BCB*/folder*/pattern')
# print(tt)
