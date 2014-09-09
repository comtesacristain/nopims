from zipfile import ZipFile
import os

def zipdir(path, z):
    for root, dirs, files in os.walk(path):
        for file in files:
            z.write(os.path.join(root, file), os.path.relpath(root,path))

            
def main(root_path='/nas/energy/ideas/RDIS/NOPIMS_repository_remediation/msutti/pytest'):
    for f in os.listdir(root_path):
        folder = os.path.join(root_path,f)
        to_zips = os.listdir(folder)
        for d in to_zips:
            zf = os.path.join(folder,d)
            with ZipFile(zf+".zip", 'w') as z:
                print "Zipping path " + zf
                zipdir(zf,z)
main()
