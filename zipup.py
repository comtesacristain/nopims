from zipfile import ZipFile
import os, shutil

def zipdir(path, z):
    for root, dirs, files in os.walk(path):
        for file in files:
            z.write(os.path.join(root, file), os.path.join(os.path.relpath(root,path),file))

            
def main(root_path="I:/RDIS/NOPIMS_repository_remediation/msutti/pytest"):
    for f in os.listdir(root_path):
        folder = os.path.join(root_path,f)
        to_zips = os.listdir(folder)
        for d in to_zips:
            zf = os.path.join(folder,d)
            z = ZipFile(zf+".zip", 'w',allowZip64=True) 
            print "Zipping path " + zf
            zipdir(zf,z)
            z.close()
            shutil.rmtree(zf)
main()
