import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    output=[]
    l=suffix
    if path:
        l=suffix+'/'+path
    for each in os.listdir(l):
        l1=l+'/'+each
        
        if os.path.isfile(l1) and l1.endswith(".c"):
            output.append(l1)
            
        elif os.pathisdir(l1):
            output=find_files(l,each,l)
    return output
            

print(find_files('.', 'testdir'))
print(find_files('.', ''))
print(find_files('.', 'testdir/subdir3'))
