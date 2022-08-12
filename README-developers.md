## Directory Structure

* `./formats` a package to hold all the [Kaitai Struct formats](https://github.com/kaitai-io/kaitai_struct_formats) compiled to python
* `./formats/__init__.py` promoting the directory to a package
* `./corelogic/kaitaistruct.py` the kaitaistruct runtime (also via `pip install kaitaistruct`)
* `./corelogic/kshelpers.py` main code
* `./plugin` code to hook up with BinaryNinja
* `./media` screenshots

QT and BinaryNinja and BinaryNinja UI stuff is intentionally kept isolated within `./plugin` so that rapid development and commandline testing can be performed.

## Compiled formats in a package

The compiled formats are in their own package called formats, like:

```
./formats/__init__.py
./formats/elf.py
./formats/mach_o.py
...
```

The reason is because the compiled formats use intra-package imports, like `from . import windows_systemtime` or `from . import ethernet_frame`. Obviously this won't work without a package set, and that requires two ingredients: the package directory structure with `__init__.py` existing and variable`__package__` being set at the time the intra-package import occurs. The `__package__` is usually set with statements like `from MyPackage import MyFormat` or `import MyPackage.MyFormat`.

Since we load the formats dynamically (to avoid statically executing `from formats import MyFormat` for every single format), we have to set the python module path carefully. We add the repository directory to the module path, so that `formats` is an immediate subdirectory and a `importlib.import_module()` call can specify `formats.MyFormat` to set the package.

See `ksImportClass()` for implementation details.
