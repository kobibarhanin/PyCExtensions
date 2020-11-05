from distutils.core import setup, Extension
 
# change here the module name only if you wish to import it differently from python
module = Extension('cModule', sources = ['c_extension.c'])
 
setup (name = 'CExtensionPackage',
        version = '1.0',
        description = 'This is a package for myModule',
        ext_modules = [module])