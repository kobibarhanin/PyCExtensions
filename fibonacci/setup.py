from distutils.core import setup, Extension
 
module = Extension('myModule', sources = ['c_extension.c'])
 
setup (name = 'CExtensionPackage',
        version = '1.0',
        description = 'This is a package for myModule',
        ext_modules = [module])